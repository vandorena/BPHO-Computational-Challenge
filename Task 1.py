import matplotlib

def time_array(delta_seconds):
    array = []
    for i in range(0,1000):
        array.append(i*delta_seconds)
    return array

def find_y(u_y,time):