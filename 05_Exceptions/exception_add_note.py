try:
    1/0
except ZeroDivisionError as zde:
    zde.add_note("This was intentional")
    raise
