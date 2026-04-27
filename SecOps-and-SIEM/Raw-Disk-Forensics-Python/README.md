# 🔍 Lab: Raw Disk Forensics & Automated File Carving
**Category:** Digital Forensics (DFIR) | **Tools:** Python (seek/read), Binwalk, Foremost, Hex Editors, Gimp

## 📖 Project Overview
This lab focused on the automated recovery of deleted JPEG files from a raw disk image (`.dd`) without relying on file system metadata. I developed a custom Python forensic tool to identify file signatures (Magic Bytes) and extract data directly from the binary stream.

## 🎯 Technical Objectives
* **Signature Analysis:** Identified JPEG headers (`FF D8 FF E0`) and footers (`FF D9`) using hex analysis.
* **Script Automation:** Developed `carve_jpg.py` to loop through a disk image, calculate offsets, and extract files automatically using Python’s `seek()` and `read()` methods.
* **Validation:** Verified the integrity of recovered files using **MD5 cryptographic hashes** and analyzed image completeness using **Gimp**.
* **Advanced Recovery:** Used `binwalk` and `foremost` to compare manual carving results with industry-standard automation tools.

## 🛠️ The Python Workflow
1. **Stream Reading:** Opened the raw disk image in binary mode.
2. **Pattern Matching:** Scanned for JPEG "Start of Image" and "End of Image" markers.
3. **Extraction:** Calculated the byte range between markers and wrote the output to new `.jpg` files.
4. **Error Handling:** Accounted for fragmented data and misplaced footers that could lead to partial recoveries.

## 🔍 Investigation Results
* **Successful Carving:** Successfully recovered multiple hidden JPEG files that were invisible to standard OS file explorers.
* **Integrity Check:** All recovered files passed MD5 validation, proving no data was altered during the extraction process.

[Link to Full Forensic Report](./Raw_Disk_Forensics_JPEG_Carving_Report.pdf) | [View the Python Script](./carve_jpg.py)
