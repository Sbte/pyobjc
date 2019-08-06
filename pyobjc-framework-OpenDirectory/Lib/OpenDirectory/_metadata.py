# This file is generated by objective.metadata
#
# Last update: Sun Aug  4 21:19:40 2019

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a

misc = {
}
constants = '''$ODFrameworkErrorDomain$ODSessionProxyAddress$ODSessionProxyPassword$ODSessionProxyPort$ODSessionProxyUsername$ODTrustTypeAnonymous$ODTrustTypeJoined$ODTrustTypeUsingCredentials$kODAttributeTypeNodeSASLRealm$kODAttributeTypeProfiles$kODAttributeTypeProfilesTimestamp$kODBackOffSeconds$kODModuleConfigOptionConnectionIdleDisconnect$kODModuleConfigOptionConnectionSetupTimeout$kODModuleConfigOptionManInTheMiddle$kODModuleConfigOptionPacketEncryption$kODModuleConfigOptionPacketSigning$kODModuleConfigOptionQueryTimeout$kODPolicyAttributeCreationTime$kODPolicyAttributeCurrentDate$kODPolicyAttributeCurrentDayOfWeek$kODPolicyAttributeCurrentTime$kODPolicyAttributeCurrentTimeOfDay$kODPolicyAttributeDaysUntilExpiration$kODPolicyAttributeEnableAtTimeOfDay$kODPolicyAttributeEnableOnDate$kODPolicyAttributeEnableOnDayOfWeek$kODPolicyAttributeExpiresAtTimeOfDay$kODPolicyAttributeExpiresEveryNDays$kODPolicyAttributeExpiresOnDate$kODPolicyAttributeExpiresOnDayOfWeek$kODPolicyAttributeFailedAuthentications$kODPolicyAttributeLastAuthenticationTime$kODPolicyAttributeLastFailedAuthenticationTime$kODPolicyAttributeLastPasswordChangeTime$kODPolicyAttributeMaximumFailedAuthentications$kODPolicyAttributeNewPasswordRequiredTime$kODPolicyAttributePassword$kODPolicyAttributePasswordHashes$kODPolicyAttributePasswordHistory$kODPolicyAttributePasswordHistoryDepth$kODPolicyAttributeRecordName$kODPolicyAttributeRecordType$kODPolicyCategoryAuthentication$kODPolicyCategoryPasswordChange$kODPolicyCategoryPasswordContent$kODPolicyKeyContent$kODPolicyKeyContentDescription$kODPolicyKeyEvaluationDetails$kODPolicyKeyIdentifier$kODPolicyKeyParameters$kODPolicyKeyPolicySatisfied$kODPolicyTypeAccountExpiresOnDate$kODPolicyTypeAccountMaximumFailedLogins$kODPolicyTypeAccountMaximumMinutesOfNonUse$kODPolicyTypeAccountMaximumMinutesUntilDisabled$kODPolicyTypeAccountMinutesUntilFailedLoginReset$kODPolicyTypePasswordCannotBeAccountName$kODPolicyTypePasswordChangeRequired$kODPolicyTypePasswordHistory$kODPolicyTypePasswordMaximumAgeInMinutes$kODPolicyTypePasswordMaximumNumberOfCharacters$kODPolicyTypePasswordMinimumNumberOfCharacters$kODPolicyTypePasswordRequiresAlpha$kODPolicyTypePasswordRequiresMixedCase$kODPolicyTypePasswordRequiresNumeric$kODPolicyTypePasswordRequiresSymbol$kODPolicyTypePasswordSelfModification$'''
enums = '''$ODPacketEncryptionAllow@1$ODPacketEncryptionDisabled@0$ODPacketEncryptionRequired@2$ODPacketEncryptionSSL@3$ODPacketSigningAllow@1$ODPacketSigningDisabled@0$ODPacketSigningRequired@2$kODErrorCredentialsAccountLocked@5305$kODErrorCredentialsAccountTemporarilyLocked@5304$kODErrorPolicyOutOfRange@6001$kODErrorPolicyUnsupported@6000$kODExpirationTimeExpired@0$kODExpirationTimeNeverExpires@-1$'''
misc.update({})
functions={'ODNodeCustomFunction': (b'@^{__ODNode=}@@^^{__CFError=}', '', {'arguments': {3: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordSetPolicy': (b'B^{__ODRecord=}@@^^{__CFError=}', '', {'arguments': {3: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODNodeCopySupportedPolicies': (b'^{__CFDictionary=}^{__ODNode=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordCopySupportedPolicies': (b'^{__CFDictionary=}^{__ODRecord=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODNodeRemovePolicy': (b'B^{__ODNode=}@^^{__CFError=}', '', {'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordSecondsUntilPasswordExpires': (b'q^{__ODRecord=}',), 'ODRecordPasswordChangeAllowed': (b'B^{__ODRecord=}@^^{__CFError=}', '', {'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordSetPolicies': (b'B^{__ODRecord=}^{__CFDictionary=}^^{__CFError=}', '', {'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODNodePasswordContentCheck': (b'B^{__ODNode=}@@^^{__CFError=}', '', {'arguments': {3: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordCopyAccountPolicies': (b'^{__CFDictionary=}^{__ODRecord=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordSecondsUntilAuthenticationsExpire': (b'q^{__ODRecord=}',), 'ODRecordCopyPolicies': (b'^{__CFDictionary=}^{__ODRecord=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordRemovePolicy': (b'B^{__ODRecord=}@^^{__CFError=}', '', {'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordAddAccountPolicy': (b'B^{__ODRecord=}^{__CFDictionary=}@^^{__CFError=}', '', {'arguments': {3: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordWillPasswordExpire': (b'B^{__ODRecord=}Q',), 'ODNodeRemoveAccountPolicy': (b'B^{__ODNode=}^{__CFDictionary=}@^^{__CFError=}', '', {'arguments': {3: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODNodeCopyAccountPolicies': (b'^{__CFDictionary=}^{__ODNode=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODNodeSetAccountPolicies': (b'B^{__ODNode=}^{__CFDictionary=}^^{__CFError=}', '', {'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordWillAuthenticationsExpire': (b'B^{__ODRecord=}Q',), 'ODNodeCopyPolicies': (b'^{__CFDictionary=}^{__ODNode=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODNodeSetPolicies': (b'B^{__ODNode=}^{__CFDictionary=}^^{__CFError=}', '', {'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordRemoveAccountPolicy': (b'B^{__ODRecord=}^{__CFDictionary=}@^^{__CFError=}', '', {'arguments': {3: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordCopyEffectivePolicies': (b'^{__CFDictionary=}^{__ODRecord=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordSetAccountPolicies': (b'B^{__ODRecord=}^{__CFDictionary=}^^{__CFError=}', '', {'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODRecordAuthenticationAllowed': (b'B^{__ODRecord=}^^{__CFError=}', '', {'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'ODNodeAddAccountPolicy': (b'B^{__ODNode=}^{__CFDictionary=}@^^{__CFError=}', '', {'arguments': {3: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}})}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'query:foundResults:error:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r(b'ODConfiguration', b'addTrustType:trustAccount:trustPassword:username:password:joinExisting:error:', {'retval': {'type': b'Z'}, 'arguments': {7: {'type': b'Z'}, 8: {'type_modifier': b'o'}}})
    r(b'ODConfiguration', b'hideRegistration', {'retval': {'type': b'Z'}})
    r(b'ODConfiguration', b'manInTheMiddleProtection', {'retval': {'type': b'Z'}})
    r(b'ODConfiguration', b'removeTrustUsingUsername:password:deleteTrustAccount:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type': b'Z'}, 5: {'type_modifier': b'o'}}})
    r(b'ODConfiguration', b'saveUsingAuthorization:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODConfiguration', b'setHideRegistration:', {'arguments': {2: {'type': b'Z'}}})
    r(b'ODConfiguration', b'setManInTheMiddleProtection:', {'arguments': {2: {'type': b'Z'}}})
    r(b'ODConfiguration', b'trustUsesKerberosKeytab', {'retval': {'type': b'Z'}})
    r(b'ODConfiguration', b'trustUsesMutualAuthentication', {'retval': {'type': b'Z'}})
    r(b'ODConfiguration', b'trustUsesSystemKeychain', {'retval': {'type': b'Z'}})
    r(b'ODNode', b'accountPoliciesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODNode', b'addAccountPolicy:toCategory:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'createRecordWithRecordType:name:attributes:error:', {'arguments': {5: {'type_modifier': b'o'}}})
    r(b'ODNode', b'customCall:sendData:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'customFunction:payload:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'initWithSession:name:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'initWithSession:type:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'nodeDetailsForKeys:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODNode', b'nodeWithSession:name:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'nodeWithSession:type:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'passwordContentCheck:forRecordName:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'policiesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODNode', b'recordWithRecordType:name:attributes:error:', {'arguments': {5: {'type_modifier': b'o'}}})
    r(b'ODNode', b'removeAccountPolicy:fromCategory:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'removePolicy:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODNode', b'setAccountPolicies:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODNode', b'setCredentialsUsingKerberosCache:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODNode', b'setCredentialsWithRecordType:authenticationType:authenticationItems:continueItems:context:error:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type_modifier': b'o'}, 6: {'type_modifier': b'o'}, 7: {'type_modifier': b'o'}}})
    r(b'ODNode', b'setCredentialsWithRecordType:recordName:password:error:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r(b'ODNode', b'setPolicies:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODNode', b'setPolicy:value:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODNode', b'subnodeNamesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODNode', b'supportedAttributesForRecordType:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODNode', b'supportedPoliciesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODNode', b'supportedRecordTypesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODNode', b'unreachableSubnodeNamesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODQuery', b'initWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:', {'arguments': {9: {'type_modifier': b'o'}}})
    r(b'ODQuery', b'queryWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:', {'arguments': {9: {'type_modifier': b'o'}}})
    r(b'ODQuery', b'resultsAllowingPartial:error:', {'arguments': {2: {'type': b'Z'}, 3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'accountPoliciesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'addAccountPolicy:toCategory:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'addMemberRecord:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'addValue:toAttribute:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'authenticationAllowedAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'changePassword:toPassword:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'deleteRecordAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'effectivePoliciesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'isMemberRecord:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'passwordChangeAllowed:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'passwordPolicyAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'policiesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'recordDetailsForAttributes:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'removeAccountPolicy:fromCategory:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'removeMemberRecord:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'removePolicy:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'removeValue:fromAttribute:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'removeValuesForAttribute:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'setAccountPolicies:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'setNodeCredentials:password:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'setNodeCredentialsUsingKerberosCache:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'setNodeCredentialsWithRecordType:authenticationType:authenticationItems:continueItems:context:error:', {'retval': {'type': b'Z'}, 'arguments': {5: {'type_modifier': b'o'}, 6: {'type_modifier': b'o'}, 7: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'setPolicies:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'setPolicy:value:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'setValue:forAttribute:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'supportedPoliciesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'synchronizeAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'valuesForAttribute:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'verifyExtendedWithAuthenticationType:authenticationItems:continueItems:context:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}, 5: {'type_modifier': b'o'}, 6: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'verifyPassword:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODRecord', b'willAuthenticationsExpire:', {'retval': {'type': b'Z'}})
    r(b'ODRecord', b'willPasswordExpire:', {'retval': {'type': b'Z'}})
    r(b'ODSession', b'addConfiguration:authorization:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODSession', b'configurationAuthorizationAllowingUserInteraction:error:', {'arguments': {2: {'type': b'Z'}, 3: {'type_modifier': b'o'}}})
    r(b'ODSession', b'deleteConfiguration:authorization:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODSession', b'deleteConfigurationWithNodename:authorization:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r(b'ODSession', b'initWithOptions:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'ODSession', b'nodeNamesAndReturnError:', {'arguments': {2: {'type_modifier': b'o'}}})
    r(b'ODSession', b'sessionWithOptions:error:', {'arguments': {3: {'type_modifier': b'o'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
