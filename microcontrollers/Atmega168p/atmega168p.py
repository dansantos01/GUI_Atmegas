from microcontrollers.Atmega168p.Modules.timer_counter_0.timer0_codegen import *
from microcontrollers.Atmega168p.Modules.timer_counter_1.timer1_codegen import *
from microcontrollers.Atmega168p.Modules.timer_counter_2.timer2_codegen import *
from microcontrollers.Atmega168p.Modules.analog_to_digital_converter.adc_codegen import *
from microcontrollers.Atmega168p.Modules.usart_0.usart0_codegen import *
from kivy.uix.screenmanager import ScreenManager, Screen
from functions import *


class Atmega168pTabWindow(Screen):

    def get_168p_data(self):
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
                f.write(tccr1a.print_code())
                f.write(tccr1b.print_code())
                f.write(timsk1.print_code())
                f.write(tifr1.print_code())
            else:
                print("Timer 1 is closed")
            if adc_is_open():
                get_adc()
                f.write(admux.print_code())
                f.write(adcsra.print_code())
                f.write(adcsrb.print_code())
                f.write(didr0.print_code())
            else:
                print("ADC is closed")
            if usart0_is_open():
                get_usart0()
                f.write(ucsr0a.print_code())
                f.write(ucsr0b.print_code())
                f.write(ucsr0c.print_code())
                f.write(ubrr0h.print_code())
                f.write(ubrr0l.print_code())


class Atmega168pTab(TabbedPanel):

    mg = GridLayout(cols=2)
    background_color = (0, 0, 0, 1)
    main_t = TabbedPanelItem(text="Atmega168p")

    def __init__(self, **kwargs):
        super(Atmega168pTab, self).__init__(**kwargs)
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
        btn4.bind(on_release=lambda x: adc_tab_start(self, btn4))
        self.mg.add_widget(btn4)
        self.mg.add_widget(Label(text="USART"))
        btn5 = Button(text="USART")
        btn5.bind(on_release=lambda x: usart0_tab_start(self, btn5))
        self.mg.add_widget(btn5)
        self.main_t.content = self.mg
