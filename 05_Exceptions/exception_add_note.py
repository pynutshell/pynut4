try:
    try:
        # intentional div-by-zero (for demonstration)
        1 / 0

        # unintentional TypeError (comment out previous line to see change in exception handling)
        1 / "0"

    except ZeroDivisionError as zde:
        zde.add_note("This was intentional")
        raise
    except Exception as e:
        e.add_note("This wasn't intentional")
        raise

except Exception as e:
    # flag unintentional exceptions for attention
    if "This was intentional" not in getattr(e, "__notes__", []):
        e.add_note("Needs attention!!!")
    raise
