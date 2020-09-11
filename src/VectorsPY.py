from math import sin,cos,radians,atan,degrees
class Vector3:
    xcor = 'i'
    ycor = 'j'
    zcor = 'k'   
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    #Arithmatice Definations
    
    def __add__(self,other):
        return self.x+other.x,self.y+other.y,self.z+other.z
    def __sub__(self,oth):
        return self.x-oth.x,self.y - oth.y,self.z - oth.z

    #Logical Definations
    
    def __le__(self,other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z
    def __ge__(self,other):
        return self.x >= other.y and self.y>=other.y and self.z >= other.z
    def __gt__(self,other):
        return self.x>other.x and self.y > other.y and self.z > other.z
    def __lt__(self,other):
        return self.x < other.x and self.y<other.y and self.z < self.z
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __ne__(self,other):
        return self.x != other.x or self.y != other.y or self.z != other.z
    def __invert__(self):
        return ~self.x,~self.y,~self.z

    #Class Functions

    def magnitude(self):
        '''returns magnitude of Vector3 object'''
        return (self.x**2 + self.y **2 + self.z **2)**0.5
    def unitvector(self):
        '''returns a new Vector3 unit vector in the\ndirection of given Vector3 object'''
        return Vector3(self.x/self.magnitude(),self.y/self.magnitude(),self.z/self.magnitude())
    def value(self):
        '''returns value of a Vector3 object in form of a tuple'''
        return self.x ,self.y,self.z
    def cartesian(self):
        '''returns value of a Vector3 object in cartisian form'''
        return '{0}{1} {y}{2}{3} {z}{4}{5}'.format(self.x,self.xcor,self.y,self.ycor,self.z,self.zcor,y = '+' if self.y > 0 else '',z= '+' if self.z > 0 else '' )                                       

class Vector2:
    xcor = 'i'
    ycor = 'j'   
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    #Arithmatice Definations
    
    def __add__(self,other):
        return self.x+other.x,self.y+other.y
    def __sub__(self,oth):
        return self.x-oth.x,self.y - oth.y

    #Logical Definations
    
    def __le__(self,other):
        return self.x <= other.x and self.y <= other.y
    def __ge__(self,other):
        return self.x >= other.y and self.y>=other.y
    def __gt__(self,other):
        return self.x>other.x and self.y > other.y
    def __lt__(self,other):
        return self.x < other.x and self.y<other.y
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __ne__(self,other):
        return self.x != other.x or self.y!= other.y
    def __invert__(self):
        return ~self.x,~self.y

    #Class Functions

    def magnitude(self):
        '''returns magnitude of Vector2 object'''
        return (self.x**2 + self.y **2)**0.5
    def unitvector(self):
        '''returns a new Vector2 unit vector in the\ndirection of given Vector2 object'''
        return Vector2(self.x/self.magnitude(),self.y/self.magnitude())
    def value(self):
        '''returns value of a Vector2 object in form of a tuple'''
        return self.x ,self.y
    def cartesian(self):
        '''returns value of a Vector2 object in cartisian form'''
        return '{0}{1} {y}{2}{3}'.format(self.x,self.xcor,self.y,self.ycor,y = '+' if self.y > 0 else '')
    def direction(self):
        '''returns direction of Vector Object in terms of angles (degree measure)\nmade from positive x-axis'''
        return degrees(atan(self.x/self.y))

def Vector(iterable):
    '''converts values from array-type iterable (list,tuple)\nto Vector2 or Vector3 accordingly'''
    if len(iterable) == 2:
        for i in iterable:
            if isinstance(i,(int,float)) ==False:
                raise ValueError('iterable has inappropriate values for vector defination')
        return Vector2(iterable[0],iterable[1])
    elif len(iterable) == 3:
        for i in iterable:
            if isinstance(i,(int,float))==False:
                raise ValueError('iterable has inappropriate values for vector defination')
        return Vector3(iterable[0],iterable[1],iterable[2])
    else:
        raise TypeError('invalid number of elements in iterable')
    
def dot(a,b,angle = 0):
    '''gives Dot (Scaler) product of 2 vectors'''
    if (isinstance(a,(Vector2,Vector3))) and (isinstance(b,(Vector2,Vector3))):
        return a.magnitude()*b.magnitude()*cos(radians(angle))
    else:
        raise NonVectorDataError('invalid type for dot product, not a vector')

def cross(a,b,angle = 0):
    '''gives cross (Vector) product of 2 vectors'''
    if (isinstance(a,(Vector2,Vector3))) and (isinstance(b,(Vector2,Vector3))):
        return a.magnitude()*b.magnitude()*sin(radians(angle))
    else:
        raise NonVectorDataError('invalid type for cross product, not a vector')

    
#Custom Error Definations

class NonVectorDataError(Exception):
    def __init__(self,message=None):
        __cause__ = message

class CCWarning(Warning):
    def __init__(self,message=None):
        __cause__= message
