import os
from PIL import Image

path = "../poses/full_size_images"
files = os.listdir(path)            
filenames = [file for file in files if (os.path.splitext(file)[1]==".png")]

for filename in filenames:
    print(f"Processing {filename}...")
    image = Image.open(os.path.join(path, filename))
    width, height = image.size
    smaller_image = image.resize((int(width*0.4), int(height*0.4)))
    
    # Convert RGBA to RGB if necessary
    # if smaller_image.mode == 'RGBA':
    #     smaller_image = smaller_image.convert('RGB')
    
    smaller_image.save(os.path.join("../poses/", os.path.splitext(filename)[0] + ".png")) #, "JPEG")
    print(f"Saved {filename} as a smaller PNG image. --------------------------")