from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanel
from kivy.uix.textinput import TextInput
from register import *


def get_value(var, match):
    for k in var:
        if var[k] == match:
            return k


def get_value_k(var, match, k):
    for k in var:
        if var[k] == match:
            return k


def decimal_to_bit(value, length):
    binary = ""
    binary = bin(value).replace("0b", "")
    for n in (range(length - len(binary))):
        binary = "0" + binary
    return binary


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


def create_textinput_ui(description, textinput, location):
    location.add_widget(Label(text=description, size_hint_x=.3))
    location.add_widget(textinput)


def create_label_ui(description, label, location):
    location.add_widget(Label(text=description, size_hint_x=.3))
    location.add_widget(label)


def change_target_bit(status, target_reg, target_bit):
    if status == '1':
        target_reg.set(target_bit)
    else:
        target_reg.clear(target_bit)

