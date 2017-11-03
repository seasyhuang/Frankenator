import sys
from PIL import Image
from PIL import ImageFilter
import glob, os
import shutil

def upside_down(input_image):

    output_image = input_image.rotate(180)
    # output_image.show()
    return output_image

# --------------------------------------------

def horizontal_flip(input_image):

    output_image = input_image.transpose(Image.FLIP_LEFT_RIGHT)
    # output_image.show()
    return output_image

# --------------------------------------------

def blurry_boi(input_image):

    output_image = input_image.filter(ImageFilter.GaussianBlur(radius=10))
    # output_image.show()
    return output_image

# --------------------------------------------

def long_boi(input_image):
    dim = get_dimensions(input_image)

    width = dim[0]
    height = dim[1] * 1.5

    size = int(width), int(height)

    output_image = input_image.resize(size)

    left = 0
    upper = dim[1]/4
    right = width
    lower = dim[1] + dim[1]/4

    box = (left, upper, right, lower)

    output_image = output_image.crop(box)

    # output_image = output_image.resize(dim)
    # output_image.show()
    return output_image

# --------------------------------------------

def fat_boi(input_image):
    dim = get_dimensions(input_image)

    width = dim[0] * 1.5
    height = dim[1]

    size = int(width), int(height)

    output_image = input_image.resize(size)

    left = dim[0]/4
    upper = 0
    right = dim[0] + dim[0]/4
    lower = height

    box = (left, upper, right, lower)

    output_image = output_image.crop(box)

    # output_image = output_image.resize(dim)
    # output_image.show()
    return output_image

# --------------------------------------------

def zoom_boi(input_image):

    dim = get_dimensions(input_image)

    left = dim[0]/2 - dim[0]/4
    upper = dim[1]/2 - dim[1]/4
    right = dim[0]/2 + dim[0]/4
    lower = dim[1]/2 + dim[1]/4

    box = (left, upper, right, lower)
    output_image = input_image.crop(box)
    output_image = output_image.resize(dim)
    # output_image.show()
    return output_image

# --------------------------------------------

def quantize(input_image):

    output_image = input_image.quantize(colors=10, method=None, kmeans=0, palette=None)
    # output_image.show()
    return output_image

# --------------------------------------------

def get_dimensions(input_image):
    width, height = input_image.size
    return width, height

def my_heart_will_go_on(imput_image, dim):

    # input_image.show()
    titanic = Image.open('./mhwgo.png')
    width = dim[0]
    height = dim[1]
    size = width, height

    # print size

    new_titanic = titanic.resize(size, resample=1)
    output_image = Image.blend(new_titanic, input_image, 0.3)

    return output_image

def overlay(input_image):

    if not os.path.isfile('./mhwgo.png'):
        print("no titanic img, quitting")
        quit()

    # input_image = Image.open(input_image)

    dim = get_dimensions(input_image)

    output_image = my_heart_will_go_on(input_image, dim)

    return output_image

# ------------------ main ------------------

# filename = raw_input("Enter the image path (OR type 'rm' to remove output_img folder): ")
filename = "./test.png"
# lazy remove output
if (filename == 'rm'):
    if os.path.exists('./output_imgs'):
        shutil.rmtree('./output_imgs')
    quit()

# myImage.show()

# create image output folder
if not os.path.exists('./output_imgs'):
    os.mkdir('./output_imgs')

input_image = Image.open(filename)
input_image.save('./output_imgs/original.png')

to_save = long_boi(input_image)
to_save.save('./output_imgs/1.png')

# to_save = overlay(input_image)
# to_save.save('./output_imgs/1.png')
#
# to_save = upside_down(input_image)
# to_save.save('./output_imgs/2.png')
#
# to_save = horizontal_flip(input_image)
# to_save.save('./output_imgs/3.png')


input_image.close()
