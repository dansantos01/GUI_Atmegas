from microcontrollers.Atmega168p.Modules.timer_counter_1.timer1_dropdowns import *

# registers

tccr1a = Register("TCCR1A", "00000000")
tccr1b = Register("TCCR1B", "00000000")
timsk1 = Register("TIMSK1", "00000000")
tifr1 = Register("TIFR1", "00000000")

# bits

icnc1 = False
ices1 = False
icie1 = False
ocie1b = False
ocie1a = False
toie1 = False

# Open or not

timer1_OPEN = False


def timer1_is_open():
    return timer1_OPEN


# TAB CREATION

opt_spn = Spinner(text="Normal", text_autoupdate=True)
opt_spn.values = ["Normal"]
coma_spn = Spinner(text="Normal port operation, OC1B disconnected.", text_autoupdate=True)
coma_spn.values = coma_nPWM_spn.values
comb_spn = Spinner(text="Normal port operation, OC1B disconnected.", text_autoupdate=True)
comb_spn.values = comb_nPWM_spn.values


def timer1_tab_start(self, btn):
    print("Timer 1 has been opened")
    timer1_t = TabbedPanelItem(text="TIMER1")
    tc = GridLayout(cols=2)
    tc.add_widget(Label(text="Wave Generation Mode:", size_hint_x=.3))
    WGM_spn.bind(text=update_spinner)
    tc.add_widget(WGM_spn)
    tc.add_widget(Label(text="Mode Options:", size_hint_x=.3))
    tc.add_widget(opt_spn)
    tc.add_widget(Label(text="Compare Output Mode A:", size_hint_x=.3))
    tc.add_widget(coma_spn)
    tc.add_widget(Label(text="Compare Output Mode B:", size_hint_x=.3))
    tc.add_widget(comb_spn)
    tc.add_widget(Label(text="Clock Select:", size_hint_x=.3))
    tc.add_widget(clk_spn)
    tc.add_widget(Label(text="Input Capture Noise Canceler"))
    icnc_switch = Switch()
    icnc_switch.bind(active=icnc_callback)
    tc.add_widget(icnc_switch)
    tc.add_widget(Label(text="Input Capture Edge Select"))
    ices_switch = Switch()
    ices_switch.bind(active=ices_callback)
    tc.add_widget(ices_switch)
    tc.add_widget(Label(text="Timer/Counter1, Input Capture Interrupt Enable"))
    icie_switch = Switch()
    icie_switch.bind(active=icie_callback)
    tc.add_widget(icie_switch)
    tc.add_widget(Label(text="Timer/Counter1, Output Compare A Match Interrupt Enable"))
    ocie1a_switch = Switch()
    ocie1a_switch.bind(active=ocie1a_callback)
    tc.add_widget(ocie1a_switch)
    tc.add_widget(Label(text="Timer/Counter1, Output Compare B Match Interrupt Enable"))
    ocie1b_switch = Switch()
    ocie1b_switch.bind(active=ocie1b_callback)
    tc.add_widget(ocie1b_switch)
    tc.add_widget(Label(text=" Timer/Counter1, Overflow Interrupt Enable"))
    toie_switch = Switch()
    toie_switch.bind(active=toie_callback)
    tc.add_widget(toie_switch)

    timer1_t.content = tc
    self.add_widget(timer1_t)
    global timer1_OPEN
    timer1_OPEN = True


def icnc_callback(instance, value):
    global icnc1
    icnc1 = value


def ices_callback(instance, value):
    global ices1
    ices1 = value


def icie_callback(instance, value):
    global icie1
    icie1 = value


def ocie1a_callback(instance, value):
    global ocie1a
    ocie1a = value


def ocie1b_callback(instance, value):
    global ocie1b
    ocie1b = value


def toie_callback(instance, value):
    global toie1
    toie1 = value


