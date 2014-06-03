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

