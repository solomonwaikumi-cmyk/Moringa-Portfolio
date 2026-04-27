# 🔍 Lab: File System-Based Digital Forensics (FAT32)
**Category:** Digital Forensics & Incident Response (DFIR) | **Tools:** The Sleuth Kit (fls, istat, icat), Python, xxd, MD5sum

## 📖 Case Background
As a Junior Digital Forensic Analyst, I investigated a forensic disk image (`.dd`) of a FAT32 USB drive. The investigation focused on recovering deleted evidence, detecting timestamp manipulation (timestomping), and validating file integrity.

## 🎯 Investigation Objectives
* **Metadata Analysis:** Used `fsstat` and `istat` to analyze file system structures and byte offsets.
* **Data Recovery:** Manually recovered deleted files using inode analysis and the Sleuth Kit CLI.
* **Automation:** Utilized a custom Python script to automate file carving based on calculated byte offsets.
* **Integrity Validation:** Performed MD5 hashing to ensure that recovered evidence remained forensically sound and unaltered.

## 🛠️ Technical Workflow
1. **Identification:** Used `fls -r` to identify deleted files marked with a `*` in the FAT32 directory structure.
2. **Analysis:** Inspected file headers using `xxd` (hex editor) to verify file types (Magic Bytes).
3. **Recovery:** Extracted raw data using `icat` and automated carving for multiple files using Python.
4. **Comparison:** Analyzed the differences between FAT32 and NTFS metadata behaviors regarding deleted file persistence.

## 🔍 Key Findings
* **Timestamp Anomalies:** Detected suspicious MACE (Modified, Accessed, Created, Entry) timestamps indicating potential user tampering.
* **Successful Recovery:** Successfully restored 100% of the targeted deleted files with matching MD5 hashes.

[Link to Full Forensic Report](./Digital_Forensics_FAT32_Metadata_Analysis.pdf)
