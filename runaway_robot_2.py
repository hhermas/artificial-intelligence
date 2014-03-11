# ----------
# Part Two
#
# Now we'll make the scenario a bit more realistic. Now Traxbot's
# sensor measurements are a bit noisy (though its motions are still
# completetly noise-free and it still moves in an almost-circle).
# You'll have to write a function that takes as input the next
# noisy (x, y) sensor measurement and outputs the best guess 
# for the robot's next position.
#
# ----------
# YOUR JOB
#
# Complete the function estimate_next_pos. You will be considered 
# correct if your estimate is within 0.01 stepsizes of Traxbot's next
# true position. 
#
# ----------
# GRADING
# 
# We will make repeated calls to your estimate_next_pos function. After
# each call, we will compare your estimated position to the robot's true
# position. As soon as you are within 0.01 stepsizes of the true position,
# you will be marked correct and we will tell you how many steps it took
# before your function successfully located the target bot.

# These import steps give you access to libraries which you may (or may
# not) want to use.
from robot import *  # Check the robot.py tab to see how this works.
from math import *
from matrix import * # Check the matrix.py tab to see how this works.
import random
import numpy as np

# This is the function you have to write. Note that measurement is a 
# single (x, y) point. This function will have to be called multiple
# times before you have enough information to accurately predict the
# next position. The OTHER variable that your function returns will be 
# passed back to your function the next time it is called. You can use
# this to keep track of important information over time.
def estimate_next_pos(measurement, OTHER = None):
    """Estimate the next (x, y) position of the wandering Traxbot
    based on noisy (x, y) measurements."""

    """ I will use OTHER to store each step.
    This will convert OTHER into an empty list for the first call
    """
    if OTHER == None:
        OTHER = []

    OTHER.append(measurement) #Appends the measurement to OTHER
    """
    I cannot determine step size until at least 2 steps
    It will take (at least) 3 steps to determine the angle step. 

    To find the Step_size I will use the distance_between function
    To find the travelling vector I will use the invTan(dx/dy)

    My prefered method of solving this would be to fit the data using
    linear least squares. However, given that I did not have access to numpy
    and I did not want
    """

    if len(OTHER) < 3:
        xy_estimate = measurement
    else:
        i = 0
        # print "!!!!!"
        angle = []
        size = 0.0
        vector = []

        for i in range(len(OTHER)-2):
            init_dx = OTHER[1+i][0]-OTHER[0+i][0] #distance in x moved for first step
            init_dy = OTHER[1+i][1]-OTHER[0+i][1] # distance in x moved for first step
            init_angle = atan2(init_dx, init_dy) #Angle of travel for first movement
            init_step_size = distance_between(OTHER[0+i], OTHER[1+i]) # distance travelled
            vector.append(init_angle)

            final_dx = OTHER[2+i][0]-OTHER[1+i][0] #distance in x moved for second step
            final_dy = OTHER[2+i][1]-OTHER[1+i][1] #distance in y moved for second step
            final_angle = atan2(final_dx, final_dy) #Angle of travel for second movement
            final_step_size = distance_between(OTHER[1+i], OTHER[2+i]) #distance travelled (with no noise, should be the same as above) 

            turn_angle = (final_angle - init_angle)
            step_size = (final_step_size+init_step_size)/2.0
            angle.append(final_angle - init_angle) #The angle the robot turned
            size += (final_step_size+init_step_size)/2.0 #Average step size (included for noise purpose)

            i += 1.0
        angle.sort()
        angle = angle[int(ceil(len(angle)/2.)-1)]

        # print angle, size/i, i

        size /= i
        turn_dx = size*sin(final_angle+angle) #Distance in x robot will move on next step
        turn_dy = size*cos(final_angle+angle) #Distance in y robot will move on next step

        xy_estimate = (measurement[0]+turn_dx, measurement[1]+turn_dy)

    # You must return xy_estimate (x, y), and OTHER (even if it is None) 
    # in this order for grading purposes.
    return xy_estimate, OTHER

# A helper function you may find useful.
def distance_between(point1, point2):
    """Computes distance between point1 and point2. Points are (x, y) pairs."""
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# This is here to give you a sense for how we will be running and grading
# your code. Note that the OTHER variable allows you to store any 
# information that you want. 
def demo_grading(estimate_next_pos_fcn, target_bot, OTHER = None):
    localized = False
    distance_tolerance = 0.01 * target_bot.distance
    ctr = 0
    # if you haven't localized the target bot, make a guess about the next
    # position, then we move the bot and compare your guess to the true
    # next position. When you are close enough, we stop checking.
    while not localized and ctr <= 5000:
        ctr += 1
        measurement = target_bot.sense()
        position_guess, OTHER = estimate_next_pos_fcn(measurement, OTHER)
        target_bot.move_in_circle()
        true_position = (target_bot.x, target_bot.y)
        error = distance_between(position_guess, true_position)
        if error <= distance_tolerance:
            print "You got it right! It took you ", ctr, " steps to localize."
            localized = True
        if ctr == 5000:
            print "Sorry, it took you too many steps to localize the target."
    return localized

# This is a demo for what a strategy could look like. This one isn't very good.
def naive_next_pos(measurement, OTHER = None):
    """This strategy records the first reported position of the target and
    assumes that eventually the target bot will eventually return to that 
    position, so it always guesses that the first position will be the next."""
    if not OTHER: # this  s the first measurement
        OTHER = measurement
    xy_estimate = OTHER 
    return xy_estimate, OTHER

# This is how we create a target bot. Check the robot.py file to understand
# How the robot class behaves.
test_target = robot(2.1, 4.3, 0.5, 2*pi / 34.0, 1.5)
measurement_noise = 0.05 * test_target.distance
test_target.set_noise(0.0, 0.0, measurement_noise)

demo_grading(estimate_next_pos, test_target)




