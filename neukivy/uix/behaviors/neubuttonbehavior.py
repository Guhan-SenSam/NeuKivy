from kivy.properties import NumericProperty
from kivy.clock import Clock

class NeuButtonBehavior:

    up_elevation = NumericProperty(0)

    down_elevation = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.elevation_setter, 0)

    def elevation_setter(self,*args):
        self.elevation = self.up_elevation

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.elevation = self.down_elevation

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.elevation = self.up_elevation
