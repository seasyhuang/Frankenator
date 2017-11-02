import sys
from PIL import Image
import os
import shutil

# ------------------ main ------------------

filename = raw_input("Enter the image path (OR type 'rm' to remove output_img folder): ")

# lazy remove output
if (filename == 'rm'):
    if os.path.exists('./output_imgs'):
        shutil.rmtree('./output_imgs')
    quit()

my_image = Image.open(filename);

# create image output folder
if not os.path.exists('./output_imgs'):
    os.mkdir('./output_imgs')

my_image.save('./output_imgs/1.png', 'PNG')
# myImage.show()
