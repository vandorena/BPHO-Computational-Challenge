import task1, Projectile, Constants
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column,row

plot = figure(match_aspect=True)
source = ColumnDataSource(data={'x': [], 'y': []})
plot.line('x', 'y', source=source)
current_x = 0
current_y = 0
current_v = 10
current_angle = 45
current_g = 9.81
def find_currents():
    return current_x,current_y,current_v,current_angle,current_g
def set_current_angle(new):
    global current_angle
    current_angle = new

def set_current_v(new):
    global current_v
    current_v = new

def set_current_g(new):
    global current_g
    current_g = new

def set_current_y(new):
    global current_y
    current_y = new

def update_data_angle(attr, old, new):
    current_x, current_y , current_v, current_angle, current_g = find_currents()
    set_current_angle(new)
    task1_projectile = Projectile.ProjectileList(x = current_x, y=current_y, v=current_v, angle=int(new), g=current_g)
    task1.calculateTrajectoryData(task1_projectile)
    x_values , y_values = task1_projectile.getXgetY()
    source.data = {'x': x_values, 'y': y_values}

def update_data_velocity(attr,old, new):
    current_x, current_y , current_v, current_angle, current_g = find_currents()
    set_current_v(new)
    task1_projectile = Projectile.ProjectileList(x = current_x, y=current_y, v=new, angle=current_angle, g=current_g)
    task1.calculateTrajectoryData(task1_projectile)
    x_values , y_values = task1_projectile.getXgetY()
    source.data = {'x': x_values, 'y': y_values}
    
def update_data_g(attr,old,new):
    current_x, current_y, current_v, current_angle, current_g = find_currents()
    set_current_g(new)
    task1_projectile = Projectile.ProjectileList(x = current_x, y=current_y, v=new, angle=current_angle, g=current_g)
    task1.calculateTrajectoryData(task1_projectile)
    x_values , y_values = task1_projectile.getXgetY()
    source.data = {'x': x_values, 'y': y_values}
    
def update_data_y(attr,old,new):
    current_x, current_y, current_v, current_angle, current_g = find_currents()
    set_current_y(new)
    task1_projectile = Projectile.ProjectileList(x = current_x, y=new, v=current_v, angle=current_angle, g=current_g)
    task1.calculateTrajectoryData(task1_projectile)
    x_values , y_values = task1_projectile.getXgetY()
    source.data = {'x': x_values, 'y': y_values}

angle_slider = Slider(start=1, end=90, value=45, step=1, title="Angle of Projectile (Degrees)")
angle_slider.on_change('value', update_data_angle)
velocity_slider = Slider(start=1,end=1000,value=50,step=0.5,title="Velocity of Projectile (m/s)")
velocity_slider.on_change('value',update_data_velocity)
g_slider = Slider(start=0.01,end=100,value=9.81,step=0.01,title=" Gravitational Acceleration (m/s^2)")
g_slider.on_change('value',update_data_g)
h_slider = Slider(start=0,end=1000,value=0,step=0.1,title="Height (m)")
h_slider.on_change('value',update_data_y)



# Add the plot and slider to the document
slider_layout = column(angle_slider, velocity_slider, g_slider, h_slider)

# Arrange the plot and slider layout side by side
layout = row(plot, slider_layout)

# Add the layout to the document
curdoc().add_root(layout)
