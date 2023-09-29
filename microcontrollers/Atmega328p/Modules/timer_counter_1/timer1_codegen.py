from microcontrollers.Atmega328p.Modules.timer_counter_1.timer1_ui import *

# registers

tccr1a = Register("TCCR1A", "00000000")
tccr1b = Register("TCCR1B", "00000000")
timsk1 = Register("TIMSK1", "00000000")
tifr1 = Register("TIFR1", "00000000")


# Open or not

timer1_OPEN = False


def timer1_is_open():
    return timer1_OPEN


def timer1_set_status(status):
    global timer1_OPEN
    if status == 1:
        timer1_OPEN = True
    else:
        timer1_OPEN = False


# Code Generation

def timer1_clk_convert(value):
    binary = decimal_to_bit(value, 3)
    # CS12
    change_target_bit(binary[0], tccr1b, '2')
    # CS11
    change_target_bit(binary[1], tccr1b, '1')
    # CS10
    change_target_bit(binary[2], tccr1b, '0')


def timer1_wgm_convert(value):
    binary = decimal_to_bit(value, 4)
    # WGM13
    change_target_bit(binary[0], tccr1b, '4')
    # WGM12
    change_target_bit(binary[1], tccr1b, '3')
    # WGM11
    change_target_bit(binary[2], tccr1a, '1')
    # WGM10
    change_target_bit(binary[3], tccr1a, '0')


def timer1_coma_convert(value):
    binary = decimal_to_bit(value, 2)
    # COM1A1
    change_target_bit(binary[0], tccr1a, '7')
    # COM1A0
    change_target_bit(binary[1], tccr1a, '6')


def timer1_comb_convert(value):
    binary = decimal_to_bit(value, 2)
    # COM1B1
    change_target_bit(binary[0], tccr1a, '5')
    # COM1B0
    change_target_bit(binary[1], tccr1a, '4')


def timer1_switch_convert():

    tccr1b.set("7") if swt_TIMER1_ICNC.active else tccr1b.clear("7")
    tccr1b.set("6") if swt_TIMER1_ICES.active else tccr1b.clear("6")
    timsk1.set("5") if swt_TIMER1_ICIE.active else timsk1.clear("5")
    timsk1.set("2") if swt_TIMER1_OCIE1B.active else timsk1.clear("2")
    timsk1.set("1") if swt_TIMER1_OCIE1A.active else timsk1.clear("1")
    timsk1.set("0") if swt_TIMER1_TOIE.active else timsk1.clear("0")


def get_timer1():
    timer1_switch_convert()
    timer1_clk_convert(get_value(TIMER1_CLK, spn_TIMER1_CLK.text))
    if TIMER1_WGM["normal"] == spn_TIMER1_WGM.text:
        timer1_wgm_convert(get_value(TIMER1_WGM_NORMAL, spn_TIMER1_WGM_OPT.text))
        timer1_coma_convert(get_value(TIMER1_COMA_NORMAL, spn_TIMER1_COMA.text))
        timer1_comb_convert(get_value(TIMER1_COMB_NORMAL, spn_TIMER1_COMB.text))
    if TIMER1_WGM["pwm"] == spn_TIMER1_WGM.text:
        timer1_wgm_convert(get_value(TIMER1_WGM_PWM, spn_TIMER1_WGM_OPT.text))
        timer1_coma_convert(get_value(TIMER1_COMA_PWM, spn_TIMER1_COMA.text))
        timer1_comb_convert(get_value(TIMER1_COMB_PWM, spn_TIMER1_COMB.text))
    if TIMER1_WGM["ctc"] == spn_TIMER1_WGM.text:
        timer1_wgm_convert(get_value(TIMER1_WGM_CTC, spn_TIMER1_WGM_OPT.text))
        timer1_coma_convert(get_value(TIMER1_COMA_NORMAL, spn_TIMER1_COMA.text))
        timer1_comb_convert(get_value(TIMER1_COMB_NORMAL, spn_TIMER1_COMB.text))
    if TIMER1_WGM["pfcpwm"] == spn_TIMER1_WGM.text:
        timer1_wgm_convert(get_value(TIMER1_WGM_PFCPWM, spn_TIMER1_WGM_OPT.text))
        timer1_coma_convert(get_value(TIMER1_COMA_PWM, spn_TIMER1_COMA.text))
        timer1_comb_convert(get_value(TIMER1_COMB_PWM, spn_TIMER1_COMB.text))
    if TIMER1_WGM["fastpwm"] == spn_TIMER1_WGM.text:
        timer1_wgm_convert(get_value(TIMER1_WGM_FASTPWM, spn_TIMER1_WGM_OPT.text))
        timer1_coma_convert(get_value(TIMER1_COMA_FASTPWM, spn_TIMER1_COMA.text))
        timer1_comb_convert(get_value(TIMER1_COMB_FASTPWM, spn_TIMER1_COMB.text))



