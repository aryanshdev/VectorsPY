***********
VectorsPY
***********

VectorsPY is utility module for using Physics Vectors in Python.
It allows you to define 2D and 3D Vectors in Python.
It also provides multiple methods that can be used along Vectors to make their usage more useful and meaning


.. contents:: Skip To Topic
    :local:

Getting Started
###############

To start using VectorsPY on your system, you need to install it using ``pip``

.. code-block:: console

     pip install VectorsPY

You can visit `PYPI <https://pypi.org/project/VectorsPY/>`_ to get older versions of module or to install it using wheel


Start Using VectorsPY
#####################

To start using VectorsPY in your project, you need to import it using conventional commands

``import VectorsPY``

To import as Variable 


``import VectorsPY as <alias name>``

To import any specific function/class use


``from VectorsPY import <Function/Class Name>(,<Second Function/Class Name,...)``

Creating Vector Object
#######################

VectorsPY has to main classes for Vector defination - 

1. **Vector2** For **2D Vectors**
2. **Vector3** For **3D Vectors**

To create new 2D Vector use **Vector2** class.
::
   new2DVector = Vector2(x_value, y_value)

Similarly use **Vector3** to create 3D Vector.
:: 
  new3DVector = Vector3(x_value, y_value, z_value)


To create Vector from List, Tuple (iterables) use Miscellaneous function **Vector**. This will return a new **Vector2** or **Vector3** object based on iterable passed as argument.
::
    iterable1 = [1,2] 
    newVector1 = Vector(iterable1) #new Vector2 object from list

    iterable2 = (4,5)
    newVector2 = Vector(iterable2) #new Vector2 object from tuple


    iterable3 = (3,4,5)
    newVector3 = Vector(iterable3) #new Vector3 object from tuple

    iterable4 = [3,4,5]
    newVector4 = Vector(iterable4) #new Vector3 object from list
    
Operations on Vectors
######################
Arithmetic Operations
----------------------
Vector Objects can be added and Subtracted in the same way as other DataTypes in Python
using ``+`` and ``-`` operator respectively. These Operations return a tuple of **cartesian sum**.
.. warning::
    Addition and Subtraction here is not a Vector Addition or Substraction,
    and only provides correct result
    for Cartesian Addition.

::
    v = Vector3(1,2,3)
    v1 = Vector3(4,5,6)
    print(v+v1)   #outputs => (5,7,9)
    print(v-v1)   #outputs => (3,3,3)

Logical Operations
------------------
Vector objects can be compared with each other using several Logical Operations in the same way as other DataTypes in
Python.

- == returns True if both Vectors have all same value, else False
- != returns True if both Vectors have atleast one diffrent coordinate value,else False
- < returns True if all values of First are smaller than the values of Second Vector, else False
- > returns True if all values of First are greater than the values of Second Vector, else False
- <= returns True if all values of First are smaller or equal than the values of Second Vector, else False
- >= returns True if all values of First are greater or equal than the values of Second Vector, else False
::
    v = Vector3(1,2,3)
    v1 = Vector3(2,5,6)
    v2 = Vector([1,2,3])

    v == v1   # False
    v != v1   # True
    v > v1    #False
    v < v1    #True
    v <= v1   #True
    v >= v1   #False

Attributes and Methods
########################

Vector objects have following Attributes :-

- xcor 
- ycor
- zcor *(only for Vector3)*
- x
- y
- z *(only for Vector3)*

Here, **xcor**, **ycor**, **zcor** are used to represent Vectors in Cartesian form and have value **i**, **j**, **k** repectively.

And **x**, **y**, **z** represent values for Vector in x,y,z axises repectively and are *needed to be defined during Vector defination*.

The following functions are defined for both **Vector2** and **Vector3** class :-

- ``.value()``
- ``.cartisian()``
- ``.magnitude()``
- ``.unitvector()``

**Vector2** class specific functions :-

- ``.direction()``

All These Methods are discussed in upcoming Sections

Attributes
##########

Alike other class Attributes, attributes of Vector Classes can be accessed by ``.`` in between Vector instance and attribute.
This can also be used to manipulate the values.
::
    vector = Vector2(69,420)
    x = vector.x            #x = 69
    vector.y = x            #now vectors has value (69,69)

    print(vector.xcor)      #outputs => i

Methods
#######