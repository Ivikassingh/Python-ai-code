# You can extend this code to implement:
# Stochastic Hill climbing
# Random-restart Hill-climbing

import math 


fabs=math.fabs
sin=math.sin
cos=math.cos
exp=math.exp
pi=math.pi

#scalar multiple for grad-ascent
scalar=0.005

# I am doing gradient ascent here, since I want to maximize the function
def grad_ascent(x):
    
    #for func1
    #delta_x = -2.0*x

    #for func2
    #delta_x = -2.0*x*exp(-x*x)

    #for func3
    delta_x =  (exp(-x*x)*(6.0*sin(3*pi*x)*cos(3*pi*x)) - 2.0*x*sin(3.0*pi*x)*exp(-x*x))

    #for func4
    #scalar=0.008
    #delta_x = -exp(-x) + exp(x)
    
    return x + (scalar*delta_x)

# simple objective functions with
# one global maxima and no local minima
def func1(x):
    return -x*x

def func2(x):
    return exp(-x*x)

#local/global maxima
def func3(x):
    return exp(-x*x)*(sin(3.0*pi*x)**2)

#with a plateau in between
def func4(x):
    return (1.0 + exp(-x)) + (1.0 + exp(x))


#Definition of the simple hill climbing search
def hill_climb(objfunc,x,next_move):
    current = x

    while True:

        current_val=objfunc(current)
        next = next_move(current)
        if objfunc(next) > current_val:
            current = next
            print current,current_val
        else:
            break;
    
if __name__=='__main__':
    x_init = 0.95 # Hill climbing stops at the nearest hill it finds.

    # call the hill_climb function with the function
    # you want to optimize, the initial point and the 'move'
    # method, that you want to use for moving to a nearby solution
    hill_climb(func3,x_init,grad_ascent) 
