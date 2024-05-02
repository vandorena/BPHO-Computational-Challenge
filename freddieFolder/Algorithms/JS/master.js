// Constants
//-------------------------------------------------
const TIMESTEP = 0.01;
const FRACTION_OF_RANGE = 0.02;
const g = 9.81;
const COE = 0.7;
// Projectile Class   
//-------------------------------------------------

class Projectile {
    constructor(x = 0, y = 2, v = 20, angle = Math.PI / 4, vx = null, vy = null) {
        this.initialVel = v;
        if (angle > Math.PI / 2) {
            angle = Math.radians(angle);
        }
        this.initialAngle = this.initialAngle = radians(angle);
        this.initialHeight = y;
        this.x = x;
        this.y = y;

        if (vx !== null && vy !== null) {
            this.vx = vx;
            this.vy = vy;
            this.initialAngle = Math.atan2(this.vy, this.vx);
            this.initialVel = Math.sqrt(vx ** 2 + vy ** 2);
        } else {
            this.vx = Math.cos(this.initialAngle) * v;
            this.vy = Math.sin(this.initialAngle) * v;
        }

        this._data = {
            'totalTime': [0],
            'rangeFraction': [0],
            'vx': [this.vx.toFixed(4)],
            'vy': [this.vy.toFixed(4)],
            'v': [this.initialVel],
            'x': [this.x],
            'y': [this.y]
        };
    }

    log() {
        let roundTo = 4;
        this._data['totalTime'].push((this._data['totalTime'][this._data['totalTime'].length - 1] + Constants.TIMESTEP).toFixed(roundTo));
        this._data['rangeFraction'].push((this._data['rangeFraction'][this._data['rangeFraction'].length - 1] + Constants.FRACTION_OF_RANGE).toFixed(roundTo));
        this._data['vx'].push(this.vx.toFixed(roundTo));
        this._data['vy'].push(this.vy.toFixed(roundTo));
        this._data['v'].push(Math.sqrt(this.vx ** 2 + this.vy ** 2).toFixed(roundTo));
        this._data['x'].push(this.x.toFixed(roundTo));
        this._data['y'].push(this.y.toFixed(roundTo));
    }

    getData() {
        return this._data;
    }

    printAsTable(columns = ['totalTime', 'rangeFraction', 'vx', 'vy', 'v', 'x', 'y'], exclude = []) {
        let dataToPrint = [];
        for (let key in this._data) {
            if (columns.includes(key) && !exclude.includes(key)) {
                dataToPrint.push([key].concat(this._data[key]));
            }
        }
        printTable(dataToPrint, true);

    }
}
//--------------
//Radian Conversion Function

function radians(degrees) {
    return degrees * Math.PI / 180;
  }
  
//Printdata
//------------------------------------------------------------
function printTable(data, dataInColumns = false) {
    // rotates 2d array if dataInColumns is true
    if (dataInColumns) {
        let tempData = [];
        for (let row = 0; row < data[0].length; row++) {
            tempData.push(data.map(col => col[row]));
        }
        data = tempData;
    }
    // Calculate the maximum width for each column
    let colWidths = data[0].map((_, i) => Math.max(...data.map(row => String(row[i]).length)));

    // Print the table row by row
    for (let row of data) {
        let formattedRow = row.map((item, i) => item.toString().padEnd(colWidths[i])).join(' | ');
        console.log(formattedRow);
    }
}

// Task 1
// --------------------------------------------------
class Projectile {
    constructor(x, y, v, angle) {
        this.x = x;
        this.y = y;
        this.vx = v * Math.cos(angle * Math.PI / 180);  // initial x velocity
        this.vy = v * Math.sin(angle * Math.PI / 180);  // initial y velocity
        this.logData = [];
    }

    log() {
        this.logData.push([this.x, this.y, this.vx, this.vy]);
    }

    printAsTable(exclude = []) {
        let dataToPrint = [];
        for (let key in this) {
            if (!exclude.includes(key)) {
                dataToPrint.push([key].concat(this[key]));
            }
        }
        printTable(dataToPrint, true);
    }
}

function task1CalculateTrajectoryData(proj,tolerance=0.001) {
    const g = 9.81;  // acceleration due to gravity
    const TIMESTEP = 0.01;  // time step

    while (proj.y >= tolerance) { // Tolerance Here to prevent errors due to floating point precision.
        // updating position
        proj.x += proj.vx * TIMESTEP;
        proj.y += (proj.vy * TIMESTEP) - (0.5 * g * (TIMESTEP ** 2));

        // updating velocity
        proj.vy += -g * TIMESTEP;  // Accelerated downwards by g

        // updating data
        proj.log();
    }
}

