"""
Overall Purpose:
This script performs Open-Source Intelligence (OSINT) gathering on a specified domain.
It retrieves registration details via WHOIS and identifies network-level information 
(IP addresses, open ports, and services) using the Shodan API. The results are 
summarized and exported to a JSON file for further analysis.
"""

import requests
import json
import whois

# Replace with your actual Shodan API Key
SHODAN_API_KEY = "your_shodan_api_key_here"

def get_whois_info(domain):
    """
    Fetches WHOIS information for a given domain.
    This includes registrar data, creation dates, and owner contact information.
    """
    try:
        w = whois.whois(domain)
        # Returns the raw text format of the WHOIS record
        return w.text
    except Exception as e:
        return f"Error retrieving WHOIS data: {e}"

def get_shodan_info(domain):
    """
    Queries the Shodan API to find the IP address of the host and then 
    retrieves a list of open ports, banners, and vulnerabilities associated with that IP.
    """
    # User-agent header to mimic a standard browser and avoid basic security blocks
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Step 1: Resolve the domain to an IP using Shodan DNS utility
        dns_url = f"https://api.shodan.io/dns/resolve?hostnames={domain}&key={SHODAN_API_KEY}"
        dns_response = requests.get(dns_url, headers=headers)
        ip = dns_response.json().get(domain)

        if ip:
            # Step 2: Use the IP to get detailed host information
            host_url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}"
            shodan_response = requests.get(host_url, headers=headers)
            # Return the full JSON response as a formatted string
            return shodan_response.json()
        else:
            return {"error": "No IP found for this domain."}
    except Exception as e:
        return {"error": f"Error retrieving Shodan data: {e}"}

def main():
    """
    Main execution logic: coordinates user input, function calls, 
    console output, and file saving.
    """
    domain = input("Enter the domain name to investigate (e.g., microsoft.com): ")
    
    print(f"\n[+] Starting investigation for: {domain}...")

    # 1. Fetch WHOIS Data
    print("[*] Retrieving WHOIS information...")
    whois_data = get_whois_info(domain)
    print(whois_data[:500] + "..." if isinstance(whois_data, str) else "Data retrieved.")

    # 2. Fetch Shodan Data
    print("[*] Querying Shodan for open ports and IP info...")
    shodan_data = get_shodan_info(domain)
    
    # 3. Compile and Save Results
    results = {
        "target_domain": domain,
        "whois_record": whois_data,
        "shodan_results": shodan_data
    }

    filename = f"{domain}_osint_report.json"
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

    print("-" * 30)
    print("OSINT data collection complete.")
    print(f"Results saved to: {filename}")

if __name__ == "__main__":
    main()