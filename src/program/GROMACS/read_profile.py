import os
import sys
import numpy as np

pulse_profile = open('profile.txt', 'r')
lines = pulse_profile.readlines()

t0 = lines[0].split()[0]
t1 = lines[1].split()[0]

dt = float(t1)-float(t0) # timestep
nsteps = len(lines)-1    # number of steps

 
