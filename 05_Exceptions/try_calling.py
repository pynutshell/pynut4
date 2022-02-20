# Accidentally hides any error case where AttributeError is raised inside
# the sought-after method, silently returning default in those cases.
# This may easily hide bugs in other code.
def trycalling(obj, attrib, default, *args, **kwds):
    try:
        return getattr(obj, attrib)(*args, **kwds)
    except AttributeError:
        return default

# This implementation of trycalling separates the getattr call, placed
# in the try clause and therefore guarded by the handler in the except
# clause, from the call of the method, placed in the else clause and
# therefore free to propagate any exception.
def trycalling(obj, attrib, default, *args, **kwds):
    try:
        method = getattr(obj, attrib)
    except AttributeError:
        return default
    else:
        return method(*args, **kwds)
