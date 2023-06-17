from PIL import Image
import os

# Specify the folder path containing the images
folder_path = r"/path/to/folder" #replace with the location of your folder with images

# Create the "Reduced" directory if it does not exist
output_directory = os.path.join(folder_path, "Reduced")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through all the files in the folder
for filename in os.listdir(folder_path):
    image_path = os.path.join(folder_path, filename)

    # Check if the file is an image
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Open the image using Pillow
        img = Image.open(image_path)

        # Resize the image to 30% of its initial size
        new_width = int(img.width * 0.3)
        new_height = int(img.height * 0.3)
        resized_img = img.resize((new_width, new_height))

        # Save the resized image with the original filename and extension in the folder "Reduced"
        output_path = os.path.join(output_directory, filename)
        resized_img.save(output_path)

        print(f"Resized: {filename}")
