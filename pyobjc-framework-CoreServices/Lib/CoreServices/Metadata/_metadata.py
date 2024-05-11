# This file is generated by objective.metadata
#
# Last update: Sat May 11 12:07:18 2024
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
misc.update(
    {
        "MDQueryBatchingParams": objc.createStructType(
            "CoreServices.Metadata.MDQueryBatchingParams",
            b"{MDQueryBatchingParams=QQQQQQ}",
            [
                "first_max_num",
                "first_max_ms",
                "progress_max_num",
                "progress_max_ms",
                "update_max_num",
                "update_max_ms",
            ],
        )
    }
)
constants = """$kMDAttributeAllValues$kMDAttributeDisplayValues$kMDAttributeMultiValued$kMDAttributeName$kMDAttributeReadOnlyValues$kMDAttributeType$kMDExporterAvaliable$kMDItemAcquisitionMake$kMDItemAcquisitionModel$kMDItemAlbum$kMDItemAltitude$kMDItemAperture$kMDItemAppleLoopDescriptors$kMDItemAppleLoopsKeyFilterType$kMDItemAppleLoopsLoopMode$kMDItemAppleLoopsRootKey$kMDItemApplicationCategories$kMDItemAttributeChangeDate$kMDItemAudiences$kMDItemAudioBitRate$kMDItemAudioChannelCount$kMDItemAudioEncodingApplication$kMDItemAudioSampleRate$kMDItemAudioTrackNumber$kMDItemAuthorAddresses$kMDItemAuthorEmailAddresses$kMDItemAuthors$kMDItemBitsPerSample$kMDItemCFBundleIdentifier$kMDItemCameraOwner$kMDItemCity$kMDItemCodecs$kMDItemColorSpace$kMDItemComment$kMDItemComposer$kMDItemContactKeywords$kMDItemContentCreationDate$kMDItemContentModificationDate$kMDItemContentType$kMDItemContentTypeTree$kMDItemContributors$kMDItemCopyright$kMDItemCountry$kMDItemCoverage$kMDItemCreator$kMDItemDateAdded$kMDItemDeliveryType$kMDItemDescription$kMDItemDirector$kMDItemDisplayName$kMDItemDownloadedDate$kMDItemDueDate$kMDItemDurationSeconds$kMDItemEXIFGPSVersion$kMDItemEXIFVersion$kMDItemEditors$kMDItemEmailAddresses$kMDItemEncodingApplications$kMDItemExecutableArchitectures$kMDItemExecutablePlatform$kMDItemExposureMode$kMDItemExposureProgram$kMDItemExposureTimeSeconds$kMDItemExposureTimeString$kMDItemFNumber$kMDItemFSContentChangeDate$kMDItemFSCreationDate$kMDItemFSExists$kMDItemFSHasCustomIcon$kMDItemFSInvisible$kMDItemFSIsExtensionHidden$kMDItemFSIsReadable$kMDItemFSIsStationery$kMDItemFSIsWriteable$kMDItemFSLabel$kMDItemFSName$kMDItemFSNodeCount$kMDItemFSOwnerGroupID$kMDItemFSOwnerUserID$kMDItemFSSize$kMDItemFinderComment$kMDItemFlashOnOff$kMDItemFocalLength$kMDItemFocalLength35mm$kMDItemFonts$kMDItemGPSAreaInformation$kMDItemGPSDOP$kMDItemGPSDateStamp$kMDItemGPSDestBearing$kMDItemGPSDestDistance$kMDItemGPSDestLatitude$kMDItemGPSDestLongitude$kMDItemGPSDifferental$kMDItemGPSMapDatum$kMDItemGPSMeasureMode$kMDItemGPSProcessingMethod$kMDItemGPSStatus$kMDItemGPSTrack$kMDItemGenre$kMDItemHTMLContent$kMDItemHasAlphaChannel$kMDItemHeadline$kMDItemISOSpeed$kMDItemIdentifier$kMDItemImageDirection$kMDItemInformation$kMDItemInstantMessageAddresses$kMDItemInstructions$kMDItemIsApplicationManaged$kMDItemIsGeneralMIDISequence$kMDItemIsLikelyJunk$kMDItemKeySignature$kMDItemKeywords$kMDItemKind$kMDItemLabelID$kMDItemLabelIcon$kMDItemLabelKind$kMDItemLabelUUID$kMDItemLanguages$kMDItemLastUsedDate$kMDItemLatitude$kMDItemLayerNames$kMDItemLensModel$kMDItemLongitude$kMDItemLyricist$kMDItemMaxAperture$kMDItemMediaTypes$kMDItemMeteringMode$kMDItemMusicalGenre$kMDItemMusicalInstrumentCategory$kMDItemMusicalInstrumentName$kMDItemNamedLocation$kMDItemNumberOfPages$kMDItemOrganizations$kMDItemOrientation$kMDItemOriginalFormat$kMDItemOriginalSource$kMDItemPageHeight$kMDItemPageWidth$kMDItemParticipants$kMDItemPath$kMDItemPerformers$kMDItemPhoneNumbers$kMDItemPixelCount$kMDItemPixelHeight$kMDItemPixelWidth$kMDItemProducer$kMDItemProfileName$kMDItemProjects$kMDItemPublishers$kMDItemRecipientAddresses$kMDItemRecipientEmailAddresses$kMDItemRecipients$kMDItemRecordingDate$kMDItemRecordingYear$kMDItemRedEyeOnOff$kMDItemResolutionHeightDPI$kMDItemResolutionWidthDPI$kMDItemRights$kMDItemSecurityMethod$kMDItemSpeed$kMDItemStarRating$kMDItemStateOrProvince$kMDItemStreamable$kMDItemSubject$kMDItemSupportFileType$kMDItemTempo$kMDItemTextContent$kMDItemTheme$kMDItemTimeSignature$kMDItemTimestamp$kMDItemTitle$kMDItemTotalBitRate$kMDItemURL$kMDItemVersion$kMDItemVideoBitRate$kMDItemWhereFroms$kMDItemWhiteBalance$kMDLabelAddedNotification$kMDLabelBundleURL$kMDLabelChangedNotification$kMDLabelContentChangeDate$kMDLabelDisplayName$kMDLabelIconData$kMDLabelIconUUID$kMDLabelIsMutuallyExclusiveSetMember$kMDLabelKind$kMDLabelKindIsMutuallyExclusiveSetKey$kMDLabelKindVisibilityKey$kMDLabelRemovedNotification$kMDLabelSetsFinderColor$kMDLabelUUID$kMDLabelVisibility$kMDPrivateVisibility$kMDPublicVisibility$kMDQueryDidFinishNotification$kMDQueryDidUpdateNotification$kMDQueryProgressNotification$kMDQueryResultContentRelevance$kMDQueryScopeAllIndexed$kMDQueryScopeComputer$kMDQueryScopeComputerIndexed$kMDQueryScopeHome$kMDQueryScopeNetwork$kMDQueryScopeNetworkIndexed$kMDQueryUpdateAddedItems$kMDQueryUpdateChangedItems$kMDQueryUpdateRemovedItems$"""
enums = """$kMDLabelLocalDomain@1$kMDLabelUserDomain@0$kMDQueryAllowFSTranslation@8$kMDQueryReverseSortOrderFlag@1$kMDQuerySynchronous@1$kMDQueryWantsUpdates@4$"""
misc.update(
    {
        "MDQuerySortOptionFlags": NewType("MDQuerySortOptionFlags", int),
        "MDLabelDomain": NewType("MDLabelDomain", int),
        "MDQueryOptionFlags": NewType("MDQueryOptionFlags", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "MDQueryCreate": (
        b"^{__MDQuery=}^{__CFAllocator=}^{__CFString=}^{__CFArray=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemCopyAttributes": (
        b"^{__CFDictionary=}^{__MDItem=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDLabelCreate": (
        b"^{__MDLabel=}^{__CFAllocator=}^{__CFString=}^{__CFString=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDLabelGetTypeID": (b"Q",),
    "MDQueryGetAttributeValueOfResultAtIndex": (b"@^{__MDQuery=}^{__CFString=}q",),
    "MDQueryCreateForItems": (
        b"^{__MDQuery=}^{__CFAllocator=}^{__CFString=}^{__CFArray=}^{__CFArray=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryCopyValueListAttributes": (
        b"^{__CFArray=}^{__MDQuery=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDLabelCopyAttributeName": (
        b"^{__CFString=}^{__MDLabel=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDCopyLabelsWithKind": (
        b"^{__CFArray=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetIndexOfResult": (b"q^{__MDQuery=}@",),
    "MDLabelDelete": (b"Z^{__MDLabel=}",),
    "MDSchemaCopyDisplayNameForAttribute": (
        b"^{__CFString=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemCopyAttribute": (
        b"@^{__MDItem=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryDisableUpdates": (b"v^{__MDQuery=}",),
    "MDItemCopyAttributeList": (
        b"^{__CFDictionary=}^{__MDItem=}",
        "",
        {"retval": {"already_cfretained": True}, "variadic": True},
    ),
    "MDItemCreate": (
        b"^{__MDItem=}^{__CFAllocator=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetSortOptionFlagsForAttribute": (b"I^{__MDQuery=}^{__CFString=}",),
    "MDQueryGetBatchingParameters": (b"{MDQueryBatchingParams=QQQQQQ}^{__MDQuery=}",),
    "MDCopyLabelWithUUID": (
        b"^{__MDLabel=}^{__CFUUID=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryEnableUpdates": (b"v^{__MDQuery=}",),
    "MDQuerySetMaxCount": (b"v^{__MDQuery=}q",),
    "MDQueryCopyValuesOfAttribute": (
        b"^{__CFArray=}^{__MDQuery=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemsCreateWithURLs": (
        b"^{__CFArray=}^{__CFAllocator=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQuerySetCreateValueFunction": (
        b"v^{__MDQuery=}^?^v^{CFArrayCallBacks=q^?^?^?^?}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"^v"},
                        "arguments": {
                            0: {"type": b"^{__MDQuery=}"},
                            1: {"type": b"^{__CFString=}"},
                            2: {"type": b"@"},
                            3: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "MDSchemaCopyDisplayDescriptionForAttribute": (
        b"^{__CFString=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDCopyLabelsMatchingExpression": (
        b"^{__CFArray=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQuerySetSortOrder": (b"Z^{__MDQuery=}^{__CFArray=}",),
    "MDQuerySetSortComparator": (
        b"v^{__MDQuery=}^?^v",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"q"},
                        "arguments": {
                            0: {
                                "type": b"^@",
                                "type_modifier": "n",
                                "c_array_of_variable_length": True,
                            },
                            1: {
                                "type": b"^@",
                                "type_modifier": "n",
                                "c_array_of_variable_length": True,
                            },
                            2: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "MDSchemaCopyAllAttributes": (
        b"^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryStop": (b"v^{__MDQuery=}",),
    "MDQuerySetSearchScope": (b"v^{__MDQuery=}^{__CFArray=}I",),
    "MDQueryIsGatheringComplete": (b"Z^{__MDQuery=}",),
    "MDQuerySetCreateResultFunction": (
        b"v^{__MDQuery=}^?^v^{CFArrayCallBacks=q^?^?^?^?}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"^v"},
                        "arguments": {
                            0: {"type": b"^{__MDQuery=}"},
                            1: {"type": b"^{__MDItem=}"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "MDItemCopyLabels": (
        b"^{__CFArray=}^{__MDItem=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDSchemaCopyAttributesForContentType": (
        b"^{__CFDictionary=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemSetLabel": (b"Z^{__MDItem=}^{__MDLabel=}",),
    "MDQueryExecute": (b"Z^{__MDQuery=}Q",),
    "MDQuerySetDispatchQueue": (b"v^{__MDQuery=}@",),
    "MDLabelSetAttributes": (b"Z^{__MDLabel=}^{__CFDictionary=}",),
    "MDItemGetTypeID": (b"Q",),
    "MDQueryCopyQueryString": (
        b"^{__CFString=}^{__MDQuery=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryCopySortingAttributes": (
        b"^{__CFArray=}^{__MDQuery=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQuerySetSortOptionFlagsForAttribute": (b"Z^{__MDQuery=}^{__CFString=}I",),
    "MDQuerySetBatchingParameters": (b"v^{__MDQuery=}{MDQueryBatchingParams=QQQQQQ}",),
    "MDQueryCreateSubset": (
        b"^{__MDQuery=}^{__CFAllocator=}^{__MDQuery=}^{__CFString=}^{__CFArray=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetTypeID": (b"Q",),
    "MDItemCreateWithURL": (
        b"^{__MDItem=}^{__CFAllocator=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQuerySetSortComparatorBlock": (
        b"v^{__MDQuery=}@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"q"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {
                                "type": "^@",
                                "type_modifier": "n",
                                "c_array_of_variable_length": True,
                            },
                            2: {
                                "type": "^@",
                                "type_modifier": "n",
                                "c_array_of_variable_length": True,
                            },
                        },
                    },
                    "block": {
                        "retval": {"type": b"q"},
                        "arguments": {0: {"type": b"^@"}, 1: {"type": b"^@"}},
                    },
                }
            }
        },
    ),
    "MDItemCopyAttributeNames": (
        b"^{__CFArray=}^{__MDItem=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetCountOfResultsWithAttributeValue": (b"q^{__MDQuery=}^{__CFString=}@",),
    "MDItemsCopyAttributes": (
        b"^{__CFArray=}^{__CFArray=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetResultCount": (b"q^{__MDQuery=}",),
    "MDCopyLabelKinds": (
        b"^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemRemoveLabel": (b"Z^{__MDItem=}^{__MDLabel=}",),
    "MDQueryGetResultAtIndex": (b"@^{__MDQuery=}q",),
    "MDSchemaCopyMetaAttributesForAttribute": (
        b"^{__CFDictionary=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDLabelCopyAttribute": (
        b"@^{__MDLabel=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
}
aliases = {
    "MD_AVAIL": "AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER",
    "MD_AVAIL_LEOPARD": "AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER",
}
cftypes = [
    ("MDItemRef", b"^{__MDItem=}", None, None),
    ("MDLabelRef", b"^{__MDLabel=}", None, None),
    ("MDQueryRef", b"^{__MDQuery=}", None, None),
]
expressions = {}

# END OF FILE
