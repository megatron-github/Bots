"""
 *****************************************************************************
   FILE:        bots.py

   AUTHOR:      Truong Pham

   ASSIGNMENT:  Project 9: Bots

   DATE:        11/4/2018

   DESCRIPTION: Create two robots and draw them on the window. The two robots
                had to move individually when each of them is clicked. The
                clicked robot will move randomly (move in given direction, 
                turn left or right) and speed up or slow down randomly for 
                each click. If the clicked bot is overlapped on another bot,
                then the parts of the clicked bot will change colors and send 
                back to its starting position.

 *****************************************************************************
"""
import random
from cs110graphics import *

class Bot:
    """ Bot """
    def __init__(self, win, width, center, direction='east', speed=20,
                 body_color="crimson", heart_color="yellow"):
        """ Define and construct characteristics and properties 
            of the robots. """

        self._win = win                  # The Window on which bot is drawn.
        self._width = width              # The robot's width.
        self._center = center            # The robot's center.
        self._start = center             # The robot's starting position.
        self._direction = direction      # The current direction of robot.
        self._speed = speed              # The number of pixel change per move.
        self._body_color = body_color    # The color of the robot's body.
        self._heart_color = heart_color  # The color of the robot's heart.

        # Draw the robot with given characteristics.
        self._body = Square(win, self._width, self._center)
        self._body.set_fill_color(self._body_color)
        self._body.set_depth(1)
        self._heart = Square(win, self._width // 2, self._center)
        self._heart.rotate(45)
        self._heart.set_fill_color(self._heart_color)
        self._heart.set_depth(0) 

        # All the parts of the robots (body, heart, etc.)
        self._parts = [self._body, self._heart] 

    def add_to_window(self):
        """ Add all the parts (characteristics and properties) 
            to the windown. """

        # Add the body and the heart of the robot to window.
        for part in self._parts:
            self._win.add(part)

    def add_handler(self, handler):
        """ provide call-back function for user interaction """

        # don't modify this.
        for part in self._parts:
            part.add_handler(handler)   
            
    def move(self):
        """ Given the bot’s current state, move the bot by speed pixels 
            in the bot’s direction. Note that the bot’s center should 
            change as well, so that collision detection can operate 
            properly. """

        # Make robot to move in different speed or turn direction 
        # randomly every clicked.
        directions = [1, 2, 3, 4]
        direction = random.choice(directions)
        if direction == 1:
            self.turn_left()
        if direction == 2:
            self.turn_right()
        if direction == 3:
            self.slow_down()
        if direction == 4:
            self.speed_up()

        # Cite: Lucas Barusek
        # Desc: For every part of the robot that moved, change the 
        # center of the robot for each time. However, the total shift 
        # of the center had to add up to the given speed pixels.

        # For each part of the robot, move it in given direction and given 
        # speed, while adjusting the center of each part of the robot.
        center_x = self._center[0]
        center_y = self._center[1]
        for part in self._parts:
            if self._direction == 'east':
                part.move(self._speed, 0)
                center_x += (self._speed / len(self._parts))
            if self._direction == 'west':
                part.move(-self._speed, 0)
                center_x -= (self._speed / len(self._parts))
            if self._direction == 'north':
                part.move(0, -self._speed)
                center_y -= (self._speed / len(self._parts))
            if self._direction == 'south':
                part.move(0, self._speed)
                center_y += (self._speed / len(self._parts))

        # Adjusting and finalize the center of the robot in a
        # tuple form.
        self._center = (int(center_x), int(center_y))

    def turn_left(self):
        """ Changes the bot’s direction, for example, 
            ‘west’ becomes ‘south’. """

        # Check the current direction of the robot is moving 
        # (or facing), then turn left from the direciton that
        # the robot is facing.
        if self._direction == 'east':
            self._direction = 'north'
            return self._direction
        if self._direction == 'west':
            self._direction = 'south'
            return self._direction
        if self._direction == 'north':
            self._direction = 'west'
            return self._direction
        if self._direction == 'south':
            self._direction = 'east'
            return self._direction
        return self._direction

    def turn_right(self):
        """  Changes the bot’s direction, for example, 
            ‘north’ becomes ‘east’. """

        # Check the current direction of the robot is moving 
        # (or facing), then turn right from the direciton that
        # the robot is facing.
        if self._direction == 'east':
            self._direction = 'south'
            return self._direction
        if self._direction == 'west':
            self._direction = 'north'
            return self._direction
        if self._direction == 'north':
            self._direction = 'east'
            return self._direction
        if self._direction == 'south':
            self._direction = 'west'
            return self._direction
        return self._direction

    def speed_up(self):
        """ Increase the bot’s speed. """

        # Bot will move five speed pixels faster
        # than the original given speed fixels every
        # click randomly.
        speed = self._speed + 5
        return speed 

    def slow_down(self):
        """ Decrease the bot’s speed. """

        # Bot will move five speed pixels slower
        # than the original given speed fixels every
        # click randomly.
        speed = self._speed - 5
        return speed

    def crash(self):
        """ When the clicked robot overlap with another robot, change
            the color of the clicked robot randomly for each part, then
            move the clikced bot backs to the starting position. """

        # Cite: Ian Nduhiu 
        # Desc: How to a back ground image after the bots crashed

        # Add an image to the background after the bots are crashed
        self._win.add(Image(self._win, "CatMeme.jpg", 400, 400, (200, 200)))

        # Given a list of colors, randomly change the color of each part
        # of the clicked bot when it overlaps another bot.
        colors = ["deepskyblue", "turquoise", "yellow", "darksalmon", 
                  "lightseagreen", "coral", "darkmagenta", "orchid", 
                  "thistle", "hotpink", "lavender", "forestgreen"]
        for part in self._parts:
            part.set_fill_color(random.choice(colors))

        # For each part of the robot, move the part back to the
        # starting position when the clicked bot overlaps another
        # bot.
        for part in self._parts:
            part.move_to(self._start)
        self._center = (self._start)

    def uncrash(self):
        """ Restore the bot to its previous un-crashed state. """

        # Change the color of each part of 
        # the crashed bot to their original colors.
        # self._body.set_fill_color(self._body_color)
        # self._heart.set_fill_color(self._heart_color)

    def get_width(self):
        """ Return the called bot’s width. """

        # Return the width of called bot.
        return self._width

    def get_center(self):
        """ Return the called bot’s center """

        # Return the center of the called bot.
        return self._center

    def overlaps(self, other):
        """ Return True if this bot overlaps with the other 
            bot, False otherwise. """

        # Find Bot1's four corners and their coordinates (in tuples).
        self_tl = (self.get_center()[0] - (self._width // 2), 
                   self.get_center()[1] - (self._width // 2))
        self_tr = (self.get_center()[0] - (self._width // 2), 
                   self.get_center()[1] + (self._width // 2))
        self_bl = (self.get_center()[0] + (self._width // 2), 
                   self.get_center()[1] - (self._width // 2))
        self_br = (self.get_center()[0] + (self._width // 2), 
                   self.get_center()[1] + (self._width // 2))

        # Find Bot2's four corners and their coordinates (in tuples).
        other_tl = (other.get_center()[0] - (other.get_width() // 2), 
                    other.get_center()[1] - (other.get_width() // 2))
        other_tr = (other.get_center()[0] - (other.get_width() // 2), 
                    other.get_center()[1] + (other.get_width() // 2))
        other_bl = (other.get_center()[0] + (other.get_width() // 2), 
                    other.get_center()[1] - (other.get_width() // 2))
        other_br = (other.get_center()[0] + (other.get_width() // 2), 
                    other.get_center()[1] + (other.get_width() // 2))

        # Make a nest list of all the pixels (and their locations) that 
        # is in the area of Bot1.
        self_grid = []
        for x in range(self_tl[0], self_br[0] + 1):
            self_row = []
            for y in range(self_tl[1], self_br[1] + 1):
                self_row.append((x, y))
            self_grid.append(self_row)

        # Make a nest list of all the pixels (and their locations) that 
        # is in the area of Bot2.
        other_grid = []
        for x in range(other_tl[0], other_br[0] + 1):
            other_row = []
            for y in range(other_tl[1], other_br[1] + 1):
                other_row.append((x, y))
            other_grid.append(other_row)

        # Cite: Ian Nduhiu 
        # Desc: Take all pixels existed in the clicked bot's area, if
        # any pixels in the clicked bot is the same as the pixels in 
        # other bot, then bots are overlapped on each other.

        # Check if any location of any corners of Bot1 is the same 
        # as the location of the pixels of Bot2. If yes, return True. 
        for row in self_grid:
            for loc in row:
                if loc in (other_tl, other_tr, \
                           other_bl, other_br):
                    return True

        # Check if any location of any corners of Bot2 is the same 
        # as the location of the pixels of Bot1. If yes, return True. 
        for row in other_grid:
            for loc in row:
                if loc in (self_tl, self_tr, \
                           self_bl, self_br):
                    return True
        return False

class BotHandler(EventHandler):
    """ A class for handling events for Bots. """

    def __init__(self, bot, other_bot=None):
        """ Constructor """

        # Add all created bots to the handler.
        EventHandler.__init__(self)
        self._bot = bot
        self._bot2 = other_bot

    def handle_mouse_release(self, event):
        """ This code will run when the user clicks on a bot """

        # For every click on the bot, move the bot in a given 
        # direction and check if the clicked bot is overlapped
        # with another bot.
        self._bot.move()
        if self._bot.overlaps(self._bot2) is True:
            self._bot.crash()

def program(win):
    """ Set up the graphics in the window """
    
    # Create two robots with certain characteristics and properties,
    # then add them to window.
    pain = Bot(win, 100, (65, 200))
    neji = Bot(win, 50, (350, 200))
    pain.add_to_window()
    neji.add_to_window()

    # Cite: Chiara Bondi
    # Desc: A bot can have its own handler, while also include
    # another bot in its handler.

    # Add the each robot and its friend-robot to the handler,
    # to check behavior of both bot when a bot is clicked.
    pain.add_handler(BotHandler(pain, neji))
    neji.add_handler(BotHandler(neji, pain))

def main():
    """ The main program """
    StartGraphicsSystem(program)

if __name__ == "__main__":
    main()
