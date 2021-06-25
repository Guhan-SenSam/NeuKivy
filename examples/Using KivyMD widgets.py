from neukivy.app import NeuApp
from kivy.lang import Builder
from kivy.animation import Animation

kv_string = """
Screen:
    canvas:
        Color:
            rgba:app.theme_manager._bg_color_alp
        Rectangle:
            size:self.size
            pos:self.pos

    MDCard:
        md_bg_color:app.theme_manager._bg_color_alp
        elevation:20
        size_hint:None,None
        size:500,200
        pos_hint:{'center_x':.5,'center_y':.5}
        radius:20,20,20,20
        FloatLayout:
            size:self.parent.size
            pos:self.parent.size

            NeuCircularIconButton:
                id:button
                pos_hint:{'center_x':.7,'center_y':.5}
                size:100,100
                icon:'account-alert'
                font_size:'40sp'

            NeuCircularButton:
                pos_hint:{'center_x':.3,'center_y':.5}
                text:'NeuKivy'
                radius:100
                down_elevation:1
                up_elevation:3
                font_size:'20sp'

    MDFloatingActionButton:
        text:'From KivyMD'
        pos_hint:{'center_x':.5,'center_y':.25}
        icon:'plus'
        md_bg_color:self.theme_cls.accent_color

    MDRaisedButton:
        text:'From KivyMD'
        pos_hint:{'center_x':.5,'center_y':.1}
        icon:'plus'
        md_bg_color:self.theme_cls.accent_color



"""


class MainApp(NeuApp):
    def build(self):
        # If set to True this will allow you to load kivymd widgets into NeuKivy
        # Check dosctrings for NeuApp class for more info
        self.use_kivymd = True
        kv = Builder.load_string(kv_string)
        # Set the app colors at start.
        # The bg_color property should not have an alpha value. This is auto computed
        self.theme_manager.bg_color = (0.2, 0.2, 0.2)
        # Set this to a lighter shade of your bg_color
        self.theme_manager.light_color = (0.3, 0.3, 0.3, 1)
        # Set this to a darker shade of your bg_color
        self.theme_manager.dark_color = (0.07, 0.07, 0.07, 1)
        # The text color of your app
        self.theme_manager.text_color = (0.5, 0.4, 0.2, 1)
        # Disabled text color of your app
        self.theme_manager.disabled_text_color = (0.1, 0.1, 0.1, 1)
        return kv


if __name__ == "__main__":
    MainApp().run()
