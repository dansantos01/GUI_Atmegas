from functions import *


# Dropdown text

USART0_CSIZE = {
    0: "5-bit",
    1: "6-bit",
    2: "7-bit",
    3: "8-bit",
    7: "9-bit"
}

USART0_MSEL = {
    0: "Asynchronous USART",
    1: "Synchronous USART"
}

USART0_PARM = {
    0: "Disabled",
    2: "Enabled, Even Parity",
    3: "Enabled, Odd Parity"
}

USART0_SBS = {
    0: "1-bit",
    1: "2-bit"
}

USART0_CLKPOL = {
    0: "Transmitted Data Changed on Rising XCKn Edge, Received data Sampled on Falling XCKn Edge",
    1: "Transmitted Data Changed on Falling XCKn Edge, Received data Sampled on Rising XCKn Edge"
}

# Dropdown box creation

spn_USART0_CSIZE = create_spinner(USART0_CSIZE)
spn_USART0_MSEL = create_spinner(USART0_MSEL)
spn_USART0_PARM = create_spinner(USART0_PARM)
spn_USART0_SBS = create_spinner(USART0_SBS)
spn_USART0_CLKPOL = create_spinner(USART0_CLKPOL)

# Switch Creation

swt_USART0_U2X = Switch()
swt_USART0_MCPM = Switch()
swt_USART0_RXCIE = Switch()
swt_USART0_TXCIE = Switch()
swt_USART0_UDRIE = Switch()
swt_USART0_RXEN = Switch()
swt_USART0_TXEN = Switch()

# Text Input Creation

txtinp_freq = TextInput()
txtinp_baudrate = TextInput()
txtinp_baudrate.disabled = True

# Dynamic Changes

spn_USART0_CLKPOL.disabled = True


def mode_disables(obj, text):
    if not USART0_MSEL[0] == spn_USART0_MSEL.text:
        spn_USART0_CLKPOL.disabled = False
        swt_USART0_U2X.active = False
        swt_USART0_U2X.disabled = True
    else:
        spn_USART0_CLKPOL.text = USART0_CLKPOL[0]
        spn_USART0_CLKPOL.disabled = True
        swt_USART0_U2X.disabled = False


def check_parameters_freq(obj, text):
    print("somehting")
    if not text.isdigit():
        print("can't work with this")
        txtinp_baudrate.disabled = True
    else:
        print("something else")
        txtinp_baudrate.disabled = False


def check_parameters_baudrate(obj, text):
    if not text.isdigit():
        print("can't work with this")

    baudrate = float(text)
    freq = float(txtinp_freq.text) * 1000000
    br_limit = [0, 0]
    # For Asynchronous Normal mode

    if swt_USART0_U2X.active:
        br_limit = calc_minmax_baudrate(freq, 8, 1, 4096)
    if not swt_USART0_U2X.active and spn_USART0_CLKPOL.disabled:
        br_limit = calc_minmax_baudrate(freq, 16, 1, 4096)
    if not swt_USART0_U2X.active and not spn_USART0_CLKPOL.disabled:
        br_limit = calc_minmax_baudrate(freq, 2, 1, 4096)

    print(br_limit[0])
    print("<- min max->")
    print(br_limit[1])

    # For Asychronous


spn_USART0_MSEL.bind(text=mode_disables)
txtinp_freq.bind(text=check_parameters_freq)
txtinp_baudrate.bind(text=check_parameters_baudrate)

# Tab Creation


def usart0_tab_start(self, btn):
    from Modules.usart_0.usart0_codegen import usart0_set_status
    usart0_tab = TabbedPanelItem(text="USART0")  # Create Tabbed Panel
    grid = GridLayout(cols=2)  # Store the content in a grid layout

    # UI Generation

    create_spinner_ui("Mode Selection", spn_USART0_MSEL, grid)
    create_spinner_ui("Character Size", spn_USART0_CSIZE, grid)
    create_spinner_ui("Parity Mode", spn_USART0_PARM, grid)
    create_spinner_ui("Stop Bit Select", spn_USART0_SBS, grid)
    create_spinner_ui("Clock Polarity", spn_USART0_CLKPOL, grid)
    create_switch_ui("Double Speed", swt_USART0_U2X, grid)
    create_switch_ui("RX Complete Interrupt Enable", swt_USART0_RXCIE, grid)
    create_switch_ui("TX Complete Interrupt Enable", swt_USART0_TXCIE, grid)
    create_switch_ui("Receiver Enable", swt_USART0_RXEN, grid)
    create_switch_ui("Transmitter Enable", swt_USART0_TXEN, grid)
    create_switch_ui("USART Data Register Empty Interrupt Enable", swt_USART0_UDRIE, grid)
    create_switch_ui("Multi-processor Communication Mode", swt_USART0_MCPM, grid)
    create_textinput_ui("Insert your Microcontroller Clock Frequency (in MHz)", txtinp_freq, grid)
    create_textinput_ui("Insert desired Baud Rate ( in bps)", txtinp_baudrate, grid)
    # create_label_ui("Error (%)", )
    # Put Content in Tab and make it available

    usart0_tab.content = grid
    self.add_widget(usart0_tab)
    usart0_set_status(1)


