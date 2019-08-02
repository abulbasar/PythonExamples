Use the following to find libraries and version of the libraries that are available in your system right now.
$ pip freeze

Install the libraries mentioned in requirements.txt
$ python -m pip install -r requirements.txt


Create package
$ python setup.py bdist_wheel

You should see a few new files created under your project directory.
build: build package information.
dist: Contains your .whl file. A WHL file is a package saved in the Wheel format,
which is the standard built-package format used for Python distributions.
You can directly install a .whl file using pip install some_package.whl on your system
project.egg.info: An egg package contains compiled bytecode, package information,
dependency links, and captures the info used by the setup.py test command when running tests.


Create a new project
$ mkdir /tmp/test-package
$ cd /tmp/test-package

Create a virtual environment
$ python -m venv myenv

Install the package you created
$ python -m pip install <full path for the wheel file>

Test whether the module methods are accessible
$ python -c "from myapp import app, db; app.ping()"