def cross_product(seq1, seq2):
    if not seq1 or not seq2:
        raise ValueError('Sequence arguments must be non-empty')
    return [(x1, x2) for x1 in seq1 for x2 in seq2]

print(cross_product([1, 2, 3], [4, 5, 6]))

# no need to check for this error, Python will raise TypeError
print(cross_product(1, [4, 5, 6]))

# cross_product will raise ValueError
print(cross_product([1, 2, 3], []))