//Task 2
//----------------------------------------------------------------------------------------

const { PI } = Math; // Use Math.PI for pi constant

function calculateTrajectoryData(proj) {

  // Calculate maximum range
  const maxRange = (proj.initialVel ** 2 / Constants.g) * (Math.sin(proj.initialAngle) * Math.cos(proj.initialAngle) + Math.cos(proj.initialAngle) * Math.sqrt(Math.sin(proj.initialAngle) ** 2 + (2 * Constants.g * proj.initialHeight) / proj.initialVel ** 2));
  const deltaX = maxRange * Constants.FRACTION_OF_RANGE; // Amount x increases per update

  // Loop until y becomes negative (hits the floor)
  for (let step = 0; step < 1 / Constants.FRACTION_OF_RANGE; step++) {
    proj.x += deltaX;
    proj.y = proj.initialHeight + proj.x * Math.tan(proj.initialAngle) - (Constants.g / (2 * proj.initialVel ** 2)) * (1 + Math.tan(proj.initialAngle) ** 2) * proj.x ** 2;
    proj.log(); // Update log data (assuming your Projectile class has a log method)
  }
}

function calculateApogee(proj) {

  const xApogee = (proj.initialVel ** 2 / Constants.g) * Math.sin(proj.initialAngle) * Math.cos(proj.initialAngle);
  const yApogee = proj.initialHeight + (proj.initialVel ** 2 / (Constants.g * 2)) * Math.sin(proj.initialAngle) ** 2;
  console.log('x Apogee:', xApogee);
  console.log('y Apogee:', yApogee, '\n');
}

// Task 3
//------------------------------------------------------------------------------------

 // Use Math.PI for pi constant

function minimumSpeed(xf, yf, xi = 0, yi = 0) {
 // """
 // This function returns a projectile object with the minimum speed to reach point (xf, yf).

  //:param xf: The desired x coordinate.
  //:param yf: The desired y coordinate.
  //:param xi: The initial x coordinate (default = 0).
  //:param yi: The initial y coordinate (default = 0).
  //:return: A Projectile object with the minimum speed and angle to reach (xf, yf).
 // """

  const minSpeed = Math.sqrt(Constants.g * (yf + Math.sqrt(xf ** 2 + yf ** 2)));
  const minAngle = Math.atan((yf + Math.sqrt(xf ** 2 + yf ** 2)) / xf);
  return new Projectile(x, xi, y, yi, v, minSpeed, angle, minAngle);
}

function lowAndHighBall(xf, yf, initialVel, xi = 0, yi = 0) {
  //"""
 // This function returns two projectile objects with the maximum and minimum angles to reach point (xf, yf) with a predetermined velocity.

 // :param xf: The desired x coordinate.
  //:param yf: The desired y coordinate.
  //:param initialVel: The initial velocity for both trajectories.
  //:param xi: The initial x coordinate (default = 0).
  //:param yi: The initial y coordinate (default = 0).
  //:return: A tuple containing two Projectile objects with low and high angles for the given initial velocity.
  

  const a = (Constants.g / (2 * initialVel ** 2)) * xf ** 2;
  const b = -xf;
  const c = yf - yi + (Constants.g * xf ** 2) / (2 * initialVel ** 2);
  const discriminant = b ** 2 - 4 * a * c;

  const lowBallAngle = Math.atan((-b - Math.sqrt(discriminant)) / (2 * a));
  const highBallAngle = Math.atan((-b + Math.sqrt(discriminant)) / (2 * a));

  return [
    new Projectile(x, xi, y, yi, v, initialVel, angle, lowBallAngle),
    new Projectile(x, xi, y, yi, v, initialVel, angle, highBallAngle),
  ];
}

function calculateTrajectoryDataToPoint(proj, xMax) {

  const deltaX = xMax * Constants.FRACTION_OF_RANGE; // Amount x increases per update
  for (let step = 0; step < 1 / Constants.FRACTION_OF_RANGE; step++) {
    proj.x += deltaX;
    proj.y = proj.initialHeight + proj.x * Math.tan(proj.initialAngle) - (Constants.g / (2 * proj.initialVel ** 2)) * (1 + Math.tan(proj.initialAngle) ** 2) * proj.x ** 2;
    proj.log(); // Update log data (assuming your Projectile class has a log method)
  }
}

