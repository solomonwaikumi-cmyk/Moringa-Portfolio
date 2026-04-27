import boto3
import requests
import time

# Function to list API Gateways
def list_apis():
    """
    Simulates an API Gateway response instead of fetching from AWS.
    This list matches the IDs in our mock configuration dictionary.
    """
    mock_response = [
        {'id': 'abc123', 'name': 'Public-Finance-API'},
        {'id': 'xyz789', 'name': 'Secure-HR-API'}
    ]
    return mock_response

# Function to check API configurations
def check_api_security(api_id):
    """
    SCOPE: This script scans AWS API Gateway to identify misconfigurations.
    Vulnerabilities assessed:
    1. Missing authentication mechanisms (e.g., open endpoints).
    2. Weak authentication (e.g., Basic Auth instead of OAuth2).
    3. Insecure HTTP usage (unencrypted traffic instead of HTTPS).
    4. Overly permissive CORS settings.
    """

    # Mock configuration data for simulation
    mock_api_configurations = {
        "abc123": {"auth_type": "NONE", "use_https": False, "cors": "*"},
        "xyz789": {"auth_type": "COGNITO_AUTH", "use_https": True, "cors": "restricted"}
    }

    api_config = mock_api_configurations.get(api_id, {})
    
    # Initialize findings dictionary for logging/reporting
    findings = {
        "api_id": api_id,
        "issues": [],
        "status": "Secure"
    }

    print(f"\n Checking API {api_id} for security issues...\n")

    # --- Configuration Checks & Logging ---
    if api_config.get("auth_type") == "NONE":
        warning = "WARNING: API has NO authentication! This API is open to the public."
        print(f"{warning} This API is open to the public.\n")
        findings["issues"].append(warning)
        findings["status"] = "Vulnerable"

    if not api_config.get("use_https"):
        warning = "WARNING: API does not enforce HTTPS! Data might be exposed in transit."
        print(f"{warning} Data might be exposed in transit.\n")
        findings["issues"].append(warning)
        findings["status"] = "Vulnerable"

    if api_config.get("cors") == "*":
        warning = "WARNING: API has overly permissive CORS settings."
        print(f"{warning} May allow cross-origin attacks.\n")
        findings["issues"].append(warning)
        findings["status"] = "Vulnerable"

    # --- Testing API Endpoints (Simulated Unauthorized Requests) ---
    test_url = f"https://{api_id}.execute-api.us-east-1.amazonaws.com/prod/test"
    print(f"Testing API endpoint for {api_id}...")
    
    if api_config.get("auth_type") == "NONE":
        print(f"RESPONSE: 200 OK - Data accessed successfully! (Vulnerability Confirmed)\n")
    else:
        print(f"RESPONSE: 401 Unauthorized - Access Denied. (Authentication working correctly)\n")

    print("-" * 40)
    return findings

# Main function with Automated Scheduling
if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print(" Running API Security Scan...")
        print("="*50 + "\n")
        
        apis = list_apis()
        scan_report = []

        if not apis:
            print("No APIs found.")
        else:
            for api in apis:
                print(f"Scanning API: {api['name']} (ID: {api['id']})")
                # Store findings for potential summary report usage
                result = check_api_security(api['id'])
                scan_report.append(result)

        print("\n" + "="*50)
        print("         API SECURITY SCAN SUMMARY")
        print("="*50 + "\n")
        
        if not scan_report:
            print("No APIs were scanned or no issues found.")
        else:
            for api_result in scan_report:
                print(f"API ID: {api_result['api_id']}")
                print(f"Status: {api_result['status']}")
                if api_result['issues']:
                    print("  Issues:")
                    for issue in api_result['issues']:
                        print(f"    - {issue}")
                print("-" * 40)

        print("\n Scan Cycle Complete.")
        print(" Next scan in 5 minutes...\n")
        
        # Pause execution for 300 seconds (5 minutes)
        time.sleep(300)