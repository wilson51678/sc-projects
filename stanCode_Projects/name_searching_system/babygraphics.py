"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

File: babygraphics.py
Name: Wilson Wang

This program shows baby names rank from 1900-2010 into graphics. User could search any names in tkinter graphics. The data
is import from dictionary'new_names'

"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # set the gap between every year in vertical line.
    gap_width = (width-GRAPH_MARGIN_SIZE*2)//len(YEARS)
    x_coordinate_list = []
    # get the x_coordinate by year into list 'x_coordinate_list'
    for i in range(len(YEARS)):
        x_coordinate_list.append(GRAPH_MARGIN_SIZE + gap_width*i)

    return x_coordinate_list[year_index]


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # This step draws vertical line and text by years
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    # Write your code below this line
    #################################

    # This value use for target the location of rank at vertical year line
    line_height_rank = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000

    name_count = 0
    # get name year from list'lookup_names'
    for name in lookup_names:
        # var 'i' use for counter in for loop
        i = 0

        # 'last_x' and 'last_y' use for memorizing the coordinate in last loop
        last_x = 0
        last_y = 0

        # set different color in every loop as 4 colors in a round
        color = COLORS[name_count % len(COLORS)]

        # counter in the first for-loop
        name_count += 1

        # get year from list'YEARS'
        for year in YEARS:
            # this step check whether the name is on the list of certain year
            if str(year) in name_data[name]:
                # get rank from dictionary'new_name'
                rank = int(name_data[name][str(year)])
                text_set = (name, rank)
            else:
                rank = 1000
                text_set = (name, '*')

            # Get x coordinate by year from function
            x = get_x_coordinate(CANVAS_WIDTH, i)
            # Set y coordinate
            y = GRAPH_MARGIN_SIZE + (rank * line_height_rank)
            canvas.create_text(x + TEXT_DX, y, text=text_set, anchor=tkinter.SW, fill=color)

            # This step create the line and start in the second times of for-loop.
            if i >= 1:
                canvas.create_line(last_x, last_y, x, y, width=LINE_WIDTH, fill=color)

            # Memorize x and y location for create line in next loop
            last_x = x
            last_y = y

            i += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
