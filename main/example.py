from flask import Flask, render_template, request
from bokeh.plotting import figure  # Import figure for plotting
from bokeh.models import ColumnDataSource  # Import ColumnDataSource
from bokeh.transform import linear_cmap  # Import linear_cmap for color mapping (optional)
from sympy import sympify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def plot_graph():
    if request.method == "POST":
        # Extract user input from the form
        try:
            x_min = float(request.form["x_min"])
            x_max = float(request.form["x_max"])
            y_min = float(request.form["y_min"])
            y_max = float(request.form["y_max"])
            function_str = request.form["function"]
        except ValueError:
            error_message = "Please enter valid numbers for all fields."
            return render_template("index.html", error_message=error_message)

        # Validate input ranges (optional, adjust based on your function)
        if x_min >= x_max or y_min >= y_max:
            error_message = "X minimum must be less than X maximum, and Y minimum must be less than Y maximum."
            return render_template("index.html", error_message=error_message)

        # Generate x-axis data points
        x_data = list(range(int(x_min), int(x_max) + 1))  # Adjust range based on your function

        # Evaluate the user-provided function for each x-value
        y_data = [sympify(function_str).subs('x', x).evalf() for x in x_data]  # Handle potential evaluation errors

        # Create a ColumnDataSource for Bokeh
        source = ColumnDataSource(data=dict(x=x_data, y=y_data))

        # Create the Bokeh plot with potential color mapping (optional)
        p = figure(title="User-defined Function Plot")
        p.line("x", "y", source=source, line_width=2, line_color=linear_cmap(field_name="y", palette="Viridis256", low=min(y_data), high=max(y_data)))  # Color mapping example

        # Return the plot object for template rendering
        return render_template("index.html", plot=p)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