def update_spinner(obj, text):
    global opt_spn
    global coma_spn
    global comb_spn

    if TIMER1_WGM[0] == text:
        opt_spn.values = ["Normal"]
        coma_spn.values = coma_nPWM_spn.values
        comb_spn.values = comb_nPWM_spn.values
    if TIMER1_WGM[1] == text:
        opt_spn.values = pcPWM_spn.values
        coma_spn.values = coma_pcPWM_spn.values
        comb_spn.values = comb_pcPWM_spn.values
    if TIMER1_WGM[2] == text:
        opt_spn.values = CTC_spn.values
        coma_spn.values = coma_nPWM_spn.values
        comb_spn.values = comb_nPWM_spn.values
    if TIMER1_WGM[3] == text:
        opt_spn.values = fPWM_spn.values
        coma_spn.values = coma_fPWM_spn.values
        comb_spn.values = comb_fPWM_spn.values
    if TIMER1_WGM[4] == text:
        opt_spn.values = pfcPWM_spn.values
        coma_spn.values = coma_pcPWM_spn.values
        comb_spn.values = comb_pcPWM_spn.values


def clk_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(3 - len(binary))):
        binary = "0" + binary
    # CS12
    if binary[0] == "1":
        tccr1b.set("2")
    else:
        tccr1b.clear("2")
    # CS11
    if binary[1] == "1":
        tccr1b.set("1")
    else:
        tccr1b.clear("1")
    # CS10
    if binary[2] == "1":
        tccr1b.set("0")
    else:
        tccr1b.clear("0")


def wgm_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(4 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr1b.set("4")
    else:
        tccr1b.clear("4")
    if binary[1] == "1":
        tccr1b.set("3")
    else:
        tccr1b.clear("3")
    if binary[2] == "1":
        tccr1a.set("1")
    else:
        tccr1a.clear("1")
    if binary[3] == "1":
        tccr1a.set("0")
    else:
        tccr1a.clear("0")


def coma_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(2 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr1a.set("7")
    else:
        tccr1a.clear("7")
    if binary[1] == "1":
        tccr1a.set("6")
    else:
        tccr1a.clear("6")


def comb_bit(value):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(2 - len(binary))):
        binary = "0" + binary
    if binary[0] == "1":
        tccr1a.set("5")
    else:
        tccr1a.clear("5")
    if binary[1] == "1":
        tccr1a.set("4")
    else:
        tccr1a.clear("4")


def timer1_bits():
    global icnc1
    global ices1
    global icie1
    global ocie1b
    global ocie1a
    global toie1

    tccr1b.set("7") if icnc1 else tccr1b.clear("7")
    tccr1b.set("6") if ices1 else tccr1b.clear("6")
    timsk1.set("5") if icie1 else timsk1.clear("5")
    timsk1.set("2") if ocie1b else timsk1.clear("2")
    timsk1.set("1") if ocie1a else timsk1.clear("1")
    timsk1.set("0") if toie1 else timsk1.clear("0")


def get_timer1():
    timer1_bits()
    clk_bit(get_value(CLK1_sel, clk_spn.text))
    wgm = get_value(TIMER1_WGM, WGM_spn.text)
    if wgm == 0 or wgm == 2:
        comb_bit(get_value(COM1B_nPWM, comb_spn.text))
        coma_bit(get_value(COM1A_nPWM, coma_spn.text))
        if wgm == 0:
            wgm_bit(0)
        else:
            wgm_bit(get_value_k(TIMER1_CTC, opt_spn.text, 16))
    elif wgm == 3:
        comb_bit(get_value(COM1B_fPWM, comb_spn.text))
        coma_bit(get_value(COM1A_fPWM, coma_spn.text))
        wgm_bit(get_value_k(TIMER1_fPWM, opt_spn.text, 16))

    else:
        comb_bit(get_value(COM1B_pcPWM, comb_spn.text))
        coma_bit(get_value(COM1A_pcPWM, coma_spn.text))
        if wgm == 2:
            wgm_bit(get_value_k(TIMER1_pcPWM, opt_spn.text, 16))
        else:
            wgm_bit(get_value_k(TIMER1_pfcPWM, opt_spn.text, 16))

    print(tccr1a.print_code())
    print(tccr1b.print_code())
    print(timsk1.print_code())
    print(tifr1.print_code())


