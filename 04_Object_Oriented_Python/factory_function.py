class SpecialCase:
    def amethod(self):
        print('special')

class NormalCase:
    def amethod(self):
        print('normal')

def appropriate_case(isnormal=True):
    if isnormal:
        return NormalCase()
    else:
        return SpecialCase()

aninstance = appropriate_case(isnormal=False)
aninstance.amethod()                  # prints: special
