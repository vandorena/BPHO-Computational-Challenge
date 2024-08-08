import math
import Projectile
import Constants
import printData


def calculateRangeTimeData(proj: Projectile.Projectile) -> list:
    """
    This takes a projectile object and runs it through regular intervals of time, and will update the y using the range formula.
    Note: this is returning the range(m) list, but the projectile will go through projectile motion, and so can still use this as normal.
    :param proj: the projectile object
    :return: list of range values, consistent with the projectile updates
    """
    list = []
    times = [0]
    distanceFromStartData = [0]
    while proj.y >= -5:
        # updating position
        proj.x += proj.vx * Constants.TIMESTEP
        proj.y += (proj.vy * Constants.TIMESTEP) - (0.5 * Constants.g * (Constants.TIMESTEP**2))

        # updating velocity
        proj.vx = proj.vx  # As x velocity isn't affected
        proj.vy += -Constants.g * Constants.TIMESTEP  # Accelerated downwards by g

        # updating data
        proj.log()
        totalTime = proj.getData()['totalTime'][-1]
        times.append(totalTime)
        distanceFromStartData.append(math.sqrt(proj.initialVel**2 * totalTime**2 - Constants.g * totalTime**3 * proj.initialVel * math.sin(proj.initialAngle) + 0.25 * Constants.g ** 2 * totalTime ** 4))
    list.append(times)
    list.append(distanceFromStartData)
    return list


def calculateMaxAndMinTime(proj: Projectile.Projectile) -> tuple[float, float]:
    """
    A procedure that will calculate and return the time at which the projectile is furthest and closest(after the furthest point), before going below y=0.
    !!!  Note: the angle has to be greater than math.asin((2*sqrt2)/3) (about 70.5 degrees)  !!!
    :param proj: the projectile object
    :return: Max and Min respectively
    """
    multiplier = (3 * proj.initialVel) / (2 * Constants.g)
    a = math.sin(proj.initialAngle)
    b = math.sqrt(math.sin(proj.initialAngle)**2 - (8/9))
    return multiplier * a - multiplier * b, multiplier * a + multiplier * b


if __name__ == '__main__':
    # Change Constants
    Constants.g = 10

    # initial Variables
    vInitial = 10
    angleInitial = 85

    # create projectile object
    normalProjectile = Projectile.Projectile(x=0, y=0, v=vInitial, angle=angleInitial)

    # run projectile objects through procedure (could also use task 1's algorithm, no preference in question)
    distanceData = calculateRangeTimeData(normalProjectile)

    # get and print min and max
    print(*calculateMaxAndMinTime(normalProjectile), sep=", ")

    # can print data if needed, (range and time below)
    printData.print_table([distanceData] + [normalProjectile.getData()['totalTime']], True)
