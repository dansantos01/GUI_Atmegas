from functions import *

# Dropdown box text

TIMER2_WGM = {
    "normal": "Normal / CTC",
    "pwm": "PWM, Phase Correct",
    "fastpwm": "Fast PWM",
}

TIMER2_WGM_NORMAL = {
    0: "Normal",
    2: "CTC"
}

TIMER2_WGM_PWM = {
    1: "TOP on 0xFF",
    5: "TOP on OCRA"
}

TIMER2_WGM_FASTPWM = {
    3: "TOP on 0xFF",
    7: "TOP on OCRA"
}

TIMER2_COMA_NORMAL = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match if TOP on OCRA, otherwise, OC0A disconnected",
    2: "Clear OC0A on Compare Match",
    3: "Set OC0A on Compare Match"
}

TIMER2_COMA_PWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match when up-counting. Set OC0A on Compare Match when down-counting.",
    3: "Set OC0A on Compare Match when up-counting. Clear OC0A on Compare Match when down-counting."
}

TIMER2_COMA_FASTPWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match if TOP on OCRA, otherwise, OC0A disconnected",
    2: "Clear OC0A on Compare Match, set OC0A at BOTTOM, (non-inverting mode).",
    3: "Set OC0A on Compare Match, clear OC0A at BOTTOM, (inverting mode)."
}

TIMER2_COMB_NORMAL = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match",
    3: "Set OC0A on Compare Match"
}

TIMER2_COMB_PWM = {
    0: "Normal port operation, OC0A disconnected.",
    2: "Clear OC0A on Compare Match when up-counting. Set OC0A on Compare Match when down-counting.",
    3: "Set OC0A on Compare Match when up-counting. Clear OC0A on Compare Match when down-counting."
}

TIMER2_COMB_FASTPWM = {
    0: "Normal port operation, OC0A disconnected.",
    2: "Clear OC0A on Compare Match, set OC0A at BOTTOM, (non-inverting mode).",
    3: "Set OC0A on Compare Match, clear OC0A at BOTTOM, (inverting mode)."
}

TIMER2_CLOCK = {
    0: "No clock (TIMER stopped)",
    1: "No prescaling",
    2: "clk / 8",
    3: "clk / 32",
    4: "clk / 64",
    5: "clk / 128",
    6: "clk / 256",
    7: "clk / 1024"
}


# Dropdown box creation

spn_TIMER2_WGM = create_spinner(TIMER2_WGM)
spn_TIMER2_WGM_OPT = create_spinner(TIMER2_WGM_NORMAL)
spn_TIMER2_COM_A = create_spinner(TIMER2_COMA_NORMAL)
spn_TIMER2_COM_B = create_spinner(TIMER2_COMB_NORMAL)
spn_TIMER2_CLOCK = create_spinner(TIMER2_CLOCK)

# Dropdown box dynamic update


def wgm_spinner_update(obj, text):
    if TIMER2_WGM["normal"] == spn_TIMER2_WGM.text:
        spn_values_update(spn_TIMER2_COM_A, TIMER2_COMA_NORMAL)
        spn_values_update(spn_TIMER2_COM_B, TIMER2_COMB_NORMAL)
        spn_values_update(spn_TIMER2_WGM_OPT, TIMER2_WGM_NORMAL)
    elif TIMER2_WGM["pwm"] == spn_TIMER2_WGM.text:
        spn_values_update(spn_TIMER2_COM_A, TIMER2_COMA_PWM)
        spn_values_update(spn_TIMER2_COM_B, TIMER2_COMB_PWM)
        spn_values_update(spn_TIMER2_WGM_OPT, TIMER2_WGM_PWM)
    elif TIMER2_WGM["fastpwm"] == spn_TIMER2_WGM.text:
        spn_values_update(spn_TIMER2_COM_A, TIMER2_COMA_FASTPWM)
        spn_values_update(spn_TIMER2_COM_B, TIMER2_COMB_FASTPWM)
        spn_values_update(spn_TIMER2_WGM_OPT, TIMER2_WGM_FASTPWM)


spn_TIMER2_WGM.bind(text=wgm_spinner_update)

# Switch Creation

swt_TIMER2_OCM_A = Switch()
swt_TIMER2_OCM_B = Switch()
swt_TIMER2_OVF = Switch()
swt_TIMER2_EXCLK = Switch()
swt_TIMER2_AS = Switch()

# Tab Creation


def timer2_tab_start(self, btn):
    from microcontrollers.Atmega328p.Modules.timer_counter_2.timer2_codegen import timer2_set_status
    timer2_tab = TabbedPanelItem(text="TIMER2")  # Create Tabbed Panel
    grid = GridLayout(cols=2)  # Store the content in a grid layout

    # UI Generation

    create_spinner_ui("Wave Generation Mode", spn_TIMER2_WGM, grid)
    create_spinner_ui("Wave Generation Mode Options", spn_TIMER2_WGM_OPT, grid)
    create_spinner_ui("Compare Output Mode A", spn_TIMER2_COM_A, grid)
    create_spinner_ui("Compare Output Mode B", spn_TIMER2_COM_B, grid)
    create_spinner_ui("Clock", spn_TIMER2_CLOCK, grid)
    create_switch_ui("Timer/Counter Output Compare Match A Interrupt Enable", swt_TIMER2_OCM_A, grid)
    create_switch_ui("Timer/Counter Output Compare Match B Interrupt Enable", swt_TIMER2_OCM_B, grid)
    create_switch_ui("Timer/Counter0 Overflow Interrupt Enable", swt_TIMER2_OVF, grid)
    create_switch_ui("Enable External Clock Input", swt_TIMER2_EXCLK, grid)
    create_switch_ui("Asynchronous Timer/Counter", swt_TIMER2_AS, grid)

    # Put Content in Tab and make it available

    timer2_tab.content = grid
    self.add_widget(timer2_tab)
    timer2_set_status(1)
