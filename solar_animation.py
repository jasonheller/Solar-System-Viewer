from ursina import *
import numpy as np

def update():
    global t
    t = t + 0.01
    angle = np.pi*40/180
    
    radius_1 = 1
    mercury2.x = np.cos(t)*radius_1
    mercury2.z = np.sin(t)*radius_1    

    radius_2 = 1.4
    venus2.x = np.cos(t+angle)*radius_2
    venus2.z = np.sin(t+angle)*radius_2    

    radius_3 = 1.8
    earth2.x = np.cos(t+angle*2)*radius_3
    earth2.z = np.sin(t+angle*2)*radius_3    

    radius_4 = 2.2
    mars2.x = np.cos(t+angle*3)*radius_4
    mars2.z = np.sin(t+angle*3)*radius_4

    radius_5 = 2.6
    jupiter2.x = np.cos(t+angle*4)*radius_5
    jupiter2.z = np.sin(t+angle*4)*radius_5  
    
    radius_6 = 3
    saturn2.x = np.cos(t+angle*5)*radius_6
    saturn2.z = np.sin(t+angle*5)*radius_6  

    radius_7 = 3.4
    uranus2.x = np.cos(t+angle*6)*radius_7
    uranus2.z = np.sin(t+angle*6)*radius_7  

    radius_8 = 3.8
    neptune2.x = np.cos(t+angle*7)*radius_8
    neptune2.z = np.sin(t+angle*7)*radius_8  

    radius_9 = 4
    pluto2.x = np.cos(t+angle*8)*radius_9
    pluto2.z = np.sin(t+angle*8)*radius_9  

sun2 = Entity(model='sphere',color=color.yellow, scale=1.5)
mercury2 = Entity(model='sphere',color=color.gray, scale=0.2)
venus2 = Entity(model='sphere',color=color.orange, scale=0.3)
earth2 = Entity(model='sphere',color=color.blue, scale=0.4)
mars2 = Entity(model='sphere',color=color.violet, scale=0.3)
jupiter2 = Entity(model='sphere',color=color.yellow, scale=0.6)
saturn2 = Entity(model='sphere',color=color.white, scale=0.5)
uranus2 = Entity(model='sphere',color=color.cyan, scale=0.5)
neptune2 = Entity(model='sphere',color=color.gold, scale=0.5)
pluto2 = Entity(model='sphere',color=color.pink, scale=0.2)

t = -np.pi