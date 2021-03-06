from graphics import *
import math
import time


class Konna:
    def __init__(self, window_dim_x=640, window_dim_y=480, no_bounds=False, framerate=1000, update_interval=1000, show_circle=True):
        self.line_color = 'black'
        self.__line_width = 1
        self.__orientation = 0

        self.__pos_x = 0
        self.__pos_y = 0

        self.pen_down = False

        self.window = GraphWin('Konna', window_dim_x, window_dim_y, autoflush=False)

        self.__window_dim_x = window_dim_x
        self.__window_dim_y = window_dim_y

        self.no_bounds = no_bounds

        self.framerate = framerate


        self.update_interval = update_interval
        self.counter = 0
        self.show_circle = show_circle

        self.drawSelf()
        # self.circle = Circle(self.position, 5)

    def drawSelf(self):
        if self.show_circle:
            self.__clearCircles()
            self.circle.draw(self.window)
        # self.update()

    def __clearCircles(self):
        for i in self.window.items[:]:
            if isinstance(i, Circle):
                i.undraw()

    def update(self):
        if not self.counter % self.update_interval:
            self.window.update()
            time.sleep(1 / self.framerate)
        self.counter += 1

    def penDown(self):
        self.pen_down = True

    def penUp(self):
        self.pen_down = False

    def turn(self, amount):
        self.orientation += amount

    def move(self, distance):
        if self.pen_down:
            pos_x_old = self.pos_x
            pos_y_old = self.pos_y

            draw_start_pos = self.position

            self.pos_x = pos_x_old + math.sin(math.radians(self.orientation)) * distance
            self.pos_y = pos_y_old + math.cos(math.radians(self.orientation)) * distance

            draw_end_pos = self.position

            line = Line(draw_start_pos, draw_end_pos)
            line.setWidth(self.__line_width)
            line.setFill(self.line_color)
            line.draw(self.window)

        else:
            self.pos_x += math.sin(math.radians(self.orientation)) * distance
            self.pos_y -= math.cos(math.radians(self.orientation)) * distance

        self.drawSelf()
        self.update()

    def goTo(self, x, y):
        if self.pen_down:
            line_start_pos = self.position

            self.pos_x = x
            self.pos_y = y

            line_end_pos = self.position

            line = Line(line_start_pos, line_end_pos)
            line.setFill(self.line_color)
            line.setWidth(self.__line_width)

            line.draw(self.window)

        else:
            self.pos_x = x
            self.pos_y = y

        self.drawSelf()
        self.update()

    def jump(self, x, y):
        if self.pen_down:
            line_start_pos = self.position

            self.pos_x += x
            self.pos_y += y

            line_end_pos = self.position

            line = Line(line_start_pos, line_end_pos)
            line.setFill(self.line_color)
            line.setWidth(self.__line_width)

            line.draw(self.window)

        else:
            self.pos_x += x
            self.pos_y += y

        self.drawSelf()
        self.update()

    @property
    def circle(self):
        # position = self.position
        # rounded_x = round(position.x, 0)
        # rounded_y = round(position.y, 0)

        cir = Circle(self.position, 5)
        cir.setFill('black')
        return cir

    @property
    def position(self):
        return Point(round(self.pos_x, 0) + self.__window_dim_x / 2, round(self.pos_y, 0) + self.__window_dim_y / 2)

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        self.__orientation = orientation % 360

    @property
    def line_width(self):
        return self.__line_width

    @line_width.setter
    def line_width(self, line_width):
        self.__line_width = line_width if line_width >= 0 else 0

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, pos_x):
        if self.no_bounds:
            self.__pos_x = pos_x
        else:
            if pos_x < -(self.__window_dim_x / 2):
                self.__pos_x = -(self.__window_dim_x / 2)
            elif pos_x > self.__window_dim_x / 2:
                self.__pos_x = (self.__window_dim_x / 2)
            else:
                self.__pos_x = pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @pos_y.setter
    def pos_y(self, pos_y):
        if self.no_bounds:
            self.__pos_y = pos_y
        else:
            if pos_y < -(self.__window_dim_y / 2):
                self.__pos_y = -(self.__window_dim_y / 2)
            elif pos_y > self.__window_dim_y / 2:
                self.__pos_y = (self.__window_dim_y / 2)
            else:
                self.__pos_y = pos_y

    @property
    def window_dim_x(self):
        return self.__window_dim_x

    @property
    def window_dim_y(self):
        return self.__window_dim_y

    def __del__(self):
        self.window.close()
        del self
