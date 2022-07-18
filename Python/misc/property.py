import sys
from traceback import format_exc


class my_property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self._fset = fset
        self._fget = fget
        self._fdel = fdel
        if not doc and fget:
            self.__doc__ = fget.__doc__
        else:
            self.__doc__ = doc

    def __get__(self, obj, objtype):
        if not self._fget:
            raise AttributeError('getter is not defined')
        else:
            return self._fget(obj)

    def __set__(self, obj, value):
        if not self._fset:
            raise AttributeError('setter is not defined')
        else:
            return self._fset(obj, value)

    def __delete__(self, obj):
        if not self._fdel:
            raise AttributeError('delete is not defined')
        else:
            return self._fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self._fset, self._fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self._fget, fset, self._fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self._fget, self._fset, fdel, self.__doc__)


class my_staticmethod:
    def __init__(self, func, doc=None):
        self._func = func
        if not doc and func:
            self.__doc__ = func.__doc__
        else:
            self.__doc__ = doc

    def __get__(self, obj, objtype):
        return self._func


class my_classmethod:
    def __init__(self, func, doc=None):
        self._func = func
        if not doc and func:
            self.__doc__ = func.__doc__
        else:
            self.__doc__ = doc

    def __get__(self, obj, objtype):
        def wrap(*args, **kwargs):
            return self._func(objtype, *args, **kwargs)
        return wrap


class Test:
    def __init__(self):
        self._data = None

    @my_staticmethod
    def static(x):
        return x * 2

    @my_classmethod
    def clazz(cls, x):
        return f'{cls.__name__}: {x}'

    @my_property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


def main():
    test = Test()
    print(f'test: {test.data}')
    test.data = 'test'
    print(f'test: {test.data}')
    print(f'test: {test.static(2)}')
    print(f'test: {Test.static(2)}')
    print(f'test: {test.clazz(2)}')


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
