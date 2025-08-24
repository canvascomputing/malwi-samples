#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Git Commit Message Generator using the AutoGemini Agent Framework.

This advanced agent can not only generate commit messages but also has
the ability to list directory contents and change its working directory
to better understand the project context before acting.

Refactored for improved structure, readability, and maintainability.
"""

import asyncio
import json
import os
import sys
import argparse
import subprocess
from pathlib import Path
import time

# --- Third-party Imports ---
try:
    from colorama import Fore, Style, init

    init(autoreset=True)
except ImportError:

    class Fore:
        RED = GREEN = YELLOW = BLUE = CYAN = WHITE = ""

    class Style:
        RESET_ALL = ""


import html2text
from autogemini import (
    create_cot_processor,
    DefaultApi,
    ToolCodeInfo,
)
from autogemini.template import parse_agent_output

# --- Constants ---
CONFIG_FILENAME = ".auto-git-msg.json"
DEFAULT_CACHE_PATH = Path.home() / CONFIG_FILENAME
API_KEY_FIELD = "api_key"
PROXY_FIELD = "grpc_proxy"


# --- Helper Functions ---
def print_colored(color: str, message: str):
    """Helper to print colored messages to stderr."""
    print(f"{color}{message}{Style.RESET_ALL}", file=sys.stderr)


def convert_html_to_readable_text(html_content: str) -> str:
    """Converts HTML content to a human-readable, Markdown-like plain text."""
    if not html_content:
        return ""
    h = html2text.HTML2Text(bodywidth=0)
    try:
        return h.handle(html_content)
    except Exception:
        import re

        return re.sub(r"<[^>]+>", "", html_content)


def _run_subprocess(command: list[str], cwd: Path) -> subprocess.CompletedProcess:
    """A wrapper for running subprocess commands."""
    return subprocess.run(
        command, capture_output=True, text=True, check=False, encoding="utf-8", cwd=cwd
    )


# --- Core Logic Classes ---
class GitAgentContext:
    """Manages the agent's file system context and security."""

    def __init__(self, start_dir: str | None = None):
        try:
            initial_path = (
                Path(start_dir).resolve() if start_dir else Path.cwd().resolve()
            )
            if not initial_path.is_dir():
                raise FileNotFoundError(f"Initial directory not found: {start_dir}")

            self.base_path = initial_path
            self.current_path = initial_path
            print_colored(
                Fore.CYAN, f"[Agent] Starting in directory: {self.current_path}"
            )
        except Exception as e:
            print_colored(
                Fore.RED, f"[Agent] Fatal: Failed to set initial directory: {e}"
            )
            sys.exit(1)

    def resolve_path(self, relative_path: str) -> Path | None:
        """Resolves a path relative to the current path and checks security bounds."""
        try:
            resolved = (self.current_path / relative_path).resolve()
            if not resolved.is_relative_to(self.base_path):
                print_colored(
                    Fore.RED,
                    f"[Agent] Security Error: Path access denied outside of {self.base_path}.",
                )
                return None
            return resolved
        except Exception as e:
            print_colored(
                Fore.RED, f"[Agent] Error resolving path '{relative_path}': {e}"
            )
            return None


