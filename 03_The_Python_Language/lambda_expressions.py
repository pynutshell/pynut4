a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 3
high = 7
print(list(filter(lambda x: low <= x < high, a_list)))    # returns: [3, 4, 5, 6]


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def within_bounds(value, low=3, high=7):
    return low <= value < high
print(list(filter(within_bounds, a_list)))           # returns: [3, 4, 5, 6]
