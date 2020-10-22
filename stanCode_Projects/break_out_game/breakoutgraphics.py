"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        # memorize paddle's location at y
        self.paddle_locate = paddle_offset

        # memorize ball's radius
        self.radius = ball_radius

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width,paddle_height, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window_width-ball_radius)/2, y=(self.window_height-ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dy = -self.__dy

        # boolean for controlling the start of animation and mouse click trigger.
        self.ball_is_moving = False

        # Initialize our mouse listeners.
        onmouseclicked(self.start_move)
        onmousemoved(self.drag_paddle)

        # Draw bricks.
        brick_y = brick_offset
        for i in range(self.brick_rows):
            brick_x = 0
            if i > 0:
                brick_y += brick_spacing+brick_height
            for j in range(self.brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'
                if i == 2 or i == 3:
                    self.brick.fill_color = 'orange'
                if i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'
                if i == 6 or i == 7:
                    self.brick.fill_color = 'green'
                if i == 8 or i == 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=brick_x, y=brick_y)
                brick_x += brick_spacing+brick_width

        # set 'score' as a counter for counting destroyed bricks
        self.score = 0

    def drag_paddle(self, mouse):
        """
        onmousemove's function, when the mouse move, the paddle should move with mouse in a vertical line. If the mouse is
        out of window, the paddle should stop at left or right side wall.
        :param mouse: mouse move
        """
        self.paddle.x = mouse.x-(self.paddle.width/2)
        self.paddle.y = self.window.height-self.paddle_locate
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x >= self.window.width-self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width

    def get_dx(self):
        """
        for user to get dx speed
        :return: self.__dx
        """
        return self.__dx

    def get_dy(self):
        """
        for user to get dy speed
        :return: self.__dy
        """
        return self.__dy

    def start_move(self, m):
        """
        :param m: mouse click
        onmouseclick's function. when the mouse click, the boolean value should change and start the animation at user side.
        """
        self.ball_is_moving = True

    def pause_move(self):
        """
        the method should change the boolean value at user side
        """
        self.ball_is_moving = False

    def reset_ball(self):
        """
        the method should help user set a new ball at the center of window
        """
        self.window.remove(self.ball)
        self.ball = GOval(self.radius*2, self.radius*2, x=(self.window_width-self.radius)/2, y=(self.window_height-self.radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

    def get_object_at(self):
        """
        Four corners of ball will be detectors. When any detector find object, the ball will bounce.
        If the object is brick, the object should be eliminated.
        """
        # These are the four corners of ball and are use as detectors.
        ball_hit1 = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_hit2 = self.window.get_object_at(self.ball.x, self.ball.y+2*self.radius)
        ball_hit3 = self.window.get_object_at(self.ball.x+2*self.radius, self.ball.y)
        ball_hit4 = self.window.get_object_at(self.ball.x+2*self.radius, self.ball.y+2*self.radius)

        # when detector find object, the object should be delete.
        if ball_hit1 is not None:
            # this step prevent deleting paddle
            if ball_hit1 is not self.paddle:
                self.window.remove(ball_hit1)
                # count score when brick is deleted
                self.score += 1
                self.__dy = -self.__dy
            else:
                # This step prevent the ball stuck in paddle.
                if self.__dy > 0:
                    self.__dy = -self.__dy

        elif ball_hit2 is not None:
            if ball_hit2 is not self.paddle:
                self.window.remove(ball_hit2)
                self.score += 1
                self.__dy = -self.__dy
            else:
                if self.__dy > 0:
                    self.__dy = -self.__dy

        elif ball_hit3 is not None:
            if ball_hit3 is not self.paddle:
                self.window.remove(ball_hit3)
                self.score += 1
                self.__dy = -self.__dy
            else:
                if self.__dy > 0:
                    self.__dy = -self.__dy

        elif ball_hit4 is not None:
            if ball_hit4 is not self.paddle:
                self.window.remove(ball_hit4)
                self.score += 1
                self.__dy = -self.__dy
            else:
                if self.__dy > 0:
                    self.__dy = -self.__dy

    def window_collision(self):
        """
        the dx and dy of ball should changer into the opposite value when the moving ball hit on the left, right and top
        of wall.
        """
        if 0 >= self.ball.x or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if 0 >= self.ball.y:
            self.__dy = -self.__dy

    def get_brick_num(self):
        return self.brick_cols * self.brick_rows

