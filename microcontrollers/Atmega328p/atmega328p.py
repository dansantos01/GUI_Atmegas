from kivy.uix.screenmanager import ScreenManager, Screen
from functions import *
from microcontrollers.Atmega328p.Modules.timer_counter_0.timer0_codegen import *
from microcontrollers.Atmega328p.Modules.timer_counter_1.timer1_codegen import *
from microcontrollers.Atmega328p.Modules.timer_counter_2.timer2_codegen import *


class Atmega328pTabWindow(Screen):

    def get_328p_data(self):
        from main import path
        from main import filename
        with open(path + filename, "w") as f:
            if timer0_is_open():
                get_timer0()
                f.write(tccr0a.print_code())
                f.write(tccr0b.print_code())
                f.write(timsk0.print_code())
            else:
                print("Timer 0 is closed")
            if timer2_is_open():
                get_timer2()
                f.write(tccr2a.print_code())
                f.write(tccr2b.print_code())
                f.write(timsk2.print_code())
                f.write(assr.print_code())
            else:
                print("Timer 2 is closed")
            if timer1_is_open():
                get_timer1()
                f.write(tccr2a.print_code())
                f.write(tccr2b.print_code())
                f.write(timsk2.print_code())
                f.write(assr.print_code())
            else:
                print("Timer 1 is closed")


class Atmega328pTab(TabbedPanel):

    mg = GridLayout(cols=2)
    background_color = (0, 0, 0, 1)
    main_t = TabbedPanelItem(text="Atmega328p")

    def __init__(self, **kwargs):
        super(Atmega328pTab, self).__init__(**kwargs)
        self.add_widget(self.main_t)
        self.add_widget(Label(text="Hello World"))
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
        self.main_t.content = self.mg
