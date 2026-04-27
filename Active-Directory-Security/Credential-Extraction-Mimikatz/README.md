# 🔑 Lab: Automated Credential Extraction with Mimikatz
**Category:** Active Directory Security / Post-Exploitation | **Tools:** Python, Mimikatz, Subprocess | **Focus:** LSASS Memory Dump

## 📖 Project Overview
Developed a Python automation framework, `mimikatz_final.py`, to streamline the execution of credential theft attacks in a Windows environment. The script automates the interaction with Mimikatz to escalate privileges and dump `sekurlsa` logon passwords from memory, simulating a sophisticated post-exploitation scenario.

## 🎯 Technical Objectives
* **Process Automation:** Utilized Python’s `subprocess` module to programmatically execute Mimikatz commands, bypassing the need for manual CLI interaction.
* **Privilege Escalation:** Automated the `privilege::debug` command to ensure the script has the necessary rights to interact with the Local Security Authority Subsystem Service (LSASS).
* **Execution Logging:** Implemented an auditing mechanism to track command execution, ensuring all penetration testing activities are logged for compliance and "Rules of Engagement" (RoE) tracking.
* **Security Validation:** Integrated environment checks to verify the presence and path of security tools before execution, preventing script failure in a live audit.



## 🛠️ The Extraction Workflow
1. **Validation:** The script verifies the path to the Mimikatz binary.
2. **Escalation:** Executes `privilege::debug` to gain access to system-level processes.
3. **Extraction:** Runs `sekurlsa::logonpasswords` to extract cleartext passwords and hashes from memory.
4. **Audit:** Logs the activity to `mimikatz_log.txt` while displaying the technical output to the tester.

[Link to Technical PDF Report](./AD_PenTest_Mimikatz_Automation_Report_Solomon_Waikumi.pdf)
