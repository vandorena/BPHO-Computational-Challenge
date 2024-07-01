import math
import Projectile
import Constants
import task1
import printData


def airResistanceFactor(dragCoefficient, crossSectionArea, airDensity, mass) -> float:
    return (0.5 * dragCoefficient * airDensity * crossSectionArea) / mass


def calculateXYDrag(vx, vy, k):
    v = math.sqrt(vx**2 + vy**2)
    ax = -vx * k * v
    ay = - Constants.g - vy * k * v
    return ax, ay
    


def calculateDragTrajectoryData(proj: Projectile.Projectile, airRes: float) -> tuple[list, list]:
    """
    A procedure that takes in a projectile object and runs it through a drag projectile motion using a predetermined delta time. It keeps going until it hits the floor (y < 0).
    :param proj: Projectile.Projectile
    :param airRes: The k factor in the equations
    :return: 2 lists of the acceleration in x and y separately, consistent with the times on the projectile used.
    """

    axList = []
    ayList = []
    ax, ay = calculateXYDrag(proj.vx, proj.vy, airRes)
    axList.append(ax)
    ayList.append(ay)

    while proj.y >= 0:
        # updating position
        proj.x += proj.vx * Constants.TIMESTEP + 0.5 * ax * Constants.TIMESTEP**2
        proj.y += proj.vy * Constants.TIMESTEP + 0.5 * ay * Constants.TIMESTEP**2

        # updating velocity
        proj.vx += ax * Constants.TIMESTEP
        proj.vy += ay * Constants.TIMESTEP

        # get drag resistance
        ax, ay = calculateXYDrag(proj.vx, proj.vy, airRes)

        # updating data
        proj.log()

        axList.append(ax)
        ayList.append(ay)

    return axList, ayList


if __name__ == '__main__':
    # change constant
    Constants.TIMESTEP = 0.01

    # create common variables
    xInitial = 0
    yInitial = 2
    vInitial = 20
    angleInitial = 30

    # create drag factor as function
    airResistance = airResistanceFactor(dragCoefficient=0.1, crossSectionArea=0.007854, airDensity=1, mass=0.1)

    # create projectile Variables
    projectileNoDrag = Projectile.Projectile(xInitial, yInitial, vInitial, angleInitial)
    projectileYesDrag = Projectile.Projectile(xInitial, yInitial, vInitial, angleInitial)

    # run through projectile motion
    task1.calculateTrajectoryData(projectileNoDrag)
    xAcceleration, yAcceleration = calculateDragTrajectoryData(projectileYesDrag, airResistance)

    # print data
    tempData = projectileYesDrag.getData()
    printData.print_table([tempData['totalTime']] + [xAcceleration] + [yAcceleration] + [tempData['vx']] + [tempData['vy']] + [tempData['v']] + [tempData['x']] + [tempData['y']], True)
