# This file is generated by objective.metadata
#
# Last update: Thu Feb  9 18:09:26 2012

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$NSAddedPersistentStoresKey$NSAffectedObjectsErrorKey$NSAffectedStoresErrorKey$NSBinaryExternalRecordType$NSBinaryStoreType$NSCoreDataVersionNumber@d$NSDeletedObjectsKey$NSDetailedErrorsKey$NSEntityNameInPathKey$NSErrorMergePolicy$NSExternalRecordExtensionOption$NSExternalRecordsDirectoryOption$NSExternalRecordsFileFormatOption$NSIgnorePersistentStoreVersioningOption$NSInMemoryStoreType$NSInferMappingModelAutomaticallyOption$NSInsertedObjectsKey$NSInvalidatedAllObjectsKey$NSInvalidatedObjectsKey$NSManagedObjectContextDidSaveNotification$NSManagedObjectContextObjectsDidChangeNotification$NSManagedObjectContextWillSaveNotification$NSMergeByPropertyObjectTrumpMergePolicy$NSMergeByPropertyStoreTrumpMergePolicy$NSMigratePersistentStoresAutomaticallyOption$NSMigrationDestinationObjectKey$NSMigrationEntityMappingKey$NSMigrationEntityPolicyKey$NSMigrationManagerKey$NSMigrationPropertyMappingKey$NSMigrationSourceObjectKey$NSModelPathKey$NSObjectURIKey$NSOverwriteMergePolicy$NSPersistentStoreCoordinatorStoresDidChangeNotification$NSPersistentStoreCoordinatorWillRemoveStoreNotification$NSPersistentStoreDidImportUbiquitousContentChangesNotification$NSPersistentStoreOSCompatibility$NSPersistentStoreSaveConflictsErrorKey$NSPersistentStoreTimeoutOption$NSPersistentStoreUbiquitousContentNameKey$NSPersistentStoreUbiquitousContentURLKey$NSReadOnlyPersistentStoreOption$NSRefreshedObjectsKey$NSRemovedPersistentStoresKey$NSRollbackMergePolicy$NSSQLiteAnalyzeOption$NSSQLiteErrorDomain$NSSQLiteManualVacuumOption$NSSQLitePragmasOption$NSSQLiteStoreType$NSStoreModelVersionHashesKey$NSStoreModelVersionIdentifiersKey$NSStorePathKey$NSStoreTypeKey$NSStoreUUIDInPathKey$NSStoreUUIDKey$NSUUIDChangedPersistentStoresKey$NSUpdatedObjectsKey$NSValidateXMLStoreOption$NSValidationKeyErrorKey$NSValidationObjectErrorKey$NSValidationPredicateErrorKey$NSValidationValueErrorKey$NSXMLExternalRecordType$NSXMLStoreType$'''
enums = '''$NSAddEntityMappingType@2$NSBinaryDataAttributeType@1000$NSBooleanAttributeType@800$NSCascadeDeleteRule@2$NSConfinementConcurrencyType@0$NSCopyEntityMappingType@4$NSCoreDataError@134060$NSCountResultType@4$NSCustomEntityMappingType@1$NSDateAttributeType@900$NSDecimalAttributeType@400$NSDenyDeleteRule@3$NSDictionaryResultType@2$NSDoubleAttributeType@500$NSEntityMigrationPolicyError@134170$NSErrorMergePolicyType@0$NSExternalRecordImportError@134200$NSFetchRequestExpressionType@50$NSFetchRequestType@1$NSFloatAttributeType@600$NSInferredMappingModelError@134190$NSInteger16AttributeType@100$NSInteger32AttributeType@200$NSInteger64AttributeType@300$NSMainQueueConcurrencyType@2$NSManagedObjectContextLockingError@132000$NSManagedObjectExternalRelationshipError@133010$NSManagedObjectIDResultType@1$NSManagedObjectMergeError@133020$NSManagedObjectReferentialIntegrityError@133000$NSManagedObjectResultType@0$NSManagedObjectValidationError@1550$NSMergeByPropertyObjectTrumpMergePolicyType@2$NSMergeByPropertyStoreTrumpMergePolicyType@1$NSMigrationCancelledError@134120$NSMigrationError@134110$NSMigrationManagerDestinationStoreError@134160$NSMigrationManagerSourceStoreError@134150$NSMigrationMissingMappingModelError@134140$NSMigrationMissingSourceModelError@134130$NSNoActionDeleteRule@0$NSNullifyDeleteRule@1$NSObjectIDAttributeType@2000$NSOverwriteMergePolicyType@3$NSPersistentStoreCoordinatorLockingError@132010$NSPersistentStoreIncompatibleSchemaError@134020$NSPersistentStoreIncompatibleVersionHashError@134100$NSPersistentStoreIncompleteSaveError@134040$NSPersistentStoreInvalidTypeError@134000$NSPersistentStoreOpenError@134080$NSPersistentStoreOperationError@134070$NSPersistentStoreSaveConflictsError@134050$NSPersistentStoreSaveError@134030$NSPersistentStoreTimeoutError@134090$NSPersistentStoreTypeMismatchError@134010$NSPersistentStoreUnsupportedRequestTypeError@134091$NSPrivateQueueConcurrencyType@1$NSRemoveEntityMappingType@3$NSRollbackMergePolicyType@4$NSSQLiteError@134180$NSSaveRequestType@2$NSSnapshotEventMergePolicy@64$NSSnapshotEventRefresh@32$NSSnapshotEventRollback@16$NSSnapshotEventUndoDeletion@4$NSSnapshotEventUndoInsertion@2$NSSnapshotEventUndoUpdate@8$NSStringAttributeType@700$NSTransformEntityMappingType@5$NSTransformableAttributeType@1800$NSUndefinedAttributeType@0$NSUndefinedEntityMappingType@0$NSValidationDateTooLateError@1630$NSValidationDateTooSoonError@1640$NSValidationInvalidDateError@1650$NSValidationMissingMandatoryPropertyError@1570$NSValidationMultipleErrorsError@1560$NSValidationNumberTooLargeError@1610$NSValidationNumberTooSmallError@1620$NSValidationRelationshipDeniedDeleteError@1600$NSValidationRelationshipExceedsMaximumCountError@1590$NSValidationRelationshipLacksMinimumCountError@1580$NSValidationStringPatternMatchingError@1680$NSValidationStringTooLongError@1660$NSValidationStringTooShortError@1670$'''
misc.update({'NSCoreDataVersionNumber_iPhoneOS_3_0': 241.0, 'NSCoreDataVersionNumber_iPhoneOS_3_1': 248.0, 'NSCoreDataVersionNumber_iPhoneOS_3_2': 310.2, 'NSCoreDataVersionNumber10_6_2': 250.0, 'NSCoreDataVersionNumber10_6_3': 251.0, 'NSCoreDataVersionNumber_iPhoneOS_4_2': 320.15, 'NSCoreDataVersionNumber_iPhoneOS_4_1': 320.11, 'NSCoreDataVersionNumber_iPhoneOS_4_0': 320.5, 'NSCoreDataVersionNumber10_4': 46.0, 'NSCoreDataVersionNumber10_5_3': 186.0, 'NSCoreDataVersionNumber_iPhoneOS_4_3': 320.17, 'NSCoreDataVersionNumber10_6': 246.0, 'NSCoreDataVersionNumber10_4_3': 77.0, 'NSCoreDataVersionNumber10_5': 185.0})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSAtomicStore', b'load:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSAtomicStore', b'save:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSAttributeDescription', b'allowsExternalBinaryDataStorage', {'retval': {'type': b'Z'}})
    r('NSAttributeDescription', b'setAllowsExternalBinaryDataStorage:', {'arguments': {2: {'type': b'Z'}}})
    r('NSEntityDescription', b'isAbstract', {'retval': {'type': 'Z'}})
    r('NSEntityDescription', b'isKindOfEntity:', {'retval': {'type': 'Z'}})
    r('NSEntityDescription', b'setAbstract:', {'arguments': {2: {'type': 'Z'}}})
    r('NSEntityMigrationPolicy', b'beginEntityMapping:manager:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'createDestinationInstancesForSourceInstance:entityMapping:manager:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'createRelationshipsForDestinationInstance:entityMapping:manager:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'endEntityMapping:manager:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'endInstanceCreationForEntityMapping:manager:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'endRelationshipCreationForEntityMapping:manager:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSEntityMigrationPolicy', b'performCustomValidationForEntityMapping:manager:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSFetchRequest', b'includesPendingChanges', {'retval': {'type': 'Z'}})
    r('NSFetchRequest', b'includesPropertyValues', {'retval': {'type': 'Z'}})
    r('NSFetchRequest', b'includesSubentities', {'retval': {'type': 'Z'}})
    r('NSFetchRequest', b'returnsDistinctResults', {'retval': {'type': 'Z'}})
    r('NSFetchRequest', b'returnsObjectsAsFaults', {'retval': {'type': 'Z'}})
    r('NSFetchRequest', b'setIncludesPendingChanges:', {'arguments': {2: {'type': 'Z'}}})
    r('NSFetchRequest', b'setIncludesPropertyValues:', {'arguments': {2: {'type': 'Z'}}})
    r('NSFetchRequest', b'setIncludesSubentities:', {'arguments': {2: {'type': 'Z'}}})
    r('NSFetchRequest', b'setReturnsDistinctResults:', {'arguments': {2: {'type': 'Z'}}})
    r('NSFetchRequest', b'setReturnsObjectsAsFaults:', {'arguments': {2: {'type': 'Z'}}})
    r('NSFetchRequest', b'setShouldRefreshRefetchedObjects:', {'arguments': {2: {'type': b'Z'}}})
    r('NSFetchRequest', b'shouldRefreshRefetchedObjects', {'retval': {'type': b'Z'}})
    r('NSFetchRequestExpression', b'expressionForFetch:context:countOnly:', {'arguments': {4: {'type': 'Z'}}})
    r('NSFetchRequestExpression', b'isCountOnlyRequest', {'retval': {'type': 'Z'}})
    r('NSIncrementalStore', b'loadMetadata:', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'contextShouldIgnoreUnmodeledPropertyChanges', {'retval': {'type': 'Z'}})
    r('NSManagedObject', b'hasChanges', {'retval': {'type': b'Z'}})
    r('NSManagedObject', b'hasFaultForRelationshipNamed:', {'retval': {'type': 'Z'}})
    r('NSManagedObject', b'isDeleted', {'retval': {'type': 'Z'}})
    r('NSManagedObject', b'isFault', {'retval': {'type': 'Z'}})
    r('NSManagedObject', b'isInserted', {'retval': {'type': 'Z'}})
    r('NSManagedObject', b'isUpdated', {'retval': {'type': 'Z'}})
    r('NSManagedObject', b'observationInfo', {'retval': {'type': '^v'}})
    r('NSManagedObject', b'setObservationInfo:', {'arguments': {2: {'type': '^v'}}})
    r('NSManagedObject', b'validateForDelete:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSManagedObject', b'validateForInsert:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSManagedObject', b'validateForUpdate:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSManagedObject', b'validateValue:forKey:error:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'N'}, 4: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'countForFetchRequest:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'executeFetchRequest:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'existingObjectWithID:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'hasChanges', {'retval': {'type': 'Z'}})
    r('NSManagedObjectContext', b'observeValueForKeyPath:ofObject:change:context:', {'arguments': {5: {'type': '^v'}}})
    r('NSManagedObjectContext', b'obtainPermanentIDsForObjects:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'propagatesDeletesAtEndOfEvent', {'retval': {'type': 'Z'}})
    r('NSManagedObjectContext', b'refreshObject:mergeChanges:', {'arguments': {3: {'type': 'Z'}}})
    r('NSManagedObjectContext', b'retainsRegisteredObjects', {'retval': {'type': 'Z'}})
    r('NSManagedObjectContext', b'save:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSManagedObjectContext', b'setPropagatesDeletesAtEndOfEvent:', {'arguments': {2: {'type': 'Z'}}})
    r('NSManagedObjectContext', b'setRetainsRegisteredObjects:', {'arguments': {2: {'type': 'Z'}}})
    r('NSManagedObjectContext', b'tryLock', {'retval': {'type': 'Z'}})
    r('NSManagedObjectID', b'isTemporaryID', {'retval': {'type': 'Z'}})
    r('NSManagedObjectModel', b'isConfiguration:compatibleWithStoreMetadata:', {'retval': {'type': 'Z'}})
    r('NSMappingModel', b'inferredMappingModelForSourceModel:destinationModel:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r('NSMergePolicy', b'resolveConflicts:error:', {'retval': {'type': b'Z'}})
    r('NSMigrationManager', b'migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:', {'retval': {'type': 'Z'}, 'arguments': {9: {'type_modifier': b'o'}}})
    r('NSMigrationManager', b'setUsesStoreSpecificMigrationManager:', {'arguments': {2: {'type': b'Z'}}})
    r('NSMigrationManager', b'usesStoreSpecificMigrationManager', {'retval': {'type': b'Z'}})
    r('NSPersistentStore', b'isReadOnly', {'retval': {'type': 'Z'}})
    r('NSPersistentStore', b'loadMetadata:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('NSPersistentStore', b'metadataForPersistentStoreWithURL:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSPersistentStore', b'setMetadata:forPersistentStoreWithURL:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('NSPersistentStore', b'setReadOnly:', {'arguments': {2: {'type': 'Z'}}})
    r('NSPersistentStoreCoordinator', b'addPersistentStoreWithType:configuration:URL:options:error:', {'arguments': {6: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'importStoreWithIdentifier:fromExternalRecordsDirectory:toURL:options:withType:error:', {'arguments': {7: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'metadataForPersistentStoreOfType:URL:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'metadataForPersistentStoreWithURL:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'migratePersistentStore:toURL:options:withType:error:', {'arguments': {6: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'removePersistentStore:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'setMetadata:forPersistentStoreOfType:URL:error:', {'retval': {'type': 'Z'}, 'arguments': {5: {'type_modifier': b'o'}}})
    r('NSPersistentStoreCoordinator', b'setURL:forPersistentStore:', {'retval': {'type': 'Z'}})
    r('NSPersistentStoreCoordinator', b'tryLock', {'retval': {'type': 'Z'}})
    r('NSPropertyDescription', b'isIndexed', {'retval': {'type': 'Z'}})
    r('NSPropertyDescription', b'isIndexedBySpotlight', {'retval': {'type': 'Z'}})
    r('NSPropertyDescription', b'isOptional', {'retval': {'type': 'Z'}})
    r('NSPropertyDescription', b'isStoredInExternalRecord', {'retval': {'type': 'Z'}})
    r('NSPropertyDescription', b'isTransient', {'retval': {'type': 'Z'}})
    r('NSPropertyDescription', b'setIndexed:', {'arguments': {2: {'type': 'Z'}}})
    r('NSPropertyDescription', b'setIndexedBySpotlight:', {'arguments': {2: {'type': 'Z'}}})
    r('NSPropertyDescription', b'setOptional:', {'arguments': {2: {'type': 'Z'}}})
    r('NSPropertyDescription', b'setStoredInExternalRecord:', {'arguments': {2: {'type': 'Z'}}})
    r('NSPropertyDescription', b'setTransient:', {'arguments': {2: {'type': 'Z'}}})
    r('NSRelationshipDescription', b'isOrdered', {'retval': {'type': b'Z'}})
    r('NSRelationshipDescription', b'isToMany', {'retval': {'type': 'Z'}})
    r('NSRelationshipDescription', b'setOrdered:', {'arguments': {2: {'type': b'Z'}}})
finally:
    objc._updatingMetadata(False)

# END OF FILE