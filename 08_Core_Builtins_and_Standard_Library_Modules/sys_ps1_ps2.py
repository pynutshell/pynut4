import sys


class Ps1:
    def __init__(self):
        self.p = 0
    def __str__(self):
        self.p += 1
        return f'[{self.p}]>>> '

class Ps2:
    def __str__(self):
        return f'[{sys.ps1.p}]... '


sys.ps1 = Ps1()
sys.ps2 = Ps2()
