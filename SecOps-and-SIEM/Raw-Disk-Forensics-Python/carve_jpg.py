#!/usr/bin/env python3

import os
import argparse
import mimetypes

def find_signatures_chunked(image_path, signature, chunk_size=4096):
    """Search for file headers/footers in the raw disk image using chunked reading.
    Returns a list of offsets where the signature is found.
    """
    offsets = []
    try:
        with open(image_path, 'rb') as f:
            file_size = os.path.getsize(image_path)
            current_offset = 0
            # Read in chunks, overlapping by the signature length to catch signatures split across chunks
            overlap_size = len(signature) - 1 if len(signature) > 1 else 0

            while current_offset < file_size:
                f.seek(current_offset)
                chunk = f.read(chunk_size + overlap_size)
                if not chunk:
                    break

                # Search within the current chunk
                search_offset = 0
                while True:
                    idx = chunk.find(signature, search_offset)
                    if idx == -1:
                        break
                    offsets.append(current_offset + idx)
                    search_offset = idx + len(signature)
                
                # Move to the next chunk, accounting for overlap
                current_offset += chunk_size
                print(f"[+] Scanned {current_offset / (1024*1024):.2f} MB...", end=\r)

    except FileNotFoundError:
        print(f"Error: {image_path} not found.")
    except IOError as e:
        print(f"Error reading file {image_path}: {e}")
    return offsets

def validate_jpeg(filepath):
    """Basic validation for JPEG files by checking magic bytes and file extension.
    More robust validation would involve parsing the JPEG structure.
    """
    try:
        with open(filepath, 'rb') as f:
            header = f.read(2)
            f.seek(-2, os.SEEK_END)
            footer = f.read(2)
            # JPEG magic bytes: FF D8 (header), FF D9 (footer)
            if header == b'\xFF\xD8' and footer == b'\xFF\xD9':
                return True
    except IOError:
        pass
    return False

def extract_files(image_path, start_offsets, end_offsets, output_folder, max_file_size=10*1024*1024): # Max 10MB per file
    """
    Extracts multiple JPEG files using dynamic header and footer offsets.
    Pairs each header with the next available footer in the stream, or uses the next header as a boundary.
    Includes basic validation.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_size = os.path.getsize(image_path)
    recovered_count = 0

    with open(image_path, 'rb') as img_file:
        for i, start in enumerate(start_offsets):
            valid_footer = None
            # Find the closest footer after the current header
            for end in sorted(end_offsets):
                if end > start:
                    # Consider the footer itself (FF D9) as part of the file
                    potential_footer_end = end + 2
                    if potential_footer_end - start <= max_file_size:
                        valid_footer = potential_footer_end
                        break
            
            # If no suitable footer is found, use the next header as a boundary
            # or carve until max_file_size or end of disk
            if not valid_footer:
                next_header_boundary = file_size
                if i + 1 < len(start_offsets):
                    next_header_boundary = start_offsets[i+1]
                
                # Use the minimum of next header, max_file_size limit, or end of disk
                valid_footer = min(next_header_boundary, start + max_file_size, file_size)

            # Ensure we don't carve backwards or with zero/negative size
            if valid_footer <= start:
                continue

            img_file.seek(start)
            size = valid_footer - start
            data = img_file.read(size)

            output_filename = os.path.join(output_folder, f"recovered_{recovered_count:04d}.jpg")
            try:
                with open(output_filename, 'wb') as out_file:
                    out_file.write(data)
                
                if validate_jpeg(output_filename):
                    print(f"[+] Carved Valid JPEG {recovered_count:04d}: Start {hex(start)}, End {hex(valid_footer)} -> {output_filename}")
                    recovered_count += 1
                else:
                    os.remove(output_filename) # Delete invalid file
                    # print(f"[-] Carved Invalid JPEG (deleted): Start {hex(start)}, End {hex(valid_footer)}")

            except IOError as e:
                print(f"Error writing file {output_filename}: {e}")

    print(f"\n[+] Successfully carved {recovered_count} valid JPEG files.")

def main():
    parser = argparse.ArgumentParser(description="Forensic file carving tool for JPEG images.")
    parser.add_argument("image_path", help="Path to the raw disk image file (e.g., M2_lab.dd)")
    parser.add_argument("-o", "--output_folder", default="recovered_files",
                        help="Output folder for recovered files (default: recovered_files)")
    parser.add_argument("-c", "--chunk_size", type=int, default=4096 * 1024, # 4MB chunks
                        help="Chunk size for reading the image in bytes (default: 4MB)")
    parser.add_argument("-m", "--max_file_size", type=int, default=10 * 1024 * 1024, # 10MB max
                        help="Maximum size for a carved file in bytes (default: 10MB)")
    
    args = parser.parse_args()

    # JPEG standard signatures
    jpg_header = b'\xFF\xD8\xFF\xE0'
    jpg_header_alt = b'\xFF\xD8\xFF\xE1'
    jpg_footer = b'\xFF\xD9'

    print(f"[+] Analyzing image: {args.image_path}")
    print(f"[+] Output folder: {args.output_folder}")
    print(f"[+] Chunk size: {args.chunk_size / (1024*1024):.2f} MB")
    print(f"[+] Max carved file size: {args.max_file_size / (1024*1024):.2f} MB")

    # Find all header and footer positions
    print("\n[+] Searching for JPEG headers...")
    start_offsets = find_signatures_chunked(args.image_path, jpg_header, args.chunk_size)
    start_offsets.extend(find_signatures_chunked(args.image_path, jpg_header_alt, args.chunk_size))
    start_offsets = sorted(list(set(start_offsets))) # Remove duplicates and sort

    print("\n[+] Searching for JPEG footers...")
    end_offsets = find_signatures_chunked(args.image_path, jpg_footer, args.chunk_size)
    end_offsets = sorted(list(set(end_offsets))) # Remove duplicates and sort

    if not start_offsets:
        print("\n[-] Error: No JPEG file headers found. File carving aborted.")
    else:
        print(f"\n[!] Detected {len(start_offsets)} potential JPEG headers. Starting extraction...")
        print("-" * 60)
        
        extract_files(args.image_path, start_offsets, end_offsets, args.output_folder, args.max_file_size)
        
        print("-" * 60)
        print(f"Analysis complete. Check the \'{args.output_folder}\' directory.")

if __name__ == "__main__":
    main()