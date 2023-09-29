from functions import *

# Dropdown box text

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

TIMER0_COMA_NORMAL = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match if TOP on OCRA, otherwise, OC0A disconnected",
    2: "Clear OC0A on Compare Match",
    3: "Set OC0A on Compare Match"
}

TIMER0_COMA_PWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match when up-counting. Set OC0A on Compare Match when down-counting.",
    3: "Set OC0A on Compare Match when up-counting. Clear OC0A on Compare Match when down-counting."
}

TIMER0_COMA_FASTPWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match if TOP on OCRA, otherwise, OC0A disconnected",
    2: "Clear OC0A on Compare Match, set OC0A at BOTTOM, (non-inverting mode).",
    3: "Set OC0A on Compare Match, clear OC0A at BOTTOM, (inverting mode)."
}

TIMER0_COMB_NORMAL = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match",
    3: "Set OC0A on Compare Match"
}

TIMER0_COMB_PWM = {
    0: "Normal port operation, OC0A disconnected.",
    2: "Clear OC0A on Compare Match when up-counting. Set OC0A on Compare Match when down-counting.",
    3: "Set OC0A on Compare Match when up-counting. Clear OC0A on Compare Match when down-counting."
}

TIMER0_COMB_FASTPWM = {
    0: "Normal port operation, OC0A disconnected.",
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


# Dropdown box creation

spn_TIMER0_WGM = create_spinner(TIMER0_WGM)
spn_TIMER0_WGM_OPT = create_spinner(TIMER0_WGM_NORMAL)
spn_TIMER0_COM_A = create_spinner(TIMER0_COMA_NORMAL)
spn_TIMER0_COM_B = create_spinner(TIMER0_COMB_NORMAL)
spn_TIMER0_CLOCK = create_spinner(TIMER0_CLOCK)

# Dropdown box dynamic update


def wgm_spinner_update(obj, text):
    if TIMER0_WGM["normal"] == spn_TIMER0_WGM.text:
        spn_values_update(spn_TIMER0_COM_A, TIMER0_COMA_NORMAL)
        spn_values_update(spn_TIMER0_COM_B, TIMER0_COMB_NORMAL)
        spn_values_update(spn_TIMER0_WGM_OPT, TIMER0_WGM_NORMAL)
    elif TIMER0_WGM["pwm"] == spn_TIMER0_WGM.text:
        spn_values_update(spn_TIMER0_COM_A, TIMER0_COMA_PWM)
        spn_values_update(spn_TIMER0_COM_B, TIMER0_COMB_PWM)
        spn_values_update(spn_TIMER0_WGM_OPT, TIMER0_WGM_PWM)
    elif TIMER0_WGM["fastpwm"] == spn_TIMER0_WGM.text:
        spn_values_update(spn_TIMER0_COM_A, TIMER0_COMA_FASTPWM)
        spn_values_update(spn_TIMER0_COM_B, TIMER0_COMB_FASTPWM)
        spn_values_update(spn_TIMER0_WGM_OPT, TIMER0_WGM_FASTPWM)


spn_TIMER0_WGM.bind(text=wgm_spinner_update)

# Switch Creation

swt_TIMER0_OCM_A = Switch()
swt_TIMER0_OCM_B = Switch()
swt_TIMER0_OVF = Switch()

# Tab Creation


def timer0_tab_start(self, btn):
    from microcontrollers.Atmega328p.Modules.timer_counter_0.timer0_codegen import timer0_set_status
    timer0_tab = TabbedPanelItem(text="TIMER0")  # Create Tabbed Panel
    grid = GridLayout(cols=2)  # Store the content in a grid layout

    # UI Generation

    create_spinner_ui("Wave Generation Mode", spn_TIMER0_WGM, grid)
    create_spinner_ui("Wave Generation Mode Options", spn_TIMER0_WGM_OPT, grid)
    create_spinner_ui("Compare Output Mode A", spn_TIMER0_COM_A, grid)
    create_spinner_ui("Compare Output Mode B", spn_TIMER0_COM_B, grid)
    create_spinner_ui("Clock", spn_TIMER0_CLOCK, grid)
    create_switch_ui("Timer/Counter Output Compare Match A Interrupt Enable", swt_TIMER0_OCM_A, grid)
    create_switch_ui("Timer/Counter Output Compare Match B Interrupt Enable", swt_TIMER0_OCM_B, grid)
    create_switch_ui("Timer/Counter0 Overflow Interrupt Enable", swt_TIMER0_OVF, grid)

    # Put Content in Tab and make it available

    timer0_tab.content = grid
    self.add_widget(timer0_tab)
    timer0_set_status(1)
