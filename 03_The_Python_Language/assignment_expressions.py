import re

# := in an if/elif statement

re_match = re.match(r'Name: (\S)', input_string)
if re_match:
    print(re_match.groups(1))

# collapsed version using :=
if (re_match := re.match(r'Name: (\S)', input_string)):
    print(re_match.groups(1))


# := in a while statement

current_value = get_next_value()
while current_value is not None:
    if not filter_condition(current_value):
        continue   # BUG! Current_value is not advanced to next
    # ... do some work with current_value ...
    current_value = get_next_value()

# collapsed version using :=
while (current_value := get_next_value()) is not None:
    if not filter_condition(current_value):
        continue   # no bug, current_value gets advanced in while statement
    # ... do some work with current_value ...


# := in a list comprehension filter
def safe_int(s):
    try:
        return int(s)
    except Exception:
        return None


input_strings = ['1', '2', 'a', '11']

valid_int_strings = [safe_int(s) for s in input_strings
                     if safe_int(s) is not None]

# collapsed version using :=
valid_int_strings = [int_s for s in input_strings
                     if (int_s := safe_int(s)) is not None]

