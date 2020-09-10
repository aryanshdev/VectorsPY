import setuptools

with open('README.md','r') as f:
    long_description = f.read()

setuptools.setup(
    name = 'Vector',
    version='0.0.1',
    author = 'Aryansh Gupta',
    author_email = 'Aryanshappmaker@gmail.com',
    description = 'Python Module to use Vectors',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/aryansh-1/Vector',
    python_requires = '>=3.1',
)