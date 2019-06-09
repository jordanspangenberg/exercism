import re


class Phone(object):
    def __init__(self, phone_number):
        self.number = self.verify(phone_number)
        self.area_code = self.number[0:3]

    def verify(self, ph_str):
        pattern = re.compile('(\d)')
        number = ''.join(pattern.findall(ph_str))
        number = number[1:] if int(number[0]) == 1 else number
        if int(number[0]) < 2 or int(number[3]) < 2 or len(number) != 10:
            raise ValueError(f'Invalid Phone Number {ph_str}')
        return number

    def pretty(self):
        return f'({self.number[0:3]}) {self.number[3:6]}-{self.number[6:]}'
