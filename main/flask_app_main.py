from flask import Flask, request, redirect, render_template, url_for, g , session
import task1,task2,task3,task4,task5,task6,task7,task8,task9,Projectile,uuid
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)



@app.route("/", methods=["POST","GET"])
def task_chooser():

    """
    Handles the root route in a Flask web application.
    Processes form data to determine the current task selected by the user,
    redirects to the corresponding task route based on the selected task number,
    and renders a template to display the basic graph display.
    """
    try:
        if int(request.args["task"]) >= 1 and int(request.args["task"]) <=9 and int(request.args["task"]) != 1:
            task_number = request.args["task"]
            return redirect(f"/task{task_number}")
    except Exception:
        print("Exception Found")
        return
        
    try:
        os.remove("static\images\Temp")
    except PermissionError:
        pass
    current_task = -1
    if request.form:    
        print(f"{request.form}")
        if "task" in request.form:
            current_task = int(request.form["task"])
            if current_task >= 1 and current_task <=9 and current_task.is_integer():
                return redirect(f"/task{current_task}")
    return render_template("graph_display_basic.html")

@app.route("/task1", methods=["POST","GET"])
def task1graph():
    """
    Handles the /task1 route in a Flask web application.
    Processes form data to create a projectile object, calculates its trajectory,
    plots the trajectory, saves the plot as an image, and renders a template to display the result.
    """
    image_rl = "\static\images\lone.png"
    if request.form:
        try:
            if int(request.args["task"]) > 1 and int(request.args["task"]) <=9 and int(request.args["task"]) != 1:
                task_number = request.args["task"]
                return redirect(f"/task{task_number}")
            task1_projectile = Projectile.ProjectileList(x=int(request.form["x"]), y=int(request.form["y"]), v=int(request.form["v"]), angle=int(request.form["angle"]))
            task1.calculateTrajectoryData(task1_projectile)
            plt.figure()
            plt.autoscale(False)
            x_data , y_data = task1_projectile.getXgetY()
            plt.plot(x_data, y_data)
            image_rl = f"static\images\Temp\{uuid.uuid4()}.png"
            plt.savefig(image_rl)   
        except Exception:
            return redirect(url_for("task_chooser"))  
    print("Task1")
    return render_template("task1_template.html",image_path=image_rl)

@app.route("/task2", methods=["POST","GET"])
def task2graph():
    """
    Route that handles generating a graph for Task 2 based on user input.
    It creates a ProjectileList object with user-provided parameters, calculates the trajectory data using task2.calculateTrajectoryData, plots the trajectory using matplotlib, and saves the plot as an image.
    If successful, it renders a template with the image path for display.
    If an exception occurs, it redirects to the task_chooser route.
    """
    base_image_url = "\static\images\lone.png"
    if request.form:
        try:
            task2_projectile = Projectile.ProjectileList(x=int(request.form["x"]), y=int(request.form["y"]), v=int(request.form["v"]), angle=int(request.form["angle"]))
            task2.calculateTrajectoryData(task2_projectile)
            plt.figure()
            plt.autoscale(False)
            x_data,y_data = task2_projectile.getXgetY()
            plt.plot(x_data,y_data)
            base_image_url = f"static\images\Temp\{uuid.uuid4()}.png"
            plt.savefig(base_image_url)
        except Exception():
            return redirect(url_for("task_chooser"))
    print("task2")
    return render_template("task2_template.html",image_path=base_image_url)

@app.route("/task3", methods=["POST","GET"])
def task3graph():
    base_image_url = "\static\images\lone.png"
    if request.form:
        try: 
            lowball,highball = task3.lowAndHighBallList(int(request.form["xf"]), int(request.form["yf"]),int(request.form["v"]),int(request.form["x"]),int(request.form["y"]))
            plt.figure()
            plt.autoscale(False)
            lowball_x_data, lowball_y_data = lowball.getXgetY()
            highball_x_data, highball_y_data = highball.getXgetY()
            plt.plot(lowball_x_data,lowball_y_data)
            plt.plot(highball_x_data,highball_y_data,)
            base_image_url = f"static\images\Temp\{uuid.uuid4()}.png"
            plt.savefig(base_image_url)
        except Exception():
            return redirect(url_for("task_chooser"))
    print("task3")
    return render_template("task3_template.html",image_path=base_image_url)


@app.route("/task4", methods=["POST","GET"])
def task4graph():
    """
    Handles the /task4 route in a Flask web application.
    This function is currently a placeholder and does not contain any specific functionality.
    """
    base_image_url = "\static\images\lone.png"
    if request.form:
        try: 
            max_range = task4.maxRangeList(xi=int(request.form["x"]),yi=int(request.form["y"]),vi=int(request.form["v"]))
            x_data , y_data = max_range.getXgetY()
            plt.figure()
            plt.plot(x_data,y_data)
            base_image_url = f"static\images\Temp\{uuid.uuid4()}.png"
            plt.savefig(base_image_url)
        except Exception():
            return redirect(url_for("task_chooser"))
    print("task4")
    return render_template("task4_template.html",image_path=base_image_url)

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