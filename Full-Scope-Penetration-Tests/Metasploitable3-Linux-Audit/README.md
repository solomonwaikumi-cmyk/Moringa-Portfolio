# 🛡️ Summative Lab: Full-Scope Linux Penetration Test
**Category:** Red Teaming / Infrastructure Audit | **Target:** Metasploitable 3 (Linux) | **Tools:** Nmap, Metasploit, Netcat, Enum4linux

## 📖 Engagement Overview
As a Junior Penetration Tester, I conducted a full-scope assessment of a Linux-based infrastructure to identify security weaknesses and demonstrate potential attack vectors. This project follows the complete Penetration Testing Execution Standard (PTES), moving from silent reconnaissance to full system compromise and persistence.

## 🎯 Technical Objectives
* **Comprehensive Reconnaissance:** Executed full-port TCP/UDP scans and service fingerprinting to map the attack surface.
* **Vulnerability Analysis:** Identified critical misconfigurations in legacy services, specifically targeting outdated versions of ProFTPD and Samba.
* **Multi-Vector Exploitation:** Leveraged the Metasploit Framework to gain initial access and utilized manual techniques to bypass version-mismatched modules.
* **Post-Exploitation & Persistence:** Demonstrated the ability to escalate privileges to `root` and establish long-term access via automated system tasks.



## 🛠️ The Audit Workflow
1. **Phase 1: Recon & Enumeration:** identified services including FTP (21), SSH (22), HTTP (80/3500), and SMB (445).
2. **Phase 2: Vulnerability Research:** Cross-referenced service versions (ProFTPD 1.3.5) with known CVEs (CVE-2015-3306).
3. **Phase 3: Exploitation:** Successfully exploited the Samba "Username Map Script" vulnerability to achieve an unauthenticated remote shell.
4. **Phase 4: Post-Exploitation:** Executed system discovery commands (`whois`, `sysinfo`) and implemented persistence mechanisms.

[Link to Full Technical PDF Report](./Summative_Penetration_Testing_Report_Solomon_Mwaura.pdf)
