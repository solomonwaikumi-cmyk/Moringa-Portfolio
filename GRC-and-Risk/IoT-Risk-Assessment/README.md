# 🚦 Lab: Smart City IoT Security Risk Assessment
**Category:** Cybersecurity Consulting / Risk Management | **Focus:** Critical Infrastructure, IoT Vulnerabilities

## 📖 Project Overview
As a Cybersecurity Consultant for *MetroTraffic Solutions*, I performed a comprehensive security audit of a Smart City Traffic Management System. The goal was to identify critical vulnerabilities in connected traffic lights, CCTV cameras, and vehicle sensors that could lead to public safety risks or data breaches.

## ⚠️ Critical Vulnerabilities Identified
* **Broken Authentication:** Discovered the use of default credentials (`admin/admin`) and hardcoded passwords across the `CityFlow-4000` and `VisionEye-200` devices.
* **Insecure Communications:** Identified unencrypted remote management (HTTP) and the use of outdated TLS 1.0 protocols, susceptible to Man-in-the-Middle (MitM) attacks.
* **Lack of Centralized Monitoring:** Logs were stored locally on devices rather than a centralized SIEM, preventing real-time incident detection.
* **Physical Exposure:** Vehicle density sensors possessed exposed USB ports, allowing for unauthorized firmware tampering.

## ⚖️ Compliance & Governance
* **GDPR Alignment:** Evaluated data retention policies and identified a lack of automated anonymization for vehicle tracking logs.
* **Shared Access:** Flagged the absence of Role-Based Access Control (RBAC) and the high-risk practice of shared administrative credentials.

## 🛡️ Strategic Mitigation Roadmap
1. **Hardening:** Immediate enforcement of a "No Default Password" policy and disabling unnecessary services (Telnet/FTP).
2. **Network Isolation:** Strengthening VLAN segmentation to air-gap the IoT traffic network from the municipal IT network.
3. **Log Centralization:** Integration of Edge Gateway logs into a centralized SIEM for real-time alerting.
4. **Encryption Upgrade:** Transitioning all traffic to HTTPS and AES-256 for data at rest.

[Link to Full Risk Assessment Report](./Smart_City_IoT_Security_Risk_Assessment.pdf)
