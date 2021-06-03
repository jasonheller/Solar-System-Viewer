# Code by Me
from ursina import *

root = Ursina()
window.exit_button.visible = False
window.fps_counter.enabled = False
window.borderless = False
window.show_ursina_splash = True
window.fullscreen = False
camera.orthographic = False
space = load_texture('./assets/space.png')
Sky(texture=space)
ec = EditorCamera(rotation_smoothing=2, enabled=True, rotation=(0,0,0), scale=2)

title = Text(text='Solar System Viewer', color=color.white, position=(-0.1,0.49,0))
title = Text(text='Right Mouse Click to View Planet', color=color.white, position=(0.5,-0.47,0))

class SolarViewExit(Button):
    def __init__(self):
        super().__init__(
            text='X',
            model = 'quad',
            collider='circle',
            scale=0.1,
            position=(0.8,-0.38,0)
        )
    def on_click(self):
        deleteEntities()
        sve.enabled = False
        moon.enabled = True
        uranus.enabled = True
        neptune.enabled = True
        ceres.enabled = True
        saturn.enabled = True
        jupiter.enabled = True
        venus.enabled = True
        mercury.enabled = True
        mars.enabled = True
        earth.enabled = True
        earth_button.enabled = True
        mars_button.enabled = True
        mercury_button.enabled = True
        venus_button.enabled = True
        ceres_button.enabled = True
        jupiter_button.enabled = True
        saturn_button.enabled = True
        neptune_button.enabled = True
        uranus_button.enabled = True
        moon_button.enabled = True
        sun_button.enabled = True

class SolarView(Button):
    def __init__(self):
        super().__init__(
            text='Solar System',
            model = 'quad',
            collider='circle',
            scale=0.1,
            position=(0.8,-0.26,0)
        )
    def on_click(self):
        deleteEntities()
        changeToSolarView()
        sve.enabled = True
        pluto2.enabled = True
        uranus2.enabled = True
        neptune2.enabled = True
        saturn2.enabled = True
        jupiter2.enabled = True
        venus2.enabled = True
        mercury2.enabled = True
        mars2.enabled = True
        earth2.enabled = True
        sun2.enabled = True

from solar_animation import *
from planets import *

sve = SolarViewExit()
sv = SolarView()
root.run()
