"""
File: green_screen.py
Ｎame: Wilson Wang 2020/08/05
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage

THRESHOLD = 1.3

def combine(background_img, figure_img):
    """
    :param background_img: img, the background image
    :param figure_img: img, green screen image
    :return: figure_img, the green pixels in figure_img should changer into background_img
    """

    for y in range(background_img.height):
        for x in range(background_img.width):
            pixel_bg_img = background_img.get_pixel(x,y)
            pixel_figure_img = figure_img.get_pixel(x,y)

            # This step should compares which pixel is bigger
            bigger = max(pixel_figure_img.red, pixel_figure_img.blue)

            # This step insure the pixel is the green screen.
            if pixel_figure_img.green > 2*bigger:
                pixel_figure_img.green = pixel_bg_img.green
                pixel_figure_img.red = pixel_bg_img.red
                pixel_figure_img.blue = pixel_bg_img.blue

    return figure_img


def main():
    """
    This program will replace the green background of photo into the other photo
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
