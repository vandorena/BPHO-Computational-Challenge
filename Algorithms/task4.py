import math
import Projectile
import Constants
import task2


def maxRange(xi: float, yi: float, vi: float) -> Projectile.Projectile:
    """
    This return the projectile object that has the maximum range, given initial height and velocity.
    :param xi: The initial x coordinate.
    :param yi: The initial y coordinate.
    :param vi: The initial velocity of the projectile.
    :return: The projectile object, starting at (xi, yi) and given the correct velocity and angle to go through (xf, yf)
    """
    angleMax = math.asin(1/math.sqrt(2 + (2 * Constants.g * yi) / (vi**2)))
    return Projectile.Projectile(xi, yi, vi, angleMax)


if __name__ == '__main__':
    # create common variables
    xInitial = 0
    yInitial = 2
    launchSpeed = 10

    # create projectile objects
    maxRangeProjectile = maxRange(xInitial, yInitial, launchSpeed)
    normalProjectile = Projectile.Projectile(xInitial, yInitial, launchSpeed, angle=60)

    # run projectile objects through procedure (could also use task 1's algorithm, no preference in question)
    task2.calculateTrajectoryData(maxRangeProjectile)
    task2.calculateTrajectoryData(normalProjectile)

    # print final range
    print('normal projectile final x :', normalProjectile.x)
    print('max range projectile final x :', maxRangeProjectile.x)

    # can print more data if needed (remove hashtag below)
    # normalProjectile.printAsTable(columns=('rangeFraction', 'x', 'y'))
    # maxRangeProjectile.printAsTable(columns=('rangeFraction', 'x', 'y'))


