"""
File: blur.py
Ｎame: Wilson Wang 2020/08/05
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    This function will average red, green and blue in pixels with neighbors. There are a few situations:
    1. pixels with 8 neighbors
    2. pixel with 5 neighbors
    3. pixel with 3 neighbors
    :param img: the origin image
    :return: new_image, the photo after blur
    """
    # make a blank image which has same size of the origin one
    new_image = SimpleImage.blank(img.width,img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixel_center = img.get_pixel(x,y)
            pixel_new_image = new_image.get_pixel(x,y)
            # This step is catching pixel which has 8 neighbors.
            if 1 < x < img.width-1 and 1 < y < img.height - 1:
                pixel1 = img.get_pixel(x - 1, y - 1)
                pixel2 = img.get_pixel(x, y - 1)
                pixel3 = img.get_pixel(x + 1, y - 1)
                pixel4 = img.get_pixel(x - 1, y)
                pixel6 = img.get_pixel(x + 1, y)
                pixel7 = img.get_pixel(x - 1, y + 1)
                pixel8 = img.get_pixel(x, y + 1)
                pixel9 = img.get_pixel(x + 1, y + 1)
                avg_red = (pixel1.red+pixel2.red+pixel3.red+pixel4.red+pixel_center.red+pixel6.red+pixel7.red+pixel8.red+pixel9.red)/9
                avg_green = (pixel1.green+pixel2.green+pixel3.green+pixel4.green+pixel_center.green+pixel6.green+pixel7.green+pixel8.green+pixel9.green)/9
                avg_blue = (pixel1.blue+pixel2.blue+pixel3.blue+pixel4.blue+pixel_center.blue+pixel6.blue+pixel7.blue+pixel8.blue+pixel9.blue)/9

                pixel_new_image.red = avg_red
                pixel_new_image.green = avg_green
                pixel_new_image.blue = avg_blue
            # This step is catching pixel which has 5 neighbors and is at top side of photo
            if 1 <= x < img.width-1 and y == 0 :
                upside_pixel1 = img.get_pixel(x-1,y)
                upside_pixel2 = img.get_pixel(x+1,y)
                upside_pixel3 = img.get_pixel(x-1,y+1)
                upside_pixel4 = img.get_pixel(x,y+1)
                upside_pixel5 = img.get_pixel(x+1,y+1)

                upside_avg_red = (upside_pixel1.red+pixel_center.red+upside_pixel2.red+upside_pixel3.red+upside_pixel4.red+upside_pixel5.red)/6
                upside_avg_green = (upside_pixel1.green+pixel_center.green+upside_pixel2.green+upside_pixel3.green+upside_pixel4.green+upside_pixel5.green)/6
                upside_avg_blue = (upside_pixel1.blue+pixel_center.blue+upside_pixel2.blue+upside_pixel3.blue+upside_pixel4.blue+upside_pixel5.blue)/6

                pixel_new_image.red = upside_avg_red
                pixel_new_image.green = upside_avg_green
                pixel_new_image.blue = upside_avg_blue
            # This step is catching pixel which has 5 neighbors and is at down side of photo
            if 1 <= x < img.width-1 and y == img.width-1:
                downside_pixel1 = img.get_pixel(x-1,y-1)
                downside_pixel2 = img.get_pixel(x,y-1)
                downside_pixel3 = img.get_pixel(x+1,y-1)
                downside_pixel4 = img.get_pixel(x-1,y)
                downside_pixel5 = img.get_pixel(x+1,y)

                downside_avg_red = (downside_pixel1.red+downside_pixel2.red+downside_pixel3.red+downside_pixel4.red+pixel_center.red+downside_pixel5.red)/6
                downside_avg_green = (downside_pixel1.green+downside_pixel2.green+downside_pixel3.green+downside_pixel4.green+pixel_center.green+downside_pixel5.green)/6
                downside_avg_blue = (downside_pixel1.blue+downside_pixel2.blue+downside_pixel3.blue+downside_pixel4.blue+pixel_center.blue+downside_pixel5.blue)/6

                pixel_new_image.red = downside_avg_red
                pixel_new_image.green = downside_avg_green
                pixel_new_image.blue = downside_avg_blue
            # This step is catching pixel which has 5 neighbors and is at left side of photo
            if x == 0 and 1 <= y < img.height - 1:
                left_pixel1 = img.get_pixel(x,y-1)
                left_pixel2 = img.get_pixel(x+1,y-1)
                left_pixel3 = img.get_pixel(x+1,y)
                left_pixel4 = img.get_pixel(x,y+1)
                left_pixel5 = img.get_pixel(x+1,y+1)

                left_avg_red = (left_pixel1.red+left_pixel2.red+pixel_center.red+left_pixel3.red+left_pixel4.red+left_pixel5.red)/6
                left_avg_green = (left_pixel1.green+left_pixel2.green+pixel_center.green+left_pixel3.green+left_pixel4.green+left_pixel5.green)/6
                left_avg_blue = (left_pixel1.blue+left_pixel2.blue+pixel_center.blue+left_pixel3.blue+left_pixel4.blue+left_pixel5.blue)/6

                pixel_new_image.red = left_avg_red
                pixel_new_image.green = left_avg_green
                pixel_new_image.blue = left_avg_blue
            # This step is catching pixel which has 5 neighbors and is at right side of photo
            if x == img.width-1 and 1 <= y < img.height - 1:
                right_pixel1 = img.get_pixel(x-1,y-1)
                right_pixel2 = img.get_pixel(x,y-1)
                right_pixel3 = img.get_pixel(x-1,y)
                right_pixel4 = img.get_pixel(x-1,y+1)
                right_pixel5 = img.get_pixel(x,y+1)

                right_avg_red = (right_pixel1.red+right_pixel2.red+right_pixel3.red+pixel_center.red+right_pixel4.red+right_pixel5.red)/6
                right_avg_green = (right_pixel1.green+right_pixel2.green+right_pixel3.green+pixel_center.green+right_pixel4.green+right_pixel5.green)/6
                right_avg_blue = (right_pixel1.blue+right_pixel2.blue+right_pixel3.blue+pixel_center.blue+right_pixel4.blue+right_pixel5.blue)/6

                pixel_new_image.red = right_avg_red
                pixel_new_image.green = right_avg_green
                pixel_new_image.blue = right_avg_blue
            # This step is catching pixel which has 3 neighbors and is at left-up corner
            if x == 0 and y == 0:
                left_up_pixel1 = img.get_pixel(x+1,y)
                left_up_pixel2 = img.get_pixel(x,y+1)

                left_up_avg_red = (pixel_center.red+left_up_pixel1.red+left_up_pixel2.red)/3
                left_up_avg_green = (pixel_center.green+left_up_pixel1.green+left_up_pixel2.green)/3
                left_up_avg_blue = (pixel_center.blue+left_up_pixel1.blue+left_up_pixel2.blue)/3

                pixel_new_image.red = left_up_avg_red
                pixel_new_image.green = left_up_avg_green
                pixel_new_image.blue = left_up_avg_blue
            # This step is catching pixel which has 3 neighbors and is at right-up corner
            if x == img.width-1 and y == 0:
                right_up_pixel1 = img.get_pixel(x-1,y)
                right_up_pixel2 = img .get_pixel(x,y+1)

                right_up_avg_red = (right_up_pixel1.red+pixel_center.red+right_up_pixel2.red)/3
                right_up_avg_green = (right_up_pixel1.green+pixel_center.green+right_up_pixel2.green)/3
                right_up_avg_blue =(right_up_pixel1.blue+pixel_center.blue+right_up_pixel2.blue)/3

                pixel_new_image.red = right_up_avg_red
                pixel_new_image.blue = right_up_avg_blue
                pixel_new_image.green = right_up_avg_green
            # This step is catching pixel which has 3 neighbors and is at left-down corner
            if x == 0 and y == img.height-1:
                left_down_pixel1 = img.get_pixel(x,y-1)
                left_down_pixel2 = img.get_pixel(x+1,y)

                left_down_avg_red = (left_down_pixel1.red+pixel_center.red+left_down_pixel2.red)/3
                left_down_avg_green = (left_down_pixel1.green+pixel_center.green+left_down_pixel2.green)/3
                left_down_avg_blue = (left_down_pixel1.blue+pixel_center.blue+left_down_pixel2.blue)/3

                pixel_new_image.red = left_down_avg_red
                pixel_new_image.green = left_down_avg_green
                pixel_new_image.blue = left_down_avg_blue
            # This step is catching pixel which has 3 neighbors and is at right-down corner
            if x == img.width-1 and y == img.height-1:
                right_down_pixel1 = img.get_pixel(x,y-1)
                right_down_pixel2 = img.get_pixel(x-1,y)

                right_down_avg_red = (right_down_pixel1.red+pixel_center.red+right_down_pixel2.red)/3
                right_down_avg_green = (right_down_pixel1.green+pixel_center.green+right_down_pixel2.green)/3
                right_down_avg_blue = (right_down_pixel1.blue+pixel_center.blue+right_down_pixel2.blue)/3

                pixel_new_image.red = right_down_avg_red
                pixel_new_image.green = right_down_avg_green
                pixel_new_image.blue = right_down_avg_blue

    return new_image


def main():
    """
    This program will blur the origin image and shows two photos for comparison.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
