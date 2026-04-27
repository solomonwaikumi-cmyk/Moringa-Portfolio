# 🔍 Automated Google Dorking & Information Gathering
**Category:** Reconnaissance / Offensive Security | **Tools:** Python, BeautifulSoup4, Requests

## 📖 Project Overview
Developed a custom automation tool, `dork_final.py`, to programmatically discover sensitive information exposed on the public internet. This tool streamlines the reconnaissance phase of a security audit by identifying "Low Hanging Fruit" that search engines have indexed, such as exposed login portals and private database directories.

## 🎯 Technical Capabilities
* **Query Engineering:** Automates high-impact Google Dorks including:
  * `inurl:login` (Identifies authentication gateways)
  * `filetype:pdf OR filetype:doc` (Locates sensitive internal documentation)
  * `intitle:index.of mysql` (Detects exposed database indexes)
* **HTML Scraping:** Integrated `BeautifulSoup4` to surgically extract unique URLs from Google's search result pages.
* **Defensive Evasion:** Implemented 2-second request intervals (`time.sleep`) and custom headers to avoid bot-detection and IP-based rate limiting.
* **Reporting:** Automatically consolidates all discovered leads into a structured `dorking_results.txt` file.

## 🛠️ How to Use
1. **Configure:** Ensure `BeautifulSoup4` and `requests` are installed.
2. **Execute:** Run `python dork_final.py`.
3. **Analyze:** Review the `dorking_results.txt` for URLs that require immediate access control remediation.

[Link to Technical PDF Report](./Google_Dorking_Automation_Report_Solomon_Mwaura.pdf) | [View Script](./dork_final.py)
