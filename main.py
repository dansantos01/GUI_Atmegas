from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from microcontrollers.Atmega168p.atmega168p import *
from microcontrollers.Atmega328p.atmega328p import *

filename = "REGISTER_CONFIG.h"
path = "output_files/"


class MainWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class FileCreationPopup(Popup):

    # FOR FILE CREATION

    def on_release_button(self, path_input):

        global path
        global filename
        if path_input.endswith("/"):
            path = path_input
        elif path_input == "":
            path = "output_files/"
        else:
            path = path_input + "/"
        f = open(path + filename, "w")
        f.write("NEW FILE")
        f.close()
        print("CONFIG FILE CREATED")
        print(filename)

    def set_screen(self):
        if self.ids.micro_sel.text == 'Atmega168p':
            App.get_running_app().root.current = "168p"
            App.get_running_app().root.transition.direction = "left"
        else:
            App.get_running_app().root.current = "328p"
            App.get_running_app().root.transition.direction = "left"


class FileEditPopup(Popup):

    # GET FILE DIRECTORY FOR EDITING

    def on_release_button(self, path_input):

        global filename
        global path

        if path_input.endswith("/"):
            path = path_input
        f = open(path + filename, "w")
        f.write("NEW FILE")
        f.close()
        print("FILE CREATED")
        print(filename)

    def set_screen(self):
        App.get_running_app().root.current = "test"
        App.get_running_app().root.transition.direction = "left"


kv = Builder.load_file('main_menu.kv')


class MyGUIApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyGUIApp().run()
