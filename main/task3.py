import math
import Projectile
import Constants
import printData


def minimumSpeed(xf: float, yf: float, xi: float = 0, yi: float = 0) -> Projectile.Projectile:
    """
    This return the projectile object of the minimum speed to go through point (xf, yf)
    :param xf: The desired x coordinate that it should go through
    :param yf: The desired y coordinate that it should go through
    :param xi: The initial x coordinate (default = 0)
    :param yi: The initial y coordinate (default = 0)
    :return: The projectile object, starting at (xi, yi) and given the correct velocity and angle to go through (xf, yf)
    """
    minSpeed = math.sqrt(Constants.g * (yf + math.sqrt(xf**2 + yf**2)))
    minAngle = math.atan((yf + math.sqrt(xf**2 + yf**2))/xf)
    return Projectile.Projectile(x=xi, y=yi, v=minSpeed, angle=minAngle)


def lowAndHighBall(xf: float, yf: float, initialVel: float, xi: float = 0, yi: float = 0) -> tuple[Projectile.Projectile, Projectile.Projectile]:
    """
    This returns 2 projectile objects of the maximum and minimum angle that goes through point (xf, yf), with predetermined velocity.
    :param xf: The desired x coordinate that it should go through
    :param yf: The desired y coordinate that it should go through
    :param initialVel: The initial velocity of the 2 trajectory objects
    :param xi: The initial x coordinate (default = 0)
    :param yi: The initial y coordinate (default = 0)
    :return: The 2 projectile objects, starting at (xi, yi) and given the correct velocity and low and high angle to go through (xf, yf), given an initial velocity.
    """
    # math from slides
    a = (Constants.g / (2 * initialVel**2)) * xf**2
    b = -xf
    c = yf - yi + (Constants.g * xf**2) / (2 * initialVel ** 2)
    discriminant = b ** 2 - 4 * a * c

    lowBallAngle = math.atan((-b - math.sqrt(discriminant)) / (2 * a))
    highBallAngle = math.atan((-b + math.sqrt(discriminant)) / (2 * a))

    return Projectile.Projectile(x=xi, y=yi, v=initialVel, angle=lowBallAngle), Projectile.Projectile(x=xi, y=yi, v=initialVel, angle=highBallAngle)

def lowAndHighBallList(xf:float,yf:float,initialVel:float,xi:float=0,yi:float = 0) -> tuple[Projectile.ProjectileList, Projectile.ProjectileList]:
    """
    Calculate the launch angles for low and high projectile trajectories to hit a target point.

    Parameters:
    xf (float): The x-coordinate of the target point.
    yf (float): The y-coordinate of the target point.
    initialVel (float): The initial velocity of the projectile.
    xi (float): The initial x-coordinate of the projectile (default is 0).
    yi (float): The initial y-coordinate of the projectile (default is 0).

    Returns:
    tuple[Projectile.ProjectileList, Projectile.ProjectileList]: A tuple containing two ProjectileList objects representing the low and high projectile trajectories.
    """
    
    a = (Constants.g / (2*initialVel**2)) * xf**2
    b = -xf
    c = yf-yi + (Constants.g * xf**2) / ( 2 * initialVel **2)
    discriminant = b **2 -4 * a * c
    
    lowBallAngle = math.atan((-b - math.sqrt(discriminant))/(2*a))
    highBallAngle = math.atan((-b + math.sqrt(discriminant))/(2*a))

    return Projectile.ProjectileList(x=xi,y=yi,v=initialVel, angle=lowBallAngle), Projectile.ProjectileList(x=xi, y=yi,v=initialVel,angle=highBallAngle)

def calculateTrajectoryDataToPoint(proj: Projectile.Projectile, xMax: float) -> None:
    """
    A procedure that takes in a projectile object and runs it through a drag-less projectile simulation, until point x. (This algorithm is similar to task 2)
    :param proj: Projectile.Projectile
    :param xMax: float
    :return: None
    """
    deltaX = xMax * Constants.FRACTION_OF_RANGE  # defined the amount that x is increasing per update
    for _ in range(int(1 / Constants.FRACTION_OF_RANGE)):  # Loop that moves through the updates
        proj.x += deltaX
        proj.y = proj.initialHeight + proj.x * math.tan(proj.initialAngle) - (Constants.g / (2 * proj.initialVel ** 2)) * (1 + math.tan(proj.initialAngle) ** 2) * proj.x ** 2  # formula for y position, based off of x position of a projectile.
        proj.log()


if __name__ == '__main__':
    # change Global Variable
    Constants.FRACTION_OF_RANGE = 0.01

    # create variables
    xFinal = 1000
    yFinal = 300
    initialSpeed = 150

    # create projectile objects
    minSpeedProjectile = minimumSpeed(xFinal, yFinal)   # can also add (xi=_, yi=_) to change starting position
    lowBallProjectile, highBallProjectile = lowAndHighBall(xFinal, yFinal, initialSpeed)    # can also add (xi=_, yi=_) to change starting position

    # run projectile objects through procedure (could use task 1/2 algorithms as well, if we need to keep going until hits the floor)
    calculateTrajectoryDataToPoint(minSpeedProjectile, xFinal)
    calculateTrajectoryDataToPoint(lowBallProjectile, xFinal)
    calculateTrajectoryDataToPoint(highBallProjectile, xFinal)

    # print data to table
    f = ['rangeFraction'] + minSpeedProjectile.getData()['rangeFraction']           # range fraction (same for all)
    x = ['x'] + minSpeedProjectile.getData()['x']                                   # x values (same for all)
    yLowBall = ['yLowBall'] + lowBallProjectile.getData()['y']                      # y values (for lowBall)
    yHighBall = ['yHighBall'] + highBallProjectile.getData()['y']                   # y values (for highBall)
    yMinVel = ['yMinVel'] + minSpeedProjectile.getData()['y']                       # y values (for minimum velocity projectile)
    printData.print_table([f] + [x] + [yLowBall] + [yHighBall] + [yMinVel], True)
