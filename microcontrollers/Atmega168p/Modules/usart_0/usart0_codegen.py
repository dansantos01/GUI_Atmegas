from microcontrollers.Atmega168p.Modules.usart_0.usart0_ui import *


# Registers
ucsr0a = Register("UCSR0A", "00000000")
ucsr0b = Register("UCSR0B", "00000000")
ucsr0c = Register("UCSR0C", "00000000")
ubrr0l = Register("UBRR0L", "00000000")
ubrr0h = Register("UBRR0H", "00000000")


# Tab Status

usart0_OPEN = False


def usart0_is_open():
    return usart0_OPEN


def usart0_set_status(status):
    global usart0_OPEN
    if status == 1:
        usart0_OPEN = True
    else:
        usart0_OPEN = False


# Code Generation

def usart0_msel_convert(value):
    # UMSEL00
    change_target_bit(value, ucsr0c, '6')


def usart0_csize_convert(value):
    binary = decimal_to_bit(value, 3)
    # UCSZ02
    change_target_bit(binary[0], ucsr0b, '2')
    # UCSZ01
    change_target_bit(binary[1], ucsr0c, '2')
    # UCSZ00
    change_target_bit(binary[2], ucsr0c, '1')


def usart0_parm_convert(value):
    binary = decimal_to_bit(value, 2)
    # UPM01
    change_target_bit(binary[0], ucsr0c, '5')
    # UPM00
    change_target_bit(binary[1], ucsr0c, '4')


def usart0_sbs_convert(value):
    # USBS00
    change_target_bit(value, ucsr0c, '3')


def usart0_clkpol_convert(value):
    binary = decimal_to_bit(value, 2)
    # UCPOL00
    change_target_bit(binary[0], ucsr0c, '0')


def usart0_switch_convert():
    ucsr0a.set('1') if swt_USART0_U2X.active else ucsr0a.clear('1')
    ucsr0a.set('0') if swt_USART0_MCPM.active else ucsr0a.clear('0')
    ucsr0b.set('7') if swt_USART0_RXCIE.active else ucsr0b.clear('7')
    ucsr0b.set('6') if swt_USART0_TXCIE.active else ucsr0b.clear('6')
    ucsr0b.set('5') if swt_USART0_UDRIE.active else ucsr0b.clear('5')
    ucsr0b.set('4') if swt_USART0_RXEN.active else ucsr0b.clear('4')
    ucsr0b.set('3') if swt_USART0_TXEN.active else ucsr0b.clear('3')


def usart0_ubrr_convert():
    freq = float(txtinp_freq.text)*1000000
    baudrate = int(txtinp_baudrate.text)
    ubrr = 0
    if swt_USART0_U2X.active:
        ubrr = calc_ubrr(freq, baudrate, 8)
    # For Asynchronous Double Speed
    if not swt_USART0_U2X.active and spn_USART0_CLKPOL.disabled:
        ubrr = calc_ubrr(freq, baudrate, 16)
    # For Synchronous
    if not swt_USART0_U2X.active and not spn_USART0_CLKPOL.disabled:
        ubrr = calc_ubrr(freq, baudrate, 2)

    print(freq)
    print(baudrate)
    print(ubrr)

    if 0 <= ubrr <= 4095:
        binary = decimal_to_bit(int(ubrr), 12)
        change_target_bit(binary[0], ubrr0h, '3')
        change_target_bit(binary[1], ubrr0h, '2')
        change_target_bit(binary[2], ubrr0h, '1')
        change_target_bit(binary[3], ubrr0h, '0')
        change_target_bit(binary[4], ubrr0l, '7')
        change_target_bit(binary[5], ubrr0l, '6')
        change_target_bit(binary[6], ubrr0l, '5')
        change_target_bit(binary[7], ubrr0l, '4')
        change_target_bit(binary[8], ubrr0l, '3')
        change_target_bit(binary[9], ubrr0l, '2')
        change_target_bit(binary[10], ubrr0l, '1')
        change_target_bit(binary[11], ubrr0l, '0')


def get_usart0():
    usart0_msel_convert(get_value(USART0_MSEL, spn_USART0_MSEL.text))
    usart0_csize_convert(get_value(USART0_CSIZE, spn_USART0_CSIZE.text))
    usart0_parm_convert(get_value(USART0_PARM, spn_USART0_PARM.text))
    usart0_sbs_convert(get_value(USART0_SBS, spn_USART0_SBS.text))
    usart0_clkpol_convert(get_value(USART0_CLKPOL, spn_USART0_CLKPOL.text))
    usart0_switch_convert()
    usart0_ubrr_convert()

    print(ucsr0a.print_code())
    print(ucsr0b.print_code())
    print(ucsr0c.print_code())
    print(ubrr0h.print_code())
    print(ubrr0l.print_code())


