import os
import requests
import argparse
import sys

# --- Configuration ---
# Default OLLama API endpoint and model.
# Make sure OLLama is running and the desired model is downloaded.
# You can check available models by running `ollama list` in your terminal.
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codestral:latest"  # A model like 'codellama' is also a great choice

# The default prompt can now be overridden from the command line.
# Note the {file_content} placeholder which will be filled by the script.
DEFAULT_PROMPT = """You are an expert Python code refactoring assistant. Your only task is to comment out the `setup()` function call in the provided Python script.
The function call might be from `distutils.core` or `setuptools`. The entire call to `setup(...)`, including all its arguments which may span multiple lines, must be commented out.
Use a multi-line string (triple single quotes: ''') to comment out the `setup(...)` block. Place the opening `'''` on the line just before the `setup(` call and the closing `'''` on the line just after the final closing parenthesis `)`.
CRITICAL: Do not add any other text, explanations, or markdown code fences like ```python. Only return the raw, modified Python code.
If no `setup()` function call is found, you MUST return the original code block completely unchanged.

Here is the code:
---
{file_content}
---
"""


def clean_llm_response(response_text: str) -> str:
    """
    Cleans the LLM's response to get only the code, removing markdown
    fences that are sometimes added despite instructions.
    """
    lines = response_text.strip().split("\n")
    # Remove ```python or ``` at the start
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    # Remove ``` at the end
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines)


def process_file(
    file_path: str, ollama_url: str, model_name: str, prompt_template: str
):
    """Reads a file, sends it to OLLama for modification, and saves it back."""
    print(f"🔍 Processing file: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_content = f.read()

        # Quick check to avoid sending irrelevant files to the LLM
        if "setup(" not in original_content:
            print("   -> Skipping, 'setup(' keyword not found.")
            return

        # Format the prompt template with the actual file content
        prompt = prompt_template.format(file_content=original_content)

        payload = {"model": model_name, "prompt": prompt, "stream": False}

        print("   -> Sending to OLLama for refactoring...")
        # Set a generous timeout for the LLM to process the code
        response = requests.post(ollama_url, json=payload, timeout=180)
        response.raise_for_status()  # Raise an exception for HTTP errors

        response_data = response.json()
        modified_content = clean_llm_response(response_data.get("response", ""))

        if not modified_content:
            print("   -> ❌ Error: Received an empty response from OLLama.")
            return

        # Only write to the file if the content has actually changed
        if modified_content.strip() != original_content.strip():
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)
            print("   -> ✅ File modified and saved.")
        else:
            print("   -> No changes were needed.")

    except requests.exceptions.RequestException as e:
        print(f"   -> ❌ HTTP Error processing {file_path}: {e}")
        print("   -> Is the OLLama server running and reachable?")
    except FileNotFoundError:
        print(f"   -> ❌ Error: File not found at {file_path}")
    except Exception as e:
        print(f"   -> ❌ An unexpected error occurred with {file_path}: {e}")


def main():
    """Parses arguments and orchestrates the file processing."""
    parser = argparse.ArgumentParser(
        description="Recursively search for Python files and use OLLama to comment out the setup() function.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "directory", help="The target directory to search for Python files."
    )
    parser.add_argument(
        "--url", default=OLLAMA_URL, help=f"The OLLama API URL (default: {OLLAMA_URL})."
    )
    parser.add_argument(
        "--model",
        default=MODEL_NAME,
        help=f"The OLLama model to use (default: {MODEL_NAME}).",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help="The prompt template to use with the LLM. Must include '{file_content}' placeholder.",
    )
    args = parser.parse_args()

    target_dir = args.directory
    if not os.path.isdir(target_dir):
        print(f"Error: Directory '{target_dir}' not found.", file=sys.stderr)
        sys.exit(1)

    # --- Safety Warning and Confirmation ---
    print("=" * 60)
    print("⚠️  DANGER: THIS SCRIPT WILL OVERWRITE FILES IN PLACE! ⚠️")
    print("=" * 60)
    print(f"\nThis script will recursively scan '{target_dir}' and ask an LLM")
    print("to modify any Python file that appears to contain a setup() function.")
    print(
        "\n>>> PLEASE BACK UP YOUR DIRECTORY OR USE VERSION CONTROL BEFORE PROCEEDING. <<<\n"
    )

    try:
        confirm = input("Are you absolutely sure you want to continue? (yes/no): ")
        if confirm.lower() != "yes":
            print("Operation cancelled.")
            sys.exit(0)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(0)

    print(f"\n🚀 Starting recursive search in '{target_dir}'...\n")
    for root, _, files in os.walk(target_dir):
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                process_file(file_path, args.url, args.model, args.prompt)

    print("\nScript finished.")


if __name__ == "__main__":
    main()
