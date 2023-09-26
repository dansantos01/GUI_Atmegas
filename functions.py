from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanel


def get_value(var, match):
    for k in var:
        if var[k] == match:
            return k


def get_value_k(var, match, k):
    for k in var:
        if var[k] == match:
            return k


def decimal_to_bit(integer, register):
    binary = ""
    binary = bin(integer).replace("0b", "") [::-1]
    print(binary)
    print(register)
    for x in range(len(register)):
        if x < len(binary):
            if binary[x] == "1":
                register[x] = True
            else:
                register[x] = False
        else:
            register[x] = False


def create_label(location, text):
    location.add_widget(Label(text=text, size_hint_x=.3))


def create_spinner_ui(description, spinner, location):
    location.add_widget(Label(text=description, size_hint_x=.3))
    location.add_widget(spinner)


def spn_values_update(spn, values_vect):
    spn.values = values_vect.values()


def create_spinner(values_dict):
    spn = Spinner(
        text="Empty",
        text_autoupdate=True,
        values="Empty",
        size_hint=(0.5, 0.2),
        pos_hint={"center_x": .5, "center_y": .5}
    )
    spn.values = values_dict.values()
    return spn


def create_switch_ui(description, switch, location):
    location.add_widget(Label(text=description, size_hint_x=.7))
    switch.size_hint_x = 0.3
    location.add_widget(switch)




