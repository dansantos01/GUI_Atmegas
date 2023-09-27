from kivy.core.window import Window
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from register import *
from functions import *
from Modules.timer_counter_0.timer0_ui import *
from Modules.timer_counter_0.timer0_codegen import *
from Modules.timer_counter_1.timer1_module import *
from Modules.timer_counter_1.timer1_dropdowns import *
from Modules.timer_counter_2.timer2_module import *
from Modules.timer_counter_2.timer2_dropdowns import *
from Modules.analog_to_digital_converter.adc_ui import *
from Modules.analog_to_digital_converter.adc_codegen import *
from Modules.usart_0.usart0_ui import *
from Modules.usart_0.usart0_codegen import *

filename = "REGISTER_CONFIG.h"
path = "output_files/"


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class TestWindow(Screen):

    def get_data(self):
        if timer0_is_open():
            get_timer0()
            with open(path + filename, "w") as f:
                f.write(tccr0a.print_code())
                f.write(tccr0b.print_code())
                f.write(timsk0.print_code())
        else:
            print("Timer 0 is closed")
        if timer2_is_open():
            get_timer2()
            with open(path + filename, "w") as f:
                f.write(tccr2a.print_code())
                f.write(tccr2b.print_code())
                f.write(timsk2.print_code())
                f.write(assr.print_code())
        else:
            print("Timer 2 is closed")
        if timer1_is_open():
            get_timer1()
            with open(path + filename, "w") as f:
                f.write(tccr2a.print_code())
                f.write(tccr2b.print_code())
                f.write(timsk2.print_code())
                f.write(assr.print_code())
        else:
            print("Timer 1 is closed")
        if adc_is_open():
            get_adc()
            with open(path + filename, "w") as f:
                f.write(admux.print_code())
                f.write(adcsra.print_code())
                f.write(adcsrb.print_code())
                f.write(didr0.print_code())
        else:
            print("Timer 1 is closed")


class TestTabs(TabbedPanel):

    mg = GridLayout(cols=2)
    background_color = (0, 0, 0, 1)
    main_t = TabbedPanelItem(text="Main")

    def __init__(self, **kwargs):
        super(TestTabs, self).__init__(**kwargs)
        self.add_widget(self.main_t)
        self.mg.add_widget(Label(text="8-bit Timer/Counter0 with PWM"))
        btn1 = Button(text="TIMER0")
        btn1.bind(on_release=lambda x: timer0_tab_start(self, btn1))
        self.mg.add_widget(btn1)
        self.mg.add_widget(Label(text="16-bit Timer/Counter1 with PWM"))
        btn2 = Button(text="TIMER1")
        btn2.bind(on_release=lambda x: timer1_tab_start(self, btn2))
        self.mg.add_widget(btn2)
        self.mg.add_widget(Label(text="8-bit Timer/Counter2 with PWM\n   and Asynchronous Operation"))
        btn3 = Button(text="TIMER2")
        btn3.bind(on_release=lambda x: timer2_tab_start(self, btn3))
        self.mg.add_widget(btn3)
        self.mg.add_widget(Label(text="Analog-to-Digital Converter"))
        btn4 = Button(text="ADC")
        btn4.bind(on_release=lambda x: adc_tab_start(self, btn3))
        self.mg.add_widget(btn4)
        self.mg.add_widget(Label(text="USART"))
        btn5 = Button(text="ADC")
        btn5.bind(on_release=lambda x: usart0_tab_start(self, btn3))
        self.mg.add_widget(btn5)
        self.main_t.content = self.mg


    def is_it_open(self, value):
        if timer0_is_open():
            print("TIMER 0 is open.")
        else:
            print("TIMER 0 is closed")





class WindowManager(ScreenManager):
    pass


class FileCreationPopup(Popup):

    global filename
    global path

    # FOR FILE CREATION

    def on_release_button(self, path_input):
        if path_input.endswith("/"):
            path = path_input
        elif path_input  == "":
            path = "output_files/"
        else:
            path = path_input + "/"
        f = open(path + filename, "w")
        f.write("NEW FILE")
        f.close()
        print("CONFIG FILE CREATED")
        print(filename)

    def set_screen(self):
        App.get_running_app().root.current = "test"
        App.get_running_app().root.transition.direction = "left"


class FileEditPopup(Popup):

    global filename
    global path

    # GET FILE DIRECTORY FOR EDITING

    def on_release_button(self, path_input):

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
