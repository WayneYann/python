# Pip install local package

A user created package on the local machine can be installed with `pip` to make
it accessible to other Python files on the system. The approach described below
is useful when developing your own package and you want to test it before
deploying to other users. Visit the links in the Resources section for detailed
information about this process.

## Directory structure

As an example, a package named `vehicles` contains the file structure shown
below. The top level directory `vehicles` is the root of the repository while
the sub-directory `vehicles` is the actual Python module. 

```
vehicles/
|-- vehicles/
|   |-- __init__.py
|   |-- cars.py
|   |-- trucks.py
|-- setup.py
```

Functions for the module can be located in sub-modules such as the `cars.py`
and `trucks.py` files. For example, the following function is contained within
the `cars` file:

```
def mustang():
    print('Ford Mustang 1999')
```

The `__init__.py` file is used to import all the functions in each sub-module
as shown below.

```
from vehicles.cars import *
from vehicles.trucks import *
```

The `setup.py` file is the main configuration file used by pip. Below is an
example of its contents.

```
from setuptools import setup

setup(name='vehicles',
      version='0.1',
      description='A vehicles package with info about automobiles',
      url='http://github.com/user/repo-vehicles',
      author='Van Rossum',
      author_email='mail@example.com',
      license='MIT',
      packages=['vehicles'],
      zip_safe=False)
```

## Pip install

To install the package on the local system as a symlink, the `--editable` pip
command can be used. This makes changes to the source files immediately
available to other files on the system.

```
pip install -e <path/to/package>
```

## Resources

See the following links for more information about the `pip install -e` command
and `setup.py`:

- http://python-packaging.readthedocs.io/en/latest/minimal.html
- https://pip.pypa.io/en/stable/reference/pip_install/

