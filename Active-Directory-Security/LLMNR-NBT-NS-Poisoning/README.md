# 🌐 Lab: LLMNR and NBT-NS Poisoning for Credential Capture
**Category:** Active Directory Security | **Tools:** Python, Scapy, Network Sniffing | **Protocol:** LLMNR, NBT-NS

## 📖 Project Overview
Developed a custom Python script, `NBT_final.py`, designed to evaluate the security of internal Windows networks by targeting Link-Local Multicast Name Resolution (LLMNR) and NetBIOS Name Service (NBT-NS). The script automates the process of "poisoning" these legacy protocols to redirect network traffic and intercept NTLM authentication hashes.

## 🎯 Technical Objectives
* **Network Traffic Sniffing:** Utilized the `Scapy` library to monitor UDP ports 137 (NetBIOS) and 5355 (LLMNR) for name resolution requests.
* **Protocol Spoofing:** Engineered a spoofing engine to send fake replies to victims, tricking them into attempting authentication against an attacker-controlled listener.
* **Credential Logging:** Implemented a persistent logging mechanism to capture and store intercepted authentication data in a structured text format for forensic analysis.
* **Error Handling & Cleanup:** Integrated system-level safeguards using `KeyboardInterrupt` to ensure clean script termination and resource release.



## 🛠️ The Poisoning Workflow
1. **Sniffing:** The script waits for a Windows machine to request the location of a resource (like a printer or file share) that it cannot find via DNS.
2. **Spoofing:** The script immediately sends a "fake" response saying, "I am that resource."
3. **Capture:** When the victim attempts to connect, the script captures the authentication attempt and logs it to `hospital_hashes.txt`.
4. **Analysis:** These captured hashes can later be cracked offline to recover plain-text passwords.

[Link to Technical PDF Report](./AD_PenTest_LLMNR_Poisoning_Report_Solomon_Waikumi.pdf)
