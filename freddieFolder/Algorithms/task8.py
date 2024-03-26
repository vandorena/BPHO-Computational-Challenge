import Projectile
import Constants


def bouncyProjectileData(proj: Projectile.Projectile, n: int) -> None:
    """
    A procedure that will update a projectile object, every timestep, through a specified number of bounces, updating and storing data.
    :param proj: the projectile object, to track and store data
    :param n: the number of times the projectile will bounce before stopping
    :return: None
    """
    bounceCount = 0
    while bounceCount <= n:
        # updating position
        proj.x += proj.vx * Constants.TIMESTEP
        proj.y += (proj.vy * Constants.TIMESTEP) - (0.5 * Constants.g * (Constants.TIMESTEP ** 2))

        # updating velocity
        proj.vx = proj.vx  # As x velocity isn't affected
        proj.vy += -Constants.g * Constants.TIMESTEP  # Accelerated downwards by g

        # updating data
        proj.log()

        # check for bounce
        if proj.y < 0:
            proj.y = 0
            proj.vy = -Constants.COE * proj.vy
            bounceCount += 1


if __name__ == '__main__':
    # projectile variables
    initialHeight = 10
    initialAngle = 45
    initialVelocity = 5

    # bouncy projectile function variables
    bounces = 6

    # projectile object
    bouncyProjectile = Projectile.Projectile(0, initialHeight, initialVelocity, initialAngle)

    # run-through simulation
    bouncyProjectileData(bouncyProjectile, bounces)

    # print data
    bouncyProjectile.printAsTable(columns=('totalTime', 'x', 'y'))


