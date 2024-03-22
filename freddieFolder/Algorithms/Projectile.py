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
        # initial coordinates
        self.x = x
        self.y = y

        # initial velocity vector
        self.initialVel = v
        self.initialAngle = math.radians(angle)  # expected in degrees

        # velocity components
        self.vx = vx
        if vx is None:
            self.vx = math.cos(self.initialAngle) * v

        self.vy = vy
        if vy is None:
            self.vy = math.sin(self.initialAngle) * v

        # history of projectile
        self._data = {'totalTime': [0], 'rangeFraction': [0], 'vx': [self.vx], 'vy': [self.vy], 'v': [self.initialVel], 'x': [self.x], 'y': [self.y]}

    def log(self, rangeFraction=False) -> None:
        if rangeFraction:
            self._data['rangeFraction'].append(self._data['rangeFraction'][-1] + Constants.FRACTION_OF_RANGE)
        self._data['totalTime'].append(self._data['totalTime'][-1] + Constants.TIMESTEP)  # takes the last time in list, then adds deltaTime
        self._data['vx'].append(self.vx)
        self._data['vy'].append(self.vy)
        self._data['v'].append(math.sqrt(self.vx ** 2 + self.vy ** 2))  # uses pythagoras to calculate magnitude of velocity
        self._data['x'].append(self.x)
        self._data['y'].append(self.y)

    def printAsTable(self, columns: iter = ('totalTime', 'rangeFraction', 'vx', 'vy', 'v', 'x', 'y'), exclude: iter = ()) -> None:
        return printData.print_table([[x] + self._data[x] for x in self._data if x in columns and x not in exclude], True)

    def getData(self) -> dict:
        return self._data


