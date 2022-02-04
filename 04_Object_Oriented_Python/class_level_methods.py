# staticmethod example
class AClass(object):
    def astatic():
        print('a static method')
    astatic = staticmethod(astatic)
an_instance = AClass()
AClass.astatic()                    # prints: a static method
an_instance.astatic()               # prints: a static method

# classmethod example
class ABase(object):
    def aclassmet(cls):
        print('a class method for', cls.__name__)
    aclassmet = classmethod(aclassmet)
class ADeriv(ABase):
    pass

b_instance = ABase()
d_instance = ADeriv()
ABase.aclassmet()               # prints: a class method for ABase
b_instance.aclassmet()          # prints: a class method for ABase
ADeriv.aclassmet()              # prints: a class method for ADeriv
d_instance.aclassmet()          # prints: a class method for ADeriv