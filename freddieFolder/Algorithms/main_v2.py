from flask import Flask, request, redirect, render_template, url_for, g , session
import task1,task2,task3,task4,task5,task6,task7,task8,task9,Projectile,Constants
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def task_graph_basic():
    current_task = -1
    if request.form:    
        print(f"{request.form}")
        if "task" in request.form:
            current_task = int(request.form["task"])
            universal_holder = False
            while not universal_holder:
                if current_task>9 or current_task<1:
                    current_task =-1
                if current_task == 1 and "x" in request.form and "y" in request.form and "v" in request.form and "angle" in request.form:
                    if int(request.form["angle"]) > 90 or int(request.form["angle"]) < 0:
                        universal_holder = True
                    else:
                        task1_projectile = Projectile.Projectile(x=int(request.form["x"]),y=int(request.form["y"]),v=int(request.form["v"]),angle=int(request.form["angle"]))
                        task1.calculateTrajectoryData(task1_projectile)
                        plt.figure()
                        plt.plot(task1_projectile._data["x"],task1_projectile._data["y"])
                        plt.savefig('static/images/current_graph.png')
    return render_template("graph_display_basic.html", curtask=str(current_task))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)