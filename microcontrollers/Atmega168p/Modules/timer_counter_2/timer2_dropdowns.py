### SELECTION INFO

TIMER2_mode = {
    0: "Normal",
    1: "PWM, Phase Correct (TOP on 0xFF)",
    2: "CTC",
    3: "Fast PWM (TOP on 0xFF)",
    4: "Reserved",
    5: "PWM, Phase Correct (TOP on OCRA)",
    6: "Reserved",
    7: "Fast PWM (TOP on OCRA)"
}

COM2_nPWM = {
    0: "Normal port operation, OC2A disconnected.",
    1: "Toggle OC2A on Compare Match",
    2: "Clear OC2A on Compare Match",
    3: "Set OC2A on Compare Match"
}

COM2_fPWM = {
    0: "Normal port operation, OC2A disconnected.",
    1: "Toggle OC2A on Compare Match",
    2: "Clear OC2A on Compare Match,set OC0A at BOTTOM, (non-inverting mode).",
    3: "Set OC2A on Compare Match, clear OC0A at BOTTOM, (inverting mode)."
}

COM2_phPWM = {
    0: "Normal port operation, OC2A disconnected.",
    1: "Toggle OC2A on Compare Match",
    2: "Clear OC2A on Compare Match when up-counting. Set OC0A on Compare Match when down-counting.",
    3: "Set OC2A on Compare Match when up-counting. Clear OC0A on Compare Match when down-counting."
}

COM2_menu = {
    0: COM2_nPWM,
    1: COM2_fPWM,
    2: COM2_phPWM
}

CLK2_sel = {
    0: "No clock (TIMER stopped)",
    1: "No prescaling",
    2: "clk / 8",
    3: "clk / 32",
    4: "clk / 64",
    5: "clk / 128",
    6: "clk / 256",
    7: "clk / 1024"
}
