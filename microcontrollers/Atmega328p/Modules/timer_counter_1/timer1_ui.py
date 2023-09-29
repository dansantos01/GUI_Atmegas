from kivy.uix.spinner import Spinner
from functions import *


TIMER1_WGM = {
    "normal": "Normal",
    "pwm": "PWM, Phase Correct",
    "ctc": "CTC",
    "fastpwm": "Fast PWM",
    "pfcpwm": "PWM, Phase and Frequency Correct"
}

TIMER1_WGM_NORMAL = {
    0: "Normal"
}

TIMER1_WGM_PWM = {
    1: "8-bit",
    2: "9-bit",
    3: "10-bit",
    10: "16-bit, TOP on ICR1",
    11: "16-bit, TOP on OCR1A"
}

TIMER1_WGM_CTC = {
    4: "TOP on OCR1A",
    12: "TOP on ICR1A"
}

TIMER1_WGM_FASTPWM = {
    5: "8-bit",
    6: "9-bit",
    7: "10-bit",
    14: "16-bit, TOP on ICR1A",
    15: "16-bit, TOP on OCR1A"
}

TIMER1_WGM_PFCPWM = {
    8: "TOP on ICR1",
    9: "TOP on OCR1A"
}

TIMER1_COMA_NORMAL = {
    0: "Normal port operation, OC1A disconnected.",
    1: "Toggle OC1A on Compare Match.",
    2: "Clear OC1A on Compare Match (Set output to low level).",
    3: "Set OC1A on Compare Match (Set output to high level)."
}

TIMER1_COMA_FASTPWM = {
    0: "Normal port operation, OC1A disconnected.",
    1: "If you chose 16-bit Fast PWM: Toggle OC1A on Compare Match\n"
       "Otherwise: Normal port operation, OC1A disconnected",
    2: "Clear OC1A on Compare Match, set OC1A at BOTTOM (non-inverting mode)",
    3: "Set OC1A on Compare Match, clear OC1A at BOTTOM (inverting mode)"
}

TIMER1_COMA_PWM = {
    0: "Normal port operation, OC1A disconnected.",
    1: "If you chose TOP on OCR1A: Toggle OC1A on Compare Match\n"
       "Otherwise: Normal port operation, OC1A disconnected",
    2: "Clear OC1A on Compare Match when upcounting. Set OC1A on Compare Match when downcounting.",
    3: "Set OC1A on Compare Match when upcounting. Clear OC1A on Compare Match when downcounting."
}

TIMER1_COMB_NORMAL = {
    0: "Normal port operation, OC1B disconnected.",
    1: "Toggle OC1B on Compare Match.",
    2: "Clear OC1B on Compare Match (Set output to low level).",
    3: "Set OC1B on Compare Match (Set output to high level)."
}

TIMER1_COMB_FASTPWM = {
    0: "Normal port operation, OC1B disconnected.",
    1: "Normal port operation, OC1B disconnected",
    2: "Clear OC1B on Compare Match, set OC1B at BOTTOM (non-inverting mode)",
    3: "Set OC1B on Compare Match, clear OC1B at BOTTOM (inverting mode)"
}

TIMER1_COMB_PWM = {
    0: "Normal port operation, OC1B disconnected.",
    1: "Normal port operation, OC1B disconnected",
    2: "Clear OC1B on Compare Match when upcounting. Set OC1B on Compare Match when downcounting.",
    3: "Set OC1B on Compare Match when upcounting. Clear OC1B on Compare Match when downcounting."
}

TIMER1_CLK = {
    0: "No clock (TIMER stopped)",
    1: "No prescaling",
    2: "clk / 8",
    3: "clk / 64",
    4: "clk / 256",
    5: "clk / 1024",
    6: "External clock source on T1 pin. Clock on falling edge",
    7: "External clock source on T1 pin. Clock on rising edge"
}

# Dropdown Box Creation

