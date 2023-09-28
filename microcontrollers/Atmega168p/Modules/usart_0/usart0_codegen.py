from microcontrollers.Atmega168p.Modules.usart_0.usart0_ui import *


# Registers
ucsr0a = Register("UCSR0A", "00000000")
ucsr0b = Register("UCSR0B", "00000000")
ucsr0c = Register("UCSR0C", "00000000")
ubrr0l = Register("UBRR0L", "00000000")


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
