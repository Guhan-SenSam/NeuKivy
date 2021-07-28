from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ColorProperty, ListProperty, NumericProperty, OptionProperty
from kivy.uix.slider import Slider
from kivymd.uix.selectioncontrol import Thumb
from neukivy.uix.behaviors.neuglow import NeuGlowCircular
from neukivy.uix.behaviors.neumorph import NeuMorphRoundedRectangle
from neukivy.uix.behaviors.themeablebehavior import ThemeableBehavior

Builder.load_string(
    """

<NeuSlider>
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
            radius:self.height/2,self.height/2,self.height/2,self.height/2
            texture:self.border_texture if self.elevation and self.elevation < 0 else None
        Color:
    size_hint:None,None
    size:dp(400),dp(50)
    background_width:0
    cursor_size:0,0
    padding:self.height/2

    NeuThumb:
        canvas.before:
            Color:
            Rectangle:
                size:self.glow_size
                pos:self.glow_pos
                texture:self.glow_texture
        canvas:
            Color:
                rgba:root.thumb_color
            Ellipse:
                size:root.height-root.thumb_padding,root.height-root.thumb_padding
                pos:self.pos
            Color:
        size_hint: None, None
        size:root.height-root.thumb_padding,root.height-root.thumb_padding
        pos:root.value_pos[0]-self.width/2,root.center_y - self.height / 2
        behind_color: root.comp_color[0:3] +[0,] if root.thumb_bg_color==[0,0,0,0] else root.thumb_bg_color
        glow_color: root.thumb_color if root.glow_color==[0,0,0,0] else root.glow_color




"""
)


class NeuSlider(ThemeableBehavior, Slider, NeuMorphRoundedRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    elevation = NumericProperty(3)
    """
    Elevation of the widget.Elevation can be any number between -5 and +5(inclusive).
    Negative elevation will cause the widget to go into the screen whereas positive
    elevation will make it pop from the screen

    This widget has a default elevation of 3
    """

    radius = NumericProperty(0)
    """
    Radius of the slider bar. The value defaults to half the height of the slider bar.

    attr:`radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'20dp'`.
    """

    thumb_color = ColorProperty([0, 0, 0, 0])
    """
    Color of the thumb of the slider
    """

    thumb_bg_color = ColorProperty([0, 0, 0, 0])
    """
    Color of background behind the thumb. This property is needed to
    properly display the glow effect. The property will default to the component
    color. But it can be manually set. If a color is manually set it will create a
    ring of that color around the thumb's glow.

    attr:`thumb_bg_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to the slider's 'comp_color'.
    """

    thumb_padding = NumericProperty()
    """
    The top and bottom padding value for the the thumb. This allows you to inset
    the thumb in the slider. It defaults to zero which means the thumb will be
    as big as the height of the slider.

    attr:`thumb_padding` is an :class:`~kivy.properties.NumericProperty`
    and defaults to the slider's '0'.
    """

    glow_color = ColorProperty([0, 0, 0, 0])
    """
    Color of the glow behind the thumb. Defaults to the thumb's color.

    attr:`glow_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to '[0,0,0,0]'
    """

    glow_radius = NumericProperty(20)
    """
    Radius of the glow behind the thumb.

    attr:`glow_radius` is an :class:`~kivy.properties.NumericProperty`
    and defaults to '20'.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.elevation_set)
        Clock.schedule_once(self.radius_set)

    def elevation_set(self, *args):
        self.elev = self.elevation

    def radius_set(self, *args):
        self.radius = self.height / 2


class NeuThumb(ThemeableBehavior, Thumb, NeuGlowCircular):

    glow_radius = NumericProperty(20)

    glow_color = ColorProperty([0.8, 0.7, 0.5, 1])

    def __init__(self, **kwargs):
        self.elev = self.elevation
        super().__init__(**kwargs)