// Task 4
//--------------------------------------------------------------------------------------------------------------------------

function maxRange(xi, yi, vi) {
    /**
     * This function returns the projectile object with the maximum range,
     * given initial height and velocity.
     * 
     * @param {number} xi - The initial x coordinate.
     * @param {number} yi - The initial y coordinate.
     * @param {number} vi - The initial velocity of the projectile.
     * @returns {Projectile} The projectile object with the maximum range.
     */
    const angleMax = Math.asin(1 / Math.sqrt(2 + (2 * Constants.g * yi) / (vi * vi)));
    return new Projectile(xi, yi, vi, angleMax);
  }
  

// Task 5 
//----------------------------------------------------------------------------------------------------------------------------
function calculateParabolaData(proj) {
    /**
     * This function takes a projectile object and calculates its trajectory
     * along a parabola defined by the equation y = (v^2 / (2g)) - (gx^2) / (2v^2),
     * where v is the initial velocity and g is the acceleration due to gravity.
     * Note: This is not simulating real projectile motion, so initial values besides velocity are irrelevant.
     * 
     * @param {Projectile} proj - The projectile object.
     */
    const maxRange = proj.initialVel ** 2 / Constants.g; // When y = 0, rearranged formula
    const deltaX = maxRange * Constants.FRACTION_OF_RANGE; // Amount x increases per update
  
    for (let step = 0; step < Math.floor(1 / Constants.FRACTION_OF_RANGE); step++) {
      proj.x += deltaX;
      proj.y = (proj.initialVel ** 2 / (2 * Constants.g)) - (Constants.g / (2 * proj.initialVel ** 2)) * proj.x ** 2;
      proj.log();
    }
  }

// Task 6
// -----------------------------------------------------------------------------------------------------------------------------------------------
function integrationFunc(lim) {
    /**
     * This function calculates the integral used for distance traveled calculation.
     * 
     * @param {number} lim - The integration limit.
     * @returns {number} The result of the integration.
     */
    return 0.5 * Math.log(Math.abs(Math.sqrt(1 + lim ** 2) + lim)) + 0.5 * lim * Math.sqrt(1 + lim ** 2);
  }
  
  function calculateDistanceTravelled(proj) {
    /**
     * This function calculates the distance traveled by a projectile.
     * 
     * @param {Projectile} proj - The projectile object.
     * @returns {void} (doesn't return anything)
     */
    const range = (proj.initialVel ** 2 / Constants.g) * (
      Math.sin(proj.initialAngle) * Math.cos(proj.initialAngle) +
      Math.cos(proj.initialAngle) * Math.sqrt(Math.sin(proj.initialAngle) ** 2 + (2 * Constants.g * proj.initialHeight) / proj.initialVel ** 2)
    );
    const multiplier = (proj.initialVel ** 2) / (Constants.g * (1 + Math.tan(proj.initialAngle) ** 2));
    const lowerLimit = Math.tan(proj.initialAngle) - (Constants.g * range) * (1 + Math.tan(proj.initialAngle) ** 2) / (proj.initialVel ** 2);
    const upperLimit = Math.tan(proj.initialAngle);
  
    const distanceTraveled = multiplier * (integrationFunc(upperLimit) - integrationFunc(lowerLimit));
    console.log('distance Traveled:', distanceTraveled);
  }

// Task 7
//-----------------------------------------------------------------------------------------------------------------------------------------

