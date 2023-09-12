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




