if condition1(x):
    process1(x)
elif x > 23 or (x < 5 and condition2(x)):
    pass  # nothing to be done in this case
elif condition3(x):
    process3(x)
else:
    process_default(x)
