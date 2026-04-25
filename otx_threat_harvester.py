import requests
import json

def fetch_threat_intelligence():
    """
    Fetches public C2 (Command & Control) data from Feodo Tracker.
    This URL is a public blocklist and does NOT require an API Key.
    """
    url = "https://feodotracker.abuse.ch/downloads/ipblocklist.json"
    
    # User-Agent is still good practice to prevent 403 errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Cybersecurity-Lab'
    }
    
    try:
        print(f"Connecting to {url}...")
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def parse_threat_intelligence(data):
    """Parses the JSON list and exports high-priority threats."""
    if not data:
        print("No data retrieved.")
        return

    report_lines = []
    report_lines.append("=== FEODO TRACKER C2 INTELLIGENCE REPORT ===\n")
    report_lines.append("Source: https://feodotracker.abuse.ch/\n")
    report_lines.append("-" * 50 + "\n")

    print(f"\nSuccessfully fetched {len(data)} threat indicators.")
    print("Processing the top 10 most recent threats...\n")
    
    # Feodo returns a simple list of dictionaries
    # We slice [:10] to keep the output readable
    for entry in data[:10]:
        ip_address = entry.get('ip_address', 'N/A')
        malware = entry.get('malware', 'Unknown')
        status = entry.get('status', 'offline')
        
        # Priority Logic: QakBot and Emotet are major Ransomware precursors
        high_risk_families = ['QakBot', 'Emotet', 'Cobalt Strike', 'BazarLoader']
        is_high_priority = any(fam.lower() in malware.lower() for fam in high_risk_families)
        
        priority = "HIGH" if is_high_priority else "LOW"
        
        # Console Output
        output = (
            f"Malware Family: {malware}\n"
            f"Priority:       {priority}\n"
            f"C2 IP Address:  {ip_address}\n"
            f"Status:         {status}\n"
            f"{'-'*40}\n"
        )
        print(output)
        report_lines.append(output)

    # Export to File
    try:
        filename = 'threat_intelligence_report.txt'
        with open(filename, 'w') as f:
            f.writelines(report_lines)
        print(f"✅ Success: Report saved to {filename}")
    except Exception as e:
        print(f"Failed to write to file: {e}")

if __name__ == '__main__':
    threat_data = fetch_threat_intelligence()
    parse_threat_intelligence(threat_data)