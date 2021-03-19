from numpy import load
from ursina import *
from solar_animation import *

earth = load_texture('assets/earth.jpg')
mars = load_texture('assets/mars.png')
mercury = load_texture('assets/mercury.jpg')
venus = load_texture('assets/venus.jpg')
ceres = load_texture('assets/ceres.jpg')
jupiter = load_texture('assets/jupiter.jpg')
saturn = load_texture('assets/saturn.jpg')
neptune =  load_texture('assets/neptune.png')
uranus = load_texture('assets/uranus.jpg')
moon = load_texture('assets/moon.png')
sun = load_texture('assets/sun.png')

def deleteEntities():
    moon.visible = False
    uranus.visible = False
    neptune.visible = False
    ceres.visible = False
    saturn.visible = False
    jupiter.visible = False
    venus.visible = False
    mercury.visible = False
    mars.visible = False
    earth.visible = False 
    sun.visible = False
    # Delete Animations
    pluto2.visible = False
    uranus2.visible = False
    neptune2.visible = False
    saturn2.visible = False
    jupiter2.visible = False
    venus2.visible = False
    mercury2.visible = False
    mars2.visible = False
    earth2.visible = False
    sun2.visible = False

def changeToSolarView():
    deleteEntities()
    earth_button.visible = False
    mars_button.visible = False
    mercury_button.visible = False
    venus_button.visible = False
    ceres_button.visible = False
    jupiter_button.visible = False
    saturn_button.visible = False
    neptune_button.visible = False
    uranus_button.visible = False
    moon_button.visible = False
    sun_button.visible = False

deleteEntities()


class Sun(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = sun,
            double_sided = True,
            parent = scene,
            scale = 15
        )

class Sun_Button(Button):
    def __init__(self):
        super().__init__(
            text='Sun',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.65,-0.13,0)
        )
    def on_click(self):
        deleteEntities()
        sun.visible = True

# MOON
class Moon(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = moon,
            double_sided = True,
            parent = scene,
            scale = 4
        )

class Moon_Button(Button):
    def __init__(self):
        super().__init__(
            text='Moon',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.65,0.00625,0)
        )
    def on_click(self):
        deleteEntities()
        moon.visible = True

# URANUS
class Uranus(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = uranus,
            double_sided = True,
            parent = scene,
            scale = 13
        )

class Uranus_Button(Button):
    def __init__(self):
        super().__init__(
            text='Uranus',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.65,-0.265,0)
        )
    def on_click(self):
        deleteEntities()
        uranus.visible = True

# NEPTUNE
class Neptune(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = neptune,
            double_sided = True,
            parent = scene,
            scale = 14
        )

class Neptune_Button(Button):
    def __init__(self):
        super().__init__(
            text='Neptune',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.65,-0.40,0)
        )
    def on_click(self):
        deleteEntities()
        neptune.visible = True

# SATURN
class Saturn(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = saturn,
            double_sided = True,
            parent = scene,
            scale = 14.5
        )

class Saturn_Button(Button):
    def __init__(self):
        super().__init__(
            text='Saturn',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.8,-0.40,0)
        )
    def on_click(self):
        deleteEntities()
        saturn.visible = True

# JUPITER
class Jupiter(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = jupiter,
            double_sided = True,
            parent = scene,
            scale = 14.5
        )

class Jupiter_Button(Button):
    def __init__(self):
        super().__init__(
            text='Jupiter',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.8,-0.265,0)
        )
    def on_click(self):
        deleteEntities()
        jupiter.visible = True

# CERES
class Ceres(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = ceres,
            double_sided = True,
            parent = scene,
            scale = 3
        )

class Ceres_Button(Button):
    def __init__(self):
        super().__init__(
            text='Ceres',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.8,0.00625,0)
        )
    def on_click(self):
        deleteEntities()
        ceres.visible = True

# VENUS
class Venus(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = venus,
            double_sided = True,
            parent = scene,
            scale = 9
        )

class Venus_Button(Button):
    def __init__(self):
        super().__init__(
            text='Venus',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.8,-0.13,0)
        )
    def on_click(self):
        deleteEntities()
        venus.visible = True

# MERCURY
class Mercury(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = mercury,
            double_sided = True,
            parent = scene,
            scale = 5
        )

class Mercury_Button(Button):
    def __init__(self):
        super().__init__(
            text='Mercury',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.8,0.14,0)
        )
    def on_click(self):
        deleteEntities()
        mercury.visible = True

# MARS
class Mars(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = mars,
            double_sided = True,
            parent = scene,
            scale = 7
        )

class Mars_Button(Button):
    def __init__(self):
        super().__init__(
            text='Mars',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.8,0.27,0)
        )
    def on_click(self):
        deleteEntities()
        mars.visible = True

# EARTH
class Earth_Button(Button):
    def __init__(self):
        super().__init__(
            text='Earth',
            scale=0.1,
            model = 'quad',
            collider='circle',
            position=(-0.8,0.4,0)    
        )
    def on_click(self):
        deleteEntities()
        earth.visible = True
        
class Earth(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = 'earth',
            double_sided = True,
            parent = scene,
            scale = 9.5
        )

sun = Sun()
sun_button = Sun_Button()
earth = Earth()
earth_button = Earth_Button()
mars = Mars()
mars_button = Mars_Button()
mercury = Mercury()
mercury_button = Mercury_Button()
venus = Venus()
venus_button = Venus_Button()
ceres = Ceres()
ceres_button = Ceres_Button()
jupiter = Jupiter()
jupiter_button = Jupiter_Button()
saturn = Saturn()
saturn_button = Saturn_Button()
neptune = Neptune()
neptune_button = Neptune_Button()
uranus = Uranus()
uranus_button = Uranus_Button()
moon = Moon()
moon_button = Moon_Button()