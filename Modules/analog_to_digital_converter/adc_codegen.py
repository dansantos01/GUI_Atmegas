from Modules.analog_to_digital_converter.adc_ui import *


# Registers

admux = Register("ADMUX", "00000000")
adcsra = Register("ADCSRA", "00000000")
adcsrb = Register("ADCSRB", "00000000")
didr0 = Register("DIDR0", "00000000")

# Tab Status

adc_OPEN = False


def adc_is_open():
    return adc_OPEN


def adc_set_status(status):
    global adc_OPEN
    if status == 1:
        adc_OPEN = True
    else:
        adc_OPEN = False


# Code Generation

def adc_vrs_convert(value):
    binary = decimal_to_bit(value, 2)

    # REFS1
    change_target_bit(binary[0], admux, '7')
    # REFS0
    change_target_bit(binary[1], admux, '6')


def adc_ics_convert(value):
    binary = decimal_to_bit(value, 4)

    # MUX3
    change_target_bit(binary[0], admux, '3')
    # MUX2
    change_target_bit(binary[1], admux, '2')
    # MUX1
    change_target_bit(binary[2], admux, '1')
    # MUX0
    change_target_bit(binary[3], admux, '0')


def adc_presc_convert(value):
    binary = decimal_to_bit(value, 3)

    # ADPS2
    change_target_bit(binary[0], adcsra, '2')
    # ADPS1
    change_target_bit(binary[1], adcsra, '1')
    # ADPS0
    change_target_bit(binary[2], adcsra, '0')


def adc_ats_convert(value):
    binary = decimal_to_bit(value, 3)

    # ADTS2
    change_target_bit(binary[0], adcsrb, '2')
    # ADTS1
    change_target_bit(binary[1], adcsrb, '1')
    # ADTS0
    change_target_bit(binary[2], adcsrb, '0')


def switch_convert():
    admux.set('5') if swt_ADC_ADLAR.active else admux.clear('5')
    adcsra.set('7') if swt_ADC_ADEN.active else adcsra.clear('7')
    adcsra.set('5') if swt_ADC_ADATE.active else adcsra.clear('5')
    adcsra.set('3') if swt_ADC_ADIE.active else adcsra.clear('3')
    didr0.set('0') if swt_ADC_DID0.active else didr0.clear('0')
    didr0.set('1') if swt_ADC_DID1.active else didr0.clear('1')
    didr0.set('2') if swt_ADC_DID2.active else didr0.clear('2')
    didr0.set('3') if swt_ADC_DID3.active else didr0.clear('3')
    didr0.set('4') if swt_ADC_DID4.active else didr0.clear('4')
    didr0.set('5') if swt_ADC_DID5.active else didr0.clear('5')


def get_adc():
    adc_vrs_convert(get_value(ADC_VRS, spn_ADC_VRS.text))
    adc_ics_convert(get_value(ADC_ICS, spn_ADC_ICS.text))
    adc_presc_convert(get_value(ADC_PRESCALER, spn_ADC_PRESCALER.text))
    adc_ats_convert(get_value(ADC_ATS, spn_ADC_ATS.text))
    switch_convert()

    print(admux.print_code())
    print(adcsra.print_code())
    print(adcsrb.print_code())
    print(didr0.print_code())
