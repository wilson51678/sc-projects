"""
File: shrink.py
Ｎame: Wilson Wang 2020/08/05
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    This function should shrink the 'filename' image into a 1/2 size new image.
    :param filename: img, the image of origin size
    :return img: new_img, the image of half size of the origin photo
    """
    img = SimpleImage(filename)
    # This step should makes a blank photo, which has half size of the origin photo
    new_img = SimpleImage.blank(img.width//2,img.height//2)

    for y in range(new_img.height):
        for x in range(new_img.width):
            # This step catch pixel in origin photo in every two pixel. x=0,2,4,6
            img_pixel = img.get_pixel(x*2,y*2)
            new_img_pixel = new_img.get_pixel(x,y)

            # These three steps are filling pixels from the origin photo into 'new_pixel'
            new_img_pixel.red = img_pixel.red
            new_img_pixel.green = img_pixel.green
            new_img_pixel.blue = img_pixel.blue

    return new_img


def main():
    """
    This program should shrink any image into a half size photo. 'without code:make_as_big_as'
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
