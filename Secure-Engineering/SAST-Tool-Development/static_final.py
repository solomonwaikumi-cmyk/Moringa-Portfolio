#!/usr/bin/env python3
import os
import ast
import argparse
import json
import sys

# Scenario: Junior Penetration Tester - Manufacturing Facility
# Mission: Identify vulnerabilities in software controlling production equipment.

# 1. Function to recursively search for Python files
def collect_source_files(directory):
    """
    Recursively searches a directory for Python files (.py).
    """
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

# 2. Function to parse code into an Abstract Syntax Tree (AST)
def parse_source_code(file_path):
    """
    Reads a source file and converts it into an AST.
    Handles I/O and parsing errors.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as source:
            return ast.parse(source.read(), filename=file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        return None
    except SyntaxError as e:
        print(f"Error parsing syntax in {file_path}: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred parsing {file_path}: {e}", file=sys.stderr)
        return None

# 3. Define Vulnerability Patterns and Helper Function
# We focus on functions often used for Command Injection or Insecure Deserialization
UNSAFE_FUNCTIONS = {
    # Command Execution
    'eval', 'exec', 'os.system', 'subprocess.call', 'subprocess.run', 'subprocess.Popen',
    # Insecure Deserialization
    'pickle.loads', 'pickle.load', 'yaml.load', 'marshal.load', 'shelve.open',
    # Input Sources (often lead to vulnerabilities if not sanitized)
    'input',
    # Other potentially risky functions/modules
    'os.popen', 'os.execv', 'os.execl', 'os.execle', 'os.execvp', 'os.execvpe',
    'shutil.rmtree', # Can be dangerous if path is untrusted
    'tempfile.mkstemp', 'tempfile.mkdtemp', # Can be dangerous if permissions are not set correctly
    'ctypes.CDLL', 'ctypes.WinDLL', 'ctypes.PyDLL', # Loading arbitrary libraries
    'xml.etree.ElementTree.parse', 'xml.sax.parse', # XML External Entity (XXE) risks
    'json.loads', # If used with object_hook and untrusted data
}

def is_vulnerable_function(node):
    """
    Checks AST nodes for the use of unsafe functions.
    """
    if isinstance(node, ast.Call):
        # Handle simple calls like eval()
        if isinstance(node.func, ast.Name):
            if node.func.id in UNSAFE_FUNCTIONS:
                return True, node.func.id
        
        # Handle attribute calls like os.system() or pickle.loads()
        elif isinstance(node.func, ast.Attribute):
            # Extract the full name, e.g., 'os.system', 'pickle.loads'
            if isinstance(node.func.value, ast.Name):
                full_func_name = f"{node.func.value.id}.{node.func.attr}"
                if full_func_name in UNSAFE_FUNCTIONS:
                    return True, full_func_name
            # Handle nested attributes like 'module.submodule.func'
            elif isinstance(node.func.value, ast.Attribute):
                # This part can be expanded for deeper nesting if needed
                # For simplicity, we'll just check the immediate parent. 
                # A more robust solution would recursively build the full path.
                pass # Current UNSAFE_FUNCTIONS are mostly module.func or func
                
    return False, None

# 4. Function to traverse and analyze the AST
def analyze_ast(tree, file_path):
    """
    Analyzes the AST of a source file for potential vulnerabilities.
    Returns a list of found issues.
    """
    issues = []
    for node in ast.walk(tree):
        vulnerable, func_name = is_vulnerable_function(node)
        if vulnerable:
            issue = {
                "file": file_path,
                "line": getattr(node, 'lineno', 'unknown'),
                "col": getattr(node, 'col_offset', 'unknown'), # Added column offset
                "issue": f"Use of unsafe function '{func_name}'"
            }
            issues.append(issue)
    return issues

# 5. Main function to tie everything together
def main():
    parser = argparse.ArgumentParser(description="Perform static analysis on Python code for security vulnerabilities.")
    parser.add_argument("target_directory", help="The directory path to scan for Python files.")
    parser.add_argument("-o", "--output", choices=['text', 'json'], default='text',
                        help="Output format for the report (default: text).")
    parser.add_argument("-f", "--output_file", help="Optional: Path to save the report to a file.")
    args = parser.parse_args()

    if not os.path.isdir(args.target_directory):
        print(f"Error: Invalid directory path: {args.target_directory}", file=sys.stderr)
        sys.exit(1)

    print(f"\nScanning directory: {args.target_directory}")
    source_files = collect_source_files(args.target_directory)
    
    if not source_files:
        print("No Python files found in the target directory.")
        sys.exit(0)

    all_issues = []
    for file_path in source_files:
        print(f"  Analyzing {file_path}...")
        tree = parse_source_code(file_path)
        if tree:
            file_issues = analyze_ast(tree, file_path)
            all_issues.extend(file_issues)

    # Reporting the findings
    report_content = ""
    if args.output == 'json':
        report_content = json.dumps(all_issues, indent=4)
    else: # text format
        report_content += "\n" + "="*50 + "\n"
        report_content += "STATIC ANALYSIS SECURITY REPORT\n"
        report_content += "="*50 + "\n"
        
        if not all_issues:
            report_content += "No vulnerabilities detected.\n"
        else:
            report_content += f"Found {len(all_issues)} potential vulnerabilities:\n\n"
            for issue in all_issues:
                report_content += f"FILE: {issue['file']}\n"
                report_content += f"LINE: {issue['line']}, COL: {issue['col']}\n"
                report_content += f"ISSUE: {issue['issue']}\n"
                report_content += "-" * 30 + "\n"
    
    if args.output_file:
        try:
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"Report saved to {args.output_file}")
        except IOError as e:
            print(f"Error saving report to {args.output_file}: {e}", file=sys.stderr)
    else:
        print(report_content)

if __name__ == "__main__":
    main()