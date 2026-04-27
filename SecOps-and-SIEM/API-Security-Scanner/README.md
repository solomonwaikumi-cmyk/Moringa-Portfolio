# ☁️ Lab: Automated AWS API Gateway Security Scanner
**Category:** Cloud Security / DevSecOps | **Tools:** Python, Boto3 (AWS SDK), REST API Auditing

## 📖 Project Overview
Developed a custom Python security tool, `API_final.py`, designed to audit AWS API Gateway configurations. The script simulates a cloud security scan to identify critical misconfigurations, weak authentication mechanisms, and insecure communication protocols that could lead to data exposure or unauthorized access.

## 🎯 Technical Objectives
* **Cloud Asset Enumeration:** Simulated the discovery of API Gateway instances within an AWS environment using the Boto3 SDK.
* **Vulnerability Scanning:** Developed a detection engine to flag:
  * **Missing Authentication:** Identifying open endpoints accessible to the public.
  * **Insecure Transport:** Detecting APIs that fail to enforce HTTPS (unencrypted traffic).
  * **CORS Misconfigurations:** Flagging overly permissive `Access-Control-Allow-Origin: *` settings.
* **Authentication Auditing:** Evaluating the strength of authentication (e.g., Cognito vs. None/Basic).
* **Automation & Scheduling:** Implemented a continuous monitoring loop to re-run scans every 5 minutes, simulating a real-world SOC automation.

## 🛠️ The Audit Workflow
1. **Discovery:** Listing all registered API Gateways.
2. **Configuration Analysis:** Fetching security metadata for each endpoint.
3. **Risk Scoring:** Flagging high-risk issues like unencrypted traffic or missing auth.
4. **Continuous Monitoring:** Scheduling the script to provide near real-time visibility into the cloud security posture.

## 🔍 Key Findings
* **Broken Authentication:** The scanner successfully identified endpoints lacking authentication, which is the #1 risk in the OWASP API Security Top 10.
* **Proactive Defense:** By identifying permissive CORS settings, the tool helps prevent cross-origin attacks and data exfiltration.

[Link to Technical Write-up](./Cloud_API_Security_Audit_Automation_Report.pdf) | [View the Python Script](./API_final.py)
