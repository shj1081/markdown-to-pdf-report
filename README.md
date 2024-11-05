# Markdown to PDF report

## Requirements

To run the Markdown-to-PDF conversion script, ensure you have the following tools installed:

- **Pandoc**: Universal document converter.
- **Pandoc-Crossref**: Enables cross-referencing within the document.
- **MacTeX**: Required for LaTeX support on macOS. _(Note: If you currently have BasicTeX installed, consider replacing it with MacTeX for full functionality.)_
- **PyYAML**: For handling YAML metadata. Install via `pip install pyyaml`.

## Procedure Overview

1. **Generate Intermediate Markdown**:
   - The Python script (`mdpdf.py`) converts simplified or partial metadata in your Markdown file to a Pandoc-compatible format.
2. **Run Pandoc**:
   - The script runs a Pandoc command to generate a PDF output from the Markdown.
3. **Clean Up**:
   - After generating the PDF, the intermediate Markdown file is deleted automatically.

## Usage Instructions

### Step 1: Add Metadata to Your Markdown File

At the start of your Markdown file, include simplified YAML metadata as shown below. This metadata is essential for generating the document header, title, author, and other elements.

```yaml
---
title: 'Test Title for Markdown'
date: \today
author: "2020xxxxxx \\ Hyungjun Shon"
affil: "Dept. of Systems Management Engineering\\Sungkyunkwan University"
left header: 'Test Left Header'
fontsize: 10
margin: '1in'
bibfile: './bib.bib'
korean: false
toc: true
output: 'output.pdf'
abstract: |

  This is the test abstract of the document. It serves as a placeholder for the actual abstract.
---
```

### Step 2: Metadata Defaults

If any metadata fields are missing, the script substitutes the following default values (defined in `mdpdf.py`):

```python
default_metadata = {
    "title": "My Document Title",          # Default document title
    "date": "\\today",                     # Current date
    "fontsize": "12pt",                    # Default font size
    "margin": "1in",                       # Default margin
    "left header": "for rachelie",         # Default left header text
    "author": "2020xxxxxx \\\\ Hyungjun Shon",  # Default author info
    "affil": "Dept. of xxxxxx\\\\Sungkyunkwan University",  # Default affiliation
    "abstract": "",                        # Empty abstract by default
    "korean": False,                       # Default language setting (English)
    "bibfile": "bib.bib",                  # Default bibliography file path
    "toc": True                            # Include table of contents
    "output": "output.pdf"                 # Default output filename
}
```

> **Note**: To adjust these defaults, modify the values directly in `mdpdf.py`.

### Step 3: Run the Conversion Script

To execute the `mdpdf.py` script, use the following command:

```bash
python3 mdpdf.py [input_file.md]
```

- **File Input**: The script will prompt you for the input Markdown filename and the desired PDF output filename.

### Extra Step: Set Up `mdpdf.py` for Easy Access from Any Directory

To run `mdpdf.py` from any location, follow these steps to configure the shebang line, make the script executable, and enable system-wide access.

#### 1. Add Shebang Line and Make the Script Executable

1. **Add the Shebang Line**:
   At the beginning of `mdpdf.py`, add the following line to specify Python 3:

   ```python
   #!/usr/bin/env python3

   # in my case
   #!/Users/hyzoon/.pyenv/versions/3.9.5/bin/python
   ```

   This ensures the script uses the Python version managed by `pyenv` on your system.

2. **Make the Script Executable**:
   Use the following command to add execute permissions:

   ```bash
   chmod +x /path/to/mdpdf.py
   ```

   Replace `/path/to/mdpdf.py` with the actual file path. This step allows you to run `mdpdf.py` directly as an executable file.

#### 2. Enable System-Wide Access

To enable running `mdpdf.py` from any directory, choose one of the following methods:

- **Option 1: Move the Script to `/usr/local/bin`**:
  Move `mdpdf.py` to `/usr/local/bin` using this command:

  ```bash
  sudo mv /path/to/mdpdf.py /usr/local/bin/mdpdf
  ```

  After this, you can simply type `mdpdf` in the terminal to execute the script from any location.

- **Option 2: Create a Symbolic Link**:
  If you prefer to keep the script in its original location, create a symbolic link in `/usr/local/bin`:

  ```bash
  sudo ln -s /path/to/mdpdf.py /usr/local/bin/mdpdf
  ```

  Replace `/path/to/mdpdf.py` with the full path to the script. This link allows you to run `mdpdf` command from any directory without moving the original file.

  #### 3. vscode keybind after system-wide access

  Add this keybind to your vscode `keybindings.json` file.

  ```json
  // execute markdown to pdf zsh script and give parameter as editor file path
  {
    "key": "cmd+shift+m",
    "command": "workbench.action.terminal.sendSequence",
    "args": {
      "text": "mdpdf ${file}\n"
    }
  }
  ```

  You can set a keybind to convert currently open markdown file to pdf. This keybind will execute the `mdpdf` command with the current file path as a parameter. At least one terminal should be running in vscode. (hiding terminal pane is okay)

## Additional Markdown Syntax

For further Markdown syntax options that Pandoc supports, refer to [additional_markdown_syntax.md](./additional_markdown_syntax.md). This document provides examples and guidelines for additional formatting, citations, and customization.

You can also see the [additional_markdown_syntax_example_pdf](./sample_files/example_output.pdf) for preview output.
