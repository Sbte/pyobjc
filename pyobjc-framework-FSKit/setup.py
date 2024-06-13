"""
Wrappers for the "FSKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "11.0a0"

setup(
    name="pyobjc-framework-FSKit",
    description="Wrappers for the framework FSKit on macOS",
    min_os_level="15.0",
    packages=["FSKit"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreMedia>=" + VERSION,
        "pyobjc-framework-CoreAudio>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
