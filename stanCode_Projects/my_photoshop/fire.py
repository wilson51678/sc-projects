"""
File: fire.py
Ｎame: Wilson Wang 2020/08/05
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    This function should highlight the area with fires in red and greyscale the rest area.
    :param filename: img
    :return: img, a picture file which shows the area with fire
    """
    img = SimpleImage(filename)
    for pixel in img:
        # This step means the grey scale in this image
        avg = (pixel.red+pixel.green+pixel.blue)/3
        # This step check whether the red in pixel is bigger than the fire threshold
        if pixel.red > avg*HURDLE_FACTOR:
            # highlight the fire pixel to maximum red
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0

        # grey scaling the rest pixels which have no fire sign
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg

    return img


def main():
    """
    This program highlight the pixel which has bigger red in the photo and grey scale the rest pixels
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
