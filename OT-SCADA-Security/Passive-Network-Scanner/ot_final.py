import pyshark

# Purpose: This script is designed for Green Energy Solutions to passively monitor 
# SCADA/ICS network traffic. It identifies industrial protocols (Modbus, DNP3, BACnet) 
# without transmitting packets, ensuring zero disruption to critical OT operations.

def log_data(details):
    """
    Task 4: Log OT traffic data to a file named ot_scan_log.txt.
    """
    with open("ot_scan_log.txt", "a") as log_file:
        log_file.write(details + "\n")
    print(f"[+] Logged: {details}")

def filter_ot_traffic(packet):
    """
    Task 3: Filters packets to identify OT-related traffic.
    Extracts Source IP, Destination IP, and the protocol layer if it matches 
    known OT protocols.
    """
    try:
        # Identifying OT-specific protocols
        if 'MODBUS' in packet or 'DNP3' in packet or 'BACnet' in packet:
            src_ip = packet.ip.src
            dest_ip = packet.ip.dst
            protocol = packet.highest_layer
            log_data(f"OT Traffic Detected: {protocol} from {src_ip} to {dest_ip}")
    except AttributeError:
        pass  # Ignore packets without IP or protocol layers

def capture_packets(interface):
    """
    Task 2 & 6: Capture packets passively and handle errors.
    Implements a loop to sniff continuously while managing potential crashes.
    """
    try:
        print(f"Listening on {interface}...")
        capture = pyshark.LiveCapture(interface=interface)
        for packet in capture.sniff_continuously(packet_count=50):
            try:
                filter_ot_traffic(packet)
            except Exception as e:
                print(f"Error processing packet: {e}")
    except Exception as e:
        print(f"Error capturing packets: {e}")

def main():
    # Example interface - should be updated based on the actual network environment
    target_interface = 'eth0'
    capture_packets(target_interface)

if __name__ == "__main__":
    # Task 7: README style message and guidance
    print("Passive Scanning Script for OT Environment")
    print("Ensure you have the correct network interface configured.")
    print("Logs will be stored in ot_scan_log.txt")
    main()