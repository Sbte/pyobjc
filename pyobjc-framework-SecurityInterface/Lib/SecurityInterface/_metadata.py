# This file is generated by objective.metadata
#
# Last update: Sat May 11 12:11:30 2024
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
constants = """$SFAuthorizationPluginViewUserNameKey$SFAuthorizationPluginViewUserShortNameKey$SFCertificateViewDisclosureStateDidChange$SFDisplayViewException$"""
enums = """$SFAuthorizationStartupState@0$SFAuthorizationViewInProgressState@2$SFAuthorizationViewLockedState@1$SFAuthorizationViewUnlockedState@3$SFButtonTypeBack@0$SFButtonTypeCancel@0$SFButtonTypeLogin@1$SFButtonTypeOK@1$SFViewTypeCredentials@1$SFViewTypeIdentityAndCredentials@0$"""
misc.update(
    {
        "SFAuthorizationViewState": NewType("SFAuthorizationViewState", int),
        "SFViewType": NewType("SFViewType", int),
        "SFButtonType": NewType("SFButtonType", int),
    }
)
misc.update({})
misc.update({})
aliases = {
    "SFButtonTypeBack": "SFButtonTypeCancel",
    "SFButtonTypeLogin": "SFButtonTypeOK",
    "SFButtonTypeOK": "NSOKButton",
    "SFButtonTypeCancel": "NSCancelButton",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"authorizationViewCreatedAuthorization:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"authorizationViewDidAuthorize:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"authorizationViewDidDeauthorize:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"authorizationViewDidHide:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"authorizationViewReleasedAuthorization:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"authorizationViewShouldDeauthorize:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"certificatePanelShowHelp:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"chooseIdentityPanelShowHelp:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"SFAuthorizationPluginView",
        b"setButton:enabled:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(b"SFAuthorizationPluginView", b"setEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SFAuthorizationView",
        b"authorizationRights",
        {"retval": {"type": b"^{_AuthorizationRights=I^{_AuthorizationItem=^cQ^vI}}"}},
    )
    r(b"SFAuthorizationView", b"authorize:", {"retval": {"type": b"Z"}})
    r(b"SFAuthorizationView", b"deauthorize:", {"retval": {"type": b"Z"}})
    r(b"SFAuthorizationView", b"isEnabled", {"retval": {"type": b"Z"}})
    r(
        b"SFAuthorizationView",
        b"setAuthorizationRights:",
        {
            "arguments": {
                2: {"type": b"^{_AuthorizationRights=I^{_AuthorizationItem=^cQ^vI}}"}
            }
        },
    )
    r(b"SFAuthorizationView", b"setAutoupdate:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SFAuthorizationView",
        b"setAutoupdate:interval:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SFAuthorizationView", b"setEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SFAuthorizationView", b"updateStatus:", {"retval": {"type": b"Z"}})
    r(
        b"SFCertificatePanel",
        b"beginSheetForWindow:modalDelegate:didEndSelector:contextInfo:certificates:showGroup:",
        {"arguments": {4: {"sel_of_type": b"v@:@q^v"}, 7: {"type": b"Z"}}},
    )
    r(
        b"SFCertificatePanel",
        b"beginSheetForWindow:modalDelegate:didEndSelector:contextInfo:trust:showGroup:",
        {"arguments": {4: {"sel_of_type": b"v@:@q^v"}, 7: {"type": b"Z"}}},
    )
    r(
        b"SFCertificatePanel",
        b"runModalForCertificates:showGroup:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"SFCertificatePanel",
        b"runModalForTrust:showGroup:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(b"SFCertificatePanel", b"setShowsHelp:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SFCertificatePanel", b"showsHelp", {"retval": {"type": b"Z"}})
    r(
        b"SFCertificateTrustPanel",
        b"beginSheetForWindow:modalDelegate:didEndSelector:contextInfo:trust:message:",
        {"arguments": {4: {"sel_of_type": b"v@:@q^v"}}},
    )
    r(b"SFCertificateView", b"detailsDisclosed", {"retval": {"type": b"Z"}})
    r(b"SFCertificateView", b"detailsDisplayed", {"retval": {"type": b"Z"}})
    r(b"SFCertificateView", b"isEditable", {"retval": {"type": b"Z"}})
    r(b"SFCertificateView", b"isTrustDisplayed", {"retval": {"type": b"Z"}})
    r(b"SFCertificateView", b"policiesDisclosed", {"retval": {"type": b"Z"}})
    r(b"SFCertificateView", b"setDetailsDisclosed:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SFCertificateView", b"setDisplayDetails:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SFCertificateView", b"setDisplayTrust:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SFCertificateView", b"setEditableTrust:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SFCertificateView",
        b"setPoliciesDisclosed:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SFChooseIdentityPanel",
        b"beginSheetForWindow:modalDelegate:didEndSelector:contextInfo:identities:message:",
        {"arguments": {4: {"sel_of_type": b"v@:@q^v"}}},
    )
    r(b"SFChooseIdentityPanel", b"setShowsHelp:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SFChooseIdentityPanel", b"showsHelp", {"retval": {"type": b"Z"}})
    r(
        b"SFKeychainSavePanel",
        b"beginSheetForDirectory:file:modalForWindow:modalDelegate:didEndSelector:contextInfo:",
        {"arguments": {6: {"sel_of_type": b"v@:@q^v"}}},
    )
    r(
        b"SFKeychainSettingsPanel",
        b"beginSheetForWindow:modalDelegate:didEndSelector:contextInfo:settings:keychain:",
        {
            "arguments": {
                4: {"sel_of_type": b"v@:@q^v"},
                6: {"type": b"^{SecKeychainSettings=IZZI}"},
            }
        },
    )
    r(
        b"SFKeychainSettingsPanel",
        b"runModalForSettings:keychain:",
        {"arguments": {2: {"type": b"^{SecKeychainSettings=IZZI}"}}},
    )
    r(b"null", b"authorizationViewShouldDeauthorize:", {"retval": {"type": b"Z"}})
    r(b"null", b"certificatePanelShowHelp:", {"retval": {"type": b"Z"}})
    r(b"null", b"chooseIdentityPanelShowHelp:", {"retval": {"type": b"Z"}})
    r(b"null", b"setButton:enabled:", {"arguments": {3: {"type": b"Z"}}})
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "SFAuthorizationPluginView", b"initWithCallbacks:andEngineRef:"
)
protocols = {
    "SFChooseIdentityPanelDelegate": objc.informal_protocol(
        "SFChooseIdentityPanelDelegate",
        [
            objc.selector(
                None, b"chooseIdentityPanelShowHelp:", b"Z@:@", isRequired=False
            )
        ],
    ),
    "SFCertificatePanelDelegate": objc.informal_protocol(
        "SFCertificatePanelDelegate",
        [objc.selector(None, b"certificatePanelShowHelp:", b"Z@:@", isRequired=False)],
    ),
    "SFAuthorizationViewDelegate": objc.informal_protocol(
        "SFAuthorizationViewDelegate",
        [
            objc.selector(
                None,
                b"authorizationViewCreatedAuthorization:",
                b"v@:@",
                isRequired=False,
            ),
            objc.selector(
                None, b"authorizationViewDidHide:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"authorizationViewDidAuthorize:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"authorizationViewDidDeauthorize:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"authorizationViewShouldDeauthorize:", b"Z@:@", isRequired=False
            ),
            objc.selector(
                None,
                b"authorizationViewReleasedAuthorization:",
                b"v@:@",
                isRequired=False,
            ),
        ],
    ),
}
expressions = {}

# END OF FILE
