# 🚗 Lab: Automotive Threat Modeling (STRIDE & ISO/SAE 21434)
**Category:** Risk Management / Automotive Security | **Frameworks:** STRIDE, ISO/SAE 21434, NIST

## 📖 Project Overview
Conducted a comprehensive threat modeling analysis for *AutoDrive Manufacturing*, a leader in autonomous vehicle technology. This project focused on securing the ecosystem of cloud-based telemetry, Over-the-Air (OTA) updates, and ADAS systems against sophisticated cyber threats.

## 🎯 Threat Analysis: The STRIDE Framework
I applied the STRIDE methodology to identify vulnerabilities across the vehicle-to-cloud infrastructure:

| Threat Category | Identified Risk | Mitigation Strategy |
| :--- | :--- | :--- |
| **Spoofing** | Unauthorized vehicle authentication attempts. | Digital certificates & MFA for remote diagnostics. |
| **Tampering** | Anomalous firmware version mismatches. | Cryptographic firmware signing & integrity checks. |
| **Repudiation** | Lack of non-repudiation in API logs. | Enhanced OAuth logging and secure audit trails. |
| **Information Disclosure** | API misconfigurations leaking telemetry. | AES-256 encryption & strict API rate limiting. |
| **Denial of Service** | Traffic spikes overwhelming vehicle connectivity. | AWS Shield & CloudFront for DoS protection. |
| **Elevation of Privilege** | Credential stuffing on fleet manager accounts. | Role-Based Access Control (RBAC) & Lifecycle MGMT. |

## 🛠️ System Components Analyzed
* **OTA Update System:** Ensuring firmware integrity and secure rollback mechanisms.
* **Vehicle Telemetry:** Protecting sensitive location and engine data in transit (TLS 1.3) and at rest.
* **Third-Party APIs:** Securing REST endpoints used by service centers via OAuth and API keys.

## ⚖️ Industry Compliance
Aligned findings with **ISO/SAE 21434** standards to ensure that cybersecurity is integrated into the entire lifecycle of the road vehicle's electrical and electronic (E/E) systems.

[Link to Full Threat Modeling Report](./AutoDrive_STRIDE_Threat_Model_Report.pdf)
