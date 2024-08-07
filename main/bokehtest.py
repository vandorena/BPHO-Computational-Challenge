from bokeh.plotting import figure, show,curdoc
import numpy as np

curdoc().theme = "dark_minimal"

x = np.arange(0,10,1)
y1 = x**2
y2 = x**3
y3 = x**4


p = figure(title="simple Line charts", x_axis_label="X",y_axis_label="y")

p.line(x,y1,color="red")
show(p)