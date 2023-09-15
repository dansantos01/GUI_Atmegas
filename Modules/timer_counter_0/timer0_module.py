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
    grid = GridLayout(cols=2)
    create_spinner_ui("Wave Generation Mode", spn_TIMER0_WGM, grid)
    create_spinner_ui("Wave Generation Mode Options", spn_TIMER0_WGM_OPT, grid)
    create_spinner_ui("Compare Output Mode A", spn_TIMER0_COM_A, grid)
    create_spinner_ui("Compare Output Mode B", spn_TIMER0_COM_B, grid)
    create_spinner_ui("Clock", spn_TIMER0_CLOCK, grid)
    create_label(grid, "Timer/Counter Output Compare Match A Interrupt Enable")
    switch = Switch()
    switch.bind(active=int_cma_callback)
    grid.add_widget(switch)
    create_label(grid, "Timer/Counter Output Compare Match B Interrupt Enable")
    switch1 = Switch()
    switch1.bind(active=int_cmb_callback)
    grid.add_widget(switch1)
    create_label(grid, "Timer/Counter0 Overflow Interrupt Enable")
    switch2 = Switch()
    switch2.bind(active=int_ovf_callback)
    grid.add_widget(switch2)

    # Put Content in Tab and add Tab to be available
    timer0_t.content = grid
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
    clk0_bit(get_value(TIMER0_CLOCK, spn_TIMER0_CLOCK.text))

    if TIMER0_WGM["normal"] == spn_TIMER0_WGM.text:
        com0a_bit(get_value(TIMER0_COM_NORMAL, spn_TIMER0_COM_A.text))
        com0b_bit(get_value(TIMER0_COM_NORMAL, spn_TIMER0_COM_B.text))
        wgm0_bit(get_value(TIMER0_WGM_NORMAL, spn_TIMER0_WGM_OPT.text))
    elif TIMER0_WGM["pwm"] == spn_TIMER0_WGM.text:
        com0a_bit(get_value(TIMER0_COM_PWM, spn_TIMER0_COM_A.text))
        com0b_bit(get_value(TIMER0_COM_PWM, spn_TIMER0_COM_B.text))
        wgm0_bit(get_value(TIMER0_WGM_PWM, spn_TIMER0_WGM_OPT.text))
    elif TIMER0_WGM["fastpwm"] == spn_TIMER0_WGM.text:
        com0a_bit(get_value(TIMER0_COM_FASTPWM, spn_TIMER0_COM_A.text))
        com0b_bit(get_value(TIMER0_COM_FASTPWM, spn_TIMER0_COM_B.text))
        wgm0_bit(get_value(TIMER0_WGM_FASTPWM, spn_TIMER0_WGM_OPT.text))

    timer0_int_bits()

    print(tccr0a.print_code())
    print(tccr0b.print_code())
    print(timsk0.print_code())
