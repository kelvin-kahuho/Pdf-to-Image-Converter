from rembg import remove
from PIL import Image
import io

def remove_background(input_image_path, output_image_path):
    # Open the input image file
    with open(input_image_path, 'rb') as img_file:
        input_image = img_file.read()
    
    # Remove background
    output_image = remove(input_image)
    
    # Convert the output byte data to an image and save it
    img = Image.open(io.BytesIO(output_image))
    img.save(output_image_path)
    print(f"Background removed and saved to {output_image_path}")

# Example usage
input_image_path = 'Dimples Pharmacy logo.png'  # Path to the input image
output_image_path = 'output_image_no_bg.png'  # Path to save the output image
remove_background(input_image_path, output_image_path)
