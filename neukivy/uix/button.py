from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import (
    ListProperty,
    NumericProperty,
    StringProperty,
    ColorProperty,
    BooleanProperty,
)
from neukivy.uix.behaviors.neumorph import (
    NeuMorphRectangle,
    NeuMorphRoundedRectangle,
    NeuMorphCircular,
)
from neukivy.uix.behaviors.neubuttonbehavior import NeuButtonBehavior
from neukivy.uix.behaviors.iconbehavior import IconBehavior
from neukivy.app import ThemeableBehavior

Builder.load_string(
    """

<NeuBaseButton>:
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
    size:100,100
    size_hint:None,None
    anchor_x:"center"
    anchor_y:"center"
    Label:
        id:label
        text:root.text
        size:self.texture_size
        size_hint:None,None
        font_size:root.font_size
        italic:root.italic
        color:root.text_color
        markup: True
        disabled: root.disabled
        font_name: root.font_name if root.font_name else 'NunitoSemiBold'

<NeuButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        Rectangle:
            size:self.size
            pos:self.pos
            texture:self.outline_texture if self.elevation and self.elevation < 0 else None
        Color:
    size:100,100
    size_hint:None,None

<NeuButtonRounded>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius,self.radius,self.radius,self.radius
            texture:self.outline_texture if self.elevation and self.elevation < 0 else None
        Color:

<NeuButtonCircular>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        Ellipse:
            size:self.radius,self.radius
            pos:self.pos
            texture:self.outline_texture if self.elevation and self.elevation < 0 else None
        Color:
    size:self.radius,self.radius

<NeuIconButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        Rectangle:
            size:self.size
            pos:self.pos
            texture:self.outline_texture if self.elevation and self.elevation < 0 else None
        Color:

<NeuIconButtonRounded>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius,self.radius,self.radius,self.radius
            texture:self.outline_texture if self.elevation and self.elevation < 0 else None
        Color:

<NeuIconButtonCircular>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elevation and self.elevation < 0 else self.comp_color
        Ellipse:
            size:self.radius,self.radius
            pos:self.pos
            texture:self.outline_texture if self.elevation and self.elevation < 0 else None
        Color:
    size:self.radius,self.radius

"""
)


class NeuBaseButton(NeuButtonBehavior, AnchorLayout, ThemeableBehavior):

    text = StringProperty()
    """
    Button text

    attr:`text` is an :class:`~kivy.properties.StringProperty`
    and defaults to `' '`.
    """

    font_size = NumericProperty("14sp")
    """
    Size of font used

    attr:`font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `"14sp"`.
    """

    disabled = BooleanProperty(False)
    """
    Whether the button is disabled or not. When a button is disabled its text color
    is greyed out and it is not longer clickable

    attr:`disabled` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """
    # TODO: Make disabled more promininet and add a disabled color property for the app

    font_name = StringProperty(default="NunitoSemiBold")
    """
    Name of the face to be used

    attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'NunitoSemiBold'`.
    """

    text_color = ColorProperty([0, 0, 0, 0])
    """
    Text color

    attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0,0,0,0]`.
    """

    italic = BooleanProperty(False)
    """
    If set tot true the text will be rendered with its italic font type. WIll only
    work if the given font name has an itallic type.

    attr:`italic` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """


class NeuButton(NeuBaseButton, NeuMorphRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])


class NeuButtonRounded(NeuBaseButton, NeuMorphRoundedRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty(20)
    """
    Radius of the corners
    """


class NeuButtonCircular(NeuBaseButton, NeuMorphCircular):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty(100)
    """
    Radius of the button
    """

    def on_size(self, *args):
        self.size = self.radius, self.radius


class NeuIconButton(NeuBaseButton, NeuMorphRectangle, IconBehavior):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    font_name = StringProperty("Icons")
    """
    Name of the font used for icon definitions.

    attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"Icons"`.
    """


class NeuIconButtonRounded(NeuBaseButton, NeuMorphRoundedRectangle, IconBehavior):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty(20)
    """
    Radius of the corners
    """

    font_name = StringProperty("Icons")
    """
    Name of the font used for icon definitions.

    attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"Icons"`.
    """


class NeuIconButtonCircular(NeuBaseButton, NeuMorphCircular, IconBehavior):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty(100)
    """
    Radius of the button
    """

    font_name = StringProperty("Icons")
    """
    Name of the font used for icon definitions.

    attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"Icons"`.
    """
