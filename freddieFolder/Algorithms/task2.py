import math
import Projectile
import Constants


def calculateTrajectoryData(proj: Projectile.Projectile) -> None:
    """
    A procedure that takes in a projectile object and runs it through a drag-less projectile motion using the projectile equation (analytic method).
    It keeps increasing x regularly until it hits the floor (y < 0).
    :param proj: Projectile.Projectile
    :return: None
    """

    #  \/ Then use formula to calculate maximum range
    maxRange = (proj.initialVel**2/Constants.g) * (math.sin(proj.initialAngle) * math.cos(proj.initialAngle) + math.cos(proj.initialAngle) * math.sqrt(math.sin(proj.initialAngle) ** 2 + (2 * Constants.g * proj.initialHeight) / proj.initialVel ** 2))
    deltaX = maxRange * Constants.FRACTION_OF_RANGE  # defined the amount that x is increasing per update
    for step in range(int(1/Constants.FRACTION_OF_RANGE)):  # Loop that moves through the updates
        proj.x += deltaX
        proj.y = proj.initialHeight + proj.x * math.tan(proj.initialAngle) - (Constants.g / (2 * proj.initialVel**2)) * (1 + math.tan(proj.initialAngle)**2) * proj.x ** 2  # formula for y position, based off of x position of a projectile.
        proj.log()


def calculateApogee(proj: Projectile.Projectile) -> None:
    # x and y coordinated for the maximum point that the projectile gets to, for later use.
    xApogee = (proj.initialVel ** 2 / Constants.g) * math.sin(proj.initialAngle) * math.cos(proj.initialAngle)
    yApogee = proj.initialHeight + (proj.initialVel ** 2 / (Constants.g * 2)) * math.sin(proj.initialAngle) ** 2
    print('x Apogee: ', xApogee)
    print('y Apogee: ', yApogee, '\n')


if __name__ == '__main__':
    projectile = Projectile.Projectile(x=0, y=1, v=10, angle=42)
    calculateTrajectoryData(projectile)  # run through projectile motion
    projectile.printAsTable(columns=('rangeFraction', 'x', 'y'))
