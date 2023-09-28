from kivy.uix.spinner import Spinner
from functions import *


TIMER1_WGM = {
    0: "Normal",
    1: "PWM, Phase Correct",
    2: "CTC",
    3: "Fast PWM",
    4: "PWM, Phase and Frequency Correct"
}

TIMER1_normal = {
    0: "Normal"
}

TIMER1_pcPWM = {
    1: "8-bit",
    2: "9-bit",
    3: "10-bit",
    10: "16-bit, TOP on ICR1",
    11: "16-bit, TOP on OCR1A"
}

TIMER1_CTC = {
    4: "TOP on OCR1A",
    12: "TOP on ICR1A"
}

TIMER1_fPWM = {
    5: "8-bit",
    6: "9-bit",
    7: "10-bit",
    14: "16-bit, TOP on ICR1A",
    15: "16-bit, TOP on OCR1A"
}

TIMER1_pfcPWM = {
    8: "TOP on ICR1",
    9: "TOP on OCR1A"
}

COM1A_nPWM = {
    0: "Normal port operation, OC1A disconnected.",
    1: "Toggle OC1A on Compare Match.",
    2: "Clear OC1A on Compare Match (Set output to low level).",
    3: "Set OC1A on Compare Match (Set output to high level)."
}

COM1A_fPWM = {
    0: "Normal port operation, OC1A disconnected.",
    1: "If you chose 16-bit Fast PWM: Toggle OC1A on Compare Match\n"
       "Otherwise: Normal port operation, OC1A disconnected",
    2: "Clear OC1A on Compare Match, set OC1A at BOTTOM (non-inverting mode)",
    3: "Set OC1A on Compare Match, clear OC1A at BOTTOM (inverting mode)"
}

COM1A_pcPWM = {
    0: "Normal port operation, OC1A disconnected.",
    1: "If you chose TOP on OCR1A: Toggle OC1A on Compare Match\n"
       "Otherwise: Normal port operation, OC1A disconnected",
    2: "Clear OC1A on Compare Match when upcounting. Set OC1A on Compare Match when downcounting.",
    3: "Set OC1A on Compare Match when upcounting. Clear OC1A on Compare Match when downcounting."
}

COM1B_nPWM = {
    0: "Normal port operation, OC1B disconnected.",
    1: "Toggle OC1B on Compare Match.",
    2: "Clear OC1B on Compare Match (Set output to low level).",
    3: "Set OC1B on Compare Match (Set output to high level)."
}

COM1B_fPWM = {
    0: "Normal port operation, OC1B disconnected.",
    1: "Normal port operation, OC1B disconnected",
    2: "Clear OC1B on Compare Match, set OC1B at BOTTOM (non-inverting mode)",
    3: "Set OC1B on Compare Match, clear OC1B at BOTTOM (inverting mode)"
}

COM1B_pcPWM = {
    0: "Normal port operation, OC1B disconnected.",
    1: "Normal port operation, OC1B disconnected",
    2: "Clear OC1B on Compare Match when upcounting. Set OC1B on Compare Match when downcounting.",
    3: "Set OC1B on Compare Match when upcounting. Clear OC1B on Compare Match when downcounting."
}




WGM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(TIMER1_WGM[0], TIMER1_WGM[1], TIMER1_WGM[2], TIMER1_WGM[3], TIMER1_WGM[4]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

normal_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(TIMER1_normal[0]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

pcPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(TIMER1_pcPWM[1], TIMER1_pcPWM[2], TIMER1_pcPWM[3], TIMER1_pcPWM[10], TIMER1_pcPWM[11]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

CTC_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(TIMER1_CTC[4], TIMER1_CTC[12]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)



fPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(TIMER1_fPWM[5], TIMER1_fPWM[6], TIMER1_fPWM[7], TIMER1_fPWM[14], TIMER1_fPWM[15]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

pfcPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(TIMER1_pfcPWM[8], TIMER1_pfcPWM[9]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

coma_nPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM1A_nPWM[0], COM1A_nPWM[1], COM1A_nPWM[2], COM1A_nPWM[3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

coma_fPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM1A_fPWM[0], COM1A_fPWM[1], COM1A_fPWM[2], COM1A_fPWM[3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

coma_pcPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM1A_pcPWM[0], COM1A_pcPWM[1], COM1A_pcPWM[2], COM1A_pcPWM[3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

comb_nPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM1B_nPWM[0], COM1B_nPWM[1], COM1B_nPWM[2], COM1B_nPWM[3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

comb_fPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM1B_fPWM[0], COM1B_fPWM[1], COM1B_fPWM[2], COM1B_fPWM[3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

comb_pcPWM_spn = Spinner(
    text="Choose Mode of Operation",
    text_autoupdate=True,
    values=(COM1B_pcPWM[0], COM1B_pcPWM[1], COM1B_pcPWM[2], COM1B_pcPWM[3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)

CLK1_sel = {
    0: "No clock (TIMER stopped)",
    1: "No prescaling",
    2: "clk / 8",
    3: "clk / 64",
    4: "clk / 256",
    5: "clk / 1024",
    6: "External clock source on T1 pin. Clock on falling edge",
    7: "External clock source on T1 pin. Clock on rising edge"
}

clk_spn = Spinner(
    text="Choose the clock",
    text_autoupdate=True,
    values=(CLK1_sel[0], CLK1_sel[1], CLK1_sel[2], CLK1_sel[3]),
    size_hint=(0.5, 0.2),
    pos_hint={"center_x": .5, "center_y": .5}
)
