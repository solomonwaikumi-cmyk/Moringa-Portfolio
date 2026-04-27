#!/usr/bin/env python3
import os
import sys
import hashlib
import argparse

def compute_md5(data):
    """Computes the MD5 hash of the given data."""
    return hashlib.md5(data).hexdigest()

def carve_files(image_path, output_dir):
    """Scans the disk image for file signatures and carves them out."""
    
    # Define common file signatures (Headers and Footers)
    signatures = [
        {'type': 'jpg', 'header': b'\xff\xd8\xff', 'footer': b'\xff\xd9'},
        {'type': 'png', 'header': b'\x89PNG\r\n\x1a\n', 'footer': b'\x49\x45\x4e\x44\xae\x42\x60\x82'},
        {'type': 'pdf', 'header': b'%PDF', 'footer': b'%%EOF'},
        {'type': 'zip', 'header': b'PK\x03\x04', 'footer': b'PK\x05\x06'}, # Simplified ZIP footer
        {'type': 'gif', 'header': b'GIF8', 'footer': b'\x00\x3b'},
    ]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    hash_file_path = os.path.join(output_dir, 'hashes.txt')
    
    try:
        with open(image_path, 'rb') as f:
            data = f.read()
            
        print(f"[*] Analyzing image: {image_path}")
        print(f"[*] Image size: {len(data)} bytes")
        print(f"[*] Output directory: {output_dir}\n")

        recovered_count = 0
        with open(hash_file_path, 'w') as hf:
            hf.write("MD5 Hash Manifest - Recovered Files\n")
            hf.write("="*60 + "\n\n")

            for sig in signatures:
                header = sig['header']
                footer = sig['footer']
                ext = sig['type']
                
                start_pos = 0
                while True:
                    # Find next header
                    header_pos = data.find(header, start_pos)
                    if header_pos == -1:
                        break
                    
                    # Find next footer after the header
                    footer_pos = data.find(footer, header_pos + len(header))
                    if footer_pos == -1:
                        # If no footer found, skip or handle (here we skip to avoid partials)
                        start_pos = header_pos + len(header)
                        continue
                    
                    # Calculate end position (include the footer itself)
                    end_pos = footer_pos + len(footer)
                    file_data = data[header_pos:end_pos]
                    file_size = len(file_data)
                    
                    # Validation: Basic size check to avoid false positives
                    if file_size > 10: 
                        recovered_count += 1
                        filename = f"recovered_{recovered_count:03d}.{ext}"
                        filepath = os.path.join(output_dir, filename)
                        
                        # Save recovered file
                        with open(filepath, 'wb') as out_f:
                            out_f.write(file_data)
                        
                        # Compute MD5
                        file_hash = compute_md5(file_data)
                        
                        # Log to console
                        print(f"[+] Found {ext.upper()} at offset {header_pos}")
                        print(f"    Size: {file_size} bytes | Saved as: {filename}")
                        
                        # Log to hash manifest
                        hf.write(f"File: {filename}\n")
                        hf.write(f"Type: {ext.upper()}\n")
                        hf.write(f"Offset: {header_pos}\n")
                        hf.write(f"Size: {file_size} bytes\n")
                        hf.write(f"MD5: {file_hash}\n")
                        hf.write("-" * 40 + "\n")
                    
                    # Move start_pos to after this file
                    start_pos = end_pos

        print(f"\n[*] Recovery complete. {recovered_count} files recovered.")
        print(f"[*] Hash manifest saved to: {hash_file_path}")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Forensic File Carver for Mwaura Lab.")
    parser.add_argument("image", help="Path to the binary disk image.")
    parser.add_argument("-o", "--output", default="Mwaura", help="Output folder name (Last Name).")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.image):
        print(f"[!] Error: File '{args.image}' not found.")
        sys.exit(1)
        
    carve_files(args.image, args.output)
