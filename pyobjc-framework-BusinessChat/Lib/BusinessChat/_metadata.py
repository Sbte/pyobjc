# This file is generated by objective.metadata
#
# Last update: Sat May 11 12:20:50 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$BCParameterNameBody$BCParameterNameGroup$BCParameterNameIntent$"""
enums = """$BCChatButtonStyleDark@1$BCChatButtonStyleLight@0$"""
misc.update({"BCChatButtonStyle": NewType("BCChatButtonStyle", int)})
misc.update({"BCParameterName": NewType("BCParameterName", str)})
misc.update({})

objc.registerNewKeywordsFromSelector("BCChatButton", b"initWithCoder:")
objc.registerNewKeywordsFromSelector("BCChatButton", b"initWithStyle:")
expressions = {}

# END OF FILE
