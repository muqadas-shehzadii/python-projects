class Robot:
    def __eq__(self,other):
        if isinstance(other,Human):
            return NotImplemented
class Human:
    def __eq__(self,other):
        if isinstance(other,Robot):
            return True
r = Robot()
h = Human()
print(r==h)
print(h==r)