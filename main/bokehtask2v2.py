import task2, Projectile, Constants
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Slider, CustomJS
from bokeh.layouts import column, row

plot = figure(match_aspect=True)
source = ColumnDataSource(data=dict(x=[], y=[]))
plot.line('x', 'y', source=source)
apogee = plot.circle(x=[0], y=[0], size=5, color='red', legend_label='Apogee Point')

# Global variables (consider using a dedicated class for state management)
current_state = {
    'x': 0,
    'y': 0,
    'v': 10,
    'angle': 45,
    'g': 9.81,
    'steps': 100,
}

def update_data(attr, old, new):
    # Update state based on slider name and new value
    current_state[attr] = new

    # ... rest of the update_data function ...

angle_slider = Slider(start=1, end=90, value=45, step=1, title="Angle (Degrees)")
velocity_slider = Slider(start=1, end=1000, value=50, step=0.5, title="Velocity (m/s)")
g_slider = Slider(start=0.01, end=100, value=9.81, step=0.01, title="Gravity (m/s^2)")
h_slider = Slider(start=0, end=1000, value=0, step=0.1, title="Height (m)")

# Use CustomJS for callbacks
angle_slider.js_on_change('value', CustomJS(args=dict(source=source, apogee=apogee, current_state=current_state), code=update_data_js_code))
velocity_slider.js_on_change('value', CustomJS(args=dict(source=source, apogee=apogee, current_state=current_state), code=update_data_js_code))
g_slider.js_on_change('value', CustomJS(args=dict(source=source, apogee=apogee, current_state=current_state), code=update_data_js_code))
h_slider.js_on_change('value', CustomJS(args=dict(source=source, apogee=apogee, current_state=current_state), code=update_data_js_code))

# ... rest of the code ...

# Define update_data_js_code as a JavaScript function that accesses the Python objects
update_data_js_code = """
    const current_state = cb_obj['current_state'];
    current_state[cb_obj.attr] = cb_obj.value;

    // ... JavaScript code to update data and plot ...
"""
