from ursina import * 

root = Ursina()
window.fps_counter.enabled = False
window.exit_button.visible = False
window.borderless = False
window.show_ursina_splash = True
window.fullscreen = False

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
        sve.visible = False
        moon.visible = True
        uranus.visible = True
        neptune.visible = True
        ceres.visible = True
        saturn.visible = True
        jupiter.visible = True
        venus.visible = True
        mercury.visible = True
        mars.visible = True
        earth.visible = True 
        earth_button.visible = True
        mars_button.visible = True
        mercury_button.visible = True
        venus_button.visible = True
        ceres_button.visible = True
        jupiter_button.visible = True
        saturn_button.visible = True
        neptune_button.visible = True
        uranus_button.visible = True
        moon_button.visible = True
        sun_button.visible = True

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
        sve.visible = True
        pluto2.visible = True
        uranus2.visible = True
        neptune2.visible = True
        saturn2.visible = True
        jupiter2.visible = True
        venus2.visible = True
        mercury2.visible = True
        mars2.visible = True
        earth2.visible = True
        sun2.visible = True

from solar_animation import *
from planets import *

sve = SolarViewExit()
sv = SolarView()
root.run()