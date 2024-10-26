#!/Users/hyzoon/.pyenv/versions/3.9.5/bin/python

"""
to use this script, in your terminal, create a symbolic link to this script
you may need to change shebang path to your python path

$ chmod +x markdown_to_pdf.py
$ ln -s /paht/to/mdpdf.py /usr/local/bin/mdpdf

than you can use this script by typing `mdpdf` in your terminal in any directory
"""

import subprocess
import os
import yaml

def extract_metadata_from_markdown(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
        # Check for YAML metadata block at the beginning of the file
        if content.startswith("---"):
            return yaml.safe_load(content.split("---", 2)[1]) or {}
    return {}

def create_intermediate_markdown(input_file, metadata):
    # Define default metadata
    # TODO: Update default title to match the input file name
    # NOTE: maybe the left header should be empty by default
    default_metadata = {
        "title": "My Document Title",
        "date": "\\today",
        "fontsize": "10",
        "margin": "1in",
        "left header": "for rachelie",
        "author": "2020xxxxxx \\\\ Hyungjun Shon",
        "affil": "Dept. of xxxxxx\\\\Sungkyunkwan University",
        "abstract": "",
        "korean": False, 
        "bibfile": "bib.bib", 
        "toc": True
    }

    # Merge default metadata with user-provided metadata, giving priority to user input
    meta = {**default_metadata, **metadata}
    
    # Create YAML metadata section for Pandoc
    yaml_metadata = f"""---
title: {meta['title']}
date: {meta['date']}
geometry: margin={meta['margin']}
papersize: a4
fontfamily: newtxtext, newtxmath
numbersections: true
autoEqnLabels: true
header-includes: |
    \\usepackage[fontsize={meta['fontsize']}pt]{{scrextend}}
    \\usepackage{{authblk}}
    \\author{{{meta['author']}}}
    \\affil{{{meta['affil']}}}
    \\usepackage{{fancyhdr}}
    \\pagestyle{{fancy}}
    \\fancyhead[L]{{{meta['left header']}}}
    \\fancyhead[R]{{\\thepage}}
    \\fancyfoot{{}}
    \\usepackage{{float}}
    \\usepackage{{url}}
"""
    
    # Include Kotex for Korean text if needed
    if meta.get('korean'):
        yaml_metadata += "    \\usepackage[hangul, nonfrench, finemath]{kotex}\n"

    # Add an abstract if provided
    if meta['abstract']:
        abstract_text = meta['abstract'].replace('\n', '\n    ')
        yaml_metadata += "abstract: |\n    {}\n".format(abstract_text)
    yaml_metadata += "---\n" + ("\\tableofcontents\n\n" if meta.get('toc') else "")
    
    # Load the original content, skipping any metadata already present
    with open(input_file, 'r', encoding='utf-8') as file:
        original_content = file.read().split("---", 2)[-1]
    
    # Define the path for the intermediate file
    intermediate_file = os.path.join(os.path.dirname(input_file), "intermediate.md")
    with open(intermediate_file, 'w', encoding='utf-8') as file:
        file.write(yaml_metadata + original_content)

    return intermediate_file, meta['bibfile']

def convert_markdown_to_pdf(intermediate_file, output_file, bibfile):
    # Execute the Pandoc command for PDF conversion with citation processing
    subprocess.run([
        "pandoc", intermediate_file, "-o", output_file,
        "--filter", "pandoc-crossref", "--citeproc",
        f"--bibliography={bibfile}", "--highlight-style=tango"
    ], check=True)

def markdown_to_pdf():
    # Prompt user for file paths
    input_file = input("Enter the input Markdown file path (e.g., 'input_file_name.md'): ")
    output_file = input("Enter the output PDF file path (e.g., 'output_file_name.pdf'): ")
    
    # Extract metadata and create an intermediate Markdown file
    metadata = extract_metadata_from_markdown(input_file)
    intermediate_file, bibfile = create_intermediate_markdown(input_file, metadata)
    
    try:
        # Convert the intermediate Markdown to PDF
        convert_markdown_to_pdf(intermediate_file, output_file, bibfile)
    except subprocess.CalledProcessError as e:
        print(f"Error during PDF conversion: {e}")
    finally:
        # Clean up the intermediate file
        os.remove(intermediate_file)
        print("Intermediate Markdown file removed.")

# Run the Markdown-to-PDF conversion
markdown_to_pdf()
