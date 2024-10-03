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
pdf_file = 'dimples logo.pdf'  # Path to the input PDF file
output_folder = 'output_images'  # Folder to save PNG images
pdf_to_png(pdf_file, output_folder)