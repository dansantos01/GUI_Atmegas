class Register:
    def __init__(self, name, reg_data):
        self.name = name
        self.reg_data = reg_data

    def get(self):
        return self.reg_data

    def set(self, target):
        output_string = ""
        target = str(7 - int(target))
        for x in range(len(self.reg_data)):
            if str(x) in target:
                output_string += "1"
            else:
                output_string += self.reg_data[x]
        self.reg_data = output_string

    def clear(self, target):
        output_string = ""
        target = str(7 - int(target))
        for x in range(len(self.reg_data)):
            if str(x) in target:
                output_string += "0"
            else:
                output_string += self.reg_data[x]
        self.reg_data = output_string

    def print_code(self):
        return self.name + " |= 0b" + self.reg_data



