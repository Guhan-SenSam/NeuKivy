from neukivy.app import NeuApp
from kivy.lang import Builder
from neukivy.uix.button import NeuButton

kv_string = '''
Screen:
    canvas:
        Color:
            rgba:(50/255,50/255,50/255,1)
        Rectangle:
            size:self.size
            pos:self.pos

    NeuButton:
        pos_hint:{'center_x':.5,'center_y':.5}
        comp_color:0.196,0.196,0.196,1
        radius:20
        up_elevation:3
        down_elevation:1



'''


class MainApp(NeuApp):
    def build(self):
        kv = Builder.load_string(kv_string)
        self.theme_manager.bg_color = (.2,.2,.2,0)
        self.theme_manager.light_color = (.3,.3,.3,1)
        self.theme_manager.dark_color = (.07,.07,.07,1)
        return kv


if __name__ == '__main__':
    MainApp().run()
