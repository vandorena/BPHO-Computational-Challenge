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

        # Non-Variable Variables (don't change after creation)
        # initial velocity vector
        self.initialVel = v
        if angle > (math.pi / 2):
            angle = math.radians(angle)
        self.initialAngle = angle  # expected in radians (but if bigger than pi/2, then assumes not and converts)
        self.initialHeight = y

        # Variable Variables
        # variable coordinates
        self.x = x
        self.y = y

        # velocity components
        if vx is not None and vy is not None:               # if vx and vy are specified over v and angle
            self.vx = vx
            self.vy = vy
            self.initialAngle = math.atan2(self.vy, self.vx)
            self.initialVel = math.sqrt(vx**2 + vy**2)
        else:                                               # if not specified
            self.vx = math.cos(self.initialAngle) * v
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


class ProjectileList(Projectile):
    
    def __init__(self, x: float = 0, y: float = 2, v: float = 20, angle: float = math.radians(45), vx=None, vy=None) -> None:
        super().__init__(x, y, v, angle, vx, vy)
        self._data = [[0],[0],[round(self.vx,4)],[round(self.vy,4)],[self.initialVel],[self.x],[self.y]]

    def log(self,roundTo=None) -> None:
        """
        Logs the current state of the projectile at each time step.
        This method updates the data list with the current values of time, range fraction, horizontal velocity, vertical velocity, velocity magnitude, x-coordinate, and y-coordinate. The values are rounded to the specified number of decimal places.
        Parameters:
        rounTo
        Returns:
        None
        """
        if roundTo == None:
            roundTo = 4
        self._data[0].append(round(self._data[0][-1] + Constants.TIMESTEP, roundTo))
        self._data[1].append(round(self._data[1][-1] + Constants.FRACTION_OF_RANGE, roundTo))  # takes the last fraction of range in list, then adds delta distance
        self._data[2].append(round(self.vx, roundTo))
        self._data[3].append(round(self.vy, roundTo))
        self._data[4].append(round(math.sqrt(self.vx ** 2 + self.vy ** 2), roundTo))  # uses pythagoras to calculate magnitude of velocity
        self._data[5].append(round(self.x, roundTo))
        self._data[6].append(round(self.y, roundTo))

    def getXgetY(self):
        """
        Returns the x and y coordinates of the projectile as a tuple.

        Parameters:
        None

        Returns:
        Tuple: A tuple containing the x and y coordinates of the projectile.
        """
        return self._data[5], self._data[6]

