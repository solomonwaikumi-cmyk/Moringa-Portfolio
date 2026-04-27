# 🔍 Lab: Internal Network Scanning & Service Enumeration
**Category:** Offensive Security / Infrastructure Audit | **Tools:** Nmap, Enum4linux, Metasploitable 2

## 📖 Project Overview
Conducted a comprehensive network reconnaissance and enumeration assessment on a simulated healthcare staging environment (Metasploitable 2). This lab focused on identifying misconfigured services and outdated software versions that present a high risk of exploitation during an audit.

## 🎯 Technical Objectives
* **Host Discovery:** Used ICMP and ARP ping sweeps to identify active assets within the virtual network.
* **Service Enumeration:** Performed version detection scans (`-sV`) and default script scans (`-sC`) using **Nmap** to identify the software stack of the target.
* **SMB Analysis:** Utilized **Enum4linux** to extract user lists, share names, and OS information from the SMB service (Port 445).
* **Attack Surface Mapping:** Categorized identified ports by risk level and documented the specific vulnerabilities associated with detected versions (e.g., FTP, SSH, and HTTP).



## 🛠️ Methodology
1. **Initial Recon:** Standard Nmap TCP connect scan to identify all 65,535 ports.
2. **Deep Dive:** Targeted scans on high-value ports (21, 22, 80, 139/445).
3. **User Enumeration:** Exploiting SMB null sessions to map the internal user structure.
4. **Documentation:** Compiling findings into a structured penetration testing report for executive review.

## 🔍 Key Findings
* **Broken Authentication:** Identified services with default configurations.
* **Information Disclosure:** SMB shares allowed anonymous enumeration of system users.
* **Vulnerable Versions:** Detected outdated service versions known for backdoor vulnerabilities.

[Link to Technical PDF Report](./Internal_Network_Scanning_and_Enumeration_Report.pdf)
