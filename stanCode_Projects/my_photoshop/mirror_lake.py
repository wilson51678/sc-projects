"""
File: mirror_lake.py
Ｎame: Wilson Wang 2020/08/05
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    This functions should shows a reflect 'original_mt' in an up-side down form photo.
    :param filename: original_mt, img, the origin photo
    :return: new_img, img , an up-side down photo
    """
    img = SimpleImage(filename)
    # This step should makes a blank photo, which has twice height of the origin photo
    new_img = SimpleImage.blank(img.width, img.height*2)

    for y in range(img.height):
        for x in range(img.width):
            img_pixel = img.get_pixel(x,y)
            # This step put pixel from the origin photo into half upper of 'new_img'
            new_pixel1 = new_img.get_pixel(x,y)
            # This step should put pixel at the opposite location as 'new_pixel1'
            new_pixel2 = new_img.get_pixel(x,new_img.height-1-y)

            new_pixel1.red = img_pixel.red
            new_pixel1.green = img_pixel.green
            new_pixel1.blue = img_pixel.blue

            new_pixel2.red = img_pixel.red
            new_pixel2.green = img_pixel.green
            new_pixel2.blue = img_pixel.blue
    return new_img


def main():
    """
    This program will make a photo into an up-side down form photo
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
