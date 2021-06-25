from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from neukivy.uix.behaviors.neumorph import (
    NeuMorphCircular,
    NeuMorphRectangle,
    NeuMorphRoundedRectangle,
)
from neukivy.uix.behaviors.themeablebehavior import ThemeableBehavior

Builder.load_string(
"""
<NeuCard>:
    canvas.before:
        Clear
        Color:
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
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        Rectangle:
            size:self.size
            pos:self.pos
            #radius:self.radius,self.radius,self.radius,self.radius
            texture:self.border_texture if self.elevation and self.elevation < 0 else None
        Color:
    size_hint:None,None
    size:200,200
<NeuCardRounded>:
    canvas.before:
        Clear
        Color:
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
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius,self.radius,self.radius,self.radius
            texture:self.border_texture if self.elevation and self.elevation < 0 else None
        Color:
    size_hint:None,None
    size:200,200 
<NeuCardCircular>:
    canvas.before:
        Clear
        Color:
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
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        Ellipse:
            size:self.size
            pos:self.pos
            texture:self.border_texture if self.elevation and self.elevation < 0 else None
        Color:
    size_hint:None,None
    size:200,200         
"""
)


class NeuCard(BoxLayout,ThemeableBehavior,NeuMorphRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty("20dp")
    """
    Radius of the edges of the card
    attr:`radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'20dp'`.
    """

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.elevation = 2
class NeuCardRounded(BoxLayout,ThemeableBehavior,NeuMorphRoundedRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty("20dp")
    """
    Radius of the edges of the card
    attr:`radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'20dp'`.
    """

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.elevation = 2
class NeuCardCircular(BoxLayout,ThemeableBehavior,NeuMorphCircular):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty("20dp")
    """
    Radius of the edges of the card
    attr:`radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'20dp'`.
    """

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.elevation = 2
