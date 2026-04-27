# ⚡ Lab: Passive OT/SCADA Network Monitoring
**Category:** OT/ICS Security | **Tools:** Python, PyShark, SCADA Protocols | **Focus:** Industrial Infrastructure Safety

## 📖 Project Overview
Developed a non-intrusive network monitoring tool for **Green Energy Solutions** to identify industrial control systems (ICS) and SCADA devices. The script is designed to passively sniff network traffic, identifying critical OT protocols (Modbus, DNP3, BACnet) without sending a single packet, ensuring zero disruption to sensitive power plant operations.

## 🎯 Technical Objectives
* **Passive Traffic Analysis:** Leveraged `PyShark` to capture live packets in a "listen-only" mode, adhering to the high-availability requirements of OT environments.
* **Industrial Protocol Identification:** Engineered filtering logic to detect and metadata-tag communications from Modbus (PLCs), DNP3 (Electric Utilities), and BACnet (Environmental Controls).
* **High-Resilience Scripting:** Integrated dual-layer exception handling to prevent script failure in high-volume traffic scenarios.
* **Forensic Logging:** Implemented structured data logging to `ot_scan_log.txt` for asset discovery and unauthorized device detection.



## 🛠️ The Monitoring Workflow
1. **Sniffing:** The script hooks into the network interface to monitor all incoming/outgoing traffic.
2. **Filtering:** Analyzes the `highest_layer` of each packet for industrial protocol signatures.
3. **Data Extraction:** Captures Source IP, Destination IP, and the specific Protocol used.
4. **Logging:** Records findings to a persistent log file for security auditing and asset inventory.

[Link to Technical PDF Report](./OT_Security_Passive_Scan_Report_Solomon_Waikumi.pdf)
