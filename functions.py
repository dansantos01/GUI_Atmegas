from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner


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


def create_spinner_ui(description, values_vect, vect_size, location):
    location.add_widget(Label(text=description, size_hint_x=.3))


def spn_values_update(spn, values_vect):
    spn.values = values_vect.values()




