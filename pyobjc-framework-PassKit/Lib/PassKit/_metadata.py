# This file is generated by objective.metadata
#
# Last update: Fri Feb 18 12:06:06 2022
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
constants = """$PKAddSecureElementPassErrorDomain$PKContactFieldEmailAddress$PKContactFieldName$PKContactFieldPhoneNumber$PKContactFieldPhoneticName$PKContactFieldPostalAddress$PKEncryptionSchemeECC_V2$PKEncryptionSchemeRSA_V2$PKPassKitErrorDomain$PKPassLibraryAddedPassesUserInfoKey$PKPassLibraryDidChangeNotification$PKPassLibraryPassTypeIdentifierUserInfoKey$PKPassLibraryRecoveredPassesUserInfoKey$PKPassLibraryRemotePaymentPassesDidChangeNotification$PKPassLibraryRemovedPassInfosUserInfoKey$PKPassLibraryReplacementPassesUserInfoKey$PKPassLibrarySerialNumberUserInfoKey$PKPaymentErrorContactFieldUserInfoKey$PKPaymentErrorDomain$PKPaymentErrorPostalAddressUserInfoKey$PKPaymentNetworkAmex$PKPaymentNetworkBarcode$PKPaymentNetworkCarteBancaire$PKPaymentNetworkCarteBancaires$PKPaymentNetworkCartesBancaires$PKPaymentNetworkChinaUnionPay$PKPaymentNetworkDankort$PKPaymentNetworkDiscover$PKPaymentNetworkEftpos$PKPaymentNetworkElectron$PKPaymentNetworkElo$PKPaymentNetworkGirocard$PKPaymentNetworkIDCredit$PKPaymentNetworkInterac$PKPaymentNetworkJCB$PKPaymentNetworkMada$PKPaymentNetworkMaestro$PKPaymentNetworkMasterCard$PKPaymentNetworkMir$PKPaymentNetworkNanaco$PKPaymentNetworkPrivateLabel$PKPaymentNetworkQuicPay$PKPaymentNetworkSuica$PKPaymentNetworkVPay$PKPaymentNetworkVisa$PKPaymentNetworkWaon$PKStoredValuePassBalanceTypeCash$PKStoredValuePassBalanceTypeLoyaltyPoints$"""
enums = """$PKAddPaymentPassErrorSystemCancelled@2$PKAddPaymentPassErrorUnsupported@0$PKAddPaymentPassErrorUserCancelled@1$PKAddPaymentPassStyleAccess@1$PKAddPaymentPassStylePayment@0$PKAddSecureElementPassDeviceNotReadyError@5$PKAddSecureElementPassDeviceNotSupportedError@4$PKAddSecureElementPassInvalidConfigurationError@3$PKAddSecureElementPassUnavailableError@2$PKAddSecureElementPassUnknownError@0$PKAddSecureElementPassUserCanceledError@1$PKAddShareablePassConfigurationPrimaryActionAdd@0$PKAddShareablePassConfigurationPrimaryActionShare@1$PKAddressFieldAll@15$PKAddressFieldEmail@4$PKAddressFieldName@8$PKAddressFieldNone@0$PKAddressFieldPhone@2$PKAddressFieldPostalAddress@1$PKAutomaticPassPresentationSuppressionResultAlreadyPresenting@1$PKAutomaticPassPresentationSuppressionResultCancelled@3$PKAutomaticPassPresentationSuppressionResultDenied@2$PKAutomaticPassPresentationSuppressionResultNotSupported@0$PKAutomaticPassPresentationSuppressionResultSuccess@4$PKBarcodeEventConfigurationDataTypeSigningCertificate@2$PKBarcodeEventConfigurationDataTypeSigningKeyMaterial@1$PKBarcodeEventConfigurationDataTypeUnknown@0$PKDisbursementRequestScheduleFuture@1$PKDisbursementRequestScheduleOneTime@0$PKInvalidDataError@1$PKInvalidSignature@3$PKIssuerProvisioningExtensionAuthorizationResultAuthorized@1$PKIssuerProvisioningExtensionAuthorizationResultCanceled@0$PKMerchantCapability3DS@1$PKMerchantCapabilityCredit@4$PKMerchantCapabilityDebit@8$PKMerchantCapabilityEMV@2$PKNotEntitledError@4$PKPassLibraryDidAddPasses@0$PKPassLibraryDidCancelAddPasses@2$PKPassLibraryShouldReviewPasses@1$PKPassTypeAny@18446744073709551615$PKPassTypeBarcode@0$PKPassTypePayment@1$PKPassTypeSecureElement@1$PKPaymentAuthorizationStatusFailure@1$PKPaymentAuthorizationStatusInvalidBillingPostalAddress@2$PKPaymentAuthorizationStatusInvalidShippingContact@4$PKPaymentAuthorizationStatusInvalidShippingPostalAddress@3$PKPaymentAuthorizationStatusPINIncorrect@6$PKPaymentAuthorizationStatusPINLockout@7$PKPaymentAuthorizationStatusPINRequired@5$PKPaymentAuthorizationStatusSuccess@0$PKPaymentBillingContactInvalidError@2$PKPaymentButtonStyleAutomatic@3$PKPaymentButtonStyleBlack@2$PKPaymentButtonStyleWhite@0$PKPaymentButtonStyleWhiteOutline@1$PKPaymentButtonTypeAddMoney@9$PKPaymentButtonTypeBook@6$PKPaymentButtonTypeBuy@1$PKPaymentButtonTypeCheckout@5$PKPaymentButtonTypeContinue@16$PKPaymentButtonTypeContribute@14$PKPaymentButtonTypeDonate@4$PKPaymentButtonTypeInStore@3$PKPaymentButtonTypeOrder@11$PKPaymentButtonTypePlain@0$PKPaymentButtonTypeReload@8$PKPaymentButtonTypeRent@12$PKPaymentButtonTypeSetUp@2$PKPaymentButtonTypeSubscribe@7$PKPaymentButtonTypeSupport@13$PKPaymentButtonTypeTip@15$PKPaymentButtonTypeTopUp@10$PKPaymentCouponCodeExpiredError@5$PKPaymentCouponCodeInvalidError@4$PKPaymentMethodTypeCredit@2$PKPaymentMethodTypeDebit@1$PKPaymentMethodTypeEMoney@5$PKPaymentMethodTypePrepaid@3$PKPaymentMethodTypeStore@4$PKPaymentMethodTypeUnknown@0$PKPaymentPassActivationStateActivated@0$PKPaymentPassActivationStateActivating@2$PKPaymentPassActivationStateDeactivated@4$PKPaymentPassActivationStateRequiresActivation@1$PKPaymentPassActivationStateSuspended@3$PKPaymentShippingAddressUnserviceableError@3$PKPaymentShippingContactInvalidError@1$PKPaymentSummaryItemTypeFinal@0$PKPaymentSummaryItemTypePending@1$PKPaymentUnknownError@-1$PKRadioTechnologyBluetooth@2$PKRadioTechnologyNFC@1$PKRadioTechnologyNone@0$PKSecureElementPassActivationStateActivated@0$PKSecureElementPassActivationStateActivating@2$PKSecureElementPassActivationStateDeactivated@4$PKSecureElementPassActivationStateRequiresActivation@1$PKSecureElementPassActivationStateSuspended@3$PKShippingContactEditingModeEnabled@1$PKShippingContactEditingModeStorePickup@2$PKShippingTypeDelivery@1$PKShippingTypeServicePickup@3$PKShippingTypeShipping@0$PKShippingTypeStorePickup@2$PKUnknownError@-1$PKUnsupportedVersionError@2$"""
misc.update(
    {
        "PKShippingContactEditingMode": NewType("PKShippingContactEditingMode", int),
        "PKPaymentButtonStyle": NewType("PKPaymentButtonStyle", int),
        "PKPaymentPassActivationState": NewType("PKPaymentPassActivationState", int),
        "PKPaymentAuthorizationStatus": NewType("PKPaymentAuthorizationStatus", int),
        "PKAddPaymentPassStyle": NewType("PKAddPaymentPassStyle", int),
        "PKRadioTechnology": NewType("PKRadioTechnology", int),
        "PKMerchantCapability": NewType("PKMerchantCapability", int),
        "PKAutomaticPassPresentationSuppressionResult": NewType(
            "PKAutomaticPassPresentationSuppressionResult", int
        ),
        "PKPassType": NewType("PKPassType", int),
        "PKAddSecureElementPassErrorCode": NewType(
            "PKAddSecureElementPassErrorCode", int
        ),
        "PKIssuerProvisioningExtensionAuthorizationResult": NewType(
            "PKIssuerProvisioningExtensionAuthorizationResult", int
        ),
        "PKPaymentButtonType": NewType("PKPaymentButtonType", int),
        "PKPassLibraryAddPassesStatus": NewType("PKPassLibraryAddPassesStatus", int),
        "PKDisbursementRequestSchedule": NewType("PKDisbursementRequestSchedule", int),
        "PKAddPaymentPassError": NewType("PKAddPaymentPassError", int),
        "PKShippingType": NewType("PKShippingType", int),
        "PKAddShareablePassConfigurationPrimaryAction": NewType(
            "PKAddShareablePassConfigurationPrimaryAction", int
        ),
        "PKPassKitErrorCode": NewType("PKPassKitErrorCode", int),
        "PKBarcodeEventConfigurationDataType": NewType(
            "PKBarcodeEventConfigurationDataType", int
        ),
        "PKAddressField": NewType("PKAddressField", int),
        "PKPaymentMethodType": NewType("PKPaymentMethodType", int),
        "PKPaymentSummaryItemType": NewType("PKPaymentSummaryItemType", int),
        "PKSecureElementPassActivationState": NewType(
            "PKSecureElementPassActivationState", int
        ),
        "PKPaymentErrorCode": NewType("PKPaymentErrorCode", int),
    }
)
misc.update({})
aliases = {"PKPassTypePayment": "PKPassTypeSecureElement"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"NSObject", b"completionHandler", {"required": True, "retval": {"type": b"@?"}})
    r(
        b"NSObject",
        b"disbursementAuthorizationController:didAuthorizeWithDisbursementVoucher:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"disbursementAuthorizationControllerDidFinish:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"handleConfigurationRequest:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"handleInformationRequest:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"handleSignatureRequest:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didAuthorizePayment:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didAuthorizePayment:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didChangeCouponCode:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didRequestMerchantSessionUpdate:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didSelectPaymentMethod:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didSelectPaymentMethod:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didSelectShippingContact:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                            3: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didSelectShippingContact:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didSelectShippingMethod:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationController:didSelectShippingMethod:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationControllerDidFinish:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentAuthorizationControllerWillAuthorizePayment:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didAuthorizePayment:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didAuthorizePayment:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didChangeCouponCode:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didRequestMerchantSessionUpdate:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didSelectPaymentMethod:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didSelectPaymentMethod:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didSelectShippingContact:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                            3: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didSelectShippingContact:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didSelectShippingMethod:completion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewController:didSelectShippingMethod:handler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewControllerDidFinish:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"paymentAuthorizationViewControllerWillAuthorizePayment:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"presentationWindowForPaymentAuthorizationController:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setCompletionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    },
                    "type": b"@?",
                }
            },
        },
    )
    r(
        b"PKAddPaymentPassRequestConfiguration",
        b"requiresFelicaSecureElement",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKAddPaymentPassRequestConfiguration",
        b"setRequiresFelicaSecureElement:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PKAddShareablePassConfiguration",
        b"configurationForPassMetadata:provisioningPolicyIdentifier:primaryAction:completion:",
        {
            "arguments": {
                5: {
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
        b"PKDisbursementAuthorizationController",
        b"authorizeDisbursementWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PKDisbursementAuthorizationController",
        b"supportsDisbursements",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKIssuerProvisioningExtensionHandler",
        b"generateAddPaymentPassRequestForPassEntryWithIdentifier:configuration:certificateChain:nonce:nonceSignature:completionHandler:",
        {
            "arguments": {
                7: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"PKIssuerProvisioningExtensionHandler",
        b"passEntriesWithCompletion:",
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
        b"PKIssuerProvisioningExtensionHandler",
        b"remotePassEntriesWithCompletion:",
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
        b"PKIssuerProvisioningExtensionHandler",
        b"statusWithCompletion:",
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
        b"PKIssuerProvisioningExtensionStatus",
        b"passEntriesAvailable",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKIssuerProvisioningExtensionStatus",
        b"remotePassEntriesAvailable",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKIssuerProvisioningExtensionStatus",
        b"requiresAuthentication",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKIssuerProvisioningExtensionStatus",
        b"setPassEntriesAvailable:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PKIssuerProvisioningExtensionStatus",
        b"setRemotePassEntriesAvailable:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PKIssuerProvisioningExtensionStatus",
        b"setRequiresAuthentication:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PKPass", b"initWithData:error:", {"arguments": {3: {"type_modifier": b"o"}}})
    r(b"PKPass", b"isRemotePass", {"retval": {"type": b"Z"}})
    r(
        b"PKPassLibrary",
        b"activatePaymentPass:withActivationCode:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PKPassLibrary",
        b"activatePaymentPass:withActivationData:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PKPassLibrary",
        b"activateSecureElementPass:withActivationData:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PKPassLibrary",
        b"addPasses:withCompletionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    }
                }
            }
        },
    )
    r(b"PKPassLibrary", b"canAddFelicaPass", {"retval": {"type": b"Z"}})
    r(
        b"PKPassLibrary",
        b"canAddPaymentPassWithPrimaryAccountIdentifier:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKPassLibrary",
        b"canAddSecureElementPassWithPrimaryAccountIdentifier:",
        {"retval": {"type": b"Z"}},
    )
    r(b"PKPassLibrary", b"containsPass:", {"retval": {"type": b"Z"}})
    r(b"PKPassLibrary", b"isPassLibraryAvailable", {"retval": {"type": b"Z"}})
    r(b"PKPassLibrary", b"isPaymentPassActivationAvailable", {"retval": {"type": b"Z"}})
    r(
        b"PKPassLibrary",
        b"isSecureElementPassActivationAvailable",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKPassLibrary",
        b"isSuppressingAutomaticPassPresentation",
        {"retval": {"type": b"Z"}},
    )
    r(b"PKPassLibrary", b"replacePassWithPass:", {"retval": {"type": b"Z"}})
    r(
        b"PKPassLibrary",
        b"requestAutomaticPassPresentationSuppressionWithResponseHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Q"}},
                    }
                }
            }
        },
    )
    r(
        b"PKPassLibrary",
        b"serviceProviderDataForSecureElementPass:completion:",
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
        b"PKPassLibrary",
        b"signData:withSecureElementPass:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PKPaymentAuthorizationController",
        b"canMakePayments",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKPaymentAuthorizationController",
        b"canMakePaymentsUsingNetworks:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKPaymentAuthorizationController",
        b"canMakePaymentsUsingNetworks:capabilities:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKPaymentAuthorizationController",
        b"dismissWithCompletion:",
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
        b"PKPaymentAuthorizationController",
        b"presentWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    }
                }
            }
        },
    )
    r(
        b"PKPaymentAuthorizationViewController",
        b"canMakePayments",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKPaymentAuthorizationViewController",
        b"canMakePaymentsUsingNetworks:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKPaymentAuthorizationViewController",
        b"canMakePaymentsUsingNetworks:capabilities:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PKPaymentRequest",
        b"setSupportsCouponCode:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PKPaymentRequest", b"supportsCouponCode", {"retval": {"type": b"Z"}})
    r(
        b"PKShareablePassMetadata",
        b"initWithProvisioningCredentialIdentifier:sharingInstanceIdentifier:passThumbnailImage:ownerDisplayName:localizedDescription:accountHash:templateIdentifier:relyingPartyIdentifier:requiresUnifiedAccessCapableDevice:",
        {"arguments": {10: {"type": b"Z"}}},
    )
    r(
        b"PKShareablePassMetadata",
        b"requiresUnifiedAccessCapableDevice",
        {"retval": {"type": b"Z"}},
    )
    r(b"PKStoredValuePassBalance", b"isEqualToBalance:", {"retval": {"type": b"Z"}})
    r(b"PKStoredValuePassProperties", b"isBlacklisted", {"retval": {"type": b"Z"}})
    r(b"PKStoredValuePassProperties", b"isBlocked", {"retval": {"type": b"Z"}})
    r(b"PKStoredValuePassProperties", b"isInStation", {"retval": {"type": "Z"}})
    r(
        b"PKSuicaPassProperties",
        b"isBalanceAllowedForCommute",
        {"retval": {"type": b"Z"}},
    )
    r(b"PKSuicaPassProperties", b"isBlacklisted", {"retval": {"type": b"Z"}})
    r(b"PKSuicaPassProperties", b"isGreenCarTicketUsed", {"retval": {"type": b"Z"}})
    r(b"PKSuicaPassProperties", b"isInShinkansenStation", {"retval": {"type": b"Z"}})
    r(b"PKSuicaPassProperties", b"isInStation", {"retval": {"type": b"Z"}})
    r(
        b"PKSuicaPassProperties",
        b"isLowBalanceGateNotificationEnabled",
        {"retval": {"type": b"Z"}},
    )
    r(b"PKTransitPassProperties", b"isBlacklisted", {"retval": {"type": b"Z"}})
    r(b"PKTransitPassProperties", b"isBlocked", {"retval": {"type": "Z"}})
    r(b"PKTransitPassProperties", b"isInStation", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
