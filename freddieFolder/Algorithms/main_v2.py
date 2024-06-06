from flask import Flask, request, redirect, render_template, url_for, g , session
import task1,task2,task3,task4,task5,task6,task7,task8,task9,Projectile,Constants
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def task_graph_basic():

    """
    Handles the root route in a Flask web application.
    Processes form data to determine the current task selected by the user,
    redirects to the corresponding task route based on the selected task number,
    and renders a template to display the basic graph display.
    """

    current_task = -1
    if request.form:    
        print(f"{request.form}")
        if "task" in request.form:
            current_task = int(request.form["task"])
            if current_task >= 1 and current_task <=9 and current_task.is_integer():
                return redirect(url_for(f"task{current_task}graph"))
    return render_template("graph_display_basic.html")

@app.route("/task1", methods=["POST","GET"])
def task1graph():
    """
    Handles the /task1 route in a Flask web application.
    Processes form data to create a projectile object, calculates its trajectory,
    plots the trajectory, saves the plot as an image, and renders a template to display the result.
    """
    if request.form:
        try:
            task1_projectile = Projectile(x=int(request.form["x"]), y=int(request.form["y"]), v=int(request.form["v"]), angle=int(request.form["angle"]))
            task1.calculateTrajectoryData(task1_projectile)
            plt.figure()
            plt.plot(task1_projectile.getData()["x"], task1_projectile.getData()["y"])
            plt.savefig('static/images/current_graph.png')   
        except Exception:
            return redirect(url_for("task_graph_basic"))  
    return render_template("task1_template.html")

@app.route("/task2", methods=["POST","GET"])
def task2graph():
    """
    Handles the /task3 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    pass

@app.route("/task3", methods=["POST","GET"])
def task3graph():
    """
    Handles the /task3 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    pass

@app.route("/task4", methods=["POST","GET"])
def task4graph():
    """
    Handles the /task4 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    pass

@app.route("/task5", methods=["POST","GET"])
def task5graph():
    """
    Handles the /task5 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    pass

@app.route("/task6", methods=["POST","GET"])
def task6graph():
    """
    Handles the /task6 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    pass

@app.route("/task7", methods=["POST","GET"])
def task7graph():
    """
    Handles the /task7 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    pass

@app.route("/task8", methods=["POST","GET"])
def task8graph():
    """
    Handles the /task8 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    pass

@app.route("/task9", methods=["POST","GET"])
def task9graph():
    """
    Handles the /task9 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)