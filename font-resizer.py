import os
import re

def reduce_font_size(line, reduction_factor):
    match = re.search(r'(\d+(\.\d+)?)px', line)
    if match:
        original_size = float(match.group(1))
        new_size = original_size * reduction_factor
        return re.sub(r'(\d+(\.\d+)?)px', f'{new_size:.1f}px', line)
    return line

def apply_font_size_reduction(css_content, reduction_factor):
    return [reduce_font_size(line, reduction_factor) for line in css_content]

def reduce_css(original_file_path, reduction_factor):
    # Open and read the original file content
    with open(original_file_path, 'r') as original_file:
        css_content = original_file.readlines()

    # Apply the font size reduction
    reduced_css = apply_font_size_reduction(css_content, reduction_factor)

    # Overwrite the original file with the reduced CSS content
    with open(original_file_path, 'w') as original_file:
        original_file.writelines(reduced_css)
    
    return

# Set the reduction factor and file path
user_reduction_factor = 0.8
original_css_file_path = './intellij-style.css'

# Call the function to modify the original file
reduce_css(original_css_file_path, user_reduction_factor)
