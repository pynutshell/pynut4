import threading

c = threading.Condition()

# thread function waits on Condition c
def reacting_thread_function(s):
    with c:
        while not is_ok_state(s):
            c.wait()
        do_some_work_using_state(s)

# thread function modifies state, and notifies all waiting threads
def modifying_thread_function(s):
    with c:
        do_something_that_modifies_state(s)
        c.notify()    # or, c.notify_all()
    # no need to call c.release(), exiting 'with' intrinsically does that
