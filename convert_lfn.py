#!/usr/bin/env python3
"""Convert lfn txt files to GXS format"""

import re

def convert_txt_to_gxs(input_file, output_file, base_file):
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Start with header and include
    gxs_lines = [
        f"# {input_file.split('/')[-1].replace('.txt', '')} Patch",
        "# Converted from txt format to GXS 2.0 format",
        "",
        f"[INC] {base_file}",
        "",
    ]
    
    # Remove .set watermark, .include, and .patch/.extend/.string directives
    content = re.sub(r'\.set watermark.*?\n', '', content)
    content = re.sub(r'\.include.*?\n', '', content)
    content = re.sub(r'\.patch.*?\n', '', content)
    content = re.sub(r'\.extend.*?\n', '', content)
    content = re.sub(r'\.string.*?\n', '', content)
    
    # Find all .code sections
    code_pattern = r'\.code b (0x[0-9A-Fa-f]+)\n(.*?)\.eoc'
    matches = list(re.finditer(code_pattern, content, re.DOTALL))
    
    # Process each .code section
    for i, match in enumerate(matches):
        addr = match.group(1)
        code_content = match.group(2)
        
        gxs_lines.append(f"# code section {i+1}")
        gxs_lines.append(f"[ASM] {addr}:")
        
        # Convert the assembly code
        for line in code_content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Remove inline comments for now (keep the code)
            if '#' in line and not line.startswith('#'):
                line = line.split('#')[0].strip()
            
            # Convert hex values to decimal
            def hex_to_dec(match):
                val = int(match.group(1), 16)
                return str(val)
            
            line = re.sub(r'0x([0-9A-Fa-f]+)', hex_to_dec, line)
            
            gxs_lines.append('\t' + line)
        
        gxs_lines.append('[!ASM]')
        gxs_lines.append('')
    
    # Handle .data sections
    data_pattern = r'\.data (0x[0-9A-Fa-f]+)\n(.*?)\.eod'
    data_matches = list(re.finditer(data_pattern, content, re.DOTALL))
    
    for match in data_matches:
        addr = match.group(1)
        data = match.group(2).strip()
        gxs_lines.append(f"{addr}: {data}")
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(gxs_lines))
        f.write('\n')
    
    print(f"Converted {input_file} to {output_file}")

# Convert files
convert_txt_to_gxs(
    '/home/e3xp0/Projects/gxBuild-patches/patches/GXS/4BL/RGLoader-8453-lfn.txt',
    '/home/e3xp0/Projects/gxBuild-patches/patches/GXS/4BL/RGLoader-8453-lfn.gxs',
    'RGLoader-8453-base.gxs'
)

convert_txt_to_gxs(
    '/home/e3xp0/Projects/gxBuild-patches/patches/GXS/4BL/RGLoader-9452-lfn.txt',
    '/home/e3xp0/Projects/gxBuild-patches/patches/GXS/4BL/RGLoader-9452-lfn.gxs',
    'RGLoader-9452-base.gxs'
)

convert_txt_to_gxs(
    '/home/e3xp0/Projects/gxBuild-patches/patches/GXS/4BL/RGLoader-14699-dev-lfn.txt',
    '/home/e3xp0/Projects/gxBuild-patches/patches/GXS/4BL/RGLoader-14699-dev-lfn.gxs',
    'RGLoader-14699-dev-base.gxs'
)

print("Done!")
