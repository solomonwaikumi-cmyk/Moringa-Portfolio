# 🔑 Lab: Password Strength Analysis & Social Engineering Defense
**Category:** Defensive Engineering / Security Awareness | **Tools:** Python (String Analysis, Logic Gates)

## 📖 Project Overview
To combat the risk of social engineering and credential harvesting, I developed `pw_final.py`, a Python-based utility that audits password strength. This tool serves as a frontline defense by educating users on password entropy and enforcing corporate security standards.

## 🎯 Technical Objectives
* **Complexity Validation:** Implemented checks for uppercase, lowercase, numerical, and special character requirements.
* **Length Analysis:** Enforced minimum length requirements to defend against modern brute-force hardware.
* **Heuristic Feedback:** Developed a recommendation engine that provides specific, actionable feedback to users rather than generic "weak password" alerts.
* **Input Validation:** Ensured robust handling of user data to prevent script errors during the analysis phase.

## 🛡️ Defensive Criteria
The script evaluates passwords against four primary pillars of credential security:
1. **Length:** Minimum 8+ characters to increase the time required for cracking.
2. **Casing:** Mixing upper and lower case to expand the character set.
3. **Diversity:** Requiring digits and special characters (`!@#$%^&*`) to defeat dictionary attacks.
4. **Actionable Recommendations:** Providing clear steps (e.g., "Add a special character") to improve security posture.

## 🔍 Impact
This project demonstrates the ability to build internal security tools that reduce the organization's attack surface by mitigating the risk of compromised accounts—the primary goal of most social engineering campaigns.

[Link to Technical Write-up](./Password_Complexity_and_Social_Engineering_Defense.pdf) | [View the Python Script](./pw_final.py)
