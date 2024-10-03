# Markdown to PDF report generator

This script generates a PDF report from a markdown file.
It uses the 'pandoc' to convert the markdown file to a PDF file.
The intellij style css file is used to style the PDF file. (some modifications are made for korean font, inline code block style, etc.)

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

1. put the markdown file in the same directory as this script (or modify the path in the script)
2. run the conversion script after modify the parameters in the script

```python
# Execution
md_file = "./file-name.md" # modify this to the markdown file name
css_file = "./intellij-style.css"
```

## Font resizing, Margin adjustment, Page size setting

The miscellaneous settings are in the script.
Modify the parameters in the `css-editor.py` script.

```python
# Set the reduction factor, margin, size, and file path
user_reduction_factor = 1
user_margin = 1.8  # Set your desired margin in cm
user_page_size = "A4"  # Set your desired page size (e.g., 'A4', 'Letter', etc.)
original_css_file_path = './intellij-style.css'
```

## Caution

- For pandoc to work with image resize, the attached image should be like this in md file:

```html
<img src="image.png" style="width: 50px; height: 50px" />
```

- Also you can use page break in markdown file for more control over the page breaks:

```html
<div style="page-break-after: always;"></div>
```

## References

- [intellij-style.css](https://gist.github.com/ivalkeen/c093e3401790a02f02e020a2884229e8)
- [pandoc](https://pandoc.org/)
