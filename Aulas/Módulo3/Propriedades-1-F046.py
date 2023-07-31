class Prop:
    def __init__(self, x = None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self,value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
        
    @x.deleter
    def x(self):
        self._x = None


prop = Prop(100)
print(prop.x)
prop.x = 10
print(prop.x)
del(prop.x)
print(prop.x)

