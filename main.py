from ursina import * 

root = Ursina()
window.fps_counter.enabled = True
window.exit_button.visible = False
window.borderless = False
window.show_ursina_splash = True
window.fullscreen = False

start_var = 2
ec = EditorCamera(rotation_smoothing=2, enabled=True, rotation=(0,0,0), scale=2)

# EARTH_TEXTURE
earth = load_texture('assets/earth.jpg')
earth_button = load_texture('assets/earth_button.png')
# MARS_TEXTURE
mars = load_texture('assets/mars.png')
mars_button = load_texture('assets/mars_button.png')
# MERCURY_TEXTURE
mercury = load_texture('assets/mercury.jpg')
mercury_button = load_texture('assets/mercury_button.png')
# VENUS_TEXTURE
venus = load_texture('assets/venus.jpg')
venus_button = load_texture('assets/venus_button.png')
# CERES_TEXTURE
ceres = load_texture('assets/ceres.jpg')
ceres_button = load_texture('assets/ceres_button.png')
# JUPITER_TEXTURE
jupiter = load_texture('assets/jupiter.jpg')
jupiter_button = load_texture('assets/jupiter_button.png')
# SATURN_TEXTURE
saturn = load_texture('assets/saturn.jpg')
saturn_button = load_texture('assets/saturn_button.png')
# NEPTUNE_TEXTURE
neptune =  load_texture('assets/neptune.png')
neptune_button = load_texture('assets/neptune_button.png')
# URANUS_TEXTURE
uranus = load_texture('assets/uranus.jpg')
uranus_button = load_texture('assets/uranus_button.png')
# MOON_TEXTURE
moon = load_texture('assets/moon.png')
moon_button = load_texture('assets/moon_button.png')

if start_var == 2:
    earth.visible = False

# AMBIENT_AUDIO
ambient = Audio('assets/sounds/ambient.mp3', pitch=1, loop=True, autoplay=True, volume=80)
class Mute_Button(Button):
    def __init__(self):
        super().__init__(
            text='Mute',
            collider='circle',
            scale=0.1,
            position=(0.8,0.4,-0.8)
        )
    def on_click(self):
        ambient.volume=0

class Unmute_Button(Button):
    def __init__(self):
        super().__init__(
            text='Unmute',
            collider='circle',
            scale=0.1,
            position=(0.8,0.26,-0.8)
        )
    def on_click(self):
        ambient.volume=80

# MOON
class Moon(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = moon,
            double_sided = True,
            parent = scene,
            scale = 5
        )

class Moon_Button(Button):
    def __init__(self):
        super().__init__(
            text='Moon',
            texture=moon_button,
            scale=0.13,
            collider='circle',
            position=(-0.65,-0.09,0)
        )
    def on_click(self):
        moon.visible = True
        uranus.visible = False
        neptune.visible = False
        ceres.visible = False
        saturn.visible = False
        jupiter.visible = False
        venus.visible = False
        mercury.visible = False
        mars.visible = False
        earth.visible = False

class Uranus(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = uranus,
            double_sided = True,
            parent = scene,
            scale = 10
        )

# URANUS
class Uranus_Button(Button):
    def __init__(self):
        super().__init__(
            text='Uranus',
            texture=uranus_button,
            scale=0.13,
            collider='circle',
            position=(-0.65,-0.23,0)
        )
    def on_click(self):
        uranus.visible = True
        moon.visible = False
        neptune.visible = False
        ceres.visible = False
        saturn.visible = False
        jupiter.visible = False
        venus.visible = False
        mercury.visible = False
        mars.visible = False
        earth.visible = False

# NEPTUNE
class Neptune(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = neptune,
            double_sided = True,
            parent = scene,
            scale = 8
        )

class Neptune_Button(Button):
    def __init__(self):
        super().__init__(
            text='Neptune',
            texture=neptune_button,
            scale=0.13,
            collider='circle',
            position=(-0.65,-0.38,0)
        )
    def on_click(self):
        neptune.visible = True
        moon.visible = False
        uranus.visible = False
        ceres.visible = False
        saturn.visible = False
        jupiter.visible = False
        venus.visible = False
        mercury.visible = False
        mars.visible = False
        earth.visible = False

