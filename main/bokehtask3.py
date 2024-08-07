import task2,task3, Projectile, Constants
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column,row

plot = figure(match_aspect=True)
line1 = ColumnDataSource(data={'x': [], 'y': []})
line2 = ColumnDataSource(data={'x': [], 'y': []})
line3 = ColumnDataSource(data={'x': [], 'y': []})
plot.line('x', 'y', source=line1, color="red",legend_label="Minimum Launch Speed")
plot.line('x','y',source=line2, color="blue",legend_label="LowBall")
plot.line('x','y',source=line3, color="yellow",legend_label="HighBall")
target = plot.circle(x=[0],y=[0],size=5,color='red',legend_label='Target Point')

current_x = 1
current_y = 1
current_v = 10

def find_currents():
    return current_x,current_y,current_v
def set_current_x(new):
    global current_x
    current_x = new
def set_current_y(new):
    global current_y
    current_y = new

def set_current_v(new):
    global current_v
    current_v = new

def update_target():
    global current_x
    global current_y
    update_target_x_y(current_x,current_y)
def update_target_x_y(x,y):
    target.data_source.data['x'] = [x]
    target.data_source.data['y'] = [y]
    #target.legend_label = f"Target Point ({x}, {y})"

def update_data_x(attr,old,new):
    current_x, current_y, current_v = find_currents()
    set_current_x(new)
    update_target()
    task3_projectile_minimum_u = task3.minimumSpeed(new,current_y)
    task2.calculateTrajectoryData(task3_projectile_minimum_u, 1000)
    x_values_1 , y_values_1 = task3_projectile_minimum_u.getXgetY()
    line1.data = {'x': x_values_1, 'y': y_values_1}
    #line1.legend_label = f"Minimum Launch Speed of {task3_projectile_minimum_u.initialVel}"
    lowball, highball = task3.lowAndHighBallList(current_x,current_y,current_v)
    x_values_2, y_values_2 = lowball.getXgetY()
    line2.data = {'x': x_values_2, 'y': y_values_2}
    x_values_3, y_values_3 = highball.getXgetY()
    line3.data = {'x': x_values_3, 'y': y_values_3}

def update_data_y(attr,old,new):
    current_x, current_y, current_v = find_currents()
    set_current_y(new)
    update_target()
    print("1")
    task3_projectile_minimum_u = task3.minimumSpeed(current_x,new)
    task2.calculateTrajectoryData(task3_projectile_minimum_u, 1000)
    x_values_1 , y_values_1 = task3_projectile_minimum_u.getXgetY()
    line1.data = {'x': x_values_1, 'y': y_values_1}
    print("2")
    #line1.legend_label = f"Minimum Launch Speed of {task3_projectile_minimum_u.initialVel}"
    lowball, highball = task3.lowAndHighBallList(current_x,current_y,current_v)
    x_values_2, y_values_2 = lowball.getXgetY()
    line2.data = {'x': x_values_2, 'y': y_values_2}
    print("3")
    x_values_3, y_values_3 = highball.getXgetY()
    line3.data = {'x': x_values_3, 'y': y_values_3}

def update_data_v(attr,old,new):
    current_x, current_y, current_v = find_currents()
    set_current_v(new)
    update_target()
    task3_projectile_minimum_u = task3.minimumSpeed(current_x,new)
    task2.calculateTrajectoryData(task3_projectile_minimum_u, 1000)
    x_values_1 , y_values_1 = task3_projectile_minimum_u.getXgetY()
    line1.data = {'x': x_values_1, 'y': y_values_1}
    #line1.legend_label = f"Minimum Launch Speed of {task3_projectile_minimum_u.initialVel}"
    lowball, highball = task3.lowAndHighBallList(current_x,current_y,new)
    x_values_2, y_values_2 = lowball.getXgetY()
    line2.data = {'x': x_values_2, 'y': y_values_2}
    x_values_3, y_values_3 = highball.getXgetY()
    line3.data = {'x': x_values_3, 'y': y_values_3}
    


y_slider = Slider(start=0,end=11,value=10,step=0.1,title="Target Point Height (m)")
y_slider.on_change('value',update_data_y)
x_slider = Slider(start=0,end=11,value=10,step=0.1,title="Target Point Distance from Origin (m)")
x_slider.on_change('value',update_data_x)
v_slider = Slider(start=8,end=10,value=10,step=0.1,title="Launch Speed (m/s)")
v_slider.on_change('value',update_data_v)


# Add the plot and slider to the document
slider_layout = column(x_slider, y_slider,v_slider)

# Arrange the plot and slider layout side by side
layout = row(plot, slider_layout)

# Add the layout to the document
curdoc().add_root(layout)