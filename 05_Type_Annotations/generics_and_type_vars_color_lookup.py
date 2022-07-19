color_lookup: dict[str, tuple[int, int, int]] = {}

color_lookup['red'] = (255, 0, 0)
color_lookup['red'][2]


# statements that generate mypy errors
color_lookup[0]
# error: Invalid index type "int" for "dict[str, tuple[int, int, int]]"; expected type "str"
color_lookup['red'] = (255, 0, 0, 0)
# error: Incompatible types in assignment (expression has type "tuple[int, int, int, int]", target has type "tuple[int, int, int]")
