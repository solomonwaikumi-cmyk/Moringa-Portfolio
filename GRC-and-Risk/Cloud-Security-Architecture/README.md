# ☁️ Lab: Hybrid Cloud Security & HIPAA Compliance Audit
**Category:** GRC / Cloud Governance | **Frameworks:** HIPAA, Shared Responsibility Model

## 📖 Case Study Overview
This lab involved a comprehensive security audit of a healthcare organization moving to a hybrid cloud environment. The primary goal was to identify gaps in **Protected Health Information (PHI)** protection and ensure alignment with HIPAA technical and administrative safeguards.

## 🎯 Key Audit Findings
* **The Encryption Gap:** Identified that while data was encrypted, a lack of **Centralized Key Management** created a significant risk for key loss or unauthorized access.
* **Shared Responsibility:** Analyzed the boundary between the Cloud Provider's infrastructure security and the Organization's responsibility for data/access control.
* **Access Control Risks:** Flagged the manual account management process and lack of MFA as high-risk vulnerabilities.

## ⚖️ HIPAA Mapping & Compliance
I mapped current organizational practices against the HIPAA Security Rule:
* **Administrative:** Identified the need for documented and tested Disaster Recovery plans.
* **Technical:** Recommended the implementation of Centralized Logging (SIEM) to replace fragmented monitoring.
* **Physical:** Validated the cloud provider's physical security certifications.

## 💡 Strategic Recommendations
1. **Unify Key Management:** Implement a Cloud KMS to centralize encryption keys for both on-prem and cloud.
2. **Identity Lifecycle:** Move from manual management to automated MFA and periodic access reviews.
3. **Network Modernization:** Replace outdated on-prem firewalls with Next-Generation Firewalls (NGFW) supporting DPI.

[Link to Full Audit Report](./Hybrid_Cloud_Security_HIPAA_Compliance_Audit.pdf)
