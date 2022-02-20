# This file is generated by objective.metadata
#
# Last update: Fri Feb 18 14:16:08 2022
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
constants = """$SCStreamFrameInfoContentRectKey$SCStreamFrameInfoContentScaleKey$SCStreamFrameInfoDirtyRectsKey$SCStreamFrameInfoDisplayTimeKey$SCStreamFrameInfoScaleFactorKey$SCStreamFrameInfoStatusKey$"""
enums = """$SCFrameStatusFrameBlank@2$SCFrameStatusFrameComplete@0$SCFrameStatusFrameIdle@1$SCFrameStatusFrameStarted@4$SCFrameStatusFrameStopped@5$SCFrameStatusFrameSuspended@3$SCStreamErrorAttemptToConfigState@-3810$SCStreamErrorAttemptToStartStreamState@-3807$SCStreamErrorAttemptToStopStreamState@-3808$SCStreamErrorAttemptToUpdateFilterState@-3809$SCStreamErrorEntitlements@-3803$SCStreamErrorFailedApplicationConnectionInterrupted@-3805$SCStreamErrorFailedApplicationConnectionInvalid@-3804$SCStreamErrorFailedNoMatchingApplicationContext@-3806$SCStreamErrorFailedToStart@-3802$SCStreamErrorFailedToStartCaptureStack@-3811$SCStreamErrorInvalidParameter@-3812$SCStreamErrorNoCaptureSource@-3815$SCStreamErrorNoDisplayList@-3814$SCStreamErrorNoWindowList@-3813$SCStreamErrorRemovingStream@-3816$SCStreamErrorUserDeclined@-3801$"""
misc.update(
    {
        "SCStreamErrorCode": NewType("SCStreamErrorCode", int),
        "SCFrameStatus": NewType("SCFrameStatus", int),
    }
)
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"stream:didStopWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"SCShareableContent",
        b"getShareableContentExcludingDesktopWindows:onScreenWindowsOnly:completionHandler:",
        {
            "arguments": {
                2: {"type": b"Z"},
                3: {"type": b"Z"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"SCShareableContent",
        b"getShareableContentExcludingDesktopWindows:onScreenWindowsOnlyAboveWindow:completionHandler:",
        {
            "arguments": {
                2: {"type": b"Z"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"SCShareableContent",
        b"getShareableContentExcludingDesktopWindows:onScreenWindowsOnlyBelowWindow:completionHandler:",
        {
            "arguments": {
                2: {"type": b"Z"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"SCShareableContent",
        b"getShareableContentWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SCStream",
        b"startCaptureWithFrameHandler:completionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"^{opaqueCMSampleBuffer=}"},
                        },
                    }
                },
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(
        b"SCStream",
        b"stopWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SCStream",
        b"updateContentFilter:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SCStream",
        b"updateStreamConfiguration:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(b"SCStreamConfiguration", b"scalesToFit", {"retval": {"type": b"Z"}})
    r(b"SCStreamConfiguration", b"setScalesToFit:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SCStreamConfiguration", b"setShowsCursor:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SCStreamConfiguration", b"showsCursor", {"retval": {"type": b"Z"}})
    r(b"SCWindow", b"isOnScreen", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
