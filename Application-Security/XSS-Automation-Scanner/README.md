# 🛡️ Lab: Automated Reflected XSS Vulnerability Scanner
**Category:** Application Security (AppSec) | **Tools:** Python, Requests, Flask (Sandbox) | **Focus:** OWASP A03:2021 Injection

## 📖 Project Overview
In this lab, I acted as an AppSec Analyst for a healthcare portal to identify Reflected Cross-Site Scripting (XSS) vulnerabilities. I developed a Python-based automation tool, `vuln_scanner.py`, that programmatically tests search endpoints with multiple payloads to verify if user input is properly sanitized before being rendered in the browser.

## 🎯 Technical Objectives
* **Payload Engineering:** Implemented a suite of XSS test vectors to simulate common attacker bypass techniques.
* **Automated Detection Logic:** Developed a script using the `requests` library to analyze HTTP responses for reflected input, distinguishing between secure and vulnerable endpoints.
* **Resilient Automation:** Integrated error handling for connection timeouts and URL failures to ensure tool stability during large-scale audits.
* **Risk Mitigation:** Analyzed findings to recommend secure coding practices, specifically context-aware output encoding and Content Security Policy (CSP) implementation.



## 🛠️ The Scanner Workflow
1. **Targeting:** The script targets a specific web form or search parameter.
2. **Injection:** Automatically submits various `<script>` tags and obfuscated payloads.
3. **Verification:** Scans the raw HTML of the response; if the payload is found verbatim, the endpoint is flagged as **Vulnerable**.
4. **Reporting:** Generates a clean console output summarizing the security posture of each tested payload.

[Link to Technical PDF Report](./Web_App_Security_XSS_Report_Solomon_Waikumi.pdf)
