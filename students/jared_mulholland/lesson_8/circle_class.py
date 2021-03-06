"""
The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter, 
and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:
    Compute the circle’s area
    Print the circle and get something nice
    Be able to add two circles together
    Be able to compare two circles to see which is bigger
    Be able to compare to see if there are equal
    (follows from above) be able to put them in a list and sort them

You will use:
    properties
    a classmethod
    a define a bunch of “special methods”

General Instructions:
    1. For each step, write a couple of unit tests that test the new features.
    2. Run these tests (and they will fail the first time)
    3. Add the code required for your tests to pass

"""

from math import pi

#Step 1: 
"""
create class called Circle – it’s signature should look like:
c = Circle(the_radius)
The radius is a required parameter (can’t have a circle without one!)
"""

class Circle_1(object):
    """has instance attribute for radius"""
    def __init__(self, radius):
        self.radius = radius


#Step 2:
"""
Add a “diameter” property, so the user can get the diameter of the circle
"""
class Circle_2(object):
    """has instance attribute for radius"""
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius*2

#Step 3:
"""
Set up the diameter property so that the user can set the 
diameter of the circle:
"""
class Circle_3(object):
    """diameter can be set as property"""
    def __init__(self, radius):
        self.radius = radius
                    
    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, d):
        radius = d/2
        self.radius = radius

#Step 4:
"""Add an area property so the user can get the area of the circle"""
class Circle_4(object):
    """diameter can be set as property"""
    def __init__(self, radius):
        self.radius = radius
                    
    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, d):
        radius = d/2
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius**2

#Step 5:
"""Add an alternate constructor that lets 
the user create a Circle directly with the diameter:"""

class Circle(object):
    """diameter can be set as property"""
    def __init__(self, radius):
        self.radius = radius
        self._diameter = radius * 2
        self._area = pi * radius**2
                
    @property
    def diameter(self):
        return self.radius*2
    
    @diameter.setter
    def diameter(self, d):
        radius = d/2
        self.radius = radius
    
    @property
    def area(self):
        return pi * self.radius**2    

    @classmethod
    def from_diameter(cls, d):
        radius = d/2
        return Circle(radius)

    """Step 6: add __str__ and __repr__ methods to class"""
    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    """Step 7: add numeric protocol to class"""
    def __add__(self,other):
        return Circle(self.radius + other.radius)

    def __mul__(self,n):
        return Circle(self.radius * n)

    def __rmul__(self,n):
        return Circle(n * self.radius)    

    """Step 8: make classes sortable"""

    def __lt__(self, other):
        return self.radius < other.radius

    



        
        


