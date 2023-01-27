# Imports modules
from ursina import *
import time
app=Ursina(vsync=False)

#Lighting and positioning
sun = DirectionalLight()
sun.look_at(Vec3(0,0,0))

# Creates the star, clouds, and moon.
# Also added a core of the star to preserve location
star_core = Entity(model='sphere',texture='earth.png', color=color.white)
star_core1 = Entity(model='cube',texture='white_cube', color=color.white,scale=1,alpha=0)
cloud1 = Entity(model='model.obj', texture="cloud.png", scale=.0009,color=color.white, parent=star_core1,alpha=.35)
cloud2 = Entity(model='model.obj', texture="cloud.png", scale=.0009,color=color.white, parent=star_core1,alpha=.35)
cloud3 = Entity(model='model.obj', texture="cloud.png", scale=.0009,color=color.white, parent=star_core1,alpha=.35)
cloud4 = Entity(model='model.obj', texture="cloud.png", scale=.0009,color=color.white, parent=star_core1,alpha=.35)
moon = Entity(model='sphere', texture="white_cube", scale=.1,color=color.white, parent=star_core)

# Positioning of the clouds and moon
cloud1.x = .25
cloud1.y = .1
cloud2.x = -.25
cloud2.y = -.5
cloud3.x = -.5
cloud3.y = .3
cloud4.x = .3
cloud4.y = -.2
cloud4.z= .4
moon.x = 1.5
moon.y = .1

# Creates atmosphere around the planet
star_halo = Entity(model='sphere', texture='white_cube',color=color.white, alpha= .1, scale=.1)

#Update that rotates everything around
counter = 0
def update():
    global counter
    star_core.rotation_y += .3
    star_core.rotation_x -= .0001
    star_core1.rotation_y += 1
    star_core1.rotation_x -= .09
    counter += 1
    star_halo.scale = 1.1 + .05 * sin(counter * .005)
    moon.rotation_y * sin(counter * 100)

#Changes background to a mp4
#Also Editor allows you to move around with mouse
Sky(texture="Nebula.mp4",scale=1000)
EditorCamera()
app.run()





