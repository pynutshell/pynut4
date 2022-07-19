import gc

gc_was_enabled = gc.isenabled()
if gc_was_enabled:
    gc.collect()
    gc.disable()

# insert some time-critical code here

if gc_was_enabled:
    gc.enable()


import contextlib

@contextlib.contextmanager
def gc_disabled():
    gc_was_enabled = gc.isenabled()
    if gc_was_enabled:
        gc.collect()
        gc.disable()

    try:
        yield
    finally:
        if gc_was_enabled:
            gc.enable()


with gc_disabled():
    # insert some time-critical code here
    ...
