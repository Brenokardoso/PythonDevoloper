class Foo:
    def __init__(self, x = None):
        self._x = x

    def __str__(self):
        return f"{self.__class__.__name__} --> {','.join([f'{chave}:{valor}' for chave,valor in self.__dict__.items()])}"
     
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self,value):
        self._x += value

    @x.deleter
    def x(self):
        self._x += -1
    

foo = Foo(10)
print(foo)
foo.x = 10
print(foo)
del(foo.x)
print(foo.x)
del(foo.x)
del(foo.x)
del(foo.x)
del(foo.x)
print(foo.x)