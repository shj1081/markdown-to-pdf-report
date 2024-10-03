import subprocess
import os

def convert_markdown_to_pdf(md_file, css_file):
    # Ensure the md_file ends with .md and derive the base name for the output
    if md_file.endswith(".md"):
        base_name = os.path.splitext(md_file)[0]
        result_file = f"{base_name}.pdf"
    else:
        raise ValueError("The provided file must have a .md extension")
    
    command = [
        "pandoc", md_file, 
        "-o", result_file, 
        "--pdf-engine=weasyprint", 
        "--css", css_file, 
        "-V", "papersize:a4"
    ]
    
    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"PDF successfully created: {result_file}")
    else:
        print(f"Error occurred: {result.stderr}")


# Execution
md_file = "./file-name.md"
css_file = "./intellij-style.css"

convert_markdown_to_pdf(md_file, css_file)
