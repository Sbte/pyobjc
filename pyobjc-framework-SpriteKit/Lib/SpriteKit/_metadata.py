# This file is generated by objective.metadata
#
# Last update: Sun Aug  7 14:53:12 2022
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
enums = """$PHYSICSKIT_MINUS_GL_IMPORTS@1$SKActionTimingEaseIn@1$SKActionTimingEaseInEaseOut@3$SKActionTimingEaseOut@2$SKActionTimingLinear@0$SKAttributeTypeFloat@1$SKAttributeTypeHalfFloat@5$SKAttributeTypeNone@0$SKAttributeTypeVectorFloat2@2$SKAttributeTypeVectorFloat3@3$SKAttributeTypeVectorFloat4@4$SKAttributeTypeVectorHalfFloat2@6$SKAttributeTypeVectorHalfFloat3@7$SKAttributeTypeVectorHalfFloat4@8$SKBlendModeAdd@1$SKBlendModeAlpha@0$SKBlendModeMultiply@3$SKBlendModeMultiplyAlpha@7$SKBlendModeMultiplyX2@4$SKBlendModeReplace@6$SKBlendModeScreen@5$SKBlendModeSubtract@2$SKInterpolationModeLinear@1$SKInterpolationModeSpline@2$SKInterpolationModeStep@3$SKLabelHorizontalAlignmentModeCenter@0$SKLabelHorizontalAlignmentModeLeft@1$SKLabelHorizontalAlignmentModeRight@2$SKLabelVerticalAlignmentModeBaseline@0$SKLabelVerticalAlignmentModeBottom@3$SKLabelVerticalAlignmentModeCenter@1$SKLabelVerticalAlignmentModeTop@2$SKNodeFocusBehaviorFocusable@2$SKNodeFocusBehaviorNone@0$SKNodeFocusBehaviorOccluding@1$SKParticleRenderOrderDontCare@2$SKParticleRenderOrderOldestFirst@1$SKParticleRenderOrderOldestLast@0$SKRepeatModeClamp@1$SKRepeatModeLoop@2$SKSceneScaleModeAspectFill@1$SKSceneScaleModeAspectFit@2$SKSceneScaleModeFill@0$SKSceneScaleModeResizeFill@3$SKTextureFilteringLinear@1$SKTextureFilteringNearest@0$SKTileAdjacencyAll@255$SKTileAdjacencyDown@16$SKTileAdjacencyDownEdge@199$SKTileAdjacencyLeft@64$SKTileAdjacencyLeftEdge@31$SKTileAdjacencyLowerLeft@32$SKTileAdjacencyLowerLeftCorner@253$SKTileAdjacencyLowerLeftEdge@7$SKTileAdjacencyLowerRight@8$SKTileAdjacencyLowerRightCorner@127$SKTileAdjacencyLowerRightEdge@193$SKTileAdjacencyRight@4$SKTileAdjacencyRightEdge@241$SKTileAdjacencyUp@1$SKTileAdjacencyUpEdge@124$SKTileAdjacencyUpperLeft@128$SKTileAdjacencyUpperLeftCorner@247$SKTileAdjacencyUpperLeftEdge@28$SKTileAdjacencyUpperRight@2$SKTileAdjacencyUpperRightCorner@223$SKTileAdjacencyUpperRightEdge@112$SKTileDefinitionRotation0@0$SKTileDefinitionRotation180@2$SKTileDefinitionRotation270@3$SKTileDefinitionRotation90@1$SKTileHexFlatAdjacencyAll@63$SKTileHexFlatAdjacencyDown@8$SKTileHexFlatAdjacencyLowerLeft@16$SKTileHexFlatAdjacencyLowerRight@4$SKTileHexFlatAdjacencyUp@1$SKTileHexFlatAdjacencyUpperLeft@32$SKTileHexFlatAdjacencyUpperRight@2$SKTileHexPointyAdjacencyAdd@63$SKTileHexPointyAdjacencyLeft@32$SKTileHexPointyAdjacencyLowerLeft@16$SKTileHexPointyAdjacencyLowerRight@8$SKTileHexPointyAdjacencyRight@4$SKTileHexPointyAdjacencyUpperLeft@1$SKTileHexPointyAdjacencyUpperRight@2$SKTileSetTypeGrid@0$SKTileSetTypeHexagonalFlat@2$SKTileSetTypeHexagonalPointy@3$SKTileSetTypeIsometric@1$SKTransitionDirectionDown@1$SKTransitionDirectionLeft@3$SKTransitionDirectionRight@2$SKTransitionDirectionUp@0$SKUniformTypeFloat@1$SKUniformTypeFloatMatrix2@5$SKUniformTypeFloatMatrix3@6$SKUniformTypeFloatMatrix4@7$SKUniformTypeFloatVector2@2$SKUniformTypeFloatVector3@3$SKUniformTypeFloatVector4@4$SKUniformTypeNone@0$SKUniformTypeTexture@8$SKVIEW_AVAILABLE@1$"""
misc.update(
    {
        "SKLabelVerticalAlignmentMode": NewType("SKLabelVerticalAlignmentMode", int),
        "SKUniformType": NewType("SKUniformType", int),
        "SKParticleRenderOrder": NewType("SKParticleRenderOrder", int),
        "SKInterpolationMode": NewType("SKInterpolationMode", int),
        "SKTextureFilteringMode": NewType("SKTextureFilteringMode", int),
        "SKAttributeType": NewType("SKAttributeType", int),
        "SKBlendMode": NewType("SKBlendMode", int),
        "SKSceneScaleMode": NewType("SKSceneScaleMode", int),
        "SKNodeFocusBehavior": NewType("SKNodeFocusBehavior", int),
        "SKTileDefinitionRotation": NewType("SKTileDefinitionRotation", int),
        "SKTransitionDirection": NewType("SKTransitionDirection", int),
        "SKTileSetType": NewType("SKTileSetType", int),
        "SKLabelHorizontalAlignmentMode": NewType(
            "SKLabelHorizontalAlignmentMode", int
        ),
        "SKActionTimingMode": NewType("SKActionTimingMode", int),
        "SKRepeatMode": NewType("SKRepeatMode", int),
        "SKTileAdjacencyMask": NewType("SKTileAdjacencyMask", int),
    }
)
misc.update({})
misc.update({})
aliases = {"SK_AVAILABLE": "__OSX_AVAILABLE_STARTING", "SKColor": "NSColor"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"didApplyConstraintsForScene:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didBeginContact:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didEndContact:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didEvaluateActionsForScene:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didFinishUpdateForScene:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didSimulatePhysicsForScene:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setSubdivisionLevels:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"q"}}},
    )
    r(
        b"NSObject",
        b"setWarpGeometry:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"subdivisionLevels", {"required": True, "retval": {"type": b"q"}})
    r(
        b"NSObject",
        b"update:forScene:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"d"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"view:shouldRenderAtTime:",
        {
            "required": False,
            "retval": {"type": "Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": "d"}},
        },
    )
    r(b"NSObject", b"warpGeometry", {"required": True, "retval": {"type": b"@"}})
    r(b"SK3DNode", b"autoenablesDefaultLighting", {"retval": {"type": b"Z"}})
    r(b"SK3DNode", b"isPlaying", {"retval": {"type": b"Z"}})
    r(b"SK3DNode", b"loops", {"retval": {"type": b"Z"}})
    r(
        b"SK3DNode",
        b"projectPoint:",
        {
            "full_signature": b"<3f>@:<3f>",
            "retval": {"type": b"<3f>"},
            "arguments": {2: {"type": b"<3f>"}},
        },
    )
    r(
        b"SK3DNode",
        b"setAutoenablesDefaultLighting:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SK3DNode", b"setLoops:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SK3DNode", b"setPlaying:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SK3DNode",
        b"unprojectPoint:",
        {
            "full_signature": b"<3f>@:<3f>",
            "retval": {"type": b"<3f>"},
            "arguments": {2: {"type": b"<3f>"}},
        },
    )
    r(
        b"SKAction",
        b"animateWithNormalTextures:timePerFrame:resize:restore:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"SKAction",
        b"animateWithTextures:timePerFrame:resize:restore:",
        {"arguments": {4: {"type": b"Z"}, 5: {"type": b"Z"}}},
    )
    r(
        b"SKAction",
        b"animateWithWarps:times:restore:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"SKAction",
        b"customActionWithDuration:actionBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": sel32or64(b"f", b"d")},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKAction",
        b"followPath:asOffset:orientToPath:duration:",
        {"arguments": {3: {"type": b"Z"}, 4: {"type": b"Z"}}},
    )
    r(
        b"SKAction",
        b"followPath:asOffset:orientToPath:speed:",
        {"arguments": {3: {"type": b"Z"}, 4: {"type": b"Z"}}},
    )
    r(
        b"SKAction",
        b"performSelector:onTarget:",
        {"arguments": {2: {"sel_of_type": b"v@:"}}},
    )
    r(
        b"SKAction",
        b"playSoundFileNamed:waitForCompletion:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"SKAction",
        b"rotateToAngle:duration:shortestUnitArc:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"SKAction",
        b"runBlock:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"SKAction",
        b"runBlock:queue:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(b"SKAction", b"setNormalTexture:resize:", {"arguments": {3: {"type": b"Z"}}})
    r(b"SKAction", b"setTexture:resize:", {"arguments": {3: {"type": b"Z"}}})
    r(
        b"SKAction",
        b"setTimingFunc:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"f"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"f"}},
                    }
                }
            }
        },
    )
    r(
        b"SKAction",
        b"setTimingFunction:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"f"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"f"}},
                    }
                }
            }
        },
    )
    r(
        b"SKAction",
        b"timingFunc",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"f"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"f"}},
                }
            }
        },
    )
    r(
        b"SKAction",
        b"timingFunction",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"f"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"f"}},
                }
            }
        },
    )
    r(
        b"SKAttributeValue",
        b"setVectorFloat2Value:",
        {"full_signature": b"v@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"SKAttributeValue",
        b"setVectorFloat3Value:",
        {"full_signature": b"v@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(
        b"SKAttributeValue",
        b"setVectorFloat4Value:",
        {"full_signature": b"v@:<4f>", "arguments": {2: {"type": b"<4f>"}}},
    )
    r(
        b"SKAttributeValue",
        b"valueWithVectorFloat2:",
        {"full_signature": b"@@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"SKAttributeValue",
        b"valueWithVectorFloat3:",
        {"full_signature": b"@@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(
        b"SKAttributeValue",
        b"valueWithVectorFloat4:",
        {"full_signature": b"@@:<4f>", "arguments": {2: {"type": b"<4f>"}}},
    )
    r(
        b"SKAttributeValue",
        b"vectorFloat2Value",
        {"full_signature": b"<2f>@:", "retval": {"type": b"<2f>"}},
    )
    r(
        b"SKAttributeValue",
        b"vectorFloat3Value",
        {"full_signature": b"<3f>@:", "retval": {"type": b"<3f>"}},
    )
    r(
        b"SKAttributeValue",
        b"vectorFloat4Value",
        {"full_signature": b"<4f>@:", "retval": {"type": b"<4f>"}},
    )
    r(b"SKAudioNode", b"autoplayLooped", {"retval": {"type": b"Z"}})
    r(b"SKAudioNode", b"isPositional", {"retval": {"type": b"Z"}})
    r(b"SKAudioNode", b"setAutoplayLooped:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKAudioNode", b"setPositional:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKCameraNode", b"containsNode:", {"retval": {"type": b"Z"}})
    r(b"SKConstraint", b"enabled", {"retval": {"type": b"Z"}})
    r(b"SKConstraint", b"setEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKEffectNode", b"setShouldCenterFilter:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKEffectNode", b"setShouldEnableEffects:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKEffectNode", b"setShouldRasterize:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKEffectNode", b"shouldCenterFilter", {"retval": {"type": b"Z"}})
    r(b"SKEffectNode", b"shouldEnableEffects", {"retval": {"type": b"Z"}})
    r(b"SKEffectNode", b"shouldRasterize", {"retval": {"type": b"Z"}})
    r(
        b"SKFieldNode",
        b"customFieldWithEvaluationBlock:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"<3f>"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"<3f>"},
                            2: {"type": b"<3f>"},
                            3: {"type": b"f"},
                            4: {"type": b"f"},
                            5: {"type": b"d"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKFieldNode",
        b"direction",
        {"full_signature": b"<3f>@:", "retval": {"type": b"<3f>"}},
    )
    r(b"SKFieldNode", b"isEnabled", {"retval": {"type": b"Z"}})
    r(b"SKFieldNode", b"isExclusive", {"retval": {"type": b"Z"}})
    r(
        b"SKFieldNode",
        b"linearGravityFieldWithVector:",
        {"full_signature": b"@@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(
        b"SKFieldNode",
        b"setDirection:",
        {"full_signature": b"v@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(b"SKFieldNode", b"setEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKFieldNode", b"setExclusive:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SKFieldNode",
        b"velocityFieldWithVector:",
        {"full_signature": b"@@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(b"SKLightNode", b"isEnabled", {"retval": {"type": b"Z"}})
    r(b"SKLightNode", b"setEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SKMutableTexture",
        b"modifyPixelDataWithBlock:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {
                                "type": b"^v",
                                "type_modifier": "N",
                                "c_array_length_in_arg": 2,
                            },
                            2: {"type": b"Q"},
                        },
                    }
                }
            }
        },
    )
    r(b"SKNode", b"containsPoint:", {"retval": {"type": b"Z"}})
    r(
        b"SKNode",
        b"enumerateChildNodesWithName:usingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"^Z", "type_modifier": "o"},
                        },
                    }
                }
            }
        },
    )
    r(b"SKNode", b"hasActions", {"retval": {"type": b"Z"}})
    r(b"SKNode", b"inParentHierarchy:", {"retval": {"type": b"Z"}})
    r(b"SKNode", b"intersectsNode:", {"retval": {"type": b"Z"}})
    r(b"SKNode", b"isAccessibilityElement", {"retval": {"type": b"Z"}})
    r(b"SKNode", b"isAccessibilityEnabled", {"retval": {"type": b"Z"}})
    r(b"SKNode", b"isEqualToNode:", {"retval": {"type": b"Z"}})
    r(b"SKNode", b"isHidden", {"retval": {"type": b"Z"}})
    r(b"SKNode", b"isPaused", {"retval": {"type": b"Z"}})
    r(b"SKNode", b"isUserInteractionEnabled", {"retval": {"type": b"Z"}})
    r(
        b"SKNode",
        b"nodeWithFileNamed:securelyWithClasses:andError:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"SKNode",
        b"runAction:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(b"SKNode", b"setAccessibilityElement:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKNode", b"setAccessibilityEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKNode", b"setHidden:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKNode", b"setPaused:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKNode", b"setUserInteractionEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKPhysicsBody", b"affectedByGravity", {"retval": {"type": b"Z"}})
    r(b"SKPhysicsBody", b"allowsRotation", {"retval": {"type": b"Z"}})
    r(b"SKPhysicsBody", b"isDynamic", {"retval": {"type": b"Z"}})
    r(b"SKPhysicsBody", b"isResting", {"retval": {"type": b"Z"}})
    r(b"SKPhysicsBody", b"pinned", {"retval": {"type": b"Z"}})
    r(b"SKPhysicsBody", b"setAffectedByGravity:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKPhysicsBody", b"setAllowsRotation:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKPhysicsBody", b"setDynamic:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKPhysicsBody", b"setPinned:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKPhysicsBody", b"setResting:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SKPhysicsBody",
        b"setUsesPreciseCollisionDetection:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SKPhysicsBody", b"usesPreciseCollisionDetection", {"retval": {"type": b"Z"}})
    r(
        b"SKPhysicsJointPin",
        b"setShouldEnableLimits:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SKPhysicsJointPin", b"shouldEnableLimits", {"retval": {"type": b"Z"}})
    r(
        b"SKPhysicsJointSliding",
        b"setShouldEnableLimits:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SKPhysicsJointSliding", b"shouldEnableLimits", {"retval": {"type": b"Z"}})
    r(
        b"SKPhysicsWorld",
        b"enumerateBodiesAlongRayStart:end:usingBlock:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"{CGPoint=dd}"},
                            3: {"type": b"{CGVector=dd}"},
                            4: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKPhysicsWorld",
        b"enumerateBodiesAtPoint:usingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"^Z", "type_modifier": "o"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKPhysicsWorld",
        b"enumerateBodiesInRect:usingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"^Z", "type_modifier": "o"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SKPhysicsWorld",
        b"sampleFieldsAt:",
        {
            "full_signature": b"<3f>@:<3f>",
            "retval": {"type": b"<3f>"},
            "arguments": {2: {"type": b"<3f>"}},
        },
    )
    r(b"SKRegion", b"containsPoint:", {"retval": {"type": b"Z"}})
    r(b"SKRenderer", b"ignoresSiblingOrder", {"retval": {"type": "Z"}})
    r(b"SKRenderer", b"setIgnoresSiblingOrder:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"SKRenderer",
        b"setShouldCullNonVisibleNodes:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"SKRenderer", b"setShowsDrawCount:", {"arguments": {2: {"type": "Z"}}})
    r(b"SKRenderer", b"setShowsFields:", {"arguments": {2: {"type": "Z"}}})
    r(b"SKRenderer", b"setShowsNodeCount:", {"arguments": {2: {"type": "Z"}}})
    r(b"SKRenderer", b"setShowsPhysics:", {"arguments": {2: {"type": "Z"}}})
    r(b"SKRenderer", b"setShowsQuadCount:", {"arguments": {2: {"type": "Z"}}})
    r(b"SKRenderer", b"shouldCullNonVisibleNodes", {"retval": {"type": "Z"}})
    r(b"SKRenderer", b"showsDrawCount", {"retval": {"type": "Z"}})
    r(b"SKRenderer", b"showsFields", {"retval": {"type": "Z"}})
    r(b"SKRenderer", b"showsNodeCount", {"retval": {"type": "Z"}})
    r(b"SKRenderer", b"showsPhysics", {"retval": {"type": "Z"}})
    r(b"SKRenderer", b"showsQuadCount", {"retval": {"type": "Z"}})
    r(b"SKShapeNode", b"isAntialiased", {"retval": {"type": b"Z"}})
    r(b"SKShapeNode", b"setAntialiased:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SKShapeNode",
        b"shapeNodeWithPath:centered:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"SKShapeNode",
        b"shapeNodeWithPoints:count:",
        {"arguments": {2: {"type_modifier": b"n", "c_array_length_in_arg": 3}}},
    )
    r(
        b"SKShapeNode",
        b"shapeNodeWithSplinePoints:count:",
        {"arguments": {2: {"type_modifier": b"n", "c_array_length_in_arg": 3}}},
    )
    r(
        b"SKSpriteNode",
        b"spriteNodeWithImageNamed:normalMapped:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"SKTexture",
        b"preloadTextures:withCompletionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"SKTexture",
        b"preloadWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(b"SKTexture", b"setUsesMipmaps:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SKTexture",
        b"textureNoiseWithSmoothness:size:grayscale:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"SKTexture",
        b"textureWithData:size:flipped:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"SKTexture", b"usesMipmaps", {"retval": {"type": b"Z"}})
    r(
        b"SKTextureAtlas",
        b"preloadTextureAtlases:withCompletionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"SKTextureAtlas",
        b"preloadTextureAtlasesNamed:withCompletionHandler:",
        {
            "arguments": {
                3: {
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
        b"SKTextureAtlas",
        b"preloadWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(b"SKTileDefinition", b"flipHorizontally", {"retval": {"type": "Z"}})
    r(b"SKTileDefinition", b"flipVertically", {"retval": {"type": "Z"}})
    r(b"SKTileDefinition", b"setFlipHorizontally:", {"arguments": {2: {"type": "Z"}}})
    r(b"SKTileDefinition", b"setFlipVertically:", {"arguments": {2: {"type": "Z"}}})
    r(b"SKTileMapNode", b"enableAutomapping", {"retval": {"type": b"Z"}})
    r(b"SKTileMapNode", b"setEnableAutomapping:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SKTransformNode",
        b"eulerAngles",
        {"full_signature": b"<3f>@:", "retval": {"type": b"<3f>"}},
    )
    r(
        b"SKTransformNode",
        b"quaternion",
        {
            "full_signature": b"{_simd_quatf=<4f>}@:",
            "retval": {"type": b"{_simd_quatf=<4f>}"},
        },
    )
    r(
        b"SKTransformNode",
        b"rotationMatrix",
        {
            "full_signature": b"{_matrix_float3x3=[3<3f>]}@:",
            "retval": {"type": b"{_matrix_float3x3=[3<3f>]}"},
        },
    )
    r(
        b"SKTransformNode",
        b"setEulerAngles:",
        {"full_signature": b"v@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(
        b"SKTransformNode",
        b"setQuaternion:",
        {
            "full_signature": b"v@:{_simd_quatf=<4f>}",
            "arguments": {2: {"type": b"{_simd_quatf=<4f>}"}},
        },
    )
    r(
        b"SKTransformNode",
        b"setRotationMatrix:",
        {
            "full_signature": b"v@:{_matrix_float3x3=[3<3f>]}",
            "arguments": {2: {"type": b"{_matrix_float3x3=[3<3f>]}"}},
        },
    )
    r(b"SKTransition", b"pausesIncomingScene", {"retval": {"type": b"Z"}})
    r(b"SKTransition", b"pausesOutgoingScene", {"retval": {"type": b"Z"}})
    r(b"SKTransition", b"setPausesIncomingScene:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKTransition", b"setPausesOutgoingScene:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SKUniform",
        b"initWithName:matrixFloat2x2:",
        {
            "full_signature": b"@@:@{_matrix_float2x2=[2<2f>]}",
            "arguments": {3: {"type": b"{_matrix_float2x2=[2<2f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"initWithName:matrixFloat3x3:",
        {
            "full_signature": b"@@:@{_matrix_float3x3=[3<3f>]}",
            "arguments": {3: {"type": b"{_matrix_float3x3=[3<3f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"initWithName:matrixFloat4x4:",
        {
            "full_signature": b"@@:@{_matrix_float4x4=[4<4f>]}",
            "arguments": {3: {"type": b"{_matrix_float4x4=[4<4f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"initWithName:vectorFloat2:",
        {"full_signature": b"@@:@<2f>", "arguments": {3: {"type": b"<2f>"}}},
    )
    r(
        b"SKUniform",
        b"initWithName:vectorFloat3:",
        {"full_signature": b"@@:@<3f>", "arguments": {3: {"type": b"<3f>"}}},
    )
    r(
        b"SKUniform",
        b"initWithName:vectorFloat4:",
        {"full_signature": b"@@:@<4f>", "arguments": {3: {"type": b"<4f>"}}},
    )
    r(
        b"SKUniform",
        b"matrixFloat2x2Value",
        {
            "full_signature": b"{_matrix_float2x2=[2<2f>]}@:",
            "retval": {"type": b"{_matrix_float2x2=[2<2f>]}"},
        },
    )
    r(
        b"SKUniform",
        b"matrixFloat3x3Value",
        {
            "full_signature": b"{_matrix_float3x3=[3<3f>]}@:",
            "retval": {"type": b"{_matrix_float3x3=[3<3f>]}"},
        },
    )
    r(
        b"SKUniform",
        b"matrixFloat4x4Value",
        {
            "full_signature": b"{_matrix_float4x4=[4<4f>]}@:",
            "retval": {"type": b"{_matrix_float4x4=[4<4f>]}"},
        },
    )
    r(
        b"SKUniform",
        b"setMatrixFloat2x2Value:",
        {
            "full_signature": b"v@:{_matrix_float2x2=[2<2f>]}",
            "arguments": {2: {"type": b"{_matrix_float2x2=[2<2f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"setMatrixFloat3x3Value:",
        {
            "full_signature": b"v@:{_matrix_float3x3=[3<3f>]}",
            "arguments": {2: {"type": b"{_matrix_float3x3=[3<3f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"setMatrixFloat4x4Value:",
        {
            "full_signature": b"v@:{_matrix_float4x4=[4<4f>]}",
            "arguments": {2: {"type": b"{_matrix_float4x4=[4<4f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"setVectorFloat2Value:",
        {"full_signature": b"v@:<2f>", "arguments": {2: {"type": b"<2f>"}}},
    )
    r(
        b"SKUniform",
        b"setVectorFloat3Value:",
        {"full_signature": b"v@:<3f>", "arguments": {2: {"type": b"<3f>"}}},
    )
    r(
        b"SKUniform",
        b"setVectorFloat4Value:",
        {"full_signature": b"v@:<4f>", "arguments": {2: {"type": b"<4f>"}}},
    )
    r(
        b"SKUniform",
        b"uniformWithName:matrixFloat2x2:",
        {
            "full_signature": b"@@:@{_matrix_float2x2=[2<2f>]}",
            "arguments": {3: {"type": b"{_matrix_float2x2=[2<2f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"uniformWithName:matrixFloat3x3:",
        {
            "full_signature": b"@@:@{_matrix_float3x3=[3<3f>]}",
            "arguments": {3: {"type": b"{_matrix_float3x3=[3<3f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"uniformWithName:matrixFloat4x4:",
        {
            "full_signature": b"@@:@{_matrix_float4x4=[4<4f>]}",
            "arguments": {3: {"type": b"{_matrix_float4x4=[4<4f>]}"}},
        },
    )
    r(
        b"SKUniform",
        b"uniformWithName:vectorFloat2:",
        {"full_signature": b"@@:@<2f>", "arguments": {3: {"type": b"<2f>"}}},
    )
    r(
        b"SKUniform",
        b"uniformWithName:vectorFloat3:",
        {"full_signature": b"@@:@<3f>", "arguments": {3: {"type": b"<3f>"}}},
    )
    r(
        b"SKUniform",
        b"uniformWithName:vectorFloat4:",
        {"full_signature": b"@@:@<4f>", "arguments": {3: {"type": b"<4f>"}}},
    )
    r(
        b"SKUniform",
        b"vectorFloat2Value",
        {"full_signature": b"<2f>@:", "retval": {"type": b"<2f>"}},
    )
    r(
        b"SKUniform",
        b"vectorFloat3Value",
        {"full_signature": b"<3f>@:", "retval": {"type": b"<3f>"}},
    )
    r(
        b"SKUniform",
        b"vectorFloat4Value",
        {"full_signature": b"<4f>@:", "retval": {"type": b"<4f>"}},
    )
    r(b"SKView", b"allowsTransparency", {"retval": {"type": b"Z"}})
    r(b"SKView", b"disableDepthStencilBuffer", {"retval": {"type": "Z"}})
    r(b"SKView", b"ignoresSiblingOrder", {"retval": {"type": b"Z"}})
    r(b"SKView", b"isAsynchronous", {"retval": {"type": b"Z"}})
    r(b"SKView", b"isPaused", {"retval": {"type": b"Z"}})
    r(b"SKView", b"setAllowsTransparency:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setAsynchronous:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setDisableDepthStencilBuffer:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setIgnoresSiblingOrder:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setPaused:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setShouldCullNonVisibleNodes:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setShowsDrawCount:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setShowsFPS:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setShowsFields:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setShowsNodeCount:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setShowsPhysics:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"setShowsQuadCount:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SKView", b"shouldCullNonVisibleNodes", {"retval": {"type": b"Z"}})
    r(b"SKView", b"showsDrawCount", {"retval": {"type": b"Z"}})
    r(b"SKView", b"showsFPS", {"retval": {"type": b"Z"}})
    r(b"SKView", b"showsFields", {"retval": {"type": b"Z"}})
    r(b"SKView", b"showsNodeCount", {"retval": {"type": b"Z"}})
    r(b"SKView", b"showsPhysics", {"retval": {"type": b"Z"}})
    r(b"SKView", b"showsQuadCount", {"retval": {"type": b"Z"}})
    r(
        b"SKWarpGeometryGrid",
        b"destPositionAtIndex:",
        {"full_signature": b"<2f>@:q", "retval": {"type": b"<2f>"}},
    )
    r(
        b"SKWarpGeometryGrid",
        b"gridByReplacingDestPositions:",
        {"full_signature": b"@@:^<2f>", "arguments": {2: {"type": b"^<2f>"}}},
    )
    r(
        b"SKWarpGeometryGrid",
        b"gridByReplacingSourcePositions:",
        {"full_signature": b"@@:^<2f>", "arguments": {2: {"type": b"^<2f>"}}},
    )
    r(
        b"SKWarpGeometryGrid",
        b"gridWithColumns:rows:sourcePositions:destPositions:",
        {
            "full_signature": b"@@:qq^<2f>^<2f>",
            "arguments": {4: {"type": b"^<2f>"}, 5: {"type": b"^<2f>"}},
        },
    )
    r(
        b"SKWarpGeometryGrid",
        b"initWithColumns:rows:sourcePositions:destPositions:",
        {
            "full_signature": b"@@:qq^<2f>^<2f>",
            "arguments": {4: {"type": b"^<2f>"}, 5: {"type": b"^<2f>"}},
        },
    )
    r(
        b"SKWarpGeometryGrid",
        b"sourcePositionAtIndex:",
        {"full_signature": b"<2f>@:q", "retval": {"type": b"<2f>"}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {
    "SKTileAdjacencyRightEdge": "SKTileAdjacencyDown | SKTileAdjacencyLowerLeft | SKTileAdjacencyLeft | SKTileAdjacencyUpperLeft | SKTileAdjacencyUp",
    "SKTileAdjacencyUpperRightCorner": "SKTileAdjacencyUp | SKTileAdjacencyUpperRight | SKTileAdjacencyRight | SKTileAdjacencyLowerRight | SKTileAdjacencyDown | SKTileAdjacencyLeft | SKTileAdjacencyUpperLeft",
    "SKTileAdjacencyUpperRightEdge": "SKTileAdjacencyDown | SKTileAdjacencyLowerLeft | SKTileAdjacencyLeft",
    "SKTileAdjacencyLowerRightCorner": "SKTileAdjacencyUp | SKTileAdjacencyUpperRight | SKTileAdjacencyRight | SKTileAdjacencyLowerRight | SKTileAdjacencyDown | SKTileAdjacencyLowerLeft | SKTileAdjacencyLeft",
    "SKTileAdjacencyLowerRightEdge": "SKTileAdjacencyLeft | SKTileAdjacencyUpperLeft | SKTileAdjacencyUp",
    "SKTileAdjacencyDownEdge": "SKTileAdjacencyUp | SKTileAdjacencyUpperRight | SKTileAdjacencyRight | SKTileAdjacencyLeft | SKTileAdjacencyUpperLeft",
    "SKTileAdjacencyLeftEdge": "SKTileAdjacencyUp | SKTileAdjacencyUpperRight | SKTileAdjacencyRight | SKTileAdjacencyLowerRight | SKTileAdjacencyDown",
    "SKTileAdjacencyUpEdge": "SKTileAdjacencyRight | SKTileAdjacencyLowerRight | SKTileAdjacencyDown | SKTileAdjacencyLowerLeft | SKTileAdjacencyLeft",
    "SKTileAdjacencyLowerLeftEdge": "SKTileAdjacencyUp | SKTileAdjacencyUpperRight | SKTileAdjacencyRight",
    "SKTileAdjacencyUpperLeftCorner": "SKTileAdjacencyUp | SKTileAdjacencyUpperRight | SKTileAdjacencyRight | SKTileAdjacencyDown | SKTileAdjacencyLowerLeft | SKTileAdjacencyLeft | SKTileAdjacencyUpperLeft",
    "SKTileAdjacencyUpperLeftEdge": "SKTileAdjacencyRight | SKTileAdjacencyLowerRight | SKTileAdjacencyDown",
    "SKTileAdjacencyLowerLeftCorner": "SKTileAdjacencyUp | SKTileAdjacencyRight | SKTileAdjacencyLowerRight | SKTileAdjacencyDown | SKTileAdjacencyLowerLeft | SKTileAdjacencyLeft | SKTileAdjacencyUpperLeft",
}

# END OF FILE
