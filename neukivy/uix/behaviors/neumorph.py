from kivy.graphics.texture import Texture
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from neukivy.tools.colorconvertor import dec_2_rgb
from PIL import Image, ImageDraw, ImageFilter


class NeuMorphRectangle:
    """
    This class is used to create the neumorphic shadows for widgets. Currently the
    method used is quite slow if there are large number of widgets on screen or if
    a widget is very big. This is especially apparent on android devices.

    This will eventually be fixed in the future, so for now you can create neumorphic ui
    on a pc. Just dont go too crazy unless you want a slideshow as your app.

    To create the neumorphic effect we basically create two shadows for each widget.
    One shadow is darker than the widget color and one is lighter. These two shadows are
    then positioned diagonally opposite of each of other to give the illusion of 3D.

    For positiive elevation we just blit these textures to the canvas.before and then
    draw our widget canvas on top of that.

    But in the case of negative elevation, we cannot just draw the widget's canvas on top
    of our shadows. Instead we dont add any canvas instructions for the widget and just
    create a outline of the widget in pillow. This outline is then used as a third texture,
    Below which we display our dark and light shadows. In this case the shadows are generated
    from outlines of the widgets rather than from a filled shape(as in the case of positive
    elevation.)

    This means as of now negtive elevation widgets will require a border. This behaviour
    will be replaced in the future by a class that can render the shadows such that a border
    is not needed(https://i1.wp.com/css-tricks.com/wp-content/uploads/2020/03/LDgH6Eug.png?fit=1024%2C368&ssl=1).

    The current implementation will then be moved to its own class.
    """

    blank_texture = ObjectProperty(None)
    """
    A blank texture that is used if the elevation is set to 0
    """

    dark_shadow = ObjectProperty(None)
    """
    Object that holds the texture for the dark shadow
    """

    dark_shadow_pos = ListProperty([0, 0])
    """
    A List containing the position of the dark shadow
    """

    dark_shadow_size = ListProperty([0, 0])
    """
    List that contains the size of the dark shadow
    """

    light_shadow = ObjectProperty(None)
    """
    Object that holds the texture of the light shadow
    """

    light_shadow_pos = ListProperty([0, 0])
    """
    A List containing the position of the light shadow
    """
    light_shadow_size = ListProperty([0, 0])
    """
    List that contains the size of the light shadow
    """

    border_texture = ObjectProperty(None)
    """
    Object that holds the texture of the widget;s outline. This only has a texture
    if the elevation is set to negative.
    """

    border_width = NumericProperty(10)
    """
    Width of the outline texture in pixels. It defaults to 10 pixels.This property
    is only used if the widget has negative elevation
    """

    increment = NumericProperty(0)
    """
    Value to be used for blurring the shadow and shifting to them the correct location.
    You can change this value but it may ruin the neumorphic aesthetic of a widget.
    """
    elev = NumericProperty(0)
    """
    Elevation of the widget. This can be any value from -5 to 5 including both -5 and 5.
    It is possible to calculate shadows for other elevations but the neumorphic effect breaks
    down at values higher than this. It is suggested to keep the elevation of a widget between
    1 and 3 or between -4 to -2 for the best effect.
    """

    elevation_data = {
        -1: 10,
        -2: 20,
        -3: 30,
        -4: 40,
        -5: 50,
        0: 0,
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
    }

    pixel_depth = NumericProperty(0)
    """
    Internal property that is used to calculate how far shadows are shifted.
    You can change this value but it may cause the neumorphic effect to be ruined
    """

    def __init__(self, *args, **kwargs):
        super(NeuMorphRectangle, self).__init__(*args, **kwargs)
        self.blank_texture = Texture.create(size=self.size, colorfmt="rgba")
        self._create_shadow()

    def _create_shadow(self, *args):
        if self.pixel_depth == 0:
            self.dark_shadow = self.blank_texture
            self.light_shadow = self.blank_texture
            return
        if self.elev > 0:
            self.increment = self.pixel_depth / 2.5
            # Create dark_shadow
            self.dark_shadow = self._outer_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.dark_color)
            )
            self.dark_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.dark_shadow_pos = (
                self.x - self.increment,
                self.y - self.pixel_depth / 2 - self.increment,
            )
            # Create light shadow
            self.light_shadow = self._outer_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.light_color)
            )
            self.light_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.light_shadow_pos = (
                self.x - self.pixel_depth / 2 - self.increment,
                self.y - self.increment,
            )
        else:
            self.increment = self.pixel_depth / 2.5
            # Create widget outline
            self.border_texture = self._widget_outline(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.comp_color)
            )
            # Create dark_shadow
            self.dark_shadow = self._inner_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.dark_color)
            )
            self.dark_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.dark_shadow_pos = (
                self.x - self.pixel_depth / 2 + self.increment / 2,
                self.y - self.pixel_depth / 2 - self.increment / 2,
            )
            # Create light shadow
            self.light_shadow = self._inner_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.light_color)
            )
            self.light_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.light_shadow_pos = (
                self.x - self.pixel_depth / 2 - self.increment / 2,
                self.y - self.pixel_depth / 2 + self.increment / 2,
            )

    def _outer_shadow_gen(self, size_x, size_y, pixel_depth, color):
        # Create blank image
        blank_x_size = int(size_x + pixel_depth)
        blank_y_size = int(size_y + pixel_depth)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=(tuple(dec_2_rgb(self.theme_manager._bg_color_noalp))),
        )
        # Convert to drawable image
        blank_draw = ImageDraw.Draw(shadow)
        x0, y0 = (blank_x_size - size_x) / 2.0, (blank_y_size - size_y) / 2.0
        x1, y1 = x0 + size_x, y0 + size_y
        blank_draw.rectangle(
            [(x0, y0), (x1, y1)],
            fill=tuple(color),
        )
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.increment))
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def _inner_shadow_gen(self, size_x, size_y, pixel_depth, color):
        # Create blank Image
        blank_x_size = int(size_x + pixel_depth)
        blank_y_size = int(size_y + pixel_depth)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=tuple(dec_2_rgb(self.theme_manager._bg_color_noalp)),
        )
        # Conver to drawable
        blank_draw = ImageDraw.Draw(shadow)
        # Calculate size for rectangle
        x0, y0 = (blank_x_size - size_x) / 2.0, (blank_y_size - size_y) / 2.0
        x1, y1 = size_x + self.increment, size_y + self.increment
        blank_draw.rectangle(
            [(x0, y0), (x1, y1)],
            outline=tuple(color),
            width=(int(self.increment)),
        )
        # add filter and blit to texture
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.increment / 2))
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    # Used to generate outline of widget
    def _widget_outline(self, size_x, size_y, pixel_depth, color):
        # Create blank Image
        outline = Image.new(
            "RGBA",
            (size_x, size_y),
            color=tuple(dec_2_rgb(self.theme_manager._bg_color_noalp)),
        )
        blank_draw = ImageDraw.Draw(outline)
        x0, y0 = 0, 0
        x1, y1 = x0 + size_x, y0 + size_y
        blank_draw.rectangle(
            [(x0, y0), (x1, y1)],
            outline=tuple(color),
            width=self.border_width,
        )
        texture = Texture.create(size=(size_x, size_y), colorfmt="rgba")
        texture.blit_buffer(outline.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def on_size(self, *args, **kwargs):
        self._create_shadow()

    def on_pos(self, *args, **kwargs):
        self._create_shadow()

    def on_elevation(self, instance, value):
        if abs(value) > 5:
            raise ValueError("Elevation must be between 5 and -5(inclusive)")
        self.pixel_depth = self.elevation_to_pixels(value)
        self._create_shadow()

    def elevation_to_pixels(self, elevation):
        return self.elevation_data[elevation]


class NeuMorphRoundedRectangle:
    """
    Creates rounded recatangular shadows


    This class is used to create the neumorphic shadows for widgets. Currently the
    method used is quite slow if there are large number of widgets on screen or if
    a widget is very big. This is especially apparent on android devices.

    This will eventually be fixed in the future, so for now you can create neumorphic ui
    on a pc. Just dont go too crazy unless you want a slideshow as your app.

    To create the neumorphic effect we basically create two shadows for each widget.
    One shadow is darker than the widget color and one is lighter. These two shadows are
    then positioned diagonally opposite of each of other to give the illusion of 3D.

    For positiive elevation we just blit these textures to the canvas.before and then
    draw our widget canvas on top of that.

    But in the case of negative elevation, we cannot just draw the widget's canvas on top
    of our shadows. Instead we dont add any canvas instructions for the widget and just
    create a outline of the widget in pillow. This outline is then used as a third texture,
    Below which we display our dark and light shadows. In this case the shadows are generated
    from outlines of the widgets rather than from a filled shape(as in the case of positive
    elevation.)

    This means as of now negtive elevation widgets will require a border. This behaviour
    will be replaced in the future by a class that can render the shadows such that a border
    is not needed(https://i1.wp.com/css-tricks.com/wp-content/uploads/2020/03/LDgH6Eug.png?fit=1024%2C368&ssl=1).

    The current implementation will then be moved to its own class.
    """

    blank_texture = ObjectProperty(None)
    """
    A blank texture that is used if the elevation is set to 0
    """

    dark_shadow = ObjectProperty(None)
    """
    Object that holds the texture for the dark shadow
    """

    dark_shadow_pos = ListProperty([0, 0])
    """
    A List containing the position of the dark shadow
    """

    dark_shadow_size = ListProperty([0, 0])
    """
    List that contains the size of the dark shadow
    """

    light_shadow = ObjectProperty(None)
    """
    Object that holds the texture of the light shadow
    """

    light_shadow_pos = ListProperty([0, 0])
    """
    A List containing the position of the light shadow
    """
    light_shadow_size = ListProperty([0, 0])
    """
    List that contains the size of the light shadow
    """

    border_texture = ObjectProperty(None)
    """
    Object that holds the texture of the widget;s outline. This only has a texture
    if the elevation is set to negative.
    """

    border_width = NumericProperty(10)
    """
    Width of the outline texture in pixels. It defaults to 10 pixels.This property
    is only used if the widget has negative elevation
    """

    increment = NumericProperty(0)
    """
    Value to be used for blurring the shadow and shifting to them the correct location.
    You can change this value but it may ruin the neumorphic aesthetic of a widget.
    """
    elev = NumericProperty(None)
    """
    Elevation of the widget. This can be any value from -5 to 5 including both -5 and 5.
    It is possible to calculate shadows for other elevations but the neumorphic effect breaks
    down at values higher than this. It is suggested to keep the elevation of a widget between
    1 and 3 or between -4 to -2 for the best effect.
    """

    elevation_data = {
        -1: 10,
        -2: 20,
        -3: 30,
        -4: 40,
        -5: 50,
        0: 0,
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
    }

    pixel_depth = NumericProperty(0)
    """
    Internal property that is used to calculate how far shadows are shifted.
    You can change this value but it may cause the neumorphic effect to be ruined
    """

    def __init__(self, *args, **kwargs):
        super(NeuMorphRoundedRectangle, self).__init__(*args, **kwargs)
        self.blank_texture = Texture.create(size=self.size, colorfmt="rgba")
        self._create_shadow()

    def _create_shadow(self, *args):
        if self.pixel_depth == 0:
            self.dark_shadow = self.blank_texture
            self.light_shadow = self.blank_texture
            return
        if self.elev > 0:
            self.increment = self.pixel_depth / 2.5
            # Create dark_shadow
            self.dark_shadow = self._outer_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.dark_color)
            )
            self.dark_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.dark_shadow_pos = (
                self.x - self.increment,
                self.y - self.pixel_depth / 2 - self.increment,
            )
            # Create light shadow
            self.light_shadow = self._outer_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.light_color)
            )
            self.light_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.light_shadow_pos = (
                self.x - self.pixel_depth / 2 - self.increment,
                self.y - self.increment,
            )
        else:
            self.increment = self.pixel_depth / 2.5
            # Create widget outline
            self.border_texture = self._widget_outline(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.comp_color)
            )
            # Create dark_shadow
            self.dark_shadow = self._inner_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.dark_color)
            )
            self.dark_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.dark_shadow_pos = (
                self.x - self.pixel_depth / 2 + self.increment / 2,
                self.y - self.pixel_depth / 2 - self.increment / 2,
            )
            # Create light shadow
            self.light_shadow = self._inner_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.light_color)
            )
            self.light_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.light_shadow_pos = (
                self.x - self.pixel_depth / 2 - self.increment / 2,
                self.y - self.pixel_depth / 2 + self.increment / 2,
            )

    def _outer_shadow_gen(self, size_x, size_y, pixel_depth, color):
        # Create blank image
        blank_x_size = int(size_x + pixel_depth)
        blank_y_size = int(size_y + pixel_depth)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=(tuple(dec_2_rgb(self.theme_manager._bg_color_noalp))),
        )
        # Convert to drawable image
        blank_draw = ImageDraw.Draw(shadow)
        x0, y0 = (blank_x_size - size_x) / 2.0, (blank_y_size - size_y) / 2.0
        x1, y1 = x0 + size_x, y0 + size_y
        blank_draw.rounded_rectangle(
            [(x0, y0), (x1, y1)],
            radius=self.radius,
            fill=tuple(color),
        )
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.increment))
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def _inner_shadow_gen(self, size_x, size_y, pixel_depth, color):
        # Create blank Image
        blank_x_size = int(size_x + pixel_depth)
        blank_y_size = int(size_y + pixel_depth)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=tuple(dec_2_rgb(self.theme_manager._bg_color_noalp)),
        )
        # Conver to drawable
        blank_draw = ImageDraw.Draw(shadow)
        # Calculate size for rectangle
        x0, y0 = (blank_x_size - size_x) / 2.0, (blank_y_size - size_y) / 2.0
        x1, y1 = size_x + self.increment, size_y + self.increment
        blank_draw.rounded_rectangle(
            [(x0, y0), (x1, y1)],
            radius=self.radius,
            outline=tuple(color),
            width=(int(self.increment)),
        )
        # add filter and blit to texture
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.increment / 2))
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    # Used to generate outline of widget
    def _widget_outline(self, size_x, size_y, pixel_depth, color):
        # Create blank Image
        outline = Image.new(
            "RGBA",
            (size_x, size_y),
            color=tuple(dec_2_rgb(self.theme_manager._bg_color_noalp)),
        )
        blank_draw = ImageDraw.Draw(outline)
        x0, y0 = 0, 0
        x1, y1 = x0 + size_x, y0 + size_y
        blank_draw.rounded_rectangle(
            [(x0, y0), (x1, y1)],
            radius=self.radius,
            outline=tuple(color),
            width=self.border_width,
        )
        texture = Texture.create(size=(size_x, size_y), colorfmt="rgba")
        texture.blit_buffer(outline.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def on_size(self, *args, **kwargs):
        self._create_shadow()

    def on_pos(self, *args, **kwargs):
        self._create_shadow()

    def on_elev(self, instance, value):
        if abs(value) > 5:
            raise ValueError("Elevation must be between 5 and -5(inclusive)")
        self.pixel_depth = self.elevation_to_pixels(value)
        self._create_shadow()

    def elevation_to_pixels(self, elevation):
        return self.elevation_data[elevation]


class NeuMorphCircular:
    """
    Creates Circular shadows


    This class is used to create the neumorphic shadows for widgets. Currently the
    method used is quite slow if there are large number of widgets on screen or if
    a widget is very big. This is especially apparent on android devices.

    This will eventually be fixed in the future, so for now you can create neumorphic ui
    on a pc. Just dont go too crazy unless you want a slideshow as your app.

    To create the neumorphic effect we basically create two shadows for each widget.
    One shadow is darker than the widget color and one is lighter. These two shadows are
    then positioned diagonally opposite of each of other to give the illusion of 3D.

    For positiive elevation we just blit these textures to the canvas.before and then
    draw our widget canvas on top of that.

    But in the case of negative elevation, we cannot just draw the widget's canvas on top
    of our shadows. Instead we dont add any canvas instructions for the widget and just
    create a outline of the widget in pillow. This outline is then used as a third texture,
    Below which we display our dark and light shadows. In this case the shadows are generated
    from outlines of the widgets rather than from a filled shape(as in the case of positive
    elevation.)

    This means as of now negtive elevation widgets will require a border. This behaviour
    will be replaced in the future by a class that can render the shadows such that a border
    is not needed(https://i1.wp.com/css-tricks.com/wp-content/uploads/2020/03/LDgH6Eug.png?fit=1024%2C368&ssl=1).

    The current implementation will then be moved to its own class.
    """

    blank_texture = ObjectProperty(None)
    """
    A blank texture that is used if the elevation is set to 0
    """

    dark_shadow = ObjectProperty(None)
    """
    Object that holds the texture for the dark shadow
    """

    dark_shadow_pos = ListProperty([0, 0])
    """
    A List containing the position of the dark shadow
    """

    dark_shadow_size = ListProperty([0, 0])
    """
    List that contains the size of the dark shadow
    """

    light_shadow = ObjectProperty(None)
    """
    Object that holds the texture of the light shadow
    """

    light_shadow_pos = ListProperty([0, 0])
    """
    A List containing the position of the light shadow
    """
    light_shadow_size = ListProperty([0, 0])
    """
    List that contains the size of the light shadow
    """

    border_texture = ObjectProperty(None)
    """
    Object that holds the texture of the widget;s outline. This only has a texture
    if the elevation is set to negative.
    """

    border_width = NumericProperty(10)
    """
    Width of the outline texture in pixels. It defaults to 10 pixels.This property
    is only used if the widget has negative elevation
    """

    increment = NumericProperty(0)
    """
    Value to be used for blurring the shadow and shifting to them the correct location.
    You can change this value but it may ruin the neumorphic aesthetic of a widget.
    """
    elev = NumericProperty(None)
    """
    Elevation of the widget. This can be any value from -5 to 5 including both -5 and 5.
    It is possible to calculate shadows for other elevations but the neumorphic effect breaks
    down at values higher than this. It is suggested to keep the elevation of a widget between
    1 and 3 or between -4 to -2 for the best effect.
    """

    elevation_data = {
        -1: 10,
        -2: 20,
        -3: 30,
        -4: 40,
        -5: 50,
        0: 0,
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
    }

    pixel_depth = NumericProperty(0)
    """
    Internal property that is used to calculate how far shadows are shifted.
    You can change this value but it may cause the neumorphic effect to be ruined
    """

    def __init__(self, *args, **kwargs):
        super(NeuMorphCircular, self).__init__(*args, **kwargs)
        self.blank_texture = Texture.create(size=self.size, colorfmt="rgba")
        self._create_shadow()

    def _create_shadow(self, *args):
        if self.pixel_depth == 0:
            self.dark_shadow = self.blank_texture
            self.light_shadow = self.blank_texture
            return
        if self.elev > 0:
            self.increment = self.pixel_depth / 2.5
            # Create dark_shadow
            self.dark_shadow = self._outer_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.dark_color)
            )
            self.dark_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.dark_shadow_pos = (
                self.x - self.increment,
                self.y - self.pixel_depth / 2 - self.increment,
            )
            # Create light shadow
            self.light_shadow = self._outer_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.light_color)
            )
            self.light_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.light_shadow_pos = (
                self.x - self.pixel_depth / 2 - self.increment,
                self.y - self.increment,
            )
        else:
            self.increment = self.pixel_depth / 2.5
            # Create widget outline
            self.border_texture = self._widget_outline(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.comp_color)
            )
            # Create dark_shadow
            self.dark_shadow = self._inner_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.dark_color)
            )
            self.dark_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.dark_shadow_pos = (
                self.x - self.pixel_depth / 2 + self.increment / 2,
                self.y - self.pixel_depth / 2 - self.increment / 2,
            )
            # Create light shadow
            self.light_shadow = self._inner_shadow_gen(
                self.width, self.height, self.pixel_depth, dec_2_rgb(self.light_color)
            )
            self.light_shadow_size = (
                self.width + self.pixel_depth,
                self.height + self.pixel_depth,
            )
            self.light_shadow_pos = (
                self.x - self.pixel_depth / 2 - self.increment / 2,
                self.y - self.pixel_depth / 2 + self.increment / 2,
            )

    def _outer_shadow_gen(self, size_x, size_y, pixel_depth, color):
        # Create blank image
        blank_x_size = int(size_x + pixel_depth)
        blank_y_size = int(size_y + pixel_depth)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=(tuple(dec_2_rgb(self.theme_manager._bg_color_noalp))),
        )
        # Convert to drawable image
        blank_draw = ImageDraw.Draw(shadow)
        x0, y0 = (blank_x_size - size_x) / 2.0, (blank_y_size - size_y) / 2.0
        x1, y1 = x0 + size_x, y0 + size_y
        blank_draw.ellipse(
            [(x0, y0), (x1, y1)],
            fill=tuple(color),
        )
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.increment))
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def _inner_shadow_gen(self, size_x, size_y, pixel_depth, color):
        # Create blank Image
        blank_x_size = int(size_x + pixel_depth)
        blank_y_size = int(size_y + pixel_depth)
        shadow = Image.new(
            "RGBA",
            (blank_x_size, blank_y_size),
            color=tuple(dec_2_rgb(self.theme_manager._bg_color_noalp)),
        )
        # Conver to drawable
        blank_draw = ImageDraw.Draw(shadow)
        # Calculate size for rectangle
        x0, y0 = (blank_x_size - size_x) / 2.0, (blank_y_size - size_y) / 2.0
        x1, y1 = size_x + self.increment, size_y + self.increment
        blank_draw.ellipse(
            [(x0, y0), (x1, y1)],
            outline=tuple(color),
            width=(int(self.increment)),
        )
        # add filter and blit to texture
        shadow = shadow.filter(ImageFilter.GaussianBlur(self.increment / 2))
        texture = Texture.create(size=(blank_x_size, blank_y_size), colorfmt="rgba")
        texture.blit_buffer(shadow.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    # Used to generate outline of widget
    def _widget_outline(self, size_x, size_y, pixel_depth, color):
        # Create blank Image
        outline = Image.new(
            "RGBA",
            (size_x, size_y),
            color=tuple(dec_2_rgb(self.theme_manager._bg_color_noalp)),
        )
        blank_draw = ImageDraw.Draw(outline)
        x0, y0 = 0, 0
        x1, y1 = x0 + size_x, y0 + size_y
        blank_draw.ellipse(
            [(x0, y0), (x1, y1)],
            outline=tuple(color),
            width=self.border_width,
        )
        texture = Texture.create(size=(size_x, size_y), colorfmt="rgba")
        texture.blit_buffer(outline.tobytes(), colorfmt="rgba", bufferfmt="ubyte")
        return texture

    def on_size(self, *args, **kwargs):
        self._create_shadow()

    def on_pos(self, *args, **kwargs):
        self._create_shadow()

    def on_elevation(self, instance, value):
        if abs(value) > 5:
            raise ValueError("Elevation must be between 5 and -5(inclusive)")
        self.pixel_depth = self.elevation_to_pixels(value)
        self._create_shadow()

    def elevation_to_pixels(self, elevation):
        return self.elevation_data[elevation]
