# Markdown to PDF report generator

This script generates a PDF report from a markdown file.
It uses the 'pandoc' to convert the markdown file to a PDF file.
The intellij style css file is used to style the PDF file.

## Prerequisites

- pandoc
- weasyprint
- (maybe you need to install basictex)

```bash
brew install pandoc, weasyprint

# may need to install basictex
brew install --cask basictex
```

## Usage

1. put the markdown file in the same directory as this script
2. run the conversion script after modify the parameters in the script

```python
# Execution
md_file = "./file-name.md" # modify this to the markdown file name
css_file = "./intellij-style.css"
```

## Font resizing

The font size can be adjusted by modifying the css file.
This can be done with `font-resizer.py` script.

```python
# Set the reduction factor and file path
user_reduction_factor = 0.8 # modify this to the desired size factor
original_css_file_path = './intellij-style.css'
```
