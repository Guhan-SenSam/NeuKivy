from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from neukivy.app import NeuApp

kv_string = """
Screen:
    canvas:
        Color:
            rgba:app.theme_manager._bg_color_alp
        Rectangle:
            size:self.size
            pos:self.pos
    NeuBanner:
        id:banner
        primary_text:"Hello this is a top banner."
        secondary_text:"This is the text that goes underneath it."
        tertiary_text:"This is the final text."
        over_widget:screen
        elevation:3

        NeuBannerAction:
            MDRaisedButton:
                text:'okay'

        NeuBannerAction:
            MDRaisedButton:
                text:'cancel'

    GridLayout:
        id:screen
        cols:2
        rows:2
        spacing:'40dp'
        padding:'40dp','40dp','40dp','40dp'

        NeuRoundedIconButton:
            icon:'plus'
            size_hint:.5,.5
            on_release:root.ids.banner.show()

        NeuRoundedIconButton:
            icon:'plus'
            size_hint:.5,.5
            on_release:root.ids.banner.show()

        NeuRoundedIconButton:
            icon:'plus'
            size_hint:.5,.5
            on_release:root.ids.banner.show()

        NeuRoundedIconButton:
            icon:'plus'
            size_hint:.5,.5
            on_release:root.ids.banner.show()




"""


class MainApp(NeuApp):
    def build(self):
        self.use_kivymd = True
        kv = Builder.load_string(kv_string)
        self.theme_manager.bg_color = (0.2, 0.2, 0.2)
        self.theme_manager.light_color = (0.3, 0.3, 0.3, 1)
        self.theme_manager.dark_color = (0.07, 0.07, 0.07, 1)
        return kv


Window.size = (360, 640)

if __name__ == "__main__":
    MainApp().run()
