import sys
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):

    """
    Template created using official documentation:
    https://kivymd.readthedocs.io/en/latest/getting-started/
    """

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        return MDLabel(text='Hello World',
                       halign='center',
                       theme_font_size='Custom',
                       font_size='70sp')


if __name__ == '__main__':
    MainApp().run()
    sys.exit(0)
