# VectorsPY

Python module to use Vector2 and Vector3 (as in Unity Game Engine - C#) in Python.

- Create Vector2 objects for 2D Vectors (x and y coordinate system)
- Create Vector3 objects for 3D Vectors (x,y and z coordinate system)
- Add, Subtract 2 Vectors
- Get Magnitude of Vector Object<br>
and much more

## What's New In this Version
- Function ```dot()``` to calculate Dot (Scaler) Product.
- Function ```cross()``` to calculate Cross (Vector) Product.
- ```.direction()``` attribute to get dirction of Vector2.

## Installation

Using pip - 
```
pip install VectorsPY
```


## General
VectorsPY has 2 Major classes
- **Vector2** For 2D Vectors
- **Vector3** For 3D Vectors


## Usage

To create new 2D Vector use **Vector2** class.
```python
new2DVector = Vector2(x_value, y_value)
```
Similarly use **Vector3** to create 3D Vector.
```python
new3DVector = Vector3(x_value, y_value, z_value)
```
<br>

To create Vector from List, Tuple (iterables) use Miscellaneous function **Vector**. This will return a new ***Vector2*** or ***Vector3*** object based on iterable passed as argument.
```python

iterable1 = [1,2] 
newVector1 = Vector(iterable1) #new Vector2 object from list

iterable2 = (4,5)
newVector2 = Vector(iterable2) #new Vector2 object from tuple


iterable3 = (3,4,5)
newVector3 = Vector(iterable3) #new Vector3 object from tuple

iterable4 = [3,4,5]
newVector4 = Vector(iterable4) #new Vector3 object from list
```


