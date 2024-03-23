import math
import Projectile
import Constants


def integrationFunc(lim: float) -> float:
    return 0.5 * math.log(abs(math.sqrt(1 + lim**2) + lim)) + 0.5 * lim * math.sqrt(1 + lim ** 2)


def calculateDistanceTravelled(proj: Projectile.Projectile) -> None:
    """
    A procedure that prints the distance traveled of a projectile.
    :param proj: Projectile.Projectile
    :return: None
    """
    Range = (proj.initialVel**2/Constants.g) * (math.sin(proj.initialAngle) * math.cos(proj.initialAngle) + math.cos(proj.initialAngle) * math.sqrt(math.sin(proj.initialAngle) ** 2 + (2 * Constants.g * proj.initialHeight) / proj.initialVel ** 2))
    multiplier = (proj.initialVel**2) / (Constants.g * (1 + math.tan(proj.initialAngle) ** 2))
    lowerLimit = math.tan(proj.initialAngle) - (Constants.g * Range) * (1 + math.tan(proj.initialAngle) ** 2) / (proj.initialVel ** 2)
    upperLimit = math.tan(proj.initialAngle)

    distanceTraveled = multiplier * (integrationFunc(upperLimit) - integrationFunc(lowerLimit))
    print('distance Travelled:', distanceTraveled)


if __name__ == '__main__':
    projectile = Projectile.Projectile(x=0, y=2, v=10, angle=60)
    calculateDistanceTravelled(projectile)
