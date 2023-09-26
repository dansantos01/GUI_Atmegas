from Modules.timer_counter_0.timer0_ui import *
from functions import *


# Registers
tccr0a = Register("TCCR0A", "00000000")
tccr0b = Register("TCCR0B", "00000000")
timsk0 = Register("TIMSK0", "00000000")


# Tab Status

timer0_OPEN = False


def timer0_is_open():
    return timer0_OPEN


def timer0_set_status(status):
    global timer0_OPEN
    if status == 1:
        timer0_OPEN = True
    else:
        timer0_OPEN = False


# Code Generation

def clk0_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(3 - len(binary))):
        binary = "0" + binary
    # CS02
    change_target_bit(binary[0], tccr0b, "2")
    # CS01
    change_target_bit(binary[1], tccr0b, "1")
    # CS00
    change_target_bit(binary[2], tccr0b, "0")


def wgm0_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(3 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr0b.set("3")
    else:
        tccr0b.clear("3")
    if binary[1] == "1":
        tccr0a.set("1")
    else:
        tccr0a.clear("1")
    if binary[2] == "1":
        tccr0a.set("0")
    else:
        tccr0a.clear("0")


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

    timsk0.set("0") if swt_TIMER0_OVF.active else timsk0.clear("0")
    timsk0.set("1") if swt_TIMER0_OCM_A.active else timsk0.clear("1")
    timsk0.set("2") if swt_TIMER0_OCM_B.active else timsk0.clear("2")


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
