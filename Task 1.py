import math

def time_array(delta_seconds,step_max):
    array = []
    for i in range(0,step_max):
        array.append(i*delta_seconds)
    return array

def decompose(u,theta):
    u_x = u*(math.cos(theta))
    u_y = u*(math.sin(theta))
    return u_x,u_y

def find_x(u_x,time):
    return (u_x*time)

def find_y(u_y,time,height,gravity_acceleration):
    return (height+(u_y*time) - (0.5*(gravity_acceleration*(time**2))))

def get_inputs():
    print("Please Input The Launch Speed of the Particle in m/s: ")
    input_holder1 = False
    launch_speed = 0
    while not input_holder1:
        try:
            launch_speed = float(input())
        except BaseException: #Im being lazy sorry
            input_holder1 = False
        if launch_speed > 0:
            input_holder1 = True
    input_holder2 = False
    print("Please enter the launch angle in degrees: ")
    launch_angle = 0
    while not input_holder2:
        try:
            launch_angle = int(input())
        except BaseException:
            pass
        if launch_angle > 0 and launch_angle <= 90:
            launch_angle = math.radians(launch_angle)
            input_holder2 = True
    input_holder3 = False
    print("Please enter your value for gravitational acceleration in m/s^2: ")
    gravity = 0
    while not input_holder3:
        try:
            gravity = float(input())
        except BaseException:
            pass
        if gravity > 0:
            input_holder3 = True
    input_holder4 = False
    print("Please enter your starting height in m: ")
    height = 0
    while not input_holder4:
        try:
            height = float(input())
        except BaseException:
            pass
        if height != None:
            input_holder4 = True
    input_holder5 = False
    print("Enter how long you want each step to be, in seconds: ")
    time_step = 0
    while not input_holder5:
        try:
            time_step = float(input())
        except BaseException:
            pass
        if time_step > 0:
            input_holder5 = True
    input_holder6 = False
    print("How many steps do you want to have?: ")
    step_max = 0
    while not input_holder6:
        try:
            step_max = int(input())
        except BaseException:
            pass
        if step_max > 0:
            input_holder6 = True

    if input_holder1 == True and input_holder2 == True and input_holder3 == True and input_holder4 == True and input_holder5 == True and input_holder6 == True:
        return launch_speed,launch_angle,gravity,height,time_step,step_max
    

def build_axes(times,u,theta,height,gravity):
    u_x,u_y = decompose(u,theta)
    x = []
    y = []
    for i in range(0,len(times)):
        x.append(find_x(u_x,times[i]))
        y.append(find_y(u_y,times[i],height,gravity))
    return x,y


launch_speed,launch_angle,gravity,height,time_delta,max_step = get_inputs()
times = time_array(time_delta,max_step)
x_axis,y_axis = build_axes(times,launch_speed,launch_angle,height,gravity)

print(x_axis)
print("")
print("")
print(y_axis)
