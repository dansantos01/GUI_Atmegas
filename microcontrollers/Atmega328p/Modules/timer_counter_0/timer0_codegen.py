from microcontrollers.Atmega328p.Modules.timer_counter_0.timer0_ui import *


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

def timer0_clk_convert(value):
    binary = decimal_to_bit(value, 3)
    # CS02
    change_target_bit(binary[0], tccr0b, "2")
    # CS01
    change_target_bit(binary[1], tccr0b, "1")
    # CS00
    change_target_bit(binary[2], tccr0b, "0")


def timer0_wgm_convert(value):
    binary = decimal_to_bit(value, 3)
    # WGM02
    change_target_bit(binary[0], tccr0b, "3")
    # WGM01
    change_target_bit(binary[1], tccr0a, "1")
    # WGM00
    change_target_bit(binary[2], tccr0a, "0")


def timer0_coma_convert(value):
    binary = decimal_to_bit(value, 2)
    # COM0A1
    change_target_bit(binary[0], tccr0a, '7')
    # COM0A0
    change_target_bit(binary[1], tccr0a, '6')


def timer0_comb_convert(value):
    binary = decimal_to_bit(value, 2)
    # COM0B1
    change_target_bit(binary[0], tccr0a, '5')
    # COM0B0
    change_target_bit(binary[1], tccr0a, '4')


def timer0_switch_convert():

    timsk0.set("0") if swt_TIMER0_OVF.active else timsk0.clear("0")
    timsk0.set("1") if swt_TIMER0_OCM_A.active else timsk0.clear("1")
    timsk0.set("2") if swt_TIMER0_OCM_B.active else timsk0.clear("2")


def get_timer0():
    timer0_clk_convert(get_value(TIMER0_CLOCK, spn_TIMER0_CLOCK.text))
    timer0_switch_convert()

    if TIMER0_WGM["normal"] == spn_TIMER0_WGM.text:
        timer0_coma_convert(get_value(TIMER0_COMA_NORMAL, spn_TIMER0_COM_A.text))
        timer0_comb_convert(get_value(TIMER0_COMB_NORMAL, spn_TIMER0_COM_B.text))
        timer0_wgm_convert(get_value(TIMER0_WGM_NORMAL, spn_TIMER0_WGM_OPT.text))
    elif TIMER0_WGM["pwm"] == spn_TIMER0_WGM.text:
        timer0_coma_convert(get_value(TIMER0_COMA_PWM, spn_TIMER0_COM_A.text))
        timer0_comb_convert(get_value(TIMER0_COMB_PWM, spn_TIMER0_COM_B.text))
        timer0_wgm_convert(get_value(TIMER0_WGM_PWM, spn_TIMER0_WGM_OPT.text))
    elif TIMER0_WGM["fastpwm"] == spn_TIMER0_WGM.text:
        timer0_coma_convert(get_value(TIMER0_COMA_FASTPWM, spn_TIMER0_COM_A.text))
        timer0_comb_convert(get_value(TIMER0_COMB_FASTPWM, spn_TIMER0_COM_B.text))
        timer0_wgm_convert(get_value(TIMER0_WGM_FASTPWM, spn_TIMER0_WGM_OPT.text))



