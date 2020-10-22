"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3  # the times that players could fail in the game


def main():
    """
    It's a breakout game. A ball will start bouncing in a GWindow when the player click the mouse.
    Player can control the paddle bar by mouse and use paddle to bounce ball toward bricks.
    Win condition: break all bricks with less than 3 times fail
    """
    graphics = BreakoutGraphics()
    # set the times that player can fail
    live = NUM_LIVES
    # Add animation loop here!
    while True:
        # player has 3 times to fail the game

        if live > 0:

            # the animation should start when the mouse click
            if graphics.ball_is_moving:
                graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                graphics.get_object_at()
                graphics.window_collision()

                # when the ball is out of window, the animation should paused and set a new ball at the center of window
                if graphics.ball.y + graphics.ball.height > graphics.window.height:
                    # player will lose one life
                    live -= 1
                    graphics.pause_move()
                    graphics.reset_ball()

            # the rate to delay animation
            pause(FRAME_RATE)

        # the game will end when player fail 3 times or break all the bricks
        if live == 0 or graphics.score == graphics.get_brick_num():
            break


if __name__ == '__main__':
    main()
