from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from neukivy.icon_definitions import icons_dict
from neukivy.uix.behaviors.neubuttonbehavior import NeuButtonBehavior
from neukivy.uix.behaviors.neumorph import (
    NeuMorphCircular,
    NeuMorphRectangle,
    NeuMorphRoundedRectangle,
)
from neukivy.uix.behaviors.themeablebehavior import ThemeableBehavior

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

<NeuIconTextBaseButton>:
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
    width:self.minimum_width
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
        pos_hint:{'center_x':.5,'center_y':.5}
    Label:
        id:icon
        text:root._icon_text
        size:self.texture_size
        size_hint:None,None
        font_size:root.icon_font_size
        italic:root.italic
        color:root.text_color if root.icon_color == [0,0,0,0] else root.icon_color
        markup: True
        disabled: root.disabled
        font_name: root.icon_font_name if root.font_name else 'Icons'
        pos_hint:{'center_x':.5,'center_y':.5}

<NeuButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elev and self.elev < 0 else self.comp_color
        Rectangle:
            size:self.size
            pos:self.pos
            texture:self.border_texture if self.elev and self.elev < 0 else None
        Color:
    size:100,100
    size_hint:None,None

<NeuRoundedButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elev and self.elev < 0 else self.comp_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius,self.radius,self.radius,self.radius
            texture:self.border_texture if self.elev and self.elev < 0 else None
        Color:

<NeuCircularButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elev and self.elev < 0 else self.comp_color
        Ellipse:
            size:self.radius,self.radius
            pos:self.pos
            texture:self.border_texture if self.elev and self.elev < 0 else None
        Color:
    size:self.radius,self.radius

<NeuIconButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elev and self.elev < 0 else self.comp_color
        Rectangle:
            size:self.size
            pos:self.pos
            texture:self.border_texture if self.elev and self.elev < 0 else None
        Color:

<NeuRoundedIconButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elev and self.elev < 0 else self.comp_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius,self.radius,self.radius,self.radius
            texture:self.border_texture if self.elev and self.elev < 0 else None
        Color:

<NeuCircularIconButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elev and self.elev < 0 else self.comp_color
        Ellipse:
            size:self.radius,self.radius
            pos:self.pos
            texture:self.border_texture if self.elev and self.elev < 0 else None
        Color:
    size:self.radius,self.radius

<NeuIconTextButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elev and self.elev < 0 else self.comp_color
        Rectangle:
            size:self.size
            pos:self.pos
            texture:self.border_texture if self.elev and self.elev < 0 else None
        Color:

<NeuRoundedIconTextButton>:
    canvas.before:
        Color:
            rgba:(1,1,1,1) if self.elev and self.elev < 0 else self.comp_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:self.radius,self.radius,self.radius,self.radius
            texture:self.border_texture if self.elev and self.elev < 0 else None
        Color:


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


class NeuIconTextBaseButton(NeuButtonBehavior, BoxLayout, ThemeableBehavior):

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

    icon_font_size = NumericProperty("14sp")
    """
    Size of font used fpr the icon

    attr:`icon_font_size` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `"14sp"`.
    """

    disabled = BooleanProperty(False)
    """
    Whether the button is disabled or not. When a button is disabled its text color
    is greyed out and it is not longer clickable

    attr:`disabled` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    font_name = StringProperty(default="NunitoSemiBold")
    """
    Name of the font face to be used

    attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'NunitoSemiBold'`.
    """

    icon_font_name = StringProperty("Icons")
    """
    Name of the font used for icon definitions.

    attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"Icons"`.
    """

    text_color = ColorProperty([0, 0, 0, 0])
    """
    Text color

    attr:`text_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0,0,0,0]`.
    """

    icon_color = ColorProperty([0, 0, 0, 0])
    """
    Icon color

    attr:`icon_color` is an :class:`~kivy.properties.ColorProperty`
    and defaults to `[0,0,0,0]`.
    """

    italic = BooleanProperty(False)
    """
    If set tot true the text will be rendered with its italic font type. WIll only
    work if the given font name has an itallic type.

    attr:`italic` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    padding = ListProperty([10, 10, 10, 10])
    """
    Padding around the text and icon of the button

    attr:`padding` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `[10, 10, 10, 10]`.
    """

    spacing = NumericProperty("10dp")
    """
    Spacing between the icon and button

    attr:`spacing` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `"10dp"`.
    """

    icon_pos = OptionProperty("Right", options=["Right", "Left"])

    def on_icon(self, *args):
        if self.icon_font_name == "Icons":
            try:
                self._icon_text = icons_dict[self.icon]
            except KeyError:
                raise KeyError("The icon '" + self.icon + "' does not exist")

    def on_icon_pos(self, *args):
        if self.icon_pos == "Right":
            label = self.ids.label
            icon = self.ids.icon
            self.clear_widgets()
            self.add_widget(label)
            self.add_widget(icon)
        else:
            label = self.ids.label
            icon = self.ids.icon
            self.clear_widgets()
            self.add_widget(icon)
            self.add_widget(label)


class NeuButton(NeuBaseButton, NeuMorphRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])


class NeuRoundedButton(NeuBaseButton, NeuMorphRoundedRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty(20)
    """
    Radius of the corners
    """


class NeuCircularButton(NeuBaseButton, NeuMorphCircular):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty(100)
    """
    Radius of the button
    """

    def on_size(self, *args):
        self.size = self.radius, self.radius


class NeuIconButton(NeuBaseButton, NeuMorphRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    font_name = StringProperty("Icons")
    """
    Name of the font used for icon definitions.

    attr:`font_name` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"Icons"`.
    """

    icon = StringProperty("android")
    """
    Icon used in the button

    attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"android"`.
    """

    def on_icon(self, *args):
        if self.font_name == "Icons":
            try:
                self.text = icons_dict[self.icon]
            except KeyError:
                raise KeyError("The icon '" + self.icon + "' does not exist")


class NeuRoundedIconButton(NeuBaseButton, NeuMorphRoundedRectangle):

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

    icon = StringProperty("android")
    """
    Icon used in the button

    attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"android"`.
    """

    def on_icon(self, *args):
        if self.font_name == "Icons":
            try:
                self.text = icons_dict[self.icon]
            except KeyError:
                raise KeyError("The icon '" + self.icon + "' does not exist")


class NeuCircularIconButton(NeuBaseButton, NeuMorphCircular):

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

    icon = StringProperty("android")
    """
    Icon used in the button

    attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"android"`.
    """

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    icon = StringProperty("android")

    text = StringProperty()

    def on_icon(self, *args):
        if self.font_name == "Icons":
            try:
                self.text = icons_dict[self.icon]
            except KeyError:
                raise KeyError("The icon '" + self.icon + "' does not exist")

    def on_size(self, *args):
        self.size = self.radius, self.radius


class NeuIconTextButton(NeuIconTextBaseButton, NeuMorphRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    icon = StringProperty("android")
    """
    Icon used in the button

    attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"android"`.
    """

    _icon_text = StringProperty()


class NeuRoundedIconTextButton(NeuIconTextBaseButton, NeuMorphRoundedRectangle):

    comp_color = ListProperty([0, 0, 0, 0])

    dark_color = ListProperty([0, 0, 0, 0])

    light_color = ListProperty([0, 0, 0, 0])

    radius = NumericProperty(20)
    """
    Radius of the corners
    """

    icon = StringProperty("android")
    """
    Icon used in the button

    attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `"android"`.
    """

    _icon_text = StringProperty()
