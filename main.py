from kivy.lang.builder import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

Builder.load_file(r"design\button.kv")


class FirstButton(MDRaisedButton):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        button = FirstButton()
        return button


if __name__ == "__main__":
    MainApp().run()
