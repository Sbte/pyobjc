# This file is generated by objective.metadata
#
# Last update: Sun Mar 22 14:59:24 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$PKAppleDrawingTypeIdentifier@^{__CFString=}$"""
enums = """$$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"PKDrawing", b"initWithData:error:", {"arguments": {3: {"type_modifier": b"o"}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE