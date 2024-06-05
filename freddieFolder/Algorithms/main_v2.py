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
            current_task = request.form["task"]
            if current_task == 1:
                return redirect(url_for("task1graph"))
            elif current_task == 2:
                return redirect(url_for("task2graph"))
            elif current_task == 3:
                return redirect(url_for("task3graph"))
            elif current_task == 4:
                return redirect(url_for("task4graph"))
            elif current_task == 5:
                return redirect(url_for("task5graph"))
            elif current_task == 6:
                return redirect(url_for("task6graph"))
            elif current_task == 7:
                return redirect(url_for("task7graph"))
            elif current_task == 8:
                return redirect(url_for("task8graph"))
            elif current_task == 9:
                return redirect(url_for("task9graph"))
    return render_template("graph_display_basic.html")

@app.route("/task1", methods=["POST","GET"])
def task1graph():
    if request.form:
        universal_holder = False
        while not universal_holder:
            task1_projectile = Projectile.Projectile(x=int(request.form["x"]),y=int(request.form["y"]),v=int(request.form["v"]),angle=int(request.form["angle"]))
            task1.calculateTrajectoryData(task1_projectile)
            plt.figure()
            plt.plot([10,523,43],[12,323,44])
            plt.savefig('static/images/current_graph.png')
            plt.show()
    return render_template("task1_template.html")

@app.route("/task2", methods=["POST","GET"])
def task2graph():
    pass

@app.route("/task3", methods=["POST","GET"])
def task3graph():
    pass

@app.route("/task4", methods=["POST","GET"])
def task4graph():
    pass

@app.route("/task5", methods=["POST","GET"])
def task5graph():
    pass

@app.route("/task6", methods=["POST","GET"])
def task6graph():
    pass

@app.route("/task7", methods=["POST","GET"])
def task7graph():
    pass

@app.route("/task8", methods=["POST","GET"])
def task8graph():
    pass

@app.route("/task9", methods=["POST","GET"])
def task9graph():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)