import math

#Same as last task but we now need to try to fit the time array linspaced.

def time_array(delta_seconds):
    array = []
    for i in range(0,1000):
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
            launch_angle = float(input())
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
    if input_holder1 == True and input_holder2 == True and input_holder3 == True and input_holder4 == True:
        return launch_speed,launch_angle,gravity,height
    

def build_axes(times,u,theta,height,gravity):
    u_x,u_y = decompose(u,theta)
    x = []
    y = []
    for i in range(0,len(times)):
        x.append(find_x(u_x,times[i]))
        y.append(find_y(u_y,times[i],height,gravity))
    return x,y

def get_range_and_time(u_x,u_y,gravity,height):
    time = quadratic_solver((-0.5*gravity),u_y,(-1*height))
    if time == "Bad Argument":
        return exit()
    time_delta = time/1010
    Range = u_x * time
    return Range,time_delta

def quadratic_solver(a,b,c):
    holder = False
    determinent = b**2 - (4*a*c)
    if determinent < 0:
        return "Bad Argument"
    determinent = math.sqrt(determinent)
    positive_result = (-1*b + determinent)/(2*a)
    negative_result = (-1*b - determinent)/(2*a)


    if positive_result > negative_result:
        return positive_result
    else:
        return negative_result
    

launch_speed,launch_angle,gravity,height = get_inputs()
u_x,u_y = decompose(launch_speed,launch_angle)
Range,time_delta = get_range_and_time(u_x,u_y,gravity,height)
times = time_array(time_delta)
x_axis,y_axis = build_axes(times,launch_speed,launch_angle,height,gravity)




#print(x_axis)
print("")
print("")
print(Range)
print(time_delta)
#print(y_axis)
