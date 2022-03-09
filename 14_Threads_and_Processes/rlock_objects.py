import threading

lock = threading.RLock()
global_state = []

def recursive_function(some, args):
    with lock:  # acquires lock, guarantees release at end
        # ...modify global_state...
        if more_changes_needed(global_state):
            recursive_function(other, args)

