from register import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanel
from functions import *
from Modules.timer_counter_0.timer0_dropdowns import *

### Variables

# Registers
tccr0a = Register("TCCR0A", "00000000")
tccr0b = Register("TCCR0B", "00000000")
timsk0 = Register("TIMSK0", "00000000")

# Bits

# Interrupt flags
ocie0a = False
ocie0b = False
toie0 = False

# Open or Not
timer0_OPEN = False


# Dropdown boxes




### METHODS


def timer0_is_open():
    return timer0_OPEN


# TAB CREATION


def timer0_tab_start(self, btn):
    timer0_t = TabbedPanelItem(text="TIMER0")
    tc = GridLayout(cols=2)
    label = Label(text=f"Mode of Operation:", size_hint_x=.3)
    tc.add_widget(label)
    WGM_spn.bind(text=update_spinner)
    tc.add_widget(WGM_spn)
    tc.add_widget(Label(text="Compare Output Mode A:", size_hint_x=.3))
    tc.add_widget(COM0A_spn)
    tc.add_widget(Label(text="Compare Output Mode B:", size_hint_x=.3))
    tc.add_widget(COM0B_spn)
    # tc.add_widget(Button(text="HAYAA"))
    tc.add_widget(Label(text="Prescaler", size_hint_x=.3))
    tc.add_widget(PRE0_spn)
    tc.add_widget(Label(text="Timer/Counter Output Compare Match A Interrupt Enable"))
    switch = Switch()
    switch.bind(active=int_cma_callback)
    tc.add_widget(switch)
    tc.add_widget(Label(text="Timer/Counter Output Compare Match B Interrupt Enable"))
    switch1 = Switch()
    switch1.bind(active=int_cmb_callback)
    tc.add_widget(switch1)
    tc.add_widget(Label(text="Timer/Counter0 Overflow Interrupt Enable"))
    switch2 = Switch()
    switch2.bind(active=int_ovf_callback)
    tc.add_widget(switch2)

    # Put Content in Tab and add Tab to be available
    timer0_t.content = tc
    self.add_widget(timer0_t)
    global timer0_OPEN
    timer0_OPEN = True


def int_cma_callback(instance, value):
    global ocie0a
    ocie0a = value


def int_cmb_callback(instance, value):
    global ocie0b
    ocie0b = value


def int_ovf_callback(instance, value):
    global toie0
    toie0 = value


def update_spinner(obj, text):
    if TIMER0_mode[1] == text or TIMER0_mode[5] == text:
        COM0A_spn.values = [COM0_menu[2][0], COM0_menu[2][1], COM0_menu[2][2], COM0_menu[2][3]]
        COM0B_spn.values = [COM0_menu[2][0], COM0_menu[2][1], COM0_menu[2][2], COM0_menu[2][3]]
    elif TIMER0_mode[3] == text or TIMER0_mode[7] == text:
        COM0A_spn.values = [COM0_menu[1][0], COM0_menu[1][1], COM0_menu[1][2], COM0_menu[1][3]]
        COM0B_spn.values = [COM0_menu[1][0], COM0_menu[1][1], COM0_menu[1][2], COM0_menu[1][3]]
    else:
        COM0A_spn.values = [COM0_menu[0][0], COM0_menu[0][1], COM0_menu[0][2], COM0_menu[0][3]]
        COM0B_spn.values = [COM0_menu[0][0], COM0_menu[0][1], COM0_menu[0][2], COM0_menu[0][3]]


def clk0_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(3 - len(binary))):
        binary = "0" + binary
    # CS02
    if binary[0] == "1":
        tccr0b.set("2")
    else:
        tccr0b.clear("2")
    # CS01
    if binary[1] == "1":
        tccr0b.set("1")
    else:
        tccr0b.clear("1")
    # CS00
    if binary[2] == "1":
        tccr0b.set("0")
    else:
        tccr0b.clear("0")


def wgm0_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(3 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr0b.set("3")
    if binary[1] == "1":
        tccr0a.set("1")
    if binary[2] == "1":
        tccr0a.set("0")


def com0a_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(2 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr0a.set("7")
    else:
        tccr0a.clear("7")
    if binary[1] == "1":
        tccr0a.set("6")
    else:
        tccr0a.clear("6")


def com0b_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(2 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr0a.set("5")
    else:
        tccr0a.clear("5")
    if binary[1] == "1":
        tccr0a.set("4")
    else:
        tccr0a.clear("4")


def timer0_int_bits():
    global toie0
    global ocie0a
    global ocie0b

    timsk0.set("0") if toie0 else timsk0.clear("0")
    timsk0.set("1") if ocie0a else timsk0.clear("1")
    timsk0.set("2") if ocie0b else timsk0.clear("2")


def get_timer0():
    clk0_bit(get_value(CLK0_sel, PRE0_spn.text))
    wgm = get_value(TIMER0_mode, WGM_spn.text)
    wgm0_bit(wgm)

    if wgm == 3 or wgm == 7:
        com0a_bit(get_value(COM0_fPWM, COM0A_spn.text))
        com0b_bit(get_value(COM0_fPWM, COM0B_spn.text))
    elif wgm == 1 or wgm == 5:
        com0a_bit(get_value(COM0_phPWM, COM0A_spn.text))
        com0b_bit(get_value(COM0_phPWM, COM0B_spn.text))
    else:
        com0a_bit(get_value(COM0_nPWM, COM0A_spn.text))
        com0b_bit(get_value(COM0_nPWM, COM0B_spn.text))

    timer0_int_bits()

    print(tccr0a.print_code())
    print(tccr0b.print_code())
    print(timsk0.print_code())
