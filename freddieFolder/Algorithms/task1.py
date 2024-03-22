import Projectile
import Constants
import printData


def calculateTrajectoryData(proj: Projectile.Projectile):
    """
    A procedure that takes in a projectile object and runs it through a drag-less projectile motion using a predetermined delta time. It keeps going until it hits the floor (y < 0).
    :param proj: Projectile.Projectile
    :return: None
    """

    while proj.y >= 0:
        # updating velocity
        proj.vx = proj.vx  # As x velocity isn't affected
        proj.vy += -Constants.g * Constants.TIMESTEP  # Accelerated downwards by g

        # updating position
        proj.x += proj.vx * Constants.TIMESTEP
        proj.y += proj.vy * Constants.TIMESTEP

        # updating data
        proj.log()


if __name__ == '__main__':
    projectile = Projectile.Projectile(x=0, y=2, v=20, angle=45)
    calculateTrajectoryData(projectile)  # run through projectile motion
    printData.print_table(projectile.getData(), True)  # print data from projectile motion