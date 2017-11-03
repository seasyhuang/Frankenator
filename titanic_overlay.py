import sys
from PIL import Image
import glob, os
import shutil


def get_dimensions(input_image):
    width, height = input_image.size
    return width, height

def my_heart_will_go_on(imput_image, dim):

    # input_image.show()

    titanic = Image.open('./mhwgo.png')
    width = dim[0]
    height = dim[1]

    size = width, height

    print size

    new_titanic = titanic.resize(size, resample=1)

    output_image = Image.blend(new_titanic, input_image, 0.3)

    return output_image

# ------------------ main ------------------

if not os.path.isfile('./mhwgo.png'):
    print("no titanic img, quitting")
    quit()

input_image = Image.open('./test.png')

dim = get_dimensions(input_image)

output_image = my_heart_will_go_on(input_image, dim)

output_image
