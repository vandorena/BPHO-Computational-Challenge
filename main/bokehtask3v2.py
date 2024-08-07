import numpy as np
import task3,task2
from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column,row

# Create initial data
x_target, y_target = 5, 5  # Initial target coordinates
v_parameter = 10  # Some parameter affecting the lines (you can change this)

# Create a scatter plot with a target point
plot = figure(title="Task 3", tools="reset,save",match_aspect=True)
target_source = ColumnDataSource(data={'x': [x_target], 'y': [y_target]})
plot.circle('x', 'y', source=target_source, size=10, color='red', legend_label='Target Point')

# Initialize line data sources
line1_source = ColumnDataSource(data={'x': [], 'y': []})
line2_source = ColumnDataSource(data={'x': [], 'y': []})
line3_source = ColumnDataSource(data={'x': [], 'y': []})

# Create lines (initially empty)
plot.line('x', 'y', source=line1_source, color="blue", legend_label="Minimum Speed")
plot.line('x', 'y', source=line2_source, color="green", legend_label="Lowball")
plot.line('x', 'y', source=line3_source, color="orange", legend_label="Highball")

# Slider callbacks
def update_target(attr, old, new):
    global x_target, y_target, v_parameter
    x_target = x_slider.value
    y_target = y_slider.value
    v_parameter = v_slider.value
    target_source.data = {'x': [x_target], 'y': [y_target]}
    update_lines()

def update_lines():
    global x_target,y_target,v_parameter
    minimum_speed = task3.minimumSpeed(x_target,y_target)
    task2.calculateTrajectoryData(minimum_speed,100)
    x_values1, y_values1 = minimum_speed.getXgetY()
    lowball,highball = task3.lowAndHighBallList(x_target,y_target,v_parameter)
    task2.calculateTrajectoryData(lowball,100)
    task2.calculateTrajectoryData(highball,100)
    x_values2,y_values2 = lowball.getXgetY()
    x_values3,y_values3 = highball.getXgetY()
    line1_source.data = {'x': x_values1, 'y': y_values1}
    line2_source.data = {'x': x_values2, 'y': y_values2}
    line3_source.data = {'x': x_values3, 'y': y_values3}

# Create sliders
x_slider = Slider(start=0, end=100, value=x_target, step=0.1, title="X Coordinate")
y_slider = Slider(start=0, end=100, value=y_target, step=0.1, title="Y Coordinate")
v_slider = Slider(start=1, end=100, value=v_parameter, step=1, title="Velocity Parameter")

x_slider.on_change('value', update_target)
y_slider.on_change('value', update_target)
v_slider.on_change('value', update_target)  # Integer values for v

update_lines()
# Arrange layout
layout = column(x_slider, y_slider, v_slider)
layout1= row(plot,layout)

# Update lines initially


# Show the plot
curdoc().add_root(layout1)
