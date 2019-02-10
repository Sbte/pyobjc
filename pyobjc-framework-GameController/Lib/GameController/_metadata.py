# This file is generated by objective.metadata
#
# Last update: Sun Feb 10 11:35:49 2019

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'GCMicroGamepadSnapshotData': objc.createStructType('GCMicroGamepadSnapshotData', b'{_GCMicroGamepadSnapshotData=SSffff}', ['version', 'size', 'dpadX', 'dpadY', 'buttonA', 'buttonX'], None, 1), 'GCQuaternion': objc.createStructType('GCQuaternion', b'{GCQuaternion=dddd}', ['x', 'y', 'z', 'w']), 'GCExtendedGamepadValueChangedHandler': objc.createStructType('GCExtendedGamepadValueChangedHandler', b'{_GCGamepadSnapShotDataV100=SSffffffff}', ['version', 'size', 'dpadX', 'dpadY', 'buttonA', 'buttonB', 'buttonX', 'buttonY', 'leftShoulder', 'rightShoulder']), 'GCAcceleration': objc.createStructType('GCAcceleration', b'{_GCAcceleration=ddd}', ['x', 'y', 'z']), 'GCGamepadSnapShotDataV100': objc.createStructType('GCGamepadSnapShotDataV100', b'{_GCGamepadSnapShotDataV100=SSffffffff}', ['version', 'size', 'dpadX', 'dpadY', 'buttonA', 'buttonB', 'buttonX', 'buttonY', 'leftShoulder', 'rightShoulder'], None, 1), 'GCEulerAngles': objc.createStructType('GCEulerAngles', b'{_GCEulerAngles=ddd}', ['pitch', 'yaw', 'roll']), 'GCExtendedGamepadSnapShotDataV100': objc.createStructType('GCExtendedGamepadSnapShotDataV100', b'{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}', ['version', 'size', 'dpadX', 'dpadY', 'buttonA', 'buttonB', 'buttonX', 'buttonY', 'leftShoulder', 'rightShoulder', 'leftThumbstickX', 'leftThumbstickY', 'rightThumbstickX', 'rightThumbstickY', 'leftTrigger', 'rightTrigger'], None, 1), 'GCRotationRate': objc.createStructType('GCRotationRate', b'{_GCRotationRate=ddd}', ['x', 'y', 'z']), 'GCMicroGamepadSnapShotDataV100': objc.createStructType('GCMicroGamepadSnapShotDataV100', b'{_GCMicroGamepadSnapShotDataV100=SSffff}', ['version', 'size', 'dpadX', 'dpadY', 'buttonA', 'buttonX'], None, 1), 'GCExtendedGamepadSnapshotData': objc.createStructType('GCExtendedGamepadSnapshotData', b'{_GCExtendedGamepadSnapshotData=SSffffffffffffffZZ}', ['version', 'size', 'dpadX', 'dpadY', 'buttonA', 'buttonB', 'buttonX', 'buttonY', 'leftShoulder', 'rightShoulder', 'leftThumbstickX', 'leftThumbstickY', 'rightThumbstickX', 'rightThumbstickY', 'leftTrigger', 'rightTrigger', 'leftThumbstickButton', 'rightThumbstickButton'], None, 1)})
constants = '''$GCControllerDidConnectNotification$GCControllerDidDisconnectNotification$GCCurrentExtendedGamepadSnapshotDataVersion@q$GCCurrentMicroGamepadSnapshotDataVersion@q$'''
enums = '''$GCControllerPlayerIndex1@0$GCControllerPlayerIndex2@1$GCControllerPlayerIndex3@2$GCControllerPlayerIndex4@3$GCControllerPlayerIndexUnset@-1$GCExtendedGamepadSnapshotDataVersion1@256$GCExtendedGamepadSnapshotDataVersion2@257$GCMicroGamepadSnapshotDataVersion1@256$'''
misc.update({})
functions={'GCExtendedGamepadSnapshotDataFromNSData': (b'Z^{_GCExtendedGamepadSnapshotData=SSffffffffffffffZZ}@', '', {'arguments': {0: {'type_modifier': 'o'}}}), 'NSDataFromGCMicroGamepadSnapShotDataV100': (b'@^{_GCMicroGamepadSnapShotDataV100=SSffff}', '', {'arguments': {0: {'type_modifier': 'n'}}}), 'GCGamepadSnapShotDataV100FromNSData': (b'Z^{_GCGamepadSnapShotDataV100=SSffffffff}@', '', {'arguments': {0: {'type_modifier': 'o'}}}), 'NSDataFromGCMicroGamepadSnapshotData': (b'@^{_GCMicroGamepadSnapshotData=SSffff}', '', {'arguments': {0: {'type_modifier': 'n'}}}), 'NSDataFromGCGamepadSnapShotDataV100': (b'@^{_GCGamepadSnapShotDataV100=SSffffffff}', '', {'arguments': {0: {'type_modifier': 'n'}}}), 'GCMicroGamepadSnapshotDataFromNSData': (b'Z^{_GCMicroGamepadSnapshotData=SSffff}@', '', {'arguments': {0: {'type_modifier': 'o'}}}), 'GCExtendedGamepadSnapShotDataV100FromNSData': (b'Z^{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}@', '', {'arguments': {0: {'type_modifier': 'o'}}}), 'GCMicroGamepadSnapShotDataV100FromNSData': (b'Z^{_GCMicroGamepadSnapShotDataV100=SSffff}@', '', {'arguments': {0: {'type_modifier': 'o'}}}), 'NSDataFromGCExtendedGamepadSnapShotDataV100': (b'@^{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}', '', {'arguments': {0: {'type_modifier': 'n'}}}), 'NSDataFromGCExtendedGamepadSnapshotData': (b'@^{_GCExtendedGamepadSnapshotData=SSffffffffffffffZZ}', '', {'arguments': {0: {'type_modifier': 'n'}}})}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'GCController', b'controllerPausedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'GCController', b'isAttachedToDevice', {'retval': {'type': b'Z'}})
    r(b'GCController', b'setControllerPausedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'GCController', b'startWirelessControllerDiscoveryWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'GCControllerAxisInput', b'setValueChangedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'f'}}}}}})
    r(b'GCControllerAxisInput', b'valueChangedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'f'}}}}})
    r(b'GCControllerButtonInput', b'isPressed', {'retval': {'type': b'Z'}})
    r(b'GCControllerButtonInput', b'pressedChangedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'f'}, 3: {'type': b'Z'}}}}})
    r(b'GCControllerButtonInput', b'setPressedChangedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'f'}, 3: {'type': b'Z'}}}}}})
    r(b'GCControllerButtonInput', b'setValueChangedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'f'}, 3: {'type': b'Z'}}}}}})
    r(b'GCControllerButtonInput', b'valueChangedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'f'}, 3: {'type': b'Z'}}}}})
    r(b'GCControllerDirectionPad', b'setValueChangedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'f'}, 3: {'type': b'f'}}}}}})
    r(b'GCControllerDirectionPad', b'valueChangedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'f'}, 3: {'type': b'f'}}}}})
    r(b'GCControllerElement', b'isAnalog', {'retval': {'type': b'Z'}})
    r(b'GCEventViewController', b'controllerUserInteractionEnabled', {'retval': {'type': 'Z'}})
    r(b'GCEventViewController', b'setControllerUserInteractionEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'GCExtendedGamepad', b'setValueChangedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'GCExtendedGamepad', b'valueChangedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'GCGamepad', b'setValueChangedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'GCGamepad', b'valueChangedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'GCMicroGamepad', b'allowsRotation', {'retval': {'type': 'Z'}})
    r(b'GCMicroGamepad', b'reportsAbsoluteDpadValues', {'retval': {'type': 'Z'}})
    r(b'GCMicroGamepad', b'setAllowsRotation:', {'arguments': {2: {'type': 'Z'}}})
    r(b'GCMicroGamepad', b'setReportsAbsoluteDpadValues:', {'arguments': {2: {'type': 'Z'}}})
    r(b'GCMicroGamepad', b'setValueChangedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'GCMicroGamepad', b'valueChangedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'GCMotion', b'gravity', {'retval': {'type': b'{_GCAcceleration=ddd}'}})
    r(b'GCMotion', b'hasAttitudeAndRotationRate', {'retval': {'type': 'Z'}})
    r(b'GCMotion', b'rotationRate', {'retval': {'type': b'{_GCRotationRate=ddd}'}})
    r(b'GCMotion', b'setValueChangedHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'GCMotion', b'userAcceleration', {'retval': {'type': b'{_GCAcceleration=ddd}'}})
    r(b'GCMotion', b'valueChangedHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
