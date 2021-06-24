from kivy.properties import StringProperty;
from neukivy.icon_definitions import icons_dict

class IconBehavior():

    icon = StringProperty('')

    def on_icon(self,*args):
        if self.font_name == 'Icons':
            try:
                self.text = icons_dict[self.icon]
            except KeyError:
                raise KeyError("The icon '"+self.icon+"' does not exist")
