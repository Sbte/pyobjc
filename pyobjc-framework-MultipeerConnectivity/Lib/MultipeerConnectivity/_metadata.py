# This file is generated by objective.metadata
#
# Last update: Sat May 11 12:12:41 2024
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
constants = """$MCErrorDomain$kMCSessionMaximumNumberOfPeers@Q$kMCSessionMinimumNumberOfPeers@Q$"""
enums = """$MCEncryptionNone@2$MCEncryptionOptional@0$MCEncryptionRequired@1$MCErrorCancelled@5$MCErrorInvalidParameter@2$MCErrorNotConnected@1$MCErrorTimedOut@4$MCErrorUnavailable@6$MCErrorUnknown@0$MCErrorUnsupported@3$MCSessionSendDataReliable@0$MCSessionSendDataUnreliable@1$MCSessionStateConnected@2$MCSessionStateConnecting@1$MCSessionStateNotConnected@0$"""
misc.update(
    {
        "MCSessionState": NewType("MCSessionState", int),
        "MCEncryptionPreference": NewType("MCEncryptionPreference", int),
        "MCSessionSendDataMode": NewType("MCSessionSendDataMode", int),
        "MCErrorCode": NewType("MCErrorCode", int),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"MCSession",
        b"nearbyConnectionDataForPeer:withCompletionHandler:",
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
        b"MCSession",
        b"sendData:toPeers:withMode:error:",
        {"retval": {"type": b"Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"MCSession",
        b"sendResourceAtURL:withName:toPeer:withCompletionHandler:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"MCSession",
        b"startStreamWithName:toPeer:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSObject",
        b"advertiser:didNotStartAdvertisingPeer:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"advertiser:didReceiveInvitationFromPeer:withContext:invitationHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"advertiserAssistantDidDismissInvitation:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"advertiserAssistantWillPresentInvitation:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"browser:didNotStartBrowsingForPeers:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"browser:foundPeer:withDiscoveryInfo:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"browser:lostPeer:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"browserViewController:shouldPresentNearbyPeer:withDiscoveryInfo:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"browserViewControllerDidFinish:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"browserViewControllerWasCancelled:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"session:didFinishReceivingResourceWithName:fromPeer:atURL:withError:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
                6: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"session:didReceiveCertificate:fromPeer:certificateHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"session:didReceiveData:fromPeer:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"session:didReceiveStream:withName:fromPeer:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"session:didStartReceivingResourceWithName:fromPeer:withProgress:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"session:peer:didChangeState:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": "Q"}},
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "MCAdvertiserAssistant", b"initWithServiceType:discoveryInfo:session:"
)
objc.registerNewKeywordsFromSelector(
    "MCBrowserViewController", b"initWithBrowser:session:"
)
objc.registerNewKeywordsFromSelector(
    "MCBrowserViewController", b"initWithServiceType:session:"
)
objc.registerNewKeywordsFromSelector(
    "MCNearbyServiceAdvertiser", b"initWithPeer:discoveryInfo:serviceType:"
)
objc.registerNewKeywordsFromSelector(
    "MCNearbyServiceBrowser", b"initWithPeer:serviceType:"
)
objc.registerNewKeywordsFromSelector("MCPeerID", b"initWithDisplayName:")
objc.registerNewKeywordsFromSelector("MCSession", b"initWithPeer:")
objc.registerNewKeywordsFromSelector(
    "MCSession", b"initWithPeer:securityIdentity:encryptionPreference:"
)
expressions = {}

# END OF FILE
