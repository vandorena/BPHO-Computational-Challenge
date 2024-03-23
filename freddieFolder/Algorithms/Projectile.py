import math
import Constants
import printData


class Projectile:
    """
    Projectile class.
    This class stores the variables for the projectile function.
    It also has a function to store variables, after being updated, for later use.
    Also, a function to retrieve this data and print it.
    """
    def __init__(self, x: float = 0, y: float = 2, v: float = 20, angle: float = math.radians(45), vx=None, vy=None) -> None:
        """
        The init function
        :param x: the starting x position
        :param y: the starting y position (or height)
        :param v: the initial velocity
        :param angle: the initial angle of trajectory
        :param vx: optional - can specify vx and vy instead of v and angle
        :param vy: optional - can specify vx and vy instead of v and angle
        :return: None
        """
        # initial coordinates
        self.x = x
        self.y = y

        # initial velocity vector
        self.initialVel = v
        if angle > (math.pi / 2):
            angle = math.radians(angle)
        self.initialAngle = angle  # expected in radians (but if bigger than pi/2, then assumes not and converts)

        # velocity components
        self.vx = vx
        if vx is None:
            self.vx = math.cos(self.initialAngle) * v

        self.vy = vy
        if vy is None:
            self.vy = math.sin(self.initialAngle) * v

        # history of projectile
        self._data = {'totalTime': [0], 'rangeFraction': [0], 'vx': [round(self.vx, 4)], 'vy': [round(self.vy, 4)], 'v': [self.initialVel], 'x': [self.x], 'y': [self.y]}

    def log(self) -> None:
        """
        Saves current projectile variables to data dictionary
        :return: None
        """
        roundTo = 4
        self._data['totalTime'].append(round(self._data['totalTime'][-1] + Constants.TIMESTEP, roundTo))  # takes the last time in list, then adds deltaTime
        self._data['rangeFraction'].append(round(self._data['rangeFraction'][-1] + Constants.FRACTION_OF_RANGE, roundTo))  # takes the last fraction of range in list, then adds delta distance
        self._data['vx'].append(round(self.vx, roundTo))
        self._data['vy'].append(round(self.vy, roundTo))
        self._data['v'].append(round(math.sqrt(self.vx ** 2 + self.vy ** 2), roundTo))  # uses pythagoras to calculate magnitude of velocity
        self._data['x'].append(round(self.x, roundTo))
        self._data['y'].append(round(self.y, roundTo))

    def printAsTable(self, columns: iter = ('totalTime', 'rangeFraction', 'vx', 'vy', 'v', 'x', 'y'), exclude: iter = ()) -> None:
        """

        :param columns: Chooses what to include (by default = all of them)
        :param exclude: Chooses what to exclude (by default = none of them)
        :return: None
        """
        printData.print_table([[x] + self._data[x] for x in self._data if x in columns and x not in exclude], True)

    def getData(self) -> dict:
        """
        A function to get dictionary data.
        :return: The raw dictionary data
        """
        return self._data


