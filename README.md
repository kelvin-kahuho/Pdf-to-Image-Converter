# PDF to PNG Converter

This Python project allows you to convert each page of a PDF file into PNG images. It uses the `pdf2image` library for converting PDF pages to images and `Pillow` for saving those images as PNG files.

## Features
- Converts each page of a PDF file into a separate PNG image.
- Saves PNG files to a specified output folder.
- Automatically creates the output folder if it doesn't exist.

## Requirements

- Python 3.x
- `pdf2image` library
- `Pillow` library

### Install required libraries:
To install the necessary libraries, you can use pip:

```bash
pip install pdf2image pillow
```

You may also need to install `poppler` to handle PDF rendering:
- **Linux**: Install `poppler-utils` using your package manager (e.g., `apt install poppler-utils` for Ubuntu).
- **Windows**: Download and install Poppler from [here](http://blog.alivate.com.au/poppler-windows/) and add it to your PATH.

## Usage

### 1. Clone the repository or download the script:

```bash
git clone https://github.com/kelvin-kahuho/Pdf-to-Image-Converter.git
cd pdf-to-png-converter
```

### 2. Run the conversion script:

```python
from pdf2image import convert_from_path
import os

def pdf_to_png(pdf_file, output_folder):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_file)
    
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save each page as PNG
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i+1}.png')
        image.save(image_path, 'PNG')
        print(f'Saved: {image_path}')

# Example usage
pdf_file = 'sample.pdf'  # Path to the input PDF file
output_folder = 'output_images'  # Folder to save PNG images
pdf_to_png(pdf_file, output_folder)
```

### 3. Example

To convert a PDF file (e.g., `sample.pdf`) to PNG images:

1. Place your PDF file in the project folder or specify the full path.
2. Run the script:

```bash
python your_script.py
```

The PNG images will be saved in the `output_images` folder (or any folder you specify).

## Output

The output PNG images will be named `page_1.png`, `page_2.png`, etc., corresponding to the PDF page numbers.
