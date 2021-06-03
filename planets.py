# code by me
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
    moon.enabled = False
    uranus.enabled = False
    neptune.enabled = False
    ceres.enabled = False
    saturn.enabled = False
    jupiter.enabled = False
    venus.enabled = False
    mercury.enabled = False
    mars.enabled = False
    earth.enabled = False
    sun.enabled = False
    # Delete Animations
    pluto2.enabled = False
    uranus2.enabled = False
    neptune2.enabled = False
    saturn2.enabled = False
    jupiter2.enabled = False
    venus2.enabled = False
    mercury2.enabled = False
    mars2.enabled = False
    earth2.enabled = False
    sun2.enabled = False

def changeToSolarView():
    deleteEntities()
    earth_button.enabled = False
    mars_button.enabled = False
    mercury_button.enabled = False
    venus_button.enabled = False
    ceres_button.enabled = False
    jupiter_button.enabled = False
    saturn_button.enabled = False
    neptune_button.enabled = False
    uranus_button.enabled = False
    moon_button.enabled = False
    sun_button.enabled = False

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
        sun.enabled = True

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
        moon.enabled = True

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
        uranus.enabled = True

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
        neptune.enabled = True

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
        saturn.enabled = True

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
        jupiter.enabled = True

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
        ceres.enabled = True

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
        venus.enabled = True

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
        mercury.enabled = True

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
        mars.enabled = True

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
        earth.enabled = True

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