spn_TIMER1_WGM = create_spinner(TIMER1_WGM)
spn_TIMER1_WGM_OPT = create_spinner(TIMER1_WGM_NORMAL)
spn_TIMER1_COMA = create_spinner(TIMER1_COMA_NORMAL)
spn_TIMER1_COMB = create_spinner(TIMER1_COMB_NORMAL)
spn_TIMER1_CLK = create_spinner(TIMER1_CLK)


# Dropdown box dynamic updates

def wgm_spinner_update(obj, text):

    if TIMER1_WGM["normal"] == text:
        spn_values_update(spn_TIMER1_WGM_OPT, TIMER1_WGM_NORMAL)
        spn_values_update(spn_TIMER1_COMA, TIMER1_COMA_NORMAL)
        spn_values_update(spn_TIMER1_COMB, TIMER1_COMB_NORMAL)
    if TIMER1_WGM["pwm"] == text:
        spn_values_update(spn_TIMER1_WGM_OPT, TIMER1_WGM_PWM)
        spn_values_update(spn_TIMER1_COMA, TIMER1_COMA_PWM)
        spn_values_update(spn_TIMER1_COMB, TIMER1_COMB_PWM)
    if TIMER1_WGM["ctc"] == text:
        spn_values_update(spn_TIMER1_WGM_OPT, TIMER1_WGM_CTC)
        spn_values_update(spn_TIMER1_COMA, TIMER1_COMA_NORMAL)
        spn_values_update(spn_TIMER1_COMB, TIMER1_COMB_NORMAL)
    if TIMER1_WGM["pfcpwm"] == text:
        spn_values_update(spn_TIMER1_WGM_OPT, TIMER1_WGM_PFCPWM)
        spn_values_update(spn_TIMER1_COMA, TIMER1_COMA_PWM)
        spn_values_update(spn_TIMER1_COMB, TIMER1_COMB_PWM)
    if TIMER1_WGM["fastpwm"] == text:
        spn_values_update(spn_TIMER1_WGM_OPT, TIMER1_WGM_FASTPWM)
        spn_values_update(spn_TIMER1_COMA, TIMER1_COMA_FASTPWM)
        spn_values_update(spn_TIMER1_COMB, TIMER1_COMB_FASTPWM)


spn_TIMER1_WGM.bind(text=wgm_spinner_update)

# Switch Creation

swt_TIMER1_ICNC = Switch()
swt_TIMER1_ICES = Switch()
swt_TIMER1_ICIE = Switch()
swt_TIMER1_OCIE1A = Switch()
swt_TIMER1_OCIE1B = Switch()
swt_TIMER1_TOIE = Switch()


# Tab Creation

def timer1_tab_start(self, btn):

    from microcontrollers.Atmega328p.Modules.timer_counter_1.timer1_codegen import timer1_set_status
    timer1_t = TabbedPanelItem(text="TIMER1")
    grid = GridLayout(cols=2)
    create_spinner_ui("Wave Generation Mode", spn_TIMER1_WGM, grid)
    create_spinner_ui("Mode Options", spn_TIMER1_WGM_OPT, grid)
    create_spinner_ui("Compare Output Match A", spn_TIMER1_COMA, grid)
    create_spinner_ui("Compare Output Match B", spn_TIMER1_COMB, grid)
    create_spinner_ui("Prescaler Selection", spn_TIMER1_CLK, grid)
    create_switch_ui("Input Capture Noise Canceler", swt_TIMER1_ICNC, grid)
    create_switch_ui("Input Capture Edge Select", swt_TIMER1_ICES, grid)
    create_switch_ui("Input Capture Interrupt Enable", swt_TIMER1_ICIE, grid)
    create_switch_ui("Output Compare A Match Interrupt Enable", swt_TIMER1_OCIE1A, grid)
    create_switch_ui("Output Compare B Match Interrupt Enable", swt_TIMER1_OCIE1B, grid)
    create_switch_ui("Overflow Interrupt Enable", swt_TIMER1_TOIE, grid)

    timer1_t.content = grid
    self.add_widget(timer1_t)
    timer1_set_status(1)