class AgentTools:
    """Container for all tool implementations callable by the AutoGemini agent."""

    def __init__(self, context: GitAgentContext):
        self.context = context

    def _get_diff(self, staged: bool) -> tuple[str | None, str | None]:
        diff_type = "staged" if staged else "unstaged"
        base_cmd = ["git", "diff", "--staged"] if staged else ["git", "diff"]

        try:
            name_only_cmd = base_cmd + ["--name-only"]
            name_result = _run_subprocess(name_only_cmd, self.context.current_path)
            if name_result.returncode != 0:
                return None, f"Failed to get {diff_type} files: {name_result.stderr}"

            files = [f.strip() for f in name_result.stdout.splitlines() if f.strip()]
            irrelevant_files = {
                "package-lock.json",
                "yarn.lock",
                "pnpm-lock.yaml",
                "uv.lock",
                "poetry.lock",
            }
            is_relevant = lambda f: not (
                f.lower().endswith((".lock", ".lock.json"))
                or f.lower() in irrelevant_files
            )

            filtered_files = [f for f in files if is_relevant(f)]
            if not filtered_files:
                return (
                    None,
                    f"All {diff_type} files are lock files or irrelevant. Nothing to show.",
                )

            diff_cmd = base_cmd + ["--"] + filtered_files
            print_colored(Fore.CYAN, f"[Agent] Running command: {' '.join(diff_cmd)}")
            diff_result = _run_subprocess(diff_cmd, self.context.current_path)
            return diff_result.stdout, diff_result.stderr
        except FileNotFoundError:
            return (
                None,
                "The 'git' command was not found. Please ensure Git is installed.",
            )
        except Exception as e:
            return None, f"An unexpected error occurred during git diff: {e}"

    def get_staged_git_changes(self) -> str:
        stdout, stderr = self._get_diff(staged=True)
        # 优先返回 stdout。只要有 diff 内容，就忽略 stderr 中的警告。
        if stdout:
            return stdout
        # 如果没有 diff 内容，再检查 stderr 是否有真正的错误。
        if stderr:
            return f"Tool execution resulted in a warning/error: {stderr.strip()}"
        return (
            "No changes are staged. Tell the user to stage files with 'git add' first."
        )

    def get_unstaged_git_changes(self) -> str:
        stdout, stderr = self._get_diff(staged=False)
        # 优先返回 stdout。
        if stdout:
            return stdout
        # 如果没有 diff 内容，再检查 stderr。
        if stderr:
            return f"Tool execution resulted in a warning/error: {stderr.strip()}"
        return "No unstaged changes found."

    def list_directory_contents(self, path: str = ".") -> str:
        target_path = self.context.resolve_path(path)
        if not target_path or not target_path.is_dir():
            return f"Error: '{path}' is not a valid directory."
        try:
            contents = [p.name for p in target_path.iterdir()]
            return (
                f"Contents of '{target_path.relative_to(self.context.base_path)}/':\n"
                + "\n".join(contents)
            )
        except Exception as e:
            return f"Error listing directory '{path}': {e}"

    def change_current_directory(self, path: str) -> str:
        new_path = self.context.resolve_path(path)
        if not new_path or not new_path.is_dir():
            return f"Error: '{path}' is not a valid directory."
        self.context.current_path = new_path
        return f"Successfully changed directory to: {self.context.current_path.relative_to(self.context.base_path)}"

    def get_last_commit_message(self) -> str:
        try:
            result = _run_subprocess(
                ["git", "log", "-1", "--pretty=%B"], self.context.current_path
            )
            return (
                result.stdout.strip()
                if result.returncode == 0
                else f"Error: {result.stderr.strip()}"
            )
        except Exception as e:
            return f"Error getting last commit message: {e}"


# --- Configuration and Argument Parsing ---
def setup_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="AutoGemini Git Commit Message Generator.",
        epilog='Examples:\n  auto-git-msg\n  auto-git-msg "Focus on API changes"\n  auto-git-msg --message "fix login"',
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "instruction",
        type=str,
        nargs="?",
        default=None,
        help="High-level instruction for the agent.",
    )
    parser.add_argument(
        "--message",
        type=str,
        default=None,
        help="Provide a message for the AI to optimize.",
    )
    parser.add_argument(
        "-C",
        "--chdir",
        metavar="DIR",
        type=str,
        default=None,
        help="Switch directory before starting.",
    )
    parser.add_argument(
        "--api-key", type=str, default=None, help="Gemini API Key (overrides config)."
    )
    parser.add_argument("--config", type=str, default=None, help="Path to config file.")
    parser.add_argument(
        "--no-cache", action="store_true", help="Do not use or write cache file."
    )
    parser.add_argument(
        "--set-proxy", type=str, help="Set grpc_proxy in user config and exit."
    )
    parser.add_argument(
        "--unset-proxy",
        action="store_true",
        help="Remove grpc_proxy from config and exit.",
    )
    parser.add_argument(
        "--no-grpc-proxy-auto",
        action="store_true",
        help="Disable automatic grpc_proxy setting.",
    )
    return parser


