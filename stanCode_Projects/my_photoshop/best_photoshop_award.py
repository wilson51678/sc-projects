"""
File: best_photoshop_award.py
Ｎame: Wilson Wang 2020/08/05
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

THRESHOLD = 1.3
BLACK = 130

def photoshop(me,bg):
    """
    :param me: Simpleimage, the photo with person in green screen
    :param bg: Simpleimage, the background image
    :return: me, Simpleimage, the photo after changing backggound
    """

    for y in range(me.height):
        for x in range(me.width):
            me_pixel = me.get_pixel(x,y)
            avg = (me_pixel.red+me_pixel.green+me_pixel.blue)//3
            # total is use for detect hair color
            total = me_pixel.red+me_pixel.green+me_pixel.blue
            # This step detect the green screen and hair
            if me_pixel.green > avg*THRESHOLD and total > BLACK:
                bg_pixel = bg.get_pixel(x, y)
                me_pixel.red = bg_pixel.red
                me_pixel.blue = bg_pixel.blue
                me_pixel.green = bg_pixel.green

    return me
def main():
    """
    This function should photoshop a person into any background
    """

    me = SimpleImage("image_contest/gaitubao_IMG_7001_jpg.jpg")
    bg = SimpleImage("image_contest/pexels-chris-f-2083180 .jpg")
    bg.make_as_big_as(me)
    combined_img = photoshop(me,bg)
    combined_img.show()


if __name__ == '__main__':
    main()
