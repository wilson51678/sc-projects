"""
File: bouncing_ball
Name: Wilson Wang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 3          # This constant is use for horizontal speed
DELAY = 10      # This constant is use for 'pause' rate
GRAVITY = 1     # This constant is the vertical speed to be add in every while loop
SIZE = 20       # This constant is use for ball size
REDUCE = 0.9    # This constant should multiply vertical speed when the ball bounce back from the floor
START_X = 30    # the location where the ball should start
START_Y = 40    # the location where the ball should start


# Global various
out_of_window = 0           # This various counts the times when the ball is out of window
ball = GOval(SIZE, SIZE)    # This is use for any function or def main()
ball_is_moving = False      # a boolean to control animation start
window = GWindow(800, 500, title='bouncing_ball.py')    # Gwindow


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(ball_move)


def ball_move(mouse):
    """
    This function is an animation that a ball move toward right side in the gravity situation. The speed should be
    slower in each time the ball bounce back from the floor and the limit times animation engage is 3.
    :param mouse: when the mouse click, the animation should start
    :return:
    """
    global out_of_window, ball_is_moving
    # This step limit the times of ball moving. If the various > 3, the function should pass
    if out_of_window < 3 and not ball_is_moving:
        # this is the start vertical speed
        rx = 1
        while True:
            # this step control mouse click to be invalid while the ball is moving
            ball_is_moving = True
            ball.move(VX, rx)
            rx += GRAVITY

            # This step engage when the ball hit the bottom of window
            if ball.y + SIZE >= window.height:
                rx = -rx * REDUCE

            # This step engage when the ball is out of window
            if ball.x >= window.width:
                # when the ball is out of window, the various should add count
                out_of_window += 1
                # this step open the mouse click function to be available
                ball_is_moving = False
                break
            pause(DELAY)
        window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
