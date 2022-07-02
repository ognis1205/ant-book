import sys
from traceback import format_exc


class my_property:
    def __init__(self, get_func=None, set_func=None, del_func=None, doc=None):
        self.get_func = get_func
        self.set_func = set_func
        self.del_func = del_func
        if doc is None and get_func is not None:
            doc = get_func.__doc__
        self.__doc__ = doc
    
    def __get__(self, obj, objtype=None):
        if not self.get_func:
            raise AttributeError("can't get attribute")
        return self.get_func(obj)
    
    def __set__(self, obj, value):
        if not self.set_func:
            raise AttributeError("can't set attribute")
        return self.set_func(obj, value)

    def __delete__(self, obj):
        if not self.del_func:
            raise AttributeError("can't delete attribute")
        self.del_func(obj)

    def getter(self, get_func):
        return type(self)(get_func, self.set_func, self.del_func, self.__doc__)

    def setter(self, set_func):
        return type(self)(self.get_func, set_func, self.del_func, self.__doc__)

    def delete(self, del_func):
        return type(self)(self.get_func, self.set_func, del_func, self.__doc__)


class my_staticmethod:
    def __init__(self, func, doc=None):
        self.func = func
        if not doc:
            doc = self.func.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        return self.func


class my_classmethod:
    def __init__(self, func, doc=None):
        self.func = func
        if not doc:
            doc = func.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype):
        def wrap(*args, **kwargs):
            return self.func(objtype, *args, **kwargs)
        return wrap


class Test:
    def __init__(self, name):
        self._name = name

    @my_staticmethod
    def add(x, y):
        return x + y

    @my_classmethod
    def fromName(clazz, name):
        return clazz(name)

    @my_property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f'Test({self.name})'


def main():
    test = Test('N/A')
    print(test.name)
    test.name = 'ognis1205'
    print(test)
    print(test.add(1, 2))
    print(Test.add(1, 2))
    test = Test.fromName('fromName')
    print(test)
    test = test.fromName('fromInstance')
    print(test)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