function calculateRangeTimeData(proj) {
    /**
     * This function calculates the projectile's range at regular time intervals.
     * 
     * @param {Projectile} proj - The projectile object.
     * @returns {number[]} A list of range values at each time step.
     */
    const distanceFromStartData = [0];
    while (proj.y >= -5) {
      // Update position
      proj.x += proj.vx * Constants.TIMESTEP;
      proj.y += (proj.vy * Constants.TIMESTEP) - (0.5 * Constants.g * (Constants.TIMESTEP ** 2));
  
      // Update velocity
      proj.vx = proj.vx; // No change in x-velocity
      proj.vy += -Constants.g * Constants.TIMESTEP; // Accelerated downwards by g
  
      // Update data and calculate range
      proj.log();
      const totalTime = proj.getData()['totalTime'][-1];
      distanceFromStartData.push(Math.sqrt(
        proj.initialVel ** 2 * totalTime ** 2 -
        Constants.g * totalTime ** 3 * proj.initialVel * Math.sin(proj.initialAngle) +
        0.25 * Constants.g ** 2 * totalTime ** 4
      ));
    }
  
    return distanceFromStartData;
  }
  
  function calculateMaxAndMinTime(proj) {
    /**
     * This function calculates the time for maximum and minimum height
     * before going below y = 0 (requires angle > ~70.5 degrees).
     * 
     * @param {Projectile} proj - The projectile object.
     * @returns {tuple<number, number>} A tuple containing max and min time.
     */
    const multiplier = (3 * proj.initialVel) / (2 * Constants.g);
    const a = Math.sin(proj.initialAngle);
    const b = Math.sqrt(Math.sin(proj.initialAngle) ** 2 - (8 / 9));
    return multiplier * a - multiplier * b, multiplier * a + multiplier * b;
  }

  // Task 8
  // ----------------------------------------------------------------------------------------------------------------------------------------------

  function bouncyProjectileData(proj, n) {
    /**
     * This function simulates a bouncing projectile for a specified number of bounces.
     * 
     * @param {Projectile} proj - The projectile object.
     * @param {number} n - The number of bounces.
     */
    let bounceCount = 0;
    while (bounceCount <= n) {
      // Update position
      proj.x += proj.vx * Constants.TIMESTEP;
      proj.y += (proj.vy * Constants.TIMESTEP) - (0.5 * Constants.g * (Constants.TIMESTEP ** 2));
  
      // Update velocity
      proj.vx = proj.vx; // No change in x-velocity
      proj.vy += -Constants.g * Constants.TIMESTEP; // Accelerated downwards by g
  
      // Update data
      proj.log();
  
      // Check for bounce
      if (proj.y < 0) {
        proj.y = 0;
        proj.vy *= -Constants.COE; // Bounce with coefficient of restitution (COE)
        bounceCount++;
      }
    }
  }
  
// Task 9
// -----------------------------------------------------------------------------------------------------------------------------
function airResistanceFactor(dragCoefficient, crossSectionArea, airDensity, mass) {
    /**
     * This function calculates the air resistance factor for a projectile.
     * 
     * @param {number} dragCoefficient - The drag coefficient of the projectile.
     * @param {number} crossSectionArea - The cross-sectional area of the projectile.
     * @param {number} airDensity - The air density.
     * @param {number} mass - The mass of the projectile.
     * @returns {number} The air resistance factor.
     */
    return (0.5 * dragCoefficient * airDensity * crossSectionArea) / mass;
  }
  
  function calculateXYDrag(vx, vy, k) {
    /**
     * This function calculates the air resistance acceleration in x and y directions.
     * 
     * @param {number} vx - The x-velocity of the projectile.
     * @param {number} vy - The y-velocity of the projectile.
     * @param {number} k - The air resistance factor.
     * @returns {tuple<number, number>} A tuple containing x and y acceleration.
     */
    const v = Math.sqrt(vx ** 2 + vy ** 2);
    const ax = -vx * k * v;
    const ay = -Constants.g - vy * k * v;
    return [ax, ay];
  }
  
  function calculateDragTrajectoryData(proj, airRes) {
    /**
     * This function calculates the trajectory of a projectile with air resistance.
     * 
     * @param {Projectile} proj - The projectile object.
     * @param {number} airRes - The air resistance factor.
     * @returns {tuple<list, list>} A tuple containing lists of x and y accelerations.
     */
    const axList = [];
    const ayList = [];
  
    // Initial acceleration due to air resistance
    const [ax, ay] = calculateXYDrag(proj.vx, proj.vy, airRes);
    axList.push(ax);
    ayList.push(ay);
  
    while (proj.y >= 0) {
      // Update position
      proj.x += proj.vx * Constants.TIMESTEP + 0.5 * ax * Constants.TIMESTEP ** 2;
      proj.y += proj.vy * Constants.TIMESTEP + 0.5 * ay * Constants.TIMESTEP ** 2;
  
      // Update velocity
      proj.vx += ax * Constants.TIMESTEP;
      proj.vy += ay * Constants.TIMESTEP;
  
      // Get drag for updated velocity
      const [newAx, newAy] = calculateXYDrag(proj.vx, proj.vy, airRes);
  
      // Update data
      proj.log();
  
      axList.push(newAx);
      ayList.push(newAy);
  
      // Update acceleration for next step
      ax = newAx;
      ay = newAy;
    }
  
    return [axList, ayList];
  }
  