# 🛠️ Lab: Static Application Security Testing (SAST) Tool Development
**Category:** Secure Software Development (DevSecOps) | **Tools:** Python, AST Module, Static Analysis

## 📖 Project Overview
Developed a custom Static Application Security Testing (SAST) tool, `static_final.py`, designed to scan Python source code for common security vulnerabilities. The tool focuses on detecting unsafe function calls that could lead to Command Injection or Arbitrary Code Execution in production environments.

## 🎯 Technical Objectives
* **Abstract Syntax Tree (AST) Parsing:** Implemented the `ast` module to convert raw source code into a structured tree, allowing for deep logical analysis rather than simple text searching.
* **Vulnerability Pattern Matching:** Defined a signature database of "unsafe functions" (e.g., `eval`, `exec`, `input`, `os.system`) that are high-risk for exploitation.
* **Recursive Directory Scanning:** Built a robust file discovery engine to crawl complex project structures and identify all `.py` files for analysis.
* **Automated Reporting:** Created a reporting module that maps vulnerabilities back to their exact line numbers and file paths for developer remediation.

## 🛠️ The "Shift Left" Workflow
1. **Discovery:** Recursively gathering all source files within a target directory.
2. **Parsing:** Generating an AST for every file to understand the program's intent and structure.
3. **Traversal:** Walking through the AST nodes to identify high-risk function calls.
4. **Analysis:** Comparing nodes against known vulnerability patterns.
5. **Remediation Report:** Generating a structured summary for the development team to prioritize security patches.

## 🔍 Key Capabilities
* **Precision:** By using AST instead of Regex, the tool minimizes false positives by understanding the context of the code.
* **Scalability:** The script can be integrated into a CI/CD pipeline to automatically scan code on every "git push."

[Link to Technical Write-up](./SAST_Tool_Development_Source_Code_Analysis.pdf) | [View the Python Script](./static_final.py)
