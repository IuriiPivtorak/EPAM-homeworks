#!/usr/bin/env python3.6


# Декоратор - это обертка для функции, которая позволяет
# трансформировать внутреннюю функцию, как мы хотим.
# Дескриптор делает похожее, переписывая протоколы __get__,
# __set__ и __delete__, поэтому сделав атрибут класса экземпляром
# декскриптора, мы можем воздейстовать на этот атрибут.
class prop(object):
    """Descriptor that triggers function calls
    when accessing attribute.
    """

    def __init__(self, getting=None, setting=None, deleting=None):
        self.get = getting
        self.set = setting
        self.delet = deleting

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.get is None:
            raise AttributeError("can't understand attribute")
        return self.get(obj)

    def __set__(self, obj, value):
        if self.set is None:
            raise AttributeError("can't set attribute")
        self.set(obj, value)

    def __delete__(self, obj):
        if self.delet is None:
            raise AttributeError("can't delete attribute")
        self.delet(obj)

    def getter(self, getting):
        return type(self)(getting, self.set, self.delet)

    def setter(self, setting):
        return type(self)(self.get, setting, self.delet)

    def deleter(self, deleting):
        return type(self)(self.get, self.set, delet)


class Something:
    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        return self.x ** 2

    @attr.setter
    def attr(self, update):
        self.x = update
        return self.x

if __name__ == '__main__':
    s = Something(10)
    print(s.attr)
    s.attr = 3
    print(s.attr)
