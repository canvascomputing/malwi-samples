import re

def format_code(code):
    # Remove trailing whitespaces
    code = re.sub(r'[ \t]+$', '', code, flags=re.MULTILINE)
    
    # Ensure newline at the end of file
    if not code ends with '\n':
        code += '\n'
    
    # Replace tabs with 4 spaces
    code = code.replace('\t', '    ')
    
    # Additional formatting can be added here
    return code

def format_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    
    formatted_code = format_code(code)
    
    with open(file_path, 'w') as file:
        file.write(formatted_code)
    
    print(f"Formatted {file_path} successfully.")

if __name__ == "__main__":
    sample_code = "def example():\n\tprint('Hello, World!')\n"
    formatted_code = format_code(sample_code)
    print(f"Original Code:\n{sample_code}")
    print(f"Formatted Code:\n{formatted_code}")