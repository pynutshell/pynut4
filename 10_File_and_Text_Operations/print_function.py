def redirect(func: Callable, *a, **k) -> (str, Any):
    """redirect(func, *a, **k) -> (func's results, return value)
    func is a callable emitting results to standard output.
    redirect captures the results as a str and returns a pair
    (output string, return value).
    """
    import sys, io
    save_out = sys.stdout
    sys.stdout = io.StringIO()
    try:
        retval = func(*args, **kwds)
        return sys.stdout.getvalue(), retval
    finally:
        sys.stdout.close()
        sys.stdout = save_out
