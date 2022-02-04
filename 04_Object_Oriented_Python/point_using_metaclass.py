import collections
import warnings
class MetaBunch(type):
    """
    Metaclass for new and improved "Bunch": implicitly defines
    __slots__, __init__ and __repr__ from variables bound in
    class scope.
    A class statement for an instance of MetaBunch (i.e., for a
    class whose metaclass is MetaBunch) must define only
    class-scope data attributes (and possibly special methods, but
    NOT __init__ and __repr__).  MetaBunch removes the data
    attributes from class scope, snuggles them instead as items in
    a class-scope dict named __dflts__, and puts in the class a
    __slots__ with those attributes' names, an __init__ that takes
    as optional named arguments each of them (using the values in
    __dflts__ as defaults for missing ones), and a __repr__ that
    shows the repr of each attribute that differs from its default
    value (the output of __repr__ can be passed to __eval__ to make
    an equal instance, as per usual convention in the matter, if
    each non-default-valued attribute respects the convention too).
    The order of data attributes remains the same as in the class body.
    """
    def __new__(mcl, classname, bases, classdict):
        """ Everything needs to be done in __new__, since
            type.__new__ is where __slots__ are taken into account.
        """
        # define as local functions the __init__ and __repr__ that
        # we'll use in the new class
        def __init__(self, **kw):
            """ __init__ is simple : first, set attributes without
                explicit values to their defaults; then, set those
                explicitly passed in kw.
            """
            for k in self.__dflts__:
                if not k in kw:
                    setattr(self, k, self.__dflts__[k])
            for k in kw:
                setattr(self, k, kw[k])
        def __repr__(self):
            """ __repr__ is "clever": shows only attributes that
                differ from default values, for compactness.
            """
            rep = [f'{k}={getattr(self, k)!r}'
                    for k in self.__dflts__
                    if getattr(self, k) != self.__dflts__[k]
                  ]
            return f"{classname}({', '.join(rep)})"
        # build the newdict that we'll use as class-dict for the
        # new class
        newdict = { '__slots__':[],
            '__dflts__': {},
            '__init__' :__init__, '__repr__' :__repr__, }
        for k in classdict:
            if k.startswith('__') and k.endswith('__'):
                # dunder methods: copy to newdict, or warn
                # about conflicts
                if k in newdict:
                    warnings.warn(
                        f'Cannot set attr {k!r} in bunch-class {classname!r}')
                else:
                    newdict[k] = classdict[k]
            else:
                # class variables, store name in __slots__, and
                # name and value as an item in __dflts__
                newdict['__slots__'].append(k)
                newdict['__dflts__'][k] = classdict[k]
        # finally delegate the rest of the work to type.__new__
        return super().__new__(
                     mcl, classname, bases, newdict)


class Bunch(metaclass=MetaBunch):
    """ For convenience: inheriting from Bunch can be used to get
        the new metaclass (same as defining metaclass= yourself).
    """
    pass


class Point(Bunch):
    """ A Point has x and y coordinates, defaulting to 0.0,
        and a color, defaulting to 'gray'-and nothing more,
        except what Python and the metaclass conspire to add,
        such as __init__ and __repr__
    """
    x = 0.0
    y = 0.0
    color = 'gray'


# example uses of class Point
q = Point()
print(q)                    # prints: Point()
p = Point(x=1.2, y=3.4)
print(p)
