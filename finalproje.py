# OOP 
# class
# attributes
# abstraction and encopsulation
# inheritance
# overriding and polymorfizim

from abc import ABC, abstractmethod
class Shape(ABC):
    # Shape= super class / abstract class
    @abstractmethod
    def area(self):pass
    @abstractmethod
    def perimeter(self):pass

    def toString(self): pass

class Square(Shape):
    #sub class
    def __init__(self,edge):
        self.__edge=edge   #encapsülation
    def area(self):
        result= self.__edge**2
        print("square area:", result)
    def perimeter(self):
        result=self.__edge*4
        print("square perimeter:",result)

# overrid and polymorfizim
def toString(self):
    print("square edge:", self.__edge)

# shape child
class circle(Shape):
    PI=3.14
    def __init__(self,radius):
        self.__radius=radius

    def area(self):
        result=self.PI* self.__radius**2
        print("circle area:",result)
  
    def perimeter(self):
        result=2*self.PI*self.__radius
        print("circle perimeter:",result)

    def toString(self):
        print("circle radius", self.__radius)


c=circle(5)
c.area()
c.perimeter()
c.toString()


s=Square(4)
s.area()
s.perimeter()
s.toString()
