# FCNABC Name Tag Generator

This project generates name tags by merging names from a text file into a PDF template. It uses the PyPDF2 library for reading and writing PDFs and ReportLab for generating the name tags.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)

## Features
- Generates name tags for multiple names from a CSV file.
- Merges names onto an existing PDF template.
- Supports custom fonts.
- Automatically handles page layout for a predefined number of name tags per page.

## Requirements
- Python 3.x
- PyPDF2 library
- ReportLab library

## Installation
1. Clone the repository:
    ```bash
   git clone https://github.com/yourusername/FCNABC-name-tag-gen.git
   cd FCNABC-name-tag-gen
   ```

2. Create and activate a virtual environment:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure that the following files are present in the project directory:
   - names.txt: A text file containing a list of names (one name per line).
   - original.pdf: The PDF template on which names will be placed.
   - LEMONMILK-Light.ttf: The custom font to be used.

2. Run the Python script to generate the name tags:
    ```bash
   python main.py
   ```

3. The generated PDF containing the name tags will be saved as namesToPrint_x.pdf, where x is the number of pages created.

## Customization
- Change the font: Replace the LEMONMILK-Light.ttf font with any other .ttf font and update the main.py script to reference the new font.
  
- Adjust the layout: You can modify the x, y coordinates and max_names_per_page in the script to adjust the name tag positioning and layout.
