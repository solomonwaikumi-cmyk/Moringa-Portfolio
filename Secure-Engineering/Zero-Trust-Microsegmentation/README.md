# 🛡️ Lab: Zero Trust Micro-Segmentation & Audit Access
**Category:** Network Security Engineering | **Tools:** VyOS, tcpdump, Linux

## 📖 Project Overview
This lab simulates a high-security enterprise environment where **Zero Trust** principles are applied to segment internal departments (HR, Finance, DB) and manage third-party auditor access.

## 🎯 Business Objectives
* **Third-Party Access:** Provisioned restricted, read-only access for a new `Audit-VM`.
* **SOC Visibility:** Implemented detailed logging for all "DROP" actions to assist the SOC in detecting lateral movement.
* **Micro-Segmentation:** Isolated the Finance subnet to ensure only authorized traffic can enter.

## 🛠️ Technical Implementation (VyOS)
* **Zone-Based Firewall:** Created a new `Audit` zone and applied strict rulesets.
* **Logging:** Enabled `log` parameters on firewall rules to monitor unauthorized access attempts.
* **Connectivity:** * Finance-VM: `192.168.1.2`
  * Audit-VM: `192.168.4.2`

## 🔍 Validation Results
I utilized `tcpdump` to verify that traffic from the Audit-VM was correctly dropped when attempting to reach unauthorized segments (HR/DB), while maintaining connectivity to the designated Finance logs.

[Link to Full Technical Report](./Zero_Trust_Micro_Segmentation_Audit_Report.pdf)
