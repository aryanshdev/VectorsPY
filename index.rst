***********
VectorsPY
***********


VectorsPY is utility module for using Physics Vectors in Python.
It allows you to define 2D and 3D Vectors in Python.
It also provides multiple methods that can be used along Vectors to make their usage more useful amd meaning


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
1. **Vector2** For 2D Vectors
2. **Vector3** For 3D Vectors

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

Properties and Methods
########################

By default, Vector objects have following Attributes :-

- xcor 
- ycor
- zcor *(only for Vector3)*
- x
- y
- z *(only for Vector3)*

Here, **xcor**, **ycor**, **zcor** are used to represent Vectors in Cartesian form and have value **i**, **j**, **k** repectively.

And **x**, **y**, **z** represent values for Vector in x,y,z axises repectively and are *needed to be defined during Vector defination*.
