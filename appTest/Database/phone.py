import random


class phone:
    def get_phone(self):
        value = random.choice(range(14595444557, 15985984564))
        return value

    def company(self):
        value = ""
        for i in range(8):
            val = random.randint(0x4e00, 0x9fbf)
            value=value+chr(val)
        return value

    def name(self):
        value = ""
        for i in range(3):
            val = random.randint(0x4e00, 0x9fbf)
            value = value + chr(val)
        return value
