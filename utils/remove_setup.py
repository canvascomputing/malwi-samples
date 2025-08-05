#!/usr/bin/env python3
"""
Remove setup() function calls from Python files using tree-sitter.
This is a safer and more accurate method than regex or LLM-based approaches.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional, List, Tuple
import tree_sitter
import tree_sitter
import tree_sitter_python as tspython


class SetupRemover:
    def __init__(self):
        """Initialize the tree-sitter parser for Python."""
        self.parser = tree_sitter.Parser()
        self.parser.language = tree_sitter.Language(tspython.language())
        
    def find_setup_calls(self, tree, source_code: bytes) -> List[Tuple[int, int, bool]]:
        """
        Find all setup() function calls in the syntax tree.
        Returns a list of (start_byte, end_byte, contains_definitions) tuples for each setup call.
        contains_definitions is True if the setup call contains function or class definitions.
        """
        setup_calls = []
        
        def contains_function_or_class_definitions(node):
            """Check if a node contains any function or class definitions."""
            if node.type in ['function_definition', 'class_definition']:
                return True
            
            # Check all children recursively
            for child in node.children:
                if contains_function_or_class_definitions(child):
                    return True
            
            return False
        
        def traverse(node):
            """Recursively traverse the syntax tree looking for setup() calls."""
            if node.type == 'call':
                # Check if this is a call to 'setup'
                function_node = node.child_by_field_name('function')
                if function_node and function_node.type == 'identifier':
                    func_name = source_code[function_node.start_byte:function_node.end_byte].decode('utf-8')
                    if func_name == 'setup':
                        # Found a setup() call
                        # Check if it contains function or class definitions
                        has_definitions = contains_function_or_class_definitions(node)
                        setup_calls.append((node.start_byte, node.end_byte, has_definitions))
            
            # Recursively check all children
            for child in node.children:
                traverse(child)
        
        traverse(tree.root_node)
        return setup_calls
    
    def remove_setup_from_code(self, source_code: str) -> Tuple[str, int, int]:
        """
        Remove all setup() calls from the source code.
        Preserves setup() calls that contain function or class definitions.
        Returns the modified code, number of setup calls removed, and number preserved.
        """
        # Parse the source code
        source_bytes = source_code.encode('utf-8')
        tree = self.parser.parse(source_bytes)
        
        # Find all setup() calls
        setup_calls = self.find_setup_calls(tree, source_bytes)
        
        if not setup_calls:
            return source_code, 0, 0
        
        # Separate calls to remove vs preserve
        calls_to_remove = [(start, end) for start, end, has_defs in setup_calls if not has_defs]
        calls_to_preserve = [(start, end) for start, end, has_defs in setup_calls if has_defs]
        
        if not calls_to_remove:
            # All setup calls contain definitions and should be preserved
            return source_code, 0, len(calls_to_preserve)
        
        # Sort by start position (in reverse order) to remove from end to beginning
        calls_to_remove.sort(key=lambda x: x[0], reverse=True)
        
        # Create a mutable byte array
        result = bytearray(source_bytes)
        
        # Remove each setup call by replacing with spaces
        for start_byte, end_byte in calls_to_remove:
            # Replace the setup call with comment
            replacement = b'# setup(...) removed'
            # If the setup call is longer than our replacement, pad with spaces
            if end_byte - start_byte > len(replacement):
                replacement = replacement + b' ' * (end_byte - start_byte - len(replacement))
            elif end_byte - start_byte < len(replacement):
                # If replacement is longer, just use the exact length
                replacement = b'# removed'
                if end_byte - start_byte > len(replacement):
                    replacement = replacement + b' ' * (end_byte - start_byte - len(replacement))
                else:
                    replacement = b'#' * (end_byte - start_byte)
            
            result[start_byte:end_byte] = replacement
        
        return result.decode('utf-8'), len(calls_to_remove), len(calls_to_preserve)
    
    def process_file(self, file_path: Path, dry_run: bool = False, verbose: bool = False) -> Tuple[bool, int, int]:
        """
        Process a single Python file to remove setup() calls.
        Returns (was_modified, num_removed, num_preserved).
        """
        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Remove setup calls
            modified_content, num_removed, num_preserved = self.remove_setup_from_code(original_content)
            
            if num_removed > 0:
                if dry_run:
                    print(f"Would remove {num_removed} setup() call(s) from: {file_path}")
                    if num_preserved > 0:
                        print(f"  Preserving {num_preserved} setup() call(s) with function/class definitions")
                else:
                    # Write the modified content back
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(modified_content)
                    print(f"Removed {num_removed} setup() call(s) from: {file_path}")
                    if num_preserved > 0:
                        print(f"  Preserved {num_preserved} setup() call(s) with function/class definitions")
                return True, num_removed, num_preserved
            else:
                if num_preserved > 0:
                    if dry_run or verbose:
                        print(f"Preserved all {num_preserved} setup() call(s) in: {file_path} (contain definitions)")
                elif verbose:
                    print(f"No setup() calls found in: {file_path}")
                return False, 0, num_preserved
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False, 0, 0
    
    def process_directory(self, directory: Path, dry_run: bool = False, verbose: bool = False) -> Tuple[int, int, int, int]:
        """
        Recursively process all Python files in a directory.
        Returns (files_modified, total_files_processed, total_removed, total_preserved).
        """
        files_modified = 0
        total_files = 0
        total_removed = 0
        total_preserved = 0
        
        for py_file in directory.rglob("*.py"):
            total_files += 1
            was_modified, num_removed, num_preserved = self.process_file(py_file, dry_run, verbose)
            if was_modified:
                files_modified += 1
            total_removed += num_removed
            total_preserved += num_preserved
        
        return files_modified, total_files, total_removed, total_preserved


def main():
    parser = argparse.ArgumentParser(
        description="Remove setup() function calls from Python files using tree-sitter.\n"
                    "Preserves setup() calls that contain function or class definitions\n"
                    "as they may contain critical malicious logic for analysis.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "path",
        help="Path to a Python file or directory to process"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics after processing"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed output including preserved setup calls"
    )
    
    args = parser.parse_args()
    
    path = Path(args.path)
    if not path.exists():
        print(f"Error: Path '{path}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    # Create the remover
    remover = SetupRemover()
    
    # Process the path
    if path.is_file():
        if path.suffix != '.py':
            print(f"Error: '{path}' is not a Python file.", file=sys.stderr)
            sys.exit(1)
        
        was_modified, num_removed, num_preserved = remover.process_file(path, args.dry_run, args.verbose)
        if args.stats:
            print(f"\nProcessed 1 file:")
            print(f"  Setup calls removed: {num_removed}")
            print(f"  Setup calls preserved: {num_preserved}")
            print(f"  File {'modified' if was_modified else 'unchanged'}.")
    else:
        # It's a directory
        print(f"Processing directory: {path}")
        if not args.dry_run:
            print("WARNING: This will modify files in place. Use --dry-run to preview changes.")
            print("Setup() calls containing function/class definitions will be preserved.")
            response = input("Continue? (y/n): ")
            if response.lower() != 'y':
                print("Aborted.")
                sys.exit(0)
        
        files_modified, total_files, total_removed, total_preserved = remover.process_directory(
            path, args.dry_run, args.verbose
        )
        
        if args.stats or True:  # Always show stats for directories
            print(f"\nStatistics:")
            print(f"  Total Python files processed: {total_files}")
            print(f"  Files modified: {files_modified}")
            print(f"  Files unchanged: {total_files - files_modified}")
            print(f"  Total setup() calls removed: {total_removed}")
            print(f"  Total setup() calls preserved: {total_preserved}")
            if total_preserved > 0:
                print(f"\n  Note: {total_preserved} setup() calls were preserved because they contain")
                print(f"        function or class definitions that may be malicious.")


if __name__ == "__main__":
    main()