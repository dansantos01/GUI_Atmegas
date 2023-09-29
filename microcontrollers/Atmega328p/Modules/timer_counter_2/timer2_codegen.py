from microcontrollers.Atmega328p.Modules.timer_counter_2.timer2_ui import *


# Registers
tccr2a = Register("TCCR0A", "00000000")
tccr2b = Register("TCCR0B", "00000000")
timsk2 = Register("TIMSK0", "00000000")
assr = Register("ASSR", "00000000")


# Tab Status

timer2_OPEN = False


def timer2_is_open():
    return timer2_OPEN


def timer2_set_status(status):
    global timer2_OPEN
    if status == 1:
        timer2_OPEN = True
    else:
        timer2_OPEN = False


# Code Generation

def timer2_clk_convert(value):
    binary = decimal_to_bit(value, 3)
    # CS02
    change_target_bit(binary[0], tccr2b, "2")
    # CS01
    change_target_bit(binary[1], tccr2b, "1")
    # CS00
    change_target_bit(binary[2], tccr2b, "0")


def timer2_wgm_convert(value):
    binary = decimal_to_bit(value, 3)
    # WGM02
    change_target_bit(binary[0], tccr2b, "3")
    # WGM01
    change_target_bit(binary[1], tccr2a, "1")
    # WGM00
    change_target_bit(binary[2], tccr2a, "0")


def timer2_coma_convert(value):
    binary = decimal_to_bit(value, 2)
    # COM0A1
    change_target_bit(binary[0], tccr2a, '7')
    # COM0A0
    change_target_bit(binary[1], tccr2a, '6')


def timer2_comb_convert(value):
    binary = decimal_to_bit(value, 2)
    # COM0B1
    change_target_bit(binary[0], tccr2a, '5')
    # COM0B0
    change_target_bit(binary[1], tccr2a, '4')


def timer2_switch_convert():

    timsk2.set("0") if swt_TIMER2_OVF.active else timsk2.clear("0")
    timsk2.set("1") if swt_TIMER2_OCM_A.active else timsk2.clear("1")
    timsk2.set("2") if swt_TIMER2_OCM_B.active else timsk2.clear("2")
    assr.set("6") if swt_TIMER2_EXCLK.active else assr.clear("6")
    assr.set("5") if swt_TIMER2_AS.active else assr.clear("5")


def get_timer2():
    timer2_clk_convert(get_value(TIMER2_CLOCK, spn_TIMER2_CLOCK.text))
    timer2_switch_convert()

    if TIMER2_WGM["normal"] == spn_TIMER2_WGM.text:
        timer2_coma_convert(get_value(TIMER2_COMA_NORMAL, spn_TIMER2_COM_A.text))
        timer2_comb_convert(get_value(TIMER2_COMB_NORMAL, spn_TIMER2_COM_B.text))
        timer2_wgm_convert(get_value(TIMER2_WGM_NORMAL, spn_TIMER2_WGM_OPT.text))
    elif TIMER2_WGM["pwm"] == spn_TIMER2_WGM.text:
        timer2_coma_convert(get_value(TIMER2_COMA_PWM, spn_TIMER2_COM_A.text))
        timer2_comb_convert(get_value(TIMER2_COMB_PWM, spn_TIMER2_COM_B.text))
        timer2_wgm_convert(get_value(TIMER2_WGM_PWM, spn_TIMER2_WGM_OPT.text))
    elif TIMER2_WGM["fastpwm"] == spn_TIMER2_WGM.text:
        timer2_coma_convert(get_value(TIMER2_COMA_FASTPWM, spn_TIMER2_COM_A.text))
        timer2_comb_convert(get_value(TIMER2_COMB_FASTPWM, spn_TIMER2_COM_B.text))
        timer2_wgm_convert(get_value(TIMER2_WGM_FASTPWM, spn_TIMER2_WGM_OPT.text))



