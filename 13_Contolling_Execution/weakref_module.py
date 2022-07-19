import weakref


class Tracking:
    _instances_dict = weakref.WeakValueDictionary()

    def __init__(self):
        Tracking._instances_dict[id(self)] = self

    @classmethod
    def instances(cls):
        return cls._instances_dict.values()



tracked = [Tracking() for _ in range(10)]

print(len(list(Tracking.instances())))

del tracked[3]
print(len(list(Tracking.instances())))
