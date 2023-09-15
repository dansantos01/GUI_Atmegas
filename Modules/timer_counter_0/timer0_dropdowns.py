from kivy.uix.spinner import Spinner
from functions import *

### SELECTION INFO

TIMER0_WGM = {
    "normal": "Normal / CTC",
    "pwm": "PWM, Phase Correct",
    "fastpwm": "Fast PWM",
}

TIMER0_WGM_NORMAL = {
    0: "Normal",
    2: "CTC"
}

TIMER0_WGM_PWM = {
    1: "TOP on 0xFF",
    5: "TOP on OCRA"
}

TIMER0_WGM_FASTPWM = {
    3: "TOP on 0xFF",
    7: "TOP on OCRA"
}

TIMER0_COM_NORMAL = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match",
    3: "Set OC0A on Compare Match"
}

TIMER0_COM_PWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match when up-counting. Set OC0A on Compare Match when down-counting.",
    3: "Set OC0A on Compare Match when up-counting. Clear OC0A on Compare Match when down-counting."
}

TIMER0_COM_FASTPWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match, set OC0A at BOTTOM, (non-inverting mode).",
    3: "Set OC0A on Compare Match, clear OC0A at BOTTOM, (inverting mode)."
}

TIMER0_CLOCK = {
    0: "No clock (TIMER stopped)",
    1: "No prescaling",
    2: "clk / 8",
    3: "clk / 64",
    4: "clk / 256",
    5: "clk / 1024",
    6: "External clock source on T0 pin. Clock on falling edge",
    7: "External clock source on T0 pin. Clock on rising edge"
}

spn_TIMER0_WGM = create_spinner(TIMER0_WGM)
spn_TIMER0_WGM_OPT = create_spinner(TIMER0_WGM_NORMAL)
spn_TIMER0_COM_A = create_spinner(TIMER0_COM_NORMAL)
spn_TIMER0_COM_B = create_spinner(TIMER0_COM_NORMAL)
spn_TIMER0_CLOCK = create_spinner(TIMER0_CLOCK)


def wgm_spinner_update(obj, text):
    if TIMER0_WGM["normal"] == spn_TIMER0_WGM.text:
        spn_values_update(spn_TIMER0_COM_A, TIMER0_COM_NORMAL)
        spn_values_update(spn_TIMER0_COM_B, TIMER0_COM_NORMAL)
        spn_values_update(spn_TIMER0_WGM_OPT, TIMER0_WGM_NORMAL)
    elif TIMER0_WGM["pwm"] == spn_TIMER0_WGM.text:
        spn_values_update(spn_TIMER0_COM_A, TIMER0_COM_PWM)
        spn_values_update(spn_TIMER0_COM_B, TIMER0_COM_PWM)
        spn_values_update(spn_TIMER0_WGM_OPT, TIMER0_WGM_PWM)
    elif TIMER0_WGM["fastpwm"] == spn_TIMER0_WGM.text:
        spn_values_update(spn_TIMER0_COM_A, TIMER0_COM_FASTPWM)
        spn_values_update(spn_TIMER0_COM_B, TIMER0_COM_FASTPWM)
        spn_values_update(spn_TIMER0_WGM_OPT, TIMER0_WGM_FASTPWM)


spn_TIMER0_WGM.bind(text=wgm_spinner_update)

