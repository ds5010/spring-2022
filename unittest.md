
# Unittest

## References

* [unittest](https://docs.python.org/3/library/unittest.html) -- python.org
  * this is extensive documentation of a built-in python library
  * it includes links to many other related tools and techniques
  * among those tools is the third party [pytest](https://docs.pytest.org/) framework
* [basic example](https://docs.python.org/3/library/unittest.html#basic-example)
  * this demonstrates a small subset of the tools that suffice for most users -- including us!

## To create a test module...

* subclass unittest.TestCase
* add methods whose names begin with "test"
  * the naming convention informs the test runner which tests to run
* tests involve a call to one or more of:
  * assertEqual()
  * assertTrue() or assertFalse()
  * assertRaises() -- to verify that a specific exception gets raised

## Running tests

Running from the command line should work for us

* `python -m file.py` -- runs file.py module as a script
* `python -m tests/*.py` -- runs each module in ./tests as a script
* [unittest command-line interface](https://docs.python.org/3/library/unittest.html#command-line-interface)

## Test discovery

* [Test discovery](https://docs.python.org/3/library/unittest.html#unittest-test-discovery) -- python.org
  * a set of rules for automatically finding the code that should run during testing
* Rules address the concept of [modules](https://docs.python.org/3/tutorial/modules.html#tut-modules)
  * A Python module is a file containing Python definitions and statements 
  * The file name is the module name with the suffix .py
  * Within a module, the module’s name is available as the value (a string) of the global variable "__name__"
  * You import a module with the "import" statement
  * You can run modules as scripts, in which case the value of __name__ is set to the string "__main__"
  * There are rules on where the Python interpreter will look to find modules that you reference in code
* Rules address the concept of [packages](https://docs.python.org/3/tutorial/modules.html#packages)
  * A Python package is a collection of modules in a directory
  * An __init__.py file is required in that directory to make Python treat the directory as a package 
  * This prevents directories with a common name, such as "string", from unintentionally hiding valid modules that occur later on the module search path. 
