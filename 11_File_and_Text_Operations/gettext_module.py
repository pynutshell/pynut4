from gettext import *

try:
    _
except NameError:
    def _(s): return s

def greet():
    print(_('Hello world'))

greet()
