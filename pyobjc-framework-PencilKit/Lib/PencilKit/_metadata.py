# This file is generated by objective.metadata
#
# Last update: Sat May 11 12:13:54 2024
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
constants = """$PKAppleDrawingTypeIdentifier$PKInkTypeCrayon$PKInkTypeFountainPen$PKInkTypeMarker$PKInkTypeMonoline$PKInkTypePen$PKInkTypePencil$PKInkTypeWatercolor$"""
enums = """$PKContentVersion1@1$PKContentVersion2@2$PKContentVersion3@3$PKEraserTypeBitmap@1$PKEraserTypeFixedWidthBitmap@2$PKEraserTypeVector@0$"""
misc.update(
    {
        "PKContentVersion": NewType("PKContentVersion", int),
        "PKEraserType": NewType("PKEraserType", int),
    }
)
misc.update({"PKInkType": NewType("PKInkType", str)})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"PKDrawing", b"initWithData:error:", {"arguments": {3: {"type_modifier": b"o"}}})
    r(
        b"PKStrokePath",
        b"enumerateInterpolatedPointsInRange:strideByDistance:usingBlock:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PKStrokePath",
        b"enumerateInterpolatedPointsInRange:strideByParametricStep:usingBlock:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PKStrokePath",
        b"enumerateInterpolatedPointsInRange:strideByTime:usingBlock:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("PKDrawing", b"initWithData:error:")
objc.registerNewKeywordsFromSelector("PKDrawing", b"initWithStrokes:")
objc.registerNewKeywordsFromSelector("PKEraserTool", b"initWithEraserType:")
objc.registerNewKeywordsFromSelector("PKEraserTool", b"initWithEraserType:width:")
objc.registerNewKeywordsFromSelector("PKFloatRange", b"initWithLowerBound:upperBound:")
objc.registerNewKeywordsFromSelector("PKInk", b"initWithInkType:color:")
objc.registerNewKeywordsFromSelector("PKInkingTool", b"initWithInk:width:")
objc.registerNewKeywordsFromSelector("PKInkingTool", b"initWithInkType:color:")
objc.registerNewKeywordsFromSelector("PKInkingTool", b"initWithInkType:color:width:")
objc.registerNewKeywordsFromSelector(
    "PKStroke", b"initWithInk:strokePath:transform:mask:"
)
objc.registerNewKeywordsFromSelector(
    "PKStroke", b"initWithInk:strokePath:transform:mask:randomSeed:"
)
objc.registerNewKeywordsFromSelector(
    "PKStrokePath", b"initWithControlPoints:creationDate:"
)
objc.registerNewKeywordsFromSelector(
    "PKStrokePoint", b"initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:"
)
objc.registerNewKeywordsFromSelector(
    "PKStrokePoint",
    b"initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:secondaryScale:",
)
expressions = {}

# END OF FILE
