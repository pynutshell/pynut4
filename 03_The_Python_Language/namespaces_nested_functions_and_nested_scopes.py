def percent1(a, b, c):
    def pc(x, total=a+b+c):
        return (x*100.0) / total
    print('Percentages are:', pc(a), pc(b), pc(c))


def percent2(a, b, c):
    def pc(x):
        return (x*100.0) / (a+b+c)
    print('Percentages are:', pc(a), pc(b), pc(c))


def make_adder(augend):
    def add(addend):
        return addend+augend
    return add

add5 = make_adder(5)
add9 = make_adder(9)

print(add5(100))   # prints 105
print(add9(100))   # prints 109


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c1 = make_counter()
c2 = make_counter()
print(c1(), c1(), c1())  # prints: 1 2 3
print(c2(), c2())  # prints: 1 2
print(c1(), c2(), c1())  # prints: 4 3 5
