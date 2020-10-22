"""
SC101 - Assignment3
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

file:stanCodoshop.py
Name: Wilson Wang
-----------------------------------------------

This program help users to create a photo without humans. The program concept is using multiple images, which took at
same scene to get best pixels and use these pixels to reconstruct a new photo.

"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    dist = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    r = 0
    g = 0
    b = 0
    count = 0

    # get each pixel in the list and count the total value of red, green and blue.
    for pixel in pixels:
        r += pixel.red
        g += pixel.green
        b += pixel.blue
        count += 1

    # count the average of red, green and blue
    red = r // count
    green = g // count
    blue = b // count

    # set a list of average red, green and blue value for return
    rgb = [red, green, blue]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages
    """

    avg = get_average(pixels)

    # set a box for pixel's minimum value
    minimum = 0
    # set a box to storage the best pixel
    best_pixel = None

    # get pixel in the pixels list
    for i in range(len(pixels)):
        pixel_distance = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])

        # storage the first data in empty boxes for comparison
        if i == 0:
            minimum = pixel_distance
            best_pixel = pixels[i]
        else:
            # this step should compare the minimum value distance(best pixel)
            if pixel_distance < minimum:
                minimum = pixel_distance
                best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    # these two for loop should target every location in the image
    for y in range(height):
        for x in range(width):
            result_pixel = result.get_pixel(x, y)
            pixels = []

            # get the same location from all images, and create a list of pixels
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)

            # use the function to get the best pixel
            best = get_best_pixel(pixels)

            # set the best pixel into the blank canvas
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
