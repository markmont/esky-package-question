# Question

This was asked at https://stackoverflow.com/questions/24021485/esky-not-including-sub-module

I have a medium-size PyQT5 desktop application that has been working fine with py2app.  I want to incorporate [Esky](https://pypi.python.org/pypi/esky) so that the app can update itself, but the app terminates during startup (before displaying the main window) with a log entry that says "HelloApp Error" (where "HelloApp" is the name of my application).

I've created a small test case that reproduces the problem that is available at https://github.com/markmont/esky-package-question

The test-case app has the following structure:

    HelloApp/
        HelloApp/
            HelloApp.py
            helloform
                __init__.py
        setup.py

setup.py contains:

    from esky import bdist_esky
    from distutils.core import setup
    
    PY2APP_OPTIONS = {
        'argv_emulation': True,
        'includes': [ 'sip', 'PyQt5', 'helloform' ],
        'qt_plugins': [ '*' ]
        }
    ESKY_OPTIONS = {
        "freezer_module": "py2app",
        "freezer_options": PY2APP_OPTIONS,
        "includes": [ 'sip', 'PyQt5', 'helloform' ]
        }
    HelloApp = bdist_esky.Executable( "HelloApp/HelloApp.py", gui_only=True )
    
    setup(
        name='HelloApp',
        version = "2014060301",
        data_files=[],
        options = { "bdist_esky": ESKY_OPTIONS },
        scripts=[ HelloApp ]
    )

HelloApp.py contains the statement `from helloform import Form` -- this appears to be what is causing the app to fail to start with the error "HelloApp Error", as if I remove that statement and paste in the contents of helloform/__init__.py the application starts up and works properly.

Also, if I move everything into a single directory and adjust the paths in setup.py, then the problem does not occur -- Esky finds helloform.py (formerly named helloform/__init__.py), includes it, and the application starts up and works properly:

    HelloApp/
        HelloApp.py
        helloform.py  # formerly ./HelloApp/helloform/__init__.py
        setup.py

...but putting everything in single directory is not a scalable solution for a medium-to-large application.

There are no error messages in the output of `python setup.py bdist_esky` when the problem occurs, and I have not found the answer in the Esky documentation or in various examples on the web.

The full error from /var/log/system.log is:

    2014-06-03 13:03:07.100 HelloApp[14968]: HelloApp Error

I'm assuming that I'm not using Esky's `includes` option properly in setup.py, but I've got no clue as to how to fix this -- can anyone help?

Other possibly relevant details:  MacOS X 10.9 Mavericks, Python 2.7.6 (local build), qt-5.3.0 opensource, sip 4.16, PyQT 5.3.0 (GPL), py2app 0.8.1 [patched to support PyQT5](https://bitbucket.org/ronaldoussoren/py2app/pull-request/7/add-support-for-pyqt5-to-sip-recipe/diff), and the latest version of [Esky from GitHub](https://github.com/cloudmatrix/esky).

I'll update this, here, if I get a solution, as well as https://stackoverflow.com/questions/24021485/esky-not-including-sub-module


