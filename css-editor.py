import os
import re

# Function to reduce the font size based on a reduction factor
def reduce_font_size(line, reduction_factor):
    match = re.search(r'(\d+(\.\d+)?)px', line)
    if match:
        original_size = float(match.group(1))
        new_size = original_size * reduction_factor
        return re.sub(r'(\d+(\.\d+)?)px', f'{new_size:.1f}px', line)
    return line

# Function to modify the @page margin and size properties
def modify_page_properties(line, margin=None, size=None):
    # Modify the margin if provided
    if margin:
        line = re.sub(r'margin:\s*[\d.]+cm;', f'margin: {margin}cm;', line)
    # Modify the page size if provided
    if size:
        line = re.sub(r'size:\s*\w+;', f'size: {size};', line)
    return line

# Apply the font size reduction to the entire content
def apply_modifications(css_content, reduction_factor, margin=None, size=None):
    modified_content = []
    in_page_block = False
    
    for line in css_content:
        # Detect @page block and apply page property modifications
        if "@page" in line:
            in_page_block = True
        if in_page_block:
            line = modify_page_properties(line, margin, size)
        if "}" in line and in_page_block:
            in_page_block = False
        
        # Apply font size reduction outside the @page block
        if not in_page_block:
            line = reduce_font_size(line, reduction_factor)
        
        modified_content.append(line)
    
    return modified_content

# Function to read, modify, and write back the CSS file
def reduce_css(original_file_path, reduction_factor, margin=None, size=None):
    # Open and read the original file content
    with open(original_file_path, 'r') as original_file:
        css_content = original_file.readlines()

    # Apply the modifications (font size, margin, and size)
    modified_css = apply_modifications(css_content, reduction_factor, margin, size)

    # Overwrite the original file with the modified CSS content
    with open(original_file_path, 'w') as original_file:
        original_file.writelines(modified_css)
    
    return

# Set the reduction factor, margin, size, and file path
user_reduction_factor = 1
user_margin = 1.8  # Set your desired margin in cm
user_page_size = "A4"  # Set your desired page size (e.g., 'A4', 'Letter', etc.)
original_css_file_path = './intellij-style.css'

# Call the function to modify the original file
reduce_css(original_css_file_path, user_reduction_factor, margin=user_margin, size=user_page_size)
