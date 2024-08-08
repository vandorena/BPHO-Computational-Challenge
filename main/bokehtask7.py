import numpy as np
import task3,task2,task4,task7, Projectile, task5, math, bisect
from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column,row

def find_closest_index_sorted(numbers, target):
  """Finds the index of the closest value to the target in a sorted list.

  Args:
    numbers: The sorted list of numbers.
    target: The target value.

  Returns:
    The index of the closest value.
  """

  # Find the insertion point for the target value
  idx = bisect.bisect_left(numbers, target)

  # Handle cases where the target is outside the list
  if idx == 0:
    return 0
  if idx == len(numbers):
    return len(numbers) - 1

  # Compare the differences between the target and the two closest elements
  if numbers[idx] - target < target - numbers[idx - 1]:
    return idx
  else:
    return idx - 1
  

# Create a scatter plot with a target point
plot = figure(title="Task 7 - u = 20m/s g = 9.81 m/s^2", tools="reset,save")


# Initialize line data sources
line1_source = ColumnDataSource(data={'x': [], 'y': []})
line2_source = ColumnDataSource(data={'x': [], 'y': []})
line3_source = ColumnDataSource(data={'x': [], 'y': []})
line4_source = ColumnDataSource(data={'x': [], 'y': []})
line5_source = ColumnDataSource(data={'x': [], 'y': []})
line6_source = ColumnDataSource(data={'x': [], 'y': []})

max1_source = ColumnDataSource(data={'x': [], 'y': []})
max2_source = ColumnDataSource(data={'x': [], 'y': []})
max3_source = ColumnDataSource(data={'x': [], 'y': []})

min1_source = ColumnDataSource(data={'x': [], 'y': []})
min2_source = ColumnDataSource(data={'x': [], 'y': []})
min3_source = ColumnDataSource(data={'x': [], 'y': []})

plot.circle('x', 'y', source=max1_source, size=5, color='blue', legend_label='Maximum Point 71 Degrees')
plot.circle('x', 'y', source=max2_source, size=5, color='blue', legend_label='Maximum Point 78 Degrees')
plot.circle('x', 'y', source=max3_source, size=5, color='blue', legend_label='Maximum Point 85 Degrees')

plot.circle('x', 'y', source=min1_source, size=5, color='green', legend_label='Minimum Point 71 Degrees')
plot.circle('x', 'y', source=min2_source, size=5, color='green', legend_label='Minimum Point 78 Degrees')
plot.circle('x', 'y', source=min3_source, size=5, color='green', legend_label='Minimum Point 85 Degrees')
# Create lines (initially empty)
plot.line('x', 'y', source=line1_source, color="blue", legend_label="30 Degrees")
plot.line('x', 'y', source=line2_source, color="green", legend_label="45 Degrees")
plot.line('x', 'y', source=line3_source, color="orange", legend_label="60 Degrees")
plot.line('x', 'y', source=line4_source, color="yellow", legend_label="71 Degrees")
plot.line('x', 'y', source=line5_source, color="red", legend_label="78 Degrees")
plot.line('x', 'y', source=line6_source, color="pink", legend_label="85 Degrees")
deg = Projectile.Projectile(angle=(math.radians(30)))
return1 = task7.calculateRangeTimeData(deg)
deg1 = Projectile.Projectile(angle=(math.radians(45)))
return2 = task7.calculateRangeTimeData(deg1)
deg2 = Projectile.Projectile(angle=(math.radians(60)))
return3 = task7.calculateRangeTimeData(deg2)

deg3 = Projectile.Projectile(angle=(math.radians(71)))
return4 = task7.calculateRangeTimeData(deg3)
seven1_max, seven1_min = task7.calculateMaxAndMinTime(deg3)
seven1_max_index = find_closest_index_sorted(return4[0],seven1_max)
max2_source.data = {'x': [seven1_max], 'y': [return4[1][seven1_max_index]]}
seven1_min_index = find_closest_index_sorted(return4[0],seven1_min)
min2_source.data = {'x': [seven1_min], 'y': [return4[1][seven1_min_index]]}

deg4 = Projectile.Projectile(angle=(math.radians(78)))
return5 = task7.calculateRangeTimeData(deg4)
seven8_max, seven8_min = task7.calculateMaxAndMinTime(deg4)
seven8_max_index = find_closest_index_sorted(return5[0],seven8_min)
max2_source.data = {'x': [seven8_max], 'y': [return5[1][seven8_max_index]]}
seven8_min_index = find_closest_index_sorted(return5[0],seven8_max)
min2_source.data = {'x': [seven8_min], 'y': [return5[1][seven8_min_index]]}

deg5 = Projectile.Projectile(angle=(math.radians(85)))
return6 = task7.calculateRangeTimeData(deg5)
eight5_max, eight5_min = task7.calculateMaxAndMinTime(deg5)
eight5_max_index = find_closest_index_sorted(return6[0],eight5_max)
max2_source.data = {'x': [eight5_max], 'y': [return6[1][eight5_max_index]]}
eight5_min_index = find_closest_index_sorted(return6[0],eight5_min)
min2_source.data = {'x': [eight5_min], 'y': [return6[1][eight5_min_index]]}

print(return6)

line1_source.data = {'x': return1[0], 'y': return1[1]}
line2_source.data = {'x': return2[0], 'y': return2[1]}
line3_source.data = {'x': return3[0], 'y': return3[1]}
line4_source.data = {'x': return4[0], 'y': return4[1]}
line5_source.data = {'x': return5[0], 'y': return5[1]}
line6_source.data = {'x': return6[0], 'y': return6[1]}


# Update lines initially


# Show the plot
curdoc().add_root(plot)
curdoc().theme = 'night_sky'