def handle_pre_run_commands(args: argparse.Namespace):
    """Handles commands that exit before the main agent runs (e.g., --set-proxy)."""
    if args.set_proxy or args.unset_proxy:
        config = {}
        if DEFAULT_CACHE_PATH.exists():
            try:
                with open(DEFAULT_CACHE_PATH, "r", encoding="utf-8") as f:
                    config = json.load(f)
            except Exception as e:
                print_colored(
                    Fore.YELLOW, f"[Config] Warning: Could not read cache: {e}"
                )
        if args.set_proxy:
            config[PROXY_FIELD] = args.set_proxy
            print_colored(Fore.GREEN, f"[Config] grpc_proxy set to: {args.set_proxy}")
        elif args.unset_proxy and PROXY_FIELD in config:
            del config[PROXY_FIELD]
            print_colored(Fore.GREEN, "[Config] grpc_proxy removed from config.")
        try:
            with open(DEFAULT_CACHE_PATH, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print_colored(
                Fore.RED, f"[Config] Fatal: Failed to write to config cache: {e}"
            )
            sys.exit(1)
        sys.exit(0)


def configure_proxy(no_auto_proxy: bool):
    """
    Configures the grpc_proxy environment variable with the correct priority.
    """
    if no_auto_proxy:
        return
    if os.environ.get("grpc_proxy") or os.environ.get("GRPC_PROXY"):
        print_colored(Fore.CYAN, "[Proxy] Using existing grpc_proxy from environment.")
        return
    config_proxy = None
    if DEFAULT_CACHE_PATH.exists():
        try:
            with open(DEFAULT_CACHE_PATH, "r", encoding="utf-8") as f:
                config_proxy = json.load(f).get(PROXY_FIELD)
        except Exception:
            pass
    if config_proxy:
        os.environ["grpc_proxy"] = config_proxy
        print_colored(
            Fore.YELLOW, f"[Proxy] Set grpc_proxy from config file: {config_proxy}"
        )
        return
    env_proxy = (
        os.environ.get("https_proxy")
        or os.environ.get("HTTPS_PROXY")
        or os.environ.get("http_proxy")
        or os.environ.get("HTTP_PROXY")
        or os.environ.get("all_proxy")
        or os.environ.get("ALL_PROXY")
    )
    if env_proxy:
        os.environ["grpc_proxy"] = env_proxy
        print_colored(
            Fore.YELLOW,
            f"[Proxy] Set grpc_proxy from environment fallback: {env_proxy}",
        )


def load_configuration(args: argparse.Namespace) -> dict:
    """Loads configuration with priority: CLI arg > config file > cache."""
    if args.api_key:
        if not args.no_cache and not DEFAULT_CACHE_PATH.exists():
            try:
                with open(DEFAULT_CACHE_PATH, "w", encoding="utf-8") as f:
                    json.dump({API_KEY_FIELD: args.api_key}, f)
            except Exception as e:
                print_colored(
                    Fore.YELLOW, f"[Config] Warning: Failed to write cache: {e}"
                )
        return {API_KEY_FIELD: args.api_key}

    config_sources = (
        [args.config, DEFAULT_CACHE_PATH] if not args.no_cache else [args.config]
    )
    for source in config_sources:
        if source:
            config_file = Path(source).expanduser().resolve()
            if config_file.exists():
                try:
                    with open(config_file, "r", encoding="utf-8") as f:
                        config = json.load(f)
                    if API_KEY_FIELD in config:
                        return config
                except Exception as e:
                    print_colored(
                        Fore.RED, f"[Config] Error loading {config_file}: {e}"
                    )
    return {}


# --- Main Execution ---
async def agent_main():
    """The main asynchronous entry point for the agent."""
    args = setup_argument_parser().parse_args()
    handle_pre_run_commands(args)
    configure_proxy(args.no_grpc_proxy_auto)

    agent_context = GitAgentContext(start_dir=args.chdir)
    config = load_configuration(args)

    if not config.get(API_KEY_FIELD):
        print_colored(
            Fore.RED,
            "[System] Fatal: No API key provided. Use --api-key, --config, or setup cache.",
        )
        sys.exit(1)

    agent_tools = AgentTools(context=agent_context)
    tool_codes = [
        ToolCodeInfo(
            name="get_staged_git_changes",
            description="Retrieves staged code changes (diff).",
            detail="Runs `git diff --staged`.",
            args={},
        ),
        ToolCodeInfo(
            name="get_unstaged_git_changes",
            description="Retrieves unstaged code changes (diff).",
            detail="Runs `git diff`.",
            args={},
        ),
        ToolCodeInfo(
            name="list_directory_contents",
            description="Lists contents of a directory.",
            detail="Use to explore project structure.",
            args={"path": "Relative path to list."},
        ),
        ToolCodeInfo(
            name="change_current_directory",
            description="Changes the agent's working directory.",
            detail="Navigate to a subdirectory for focus.",
            args={"path": "Relative path to change to."},
        ),
        ToolCodeInfo(
            name="get_last_commit_message",
            description="Retrieves the last git commit message.",
            detail="Use to reference previous style.",
            args={},
        ),
    ]

    async def api_handler(method_name: str, **kwargs) -> str:
        """Dispatches tool calls to the AgentTools instance."""
        print_colored(
            Fore.CYAN, f"[Agent] Calling tool '{method_name}' with args: {kwargs}"
        )
        if hasattr(agent_tools, method_name):
            result = getattr(agent_tools, method_name)(**kwargs)
            return str(result)
        return f"Unknown tool: {method_name}"

    character_description = "You are an expert Git specialist. Your sole purpose is to create a clear, Conventional Commits-formatted commit message. Analyze the changes using your tools, then provide the formatted HTML for the commit message. Do not add any explanations."

    try:
        processor = create_cot_processor(
            api_key=config[API_KEY_FIELD],
            default_api=DefaultApi(api_handler),
            tool_codes=tool_codes,
            character_description=character_description,
            model=config.get("model", "gemini-2.5-flash"),
            temperature=config.get("temperature", 0.4),
            api_delay=float(config.get("api_delay", 5.0)),
            max_output_size=int(config.get("max_output_size", 65536 * 8)),
        )
    except Exception as e:
        print_colored(
            Fore.RED, f"[System] Fatal: Failed to initialize AutoGemini processor: {e}"
        )
        sys.exit(1)

    if args.message:
        instruction = f"Optimize this commit message to follow Conventional Commits spec:\n\n{args.message.strip()}"
    else:
        instruction = (
            args.instruction or "Generate a git commit message for the staged changes."
        )

    print_colored(Fore.BLUE, f'[System] Sending instruction to agent: "{instruction}"')
    final_response_html = await processor.process_conversation(
        instruction, max_cycle_cost=5
    )

    if final_response_html:
        response_content = next(
            (
                item.content
                for item in parse_agent_output(final_response_html)
                if getattr(item, "type", None) == "response"
            ),
            final_response_html,
        )
        readable_text = convert_html_to_readable_text(response_content.strip())
        print("\n" + "=" * 60)
        print_colored(Fore.GREEN, "AI-Generated Git Commit Message:")
        print("=" * 60 + "\n")
        print(Fore.WHITE + readable_text.strip())
        print("\n" + "=" * 60)
        print_colored(
            Fore.YELLOW, "Copy the message and use it with 'git commit -m \"...\"'"
        )
    else:
        print_colored(
            Fore.RED,
            "[System] The agent did not produce a final response. Check proxy/API key.",
        )
