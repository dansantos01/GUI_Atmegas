from kivy.uix.spinner import Spinner

### SELECTION INFO

TIMER0_mode = {
    0: "Normal",
    1: "PWM, Phase Correct (TOP on 0xFF)",
    2: "CTC",
    3: "Fast PWM (TOP on 0xFF)",
    4: "Reserved",
    5: "PWM, Phase Correct (TOP on OCRA)",
    6: "Reserved",
    7: "Fast PWM (TOP on OCRA)"
}

COM0_nPWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match",
    3: "Set OC0A on Compare Match"
}

COM0_fPWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match, set OC0A at BOTTOM, (non-inverting mode).",
    3: "Set OC0A on Compare Match, clear OC0A at BOTTOM, (inverting mode)."
}

COM0_phPWM = {
    0: "Normal port operation, OC0A disconnected.",
    1: "Toggle OC0A on Compare Match",
    2: "Clear OC0A on Compare Match when up-counting. Set OC0A on Compare Match when down-counting.",
    3: "Set OC0A on Compare Match when up-counting. Clear OC0A on Compare Match when down-counting."
}

COM0_menu = {
    0: COM0_nPWM,
    1: COM0_fPWM,
    2: COM0_phPWM
}

CLK0_sel = {
    0: "No clock (TIMER stopped)",
    1: "No prescaling",
    2: "clk / 8",
    3: "clk / 64",
    4: "clk / 256",
    5: "clk / 1024",
    6: "External clock source on T0 pin. Clock on falling edge",
    7: "External clock source on T0 pin. Clock on rising edge"
}


def create_spinner(vect, size):
    spn = Spinner(
        text="Choose Mode of Operation",
        text_autoupdate=True,
        values=(TIMER0_mode[0], TIMER0_mode[1], TIMER0_mode[2], TIMER0_mode[3], TIMER0_mode[4], TIMER0_mode[5],
                TIMER0_mode[6], TIMER0_mode[7]),
        size_hint=(0.5, 0.2),
        pos_hint={"center_x": .5, "center_y": .5}
    )
    return spn


def update_spinner():
    spn = Spinner(
        text="Choose Mode of Operation",
        text_autoupdate=True,
        values=(TIMER0_mode[0], TIMER0_mode[1], TIMER0_mode[2], TIMER0_mode[3], TIMER0_mode[4], TIMER0_mode[5],
                TIMER0_mode[6], TIMER0_mode[6]),
        size_hint=(0.5, 0.2),
        pos_hint={"center_x": .5, "center_y": .5}
    )
    return spn



WGM_spn = create_spinner(TIMER0_mode, len(TIMER0_mode))

WGM_spn = update_spinner()

COM0A_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM0_menu[1][0], COM0_menu[1][1], COM0_menu[1][2], COM0_menu[1][3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)
COM0B_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM0_menu[1][0], COM0_menu[1][1], COM0_menu[1][2], COM0_menu[1][3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)
PRE0_spn = Spinner(
    text="Choose Prescaler",
    text_autoupdate=True,
    values=(CLK0_sel[0], CLK0_sel[1], CLK0_sel[2], CLK0_sel[3], CLK0_sel[4], CLK0_sel[5], CLK0_sel[6], CLK0_sel[7])
)