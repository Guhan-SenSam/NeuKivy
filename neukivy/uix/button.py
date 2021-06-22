from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty
from neukivy.uix.behaviors.neumorph import NeuMorphRoundedRectangle
from neukivy.uix.behaviors.neubuttonbehavior import NeuButtonBehavior
from neukivy.app import ThemeableBehavior
from kivy.clock import Clock

Builder.load_string(
    """
<NeuButton>:
    canvas.before:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.light_shadow_size
            pos:self.light_shadow_pos
            texture:self.light_shadow
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.dark_shadow_size
            pos:self.dark_shadow_pos
            texture:self.dark_shadow
    canvas:
        Color:
            rgba:self.comp_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius,self.radius,self.radius,self.radius
    size:400,100
    size_hint:None,None

<NeuButtonEmboss>:
    canvas.after:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.light_shadow_size
            pos:self.light_shadow_pos
            texture:self.light_shadow
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.dark_shadow_size
            pos:self.dark_shadow_pos
            texture:self.dark_shadow
    canvas:
        Color:
            rgba:self.comp_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius,self.radius,self.radius,self.radius
    size:400,100
    size_hint:None,None
"""
)


class NeuButton(
    NeuButtonBehavior, AnchorLayout, NeuMorphRoundedRectangle, ThemeableBehavior
):

    comp_color = ListProperty([0, 0, 0, 0])

    bg_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty(20)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.color_setter, 0)

    def color_setter(self, *args):
        if self.comp_color == [0, 0, 0, 0]:
            self.comp_color = self.theme_manager.bg_color
        if self.dark_color == [0, 0, 0, 0]:
            self.dark_color = self.theme_manager.dark_color
        if self.light_color == [0, 0, 0, 0]:
            self.light_color = self.theme_manager.light_color
