import re

def check_trailing_whitespace(code):
    """Check for lines with trailing whitespace."""
    lines_with_issues = []
    for i, line in enumerate(code.splitlines(), 1):
        if re.search(r'[ \t]+$', line):
            lines_with_issues.append(i)
    return lines_with_issues

def check_missing_newline(code):
    """Check if the file ends without a newline."""
    return not code.endswith('\n')

def run_linter(file_path):
    """Run basic linting on the given file."""
    with open(file_path, 'r') as file:
        code = file.read()
    
    # Check for issues
    trailing_whitespace_lines = check_trailing_whitespace(code)
    missing_newline = check_missing_newline(code)
    
    # Report issues
    if trailing_whitespace_lines:
        print(f"Linting issue: Trailing whitespace found on lines: {trailing_whitespace_lines}")
    if missing_newline:
        print("Linting issue: File does not end with a newline.")
    
    if not trailing_whitespace_lines and not missing_newline:
        print(f"{file_path} passed linting successfully.")
    else:
        print(f"{file_path} has linting issues.")

if __name__ == "__main__":
    sample_code = "def example():    \n    print('Hello, World!')\n"
    with open("sample_file.py", "w") as f:
        f.write(sample_code)
    
    run_linter("sample_file.py")
