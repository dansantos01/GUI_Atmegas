from kivy.uix.screenmanager import ScreenManager, Screen
from functions import *


class Atmega328pTabWindow(Screen):

    def get_data(self):
        print("No Data")


class Atmega328pTab(TabbedPanel):

    mg = GridLayout(cols=2)
    background_color = (0, 0, 0, 1)
    main_t = TabbedPanelItem(text="Atmega328p")

    def __init__(self, **kwargs):
        super(Atmega328pTab, self).__init__(**kwargs)
        self.add_widget(self.main_t)
        self.add_widget(Label(text="Hello World"))
