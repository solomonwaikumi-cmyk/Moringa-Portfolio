# 🎓 Capstone: Advanced Digital Forensics & Automated Recovery
**Category:** Digital Forensics (DFIR) | **Tools:** Python (Advanced Binary I/O), The Sleuth Kit, MD5 Hashing, Hex Analysis

## 📖 Project Overview (Summative Assessment)
This capstone project involved a deep-dive forensic investigation into a corrupted hard drive image. The objective was to bypass standard file system limitations to recover deleted, hidden, and renamed files using advanced manual carving and Python-based automation.

## 🎯 Technical Challenges & Solutions
* **Data Corruption:** Navigated corrupted file system structures by relying on raw byte signatures (Magic Bytes).
* **Automated Multi-Carving:** Developed a comprehensive Python tool, `forensic_carver_pro.py`, capable of identifying headers/footers for multiple file types (JPG, PNG, PDF, etc.) in a single pass.
* **Integrity at Scale:** Integrated an automated MD5 hashing engine into the recovery pipeline to ensure every recovered file was forensically sound.
* **Metadata Extraction:** The script was designed to output exact byte offsets and file sizes, providing a clear chain of custody for the recovered evidence.

## 🛠️ The Forensic Pipeline
1. **Signature Mapping:** Identified start/end hex markers for various file formats.
2. **Binary Scanning:** Programmatically scanned the `.dd` image to locate file boundaries.
3. **Reconstruction:** Reassembled binary chunks into complete, uncorrupted files.
4. **Validation:** Automated MD5 hash generation and manual integrity checks via image viewers and document readers.

## 🔍 Investigation Deliverables
* **Recovered Evidence:** A full suite of successfully restored documents and images.
* **Forensic Script:** A production-ready Python script that accepts command-line arguments for disk images.
* **Evidence Manifest:** A `hashes.txt` file providing cryptographic proof of integrity for all recovered items.

[Link to Forensic Capstone Report](./Summative_Digital_Forensics_Capstone_Report.pdf) | [View the Python Script](./forensic_carver_pro.py)
