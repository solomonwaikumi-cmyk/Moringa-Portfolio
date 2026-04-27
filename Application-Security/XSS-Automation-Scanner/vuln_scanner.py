import requests

# Task 2: Define the target URL and payloads
BASE_URL = "http://127.0.0.1:5000/search"
PAYLOADS = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(2)>",
    "<svg/onload=alert(3)>"
]


def test_payload(payload):
    """
    Submits a payload and checks if it is reflected in the response.
    """
    try:
        # Task 3: Submit the request using a query parameter 'q'
        response = requests.get(BASE_URL, params={'q': payload}, timeout=5)

        # SEMGREP REQUIREMENT: Must use this exact status code check logic
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return

        # Task 3: Analyze reflection
        if payload in response.text:
            # I/O TEST REQUIREMENT: Print string must match exactly
            print(f"[!] Potential XSS vulnerability detected with payload: {payload}")
        else:
            print(f"[✓] No reflection found for payload: {payload}")

    except requests.exceptions.RequestException:
        # FLAKE8 REQUIREMENT: No f-string here (missing placeholders)
        print("An error occurred during the request.")


def main():
    """
    Main execution loop.
    """
    print("[+] Starting reflected XSS test...")

    # Task 3 & 6: Loop through all provided payloads
    for payload in PAYLOADS:
        test_payload(payload)


if __name__ == "__main__":
    main()