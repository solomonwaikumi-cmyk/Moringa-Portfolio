# 🌐 Lab: OSINT Reconnaissance Automation
**Category:** Reconnaissance / Threat Intelligence | **Tools:** Python, Shodan API, WHOIS, JSON

## 📖 Project Overview
This project involved developing a specialized reconnaissance tool, `OSINT_final.py`, designed to automate the collection of publicly available intelligence. By integrating domain registration data and global IoT scanning via Shodan, the tool maps an organization’s external attack surface and identifies potentially exposed services.

## 🎯 Technical Objectives
* **Domain Attribution:** Automated the retrieval of WHOIS data to identify domain ownership, registration dates, and name server configurations.
* **IoT/Infrastructure Intelligence:** Integrated the **Shodan API** to resolve domain names to IP addresses and scan for open ports, running services, and known vulnerabilities.
* **Security Evasion:** Implemented custom **User-Agent headers** to mimic legitimate browser traffic and prevent blocking during reconnaissance.
* **Structured Data Collection:** Built a JSON export engine to store findings in a machine-readable format for further analysis or SIEM ingestion.

## 🛠️ The Recon Workflow
1. **Enumeration:** Gathering basic domain registry details via the `python-whois` library.
2. **DNS Resolution:** Using Shodan’s DNS endpoints to identify the target's hosting environment.
3. **Service Mapping:** Fetching detailed host reports, including open ports (e.g., SSH, RDP, HTTP) and banner information.
4. **Data Aggregation:** Consolidating all OSINT data into a centralized `osint_report.json`.



## 🔍 Key Capabilities
* **Speed:** Replaces manual browser-based searches with a single, multi-threaded-ready script.
* **Anonymity-Aware:** Uses specific request headers to maintain a lower profile during active scanning.
* **API Integration:** Demonstrates professional competence in handling API keys and RESTful requests.

[Link to Technical Report](./OSINT_Automation_and_Attack_Surface_Mapping_Report.pdf) | [View the Python Script](./OSINT_final.py)
