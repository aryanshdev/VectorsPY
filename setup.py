import setuptools

with open('README.md','r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'VectorsPY',
    version='1.0.0',
    author = 'Aryansh Gupta',
    author_email = 'Aryanshappmaker@gmail.com',
    description = 'Python Module to allow the use of Vectors',
    py_modules = ["VectorsPY"],
    package_dir = {'':'src'},
    long_description = long_description+'<br>More Documentaion can be found on [Github](https://github.com/aryansh-1/VectorsPY)',
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/aryansh-1/VectorsPY',
    python_requires = '>=3.1',
)
