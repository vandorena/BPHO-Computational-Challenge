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

