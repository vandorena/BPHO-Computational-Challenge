import numpy as np
import task4,task2, Projectile,math
from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column,row

# Create initial data
u_global = 10
h_global = 0
g_global = 9.81
angle_global = math.pi/4  # Some parameter affecting the lines (you can change this)

# Create a scatter plot
plot = figure(title="Task 4", tools="reset,save",match_aspect=True)

# Initialize line data sources
line1_source = ColumnDataSource(data={'x': [], 'y': []})
line2_source = ColumnDataSource(data={'x': [], 'y': []})

# Create lines (initially empty)
plot.line('x', 'y', source=line1_source, color="blue", legend_label="Inputted Trajectory")
plot.line('x', 'y', source=line2_source, color="red", legend_label="Maximising Range")


# Slider callbacks
def update_target(attr, old, new):
    global u_global, h_global, g_global, angle_global
    u_global = u_slider.value
    h_global = h_slider.value
    g_global = g_slider.value
    angle_global = math.radians(angle_slider.value)
    update_lines()

def update_lines():
    global u_global, h_global, g_global, angle_global
    input_projectile = Projectile.ProjectileList(y=h_global,v=u_global,angle=angle_global,g=g_global)
    task2.calculateTrajectoryData(input_projectile,100)
    x_values1, y_values1 = input_projectile.getXgetY()
    max_range = task4.maxRangeList(0,h_global,u_global,g_global)
    task2.calculateTrajectoryData(max_range,100)
    x_values2,y_values2 = max_range.getXgetY()
    line1_source.data = {'x': x_values1, 'y': y_values1}
    line2_source.data = {'x': x_values2, 'y': y_values2}

# Create sliders
u_slider = Slider(start=0, end=100, value=u_global, step=0.1, title="Initial Velocity (m/s)")
h_slider = Slider(start=0, end=100, value=h_global, step=0.1, title="Initial Height (m)")
g_slider = Slider(start=0.01, end=20, value=g_global, step=0.01, title="Gravitational Acceleration (m/s^2)")
angle_slider = Slider(start=1, end=90, value=angle_global, step=1, title="Launch angle to horizontal (degrees)")

u_slider.on_change('value', update_target)
h_slider.on_change('value', update_target)
g_slider.on_change('value', update_target)
angle_slider.on_change('value', update_target)  # Integer values for v

update_lines()
# Arrange layout
layout = column(h_slider,u_slider, angle_slider,g_slider)
layout1= row(plot,layout)

# Update lines initially


# Show the plot
curdoc().add_root(layout1)
