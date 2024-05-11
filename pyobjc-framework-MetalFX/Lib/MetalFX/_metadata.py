# This file is generated by objective.metadata
#
# Last update: Sat May 11 12:07:58 2024
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
constants = """$$"""
enums = """$MTLFXSpatialScalerColorProcessingModeHDR@2$MTLFXSpatialScalerColorProcessingModeLinear@1$MTLFXSpatialScalerColorProcessingModePerceptual@0$"""
misc.update(
    {
        "MTLFXSpatialScalerColorProcessingMode": NewType(
            "MTLFXSpatialScalerColorProcessingMode", int
        )
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"MTLFXSpatialScalerDescriptor", b"supportsDevice:", {"retval": {"type": b"Z"}})
    r(
        b"MTLFXTemporalScalerDescriptor",
        b"isAutoExposureEnabled",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MTLFXTemporalScalerDescriptor",
        b"isInputContentPropertiesEnabled",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MTLFXTemporalScalerDescriptor",
        b"isReactiveMaskTextureEnabled",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MTLFXTemporalScalerDescriptor",
        b"setAutoExposureEnabled:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MTLFXTemporalScalerDescriptor",
        b"setInputContentPropertiesEnabled:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MTLFXTemporalScalerDescriptor",
        b"setReactiveMaskTextureEnabled:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"MTLFXTemporalScalerDescriptor", b"supportsDevice:", {"retval": {"type": b"Z"}})
    r(b"NSObject", b"colorProcessingMode", {"required": True, "retval": {"type": b"q"}})
    r(b"NSObject", b"colorTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"colorTextureFormat", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"colorTextureUsage", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"depthTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"depthTextureFormat", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"depthTextureUsage", {"required": True, "retval": {"type": b"Q"}})
    r(
        b"NSObject",
        b"encodeToCommandBuffer:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"exposureTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"fence", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"inputContentHeight", {"required": True, "retval": {"type": b"Q"}})
    r(
        b"NSObject",
        b"inputContentMaxScale",
        {"required": True, "retval": {"type": b"f"}},
    )
    r(
        b"NSObject",
        b"inputContentMinScale",
        {"required": True, "retval": {"type": b"f"}},
    )
    r(b"NSObject", b"inputContentWidth", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"inputHeight", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"inputWidth", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"isDepthReversed", {"required": True, "retval": {"type": b"Z"}})
    r(b"NSObject", b"jitterOffsetX", {"required": True, "retval": {"type": b"f"}})
    r(b"NSObject", b"jitterOffsetY", {"required": True, "retval": {"type": b"f"}})
    r(b"NSObject", b"motionTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"motionTextureFormat", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"motionTextureUsage", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"motionVectorScaleX", {"required": True, "retval": {"type": b"f"}})
    r(b"NSObject", b"motionVectorScaleY", {"required": True, "retval": {"type": b"f"}})
    r(b"NSObject", b"outputHeight", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"outputTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"outputTextureFormat", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"outputTextureUsage", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"outputWidth", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"preExposure", {"required": True, "retval": {"type": b"f"}})
    r(b"NSObject", b"reactiveMaskTexture", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"reactiveTextureUsage",
        {"required": True, "retval": {"type": b"Q"}},
    )
    r(b"NSObject", b"reset", {"required": True, "retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"setColorTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setDepthReversed:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSObject",
        b"setDepthTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setExposureTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setFence:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setInputContentHeight:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Q"}}},
    )
    r(
        b"NSObject",
        b"setInputContentWidth:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Q"}}},
    )
    r(
        b"NSObject",
        b"setJitterOffsetX:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"f"}}},
    )
    r(
        b"NSObject",
        b"setJitterOffsetY:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"f"}}},
    )
    r(
        b"NSObject",
        b"setMotionTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setMotionVectorScaleX:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"f"}}},
    )
    r(
        b"NSObject",
        b"setMotionVectorScaleY:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"f"}}},
    )
    r(
        b"NSObject",
        b"setOutputTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setPreExposure:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"f"}}},
    )
    r(
        b"NSObject",
        b"setReactiveMaskTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setReset:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Z"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
