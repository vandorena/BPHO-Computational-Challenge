import Projectile
import Constants


def calculateParabolaData(proj: Projectile.Projectile) -> None:
    """
    This takes a projectile object and runs it through regular intervals of x, and will update the y using the bounding parabola equation.
    Note: this isn't directly projectile motion, so initial values are irrelevant.
    :param proj: the projectile object going along the parabola path
    :return: None
    """
    maxRange = proj.initialVel ** 2 / Constants.g       # when y = 0, rearranged formula and calculated
    deltaX = maxRange * Constants.FRACTION_OF_RANGE  # defined the amount that x is increasing per update
    for step in range(int(1 / Constants.FRACTION_OF_RANGE)):  # Loop that moves through the updates
        proj.x += deltaX
        proj.y = (proj.initialVel ** 2 / (2 * Constants.g)) - (Constants.g / (2 * proj.initialVel ** 2)) * proj.x ** 2
        proj.log()
    return


if __name__ == '__main__':
    vInitial = 1.3063 * 115
    yInitial = 0

    # create projectile object
    boundingProjectile = Projectile.Projectile(x=0, y=yInitial, v=vInitial)       # angle irrelevant

    # run projectile objects through procedure (could also use task 1's algorithm, no preference in question)
    calculateParabolaData(boundingProjectile)

    # can print data if needed,
    boundingProjectile.printAsTable(columns=('rangeFraction', 'x', 'y'))


