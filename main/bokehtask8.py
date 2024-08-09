import numpy as np
import math, Projectile, task8, time
from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, Slider, CustomJS
from bokeh.layouts import column,row


# Create a scatter plot with a target point
plot = figure(title="Task 8", tools="reset,save", )

# Initialize line data sources
v_global = 10
h_global = 0
angle_global = 45
g_global = 9.81
bounce_global = 0
coe_global = 0.3
projectile = Projectile.ProjectileList(v=v_global, y=h_global, angle=angle_global, g=g_global, coe=coe_global)
task8.bouncyProjectileData(projectile, bounce_global)
x_values, y_values = projectile.getXgetY()

line1_source = ColumnDataSource(data=dict(x=x_values, y=y_values))
# Create lines (initially empty)
plot.line('x', 'y', source=line1_source, color="blue", legend_label="Bouncy")




# Initialize line data source with initial data



def update_target(attr, old, new):
    global g_global, h_global, angle_global, v_global, bounce_global, coe_global
    v_global = v_slider.value
    h_global = h_slider.value
    angle_global = math.radians(angle_slider.value)
    g_global = g_slider.value
    bounce_global = bounce_slider.value
    coe_global = coe_slider.value
    update_lines()


def update_lines():
    global v_global, h_global, angle_global, g_global, bounce_global, coe_global
    projectile = Projectile.ProjectileList(v=v_global, y=h_global, angle=angle_global, g=g_global, coe=coe_global)
    task8.bouncyProjectileData(projectile, bounce_global)
    x_values, y_values = projectile.getXgetY()

    # Update existing line source with new data
    line1_source.data = dict(x=x_values, y=y_values)

def animate_line(x_values: list, y_values: list):
    length = len(x_values)
    current_xs, current_ys = [], []
    index = 0

    source = ColumnDataSource(data={'x': current_xs, 'y': current_ys})

    callback = CustomJS(args=dict(source=source, x_values=x_values, y_values=y_values), code="""
        const length = x_values.length;
        const index = cb_obj.index;
        if (index < length) {
            cb_obj.data['x'].push(x_values[index]);
            cb_obj.data['y'].push(y_values[index]);
            source.change.emit();
            cb_obj.index = index + 1;  # Update index directly within the code
        }
    """)

    # Update index within the callback code itself
    # No need for a separate js_property_callback for index

    plot.line('x', 'y', source=source, color="blue", legend_label="Bouncy")

    
    

# Create sliders
v_slider = Slider(start=1, end=100, value=v_global, step=1, title="Velocity Parameter")
h_slider = Slider(start=0, end=100, value=h_global, step=0.1, title="Initial Height (m)")
g_slider = Slider(start=0.01, end=20, value=g_global, step=0.01, title="Gravitational Acceleration (m/s^2)")
angle_slider = Slider(start=1,end = 90, value=angle_global,step=0.1,title="Launch Angle (deg)")
bounce_slider = Slider(start=1,end=15,step=1,value=bounce_global,title='Number of Bounces')
coe_slider =  Slider(start=0.001, end=0.99, step=0.001, value=coe_global, title='Coefficient of Restitution')

h_slider.on_change('value', update_target)
g_slider.on_change('value', update_target)  # Integer values for v
v_slider.on_change('value', update_target)
angle_slider.on_change('value',update_target)
bounce_slider.on_change('value',update_target)
coe_slider.on_change('value',update_target)  # Integer values for v

update_lines()
# Arrange layout
layout = column(v_slider,angle_slider, h_slider, g_slider, bounce_slider,coe_slider)
layout1= row(plot,layout)

# Update lines initially


# Show the plot
curdoc().add_root(layout1)
