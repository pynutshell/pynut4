import typing

Identifier = int

# for the purposes of type checking, use TypeAlias:
Identifier: typing.TypeAlias = int

# Python will treat this like a standard str assignment
TBDType = 'ClassNotDefinedYet'

# indicates that this is actually a forward reference to a class
TBDType: typing.TypeAlias = 'ClassNotDefinedYet'
