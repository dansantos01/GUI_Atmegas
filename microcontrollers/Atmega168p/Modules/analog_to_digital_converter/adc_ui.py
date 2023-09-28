from functions import *


# Dropdown box text

ADC_VRS = {
    0: "AREF, Internal Vref turned off",
    1: "AVCC with external capacitor at AREF pin",
    3: "Internal 1.1V Voltage Reference with external capacitor at AREF pin"
}

ADC_ICS = {
    0: "ADC0",
    1: "ADC1",
    2: "ADC2",
    3: "ADC3",
    4: "ADC4",
    5: "ADC5",
    6: "ADC6",
    7: "ADC7",
    8: "ADC8",
    14: "1.1V (VBG)",
    15: "0V (GND)"
}

ADC_PRESCALER = {
    0: "2",
    1: "2",
    2: "4",
    3: "8",
    4: "16",
    5: "32",
    6: "64",
    7: "128"
}

ADC_ATS = {
    0: "Free Running mode",
    1: "Analog Comparator",
    2: "External Interrupt Request 0",
    3: "Timer/Counter0 Compare Match A",
    4: "Timer/Counter0 Overflow",
    5: "Timer/Counter1 Compare Match B",
    6: "Timer/Counter1 Overflow",
    7: "Timer/Counter1 Capture Event"
}

# Dropdown box creation

spn_ADC_VRS = create_spinner(ADC_VRS)
spn_ADC_ICS = create_spinner(ADC_ICS)
spn_ADC_PRESCALER = create_spinner(ADC_PRESCALER)
spn_ADC_ATS = create_spinner(ADC_ATS)

# Switch Creation

swt_ADC_ADLAR = Switch()
swt_ADC_ADEN = Switch()
swt_ADC_ADATE = Switch()
swt_ADC_ADIE = Switch()
swt_ADC_DID0 = Switch()
swt_ADC_DID1 = Switch()
swt_ADC_DID2 = Switch()
swt_ADC_DID3 = Switch()
swt_ADC_DID4 = Switch()
swt_ADC_DID5 = Switch()


# Tab Creation

def adc_tab_start(self, btn):
    from microcontrollers.Atmega168p.Modules.analog_to_digital_converter.adc_codegen import adc_set_status
    adc_tab = TabbedPanelItem(text="ADC")  # create tabbed panel
    grid = GridLayout(cols=2)  # Store the content in a grid layout

    # UI Generation

    create_spinner_ui("Voltage Reference Selection", spn_ADC_VRS, grid)
    create_spinner_ui("Input Channel Selection", spn_ADC_ICS, grid)
    create_spinner_ui("Prescaler Selection", spn_ADC_PRESCALER, grid)
    create_spinner_ui("Auto-trigger Selection", spn_ADC_ATS, grid)
    create_switch_ui("Left Adjust Result", swt_ADC_ADLAR, grid)
    create_switch_ui("ADC Enable", swt_ADC_ADEN, grid)
    create_switch_ui("ADC Auto-trigger Enable", swt_ADC_ADATE, grid)
    create_switch_ui("ADC Interrupt Enable", swt_ADC_ADIE, grid)
    create_switch_ui("Digital Input Disable ADC0", swt_ADC_DID0, grid)
    create_switch_ui("Digital Input Disable ADC1", swt_ADC_DID1, grid)
    create_switch_ui("Digital Input Disable ADC2", swt_ADC_DID2, grid)
    create_switch_ui("Digital Input Disable ADC3", swt_ADC_DID3, grid)
    create_switch_ui("Digital Input Disable ADC4", swt_ADC_DID4, grid)
    create_switch_ui("Digital Input Disable ADC5", swt_ADC_DID5, grid)

    # Put Content in Tab and make it available

    adc_tab.content = grid
    self.add_widget(adc_tab)
    adc_set_status(1)
