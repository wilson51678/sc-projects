"""
File: draw_line
Name:Wilson Wang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# this constant is use for oval size
SIZE = 10
# this is a window which can use in every function
window = GWindow()

# this global various counts the hole_punch in the window
click = 0
# this global various creates Goval in any function
hole = GOval(SIZE, SIZE)

# These various(x1,y1,x2,y2) control the location to create Gline
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(hole_punch)


def hole_punch(mouse):
    """
    This function should creates a hole in the window when the user hit the mouse in the first time, and creates a
    line when user hit the mouse at the second time.
    :param mouse: mouse should trigger this function
    :return: hole
    """
    global click, x1, y1

    click += 1
    # this step check the number of hole in the window
    if click % 2 == 1:
        # this various update the location in the global various
        x1 = mouse.x
        y1 = mouse.y
        window.add(hole, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
    # this step creates a line in the window because a hole is already in the window
    if click % 2 == 0:
        x2 = mouse.x
        y2 = mouse.y
        line = GLine(x1, y1, x2, y2)
        window.add(line)
        window.remove(hole)


if __name__ == "__main__":
    main()
