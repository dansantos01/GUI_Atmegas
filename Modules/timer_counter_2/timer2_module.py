from register import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanel
from functions import *
from Modules.timer_counter_2.timer2_dropdowns import *

# Variables

# Registers
tccr2a = Register("TCCR2A", "00000000")
tccr2b = Register("TCCR2B", "00000000")
timsk2 = Register("TIMSK2", "00000000")
assr = Register("ASSR", "00000000")

# Bits

ocie2a = False
ocie2b = False
toie2 = False
exclk = False
as2 = False

# Open or Not

timer2_OPEN = False


def timer2_is_open():
    return timer2_OPEN

# Dropdown boxes

WGM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(TIMER2_mode[0], TIMER2_mode[1], TIMER2_mode[2], TIMER2_mode[3], TIMER2_mode[4], TIMER2_mode[5],
            TIMER2_mode[6], TIMER2_mode[7]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)
COM2A_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM2_menu[1][0], COM2_menu[1][1], COM2_menu[1][2], COM2_menu[1][3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)
COM2B_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM2_menu[1][0], COM2_menu[1][1], COM2_menu[1][2], COM2_menu[1][3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)
PRE2_spn = Spinner(
    text="Choose Prescaler",
    text_autoupdate=True,
    values=(CLK2_sel[0], CLK2_sel[1], CLK2_sel[2], CLK2_sel[3], CLK2_sel[4], CLK2_sel[5], CLK2_sel[6], CLK2_sel[7])
)

# METHODS



# TAB CREATION


def timer2_tab_start(self, btn):
    timer2_t = TabbedPanelItem(text="TIMER2")
    tc = GridLayout(cols=2)
    label = Label(text="Mode of Operation:", size_hint_x=.3)
    tc.add_widget(label)
    WGM_spn.bind(text=update_spinner)
    tc.add_widget(WGM_spn)
    tc.add_widget(Label(text="Compare Output Mode A:", size_hint_x=.3))
    tc.add_widget(COM2A_spn)
    tc.add_widget(Label(text="Compare Output Mode B:", size_hint_x=.3))
    tc.add_widget(COM2B_spn)
    # tc.add_widget(Button(text="HAYAA"))
    tc.add_widget(Label(text="Prescaler", size_hint_x=.3))
    tc.add_widget(PRE2_spn)
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
    tc.add_widget(Label(text="Enable External Clock Input"))
    switch3 = Switch()
    switch3.bind(active=exclk_callback)
    tc.add_widget(switch3)
    tc.add_widget(Label(text="Asynchronous Timer/Counter2"))
    switch4 = Switch()
    switch4.bind(active=as2_callback)
    tc.add_widget(switch4)

    # Put Content in Tab and add Tab to be available
    timer2_t.content = tc
    self.add_widget(timer2_t)
    global timer2_OPEN
    timer2_OPEN = True


def int_cma_callback(instance, value):
    global ocie2a
    ocie0a = value


def int_cmb_callback(instance, value):
    global ocie2b
    ocie0b = value


def int_ovf_callback(instance, value):
    global toie2
    toie0 = value


def exclk_callback(instance, value):
    global exclk
    exclk = value


def as2_callback(instance, value):
    global as2
    as2 = value


def update_spinner(obj, text):
    if TIMER2_mode[1] == text or TIMER2_mode[5] == text:
        COM2A_spn.values = [COM2_menu[2][0], COM2_menu[2][1], COM2_menu[2][2], COM2_menu[2][3]]
        COM2B_spn.values = [COM2_menu[2][0], COM2_menu[2][1], COM2_menu[2][2], COM2_menu[2][3]]
    elif TIMER2_mode[3] == text or TIMER2_mode[7] == text:
        COM2A_spn.values = [COM2_menu[1][0], COM2_menu[1][1], COM2_menu[1][2], COM2_menu[1][3]]
        COM2B_spn.values = [COM2_menu[1][0], COM2_menu[1][1], COM2_menu[1][2], COM2_menu[1][3]]
    else:
        COM2A_spn.values = [COM2_menu[0][0], COM2_menu[0][1], COM2_menu[0][2], COM2_menu[0][3]]
        COM2B_spn.values = [COM2_menu[0][0], COM2_menu[0][1], COM2_menu[0][2], COM2_menu[0][3]]


def clk2_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(3 - len(binary))):
        binary = "0" + binary
    # CS02
    if binary[0] == "1":
        tccr2b.set("2")
    else:
        tccr2b.clear("2")
    # CS01
    if binary[1] == "1":
        tccr2b.set("1")
    else:
        tccr2b.clear("1")
    # CS00
    if binary[2] == "1":
        tccr2b.set("0")
    else:
        tccr2b.clear("0")


def wgm2_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(3 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr2b.set("3")
    else:
        tccr2b.clear("3")
    if binary[1] == "1":
        tccr2a.set("1")
    else:
        tccr2a.clear("1")
    if binary[2] == "1":
        tccr2a.set("0")
    else:
        tccr2a.clear("0")


def com2a_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(2 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr2a.set("7")
    else:
        tccr2a.clear("7")
    if binary[1] == "1":
        tccr2a.set("6")
    else:
        tccr2a.clear("6")


def com2b_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(2 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr2a.set("5")
    else:
        tccr2a.clear("5")
    if binary[1] == "1":
        tccr2a.set("4")
    else:
        tccr2a.clear("4")


def timer2_int_bits():
    global toie2
    global ocie2a
    global ocie2b
    global exclk
    global as2

    timsk2.set("0") if toie2 else timsk2.clear("0")
    timsk2.set("1") if ocie2a else timsk2.clear("1")
    timsk2.set("2") if ocie2b else timsk2.clear("2")
    assr.set("6") if exclk else assr.clear("6")
    assr.set("5") if as2 else assr.clear("5")


def get_timer2():
    clk2_bit(get_value(CLK2_sel, PRE2_spn.text))
    wgm = get_value(TIMER2_mode, WGM_spn.text)
    wgm2_bit(wgm)

    if wgm == 3 or wgm == 7:
        com2a_bit(get_value(COM2_fPWM, COM2A_spn.text))
        com2b_bit(get_value(COM2_fPWM, COM2B_spn.text))
    elif wgm == 1 or wgm == 5:
        com2a_bit(get_value(COM2_phPWM, COM2A_spn.text))
        com2b_bit(get_value(COM2_phPWM, COM2B_spn.text))
    else:
        com2a_bit(get_value(COM2_nPWM, COM2A_spn.text))
        com2b_bit(get_value(COM2_nPWM, COM2B_spn.text))

    timer2_int_bits()

    print(tccr2a.print_code())
    print(tccr2b.print_code())
    print(timsk2.print_code())
    print(assr.print_code())




