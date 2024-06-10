import Projectile
import task1
import task2
import task3
import task4
import task5
import task6


if __name__ == '__main__':
    # initial variables
    xInitial = 0
    yInitial = 0
    vInitial = 30
    angleInitial = 40

    xFinal = 10
    yFinal = 20

    # projectile types
    normalProjectile = Projectile.Projectile(x=xInitial, y=yInitial, v=vInitial, angle=angleInitial)
    minimumSpeedProjectile = task3.minimumSpeed(xFinal, yFinal, xInitial, yInitial)
    lowBallProjectile, highBallProjectile = task3.lowAndHighBall(xFinal, yFinal, vInitial, xInitial, yInitial)
    maxRangeProjectile = task4.maxRange(xInitial, yInitial, vInitial)

    # (special other uses of projectile class)
    boundingParabolaProjectile = Projectile.Projectile(x=xInitial, y=yInitial, v=vInitial)

    # projectile Functions
    functions = [task1.calculateTrajectoryData, task2.calculateTrajectoryData, task3.calculateTrajectoryDataToPoint]
    for i in [normalProjectile, minimumSpeedProjectile, lowBallProjectile, highBallProjectile, maxRangeProjectile]:
        functions[1](i)     # note: if 2 (or last function in list used), then need second argument (i, xMax=_).

    # special function
    task5.calculateParabolaData(boundingParabolaProjectile)

    # calculate and print specific data. eg,
    task2.calculateApogee(normalProjectile)             # or any projectile object (except boundingParabola)
    task6.calculateDistanceTravelled(normalProjectile)  # or any projectile object (except boundingParabola)

    # print projectiles as a table. eg,
    normalProjectile.printAsTable(columns=('rangeFraction', 'x', 'y'), exclude=())      # any combination for projectile, columns, exclude