# SATURN
class Saturn(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = saturn,
            double_sided = True,
            parent = scene,
            scale = 12
        )

class Saturn_Button(Button):
    def __init__(self):
        super().__init__(
            text='Saturn',
            texture=saturn_button,
            scale=0.18,
            collider='circle',
            position=(-0.8,-0.38,0)
        )
    def on_click(self):
        saturn.visible = True
        moon.visible = False
        uranus.visible = False
        neptune.visible = False
        jupiter.visible = False
        ceres.visible = False
        venus.visible = False
        mercury.visible = False
        mars.visible = False
        earth.visible = False

# JUPITER
class Jupiter(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = jupiter,
            double_sided = True,
            parent = scene,
            scale = 14
        )

class Jupiter_Button(Button):
    def __init__(self):
        super().__init__(
            text='Jupiter',
            texture=jupiter_button,
            scale=0.15,
            collider='circle',
            position=(-0.8,-0.23,0)
        )
    def on_click(self):
        jupiter.visible = True
        moon.visible = False
        uranus.visible = False
        neptune.visible = False
        saturn.visible = False
        ceres.visible = False
        venus.visible = False
        mercury.visible = False
        mars.visible = False
        earth.visible = False

# CERES
class Ceres(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = ceres,
            double_sided = True,
            parent = scene,
            scale = 2
        )

class Ceres_Button(Button):
    def __init__(self):
        super().__init__(
            text='Ceres',
            texture=ceres_button,
            scale=0.06,
            collider='circle',
            position=(-0.8,-0.0999,0)
        )
    def on_click(self):
        ceres.visible = True
        moon.visible = False
        uranus.visible = False
        neptune.visible = False
        saturn.visible = False
        jupiter.visible = False
        venus.visible = False
        mercury.visible = False
        mars.visible = False
        earth.visible = False

# VENUS
class Venus(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = venus,
            double_sided = True,
            parent = scene,
            scale = 6
        )

class Venus_Button(Button):
    def __init__(self):
        super().__init__(
            text='Venus',
            texture=venus_button,
            scale=0.101,
            collider='circle',
            position=(-0.8,0.0,0)
        )
    def on_click(self):
        venus.visible = True
        moon.visible = False
        uranus.visible = False
        neptune.visible = False
        jupiter.visible = False
        ceres.visible = False
        mercury.visible = False
        mars.visible = False
        earth.visible = False

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
            texture=mercury_button,
            scale=0.101,
            collider='circle',
            position=(-0.8,0.12,0)
        )
    def on_click(self):
        mercury.visible = True
        moon.visible = False
        uranus.visible = False
        neptune.visible = False
        saturn.visible = False
        jupiter.visible = False
        ceres.visible = False
        venus.visible = False
        mars.visible = False
        earth.visible = False

# MARS
class Mars(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = mars,
            double_sided = True,
            parent = scene,
            scale = 5.5
        )

class Mars_Button(Button):
    def __init__(self):
        super().__init__(
            text='Mars',
            texture=mars_button,
            scale=0.1,
            position=(-0.8,0.25,0)
        )
    def on_click(self):
        mars.visible = True
        moon.visible = False
        uranus.visible = False
        neptune.visible = False
        saturn.visible = False
        jupiter.visible = False
        ceres.visible = False
        venus.visible = False
        mercury.visible = False
        earth.visible = False

# EARTH
class Earth_Button(Button):
    def __init__(self):
        super().__init__(
            text='Earth',
            texture=earth_button,
            scale=0.2,
            position=(-0.8,0.4,0)    
        )
    def on_click(self):
        earth.visible = True
        moon.visible = False
        uranus.visible = False
        neptune.visible = False
        saturn.visible = False
        jupiter.visible = False
        ceres.visible = False
        mars.visible = False
        venus.visible = False
        mercury.visible = False

class Earth(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = earth,
            double_sided = True,
            parent = scene,
            scale = 7
        )

title = Text(text='Solar System Viewer', color=color.white, position=(-0.1,0.49,0))
title = Text(text='Right Mouse Click to View Planet', color=color.white, position=(0.37,-0.44,0))
title = Text(text='Saturns Rings not included because of Bugs', color=color.white, position=(0.37,-0.47,0))

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

audio = Mute_Button()
audio2 = Unmute_Button()

root.run()
