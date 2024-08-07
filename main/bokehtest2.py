import Projectile, task1
from bokeh.plotting  import figure,show,curdoc
from bokeh.models import Div , Spinner,TextInput

starting_x = Div(text="<p> Select Starting X Coordinate")
starting_y = Div(text="<p> Select Starting Y Coordinate")
starting_v = Div(text="<p> Select Starting Velocity")
starting_angle = Div(text="<p> Select Starting Angle to horizontal")
