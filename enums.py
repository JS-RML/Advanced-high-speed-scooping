from enum import Enum
class MotorDriverSerialNumber(Enum):
    L0 = '384D34783539'
    L1 = '383F34723539'
    R0 = '3868345A3539'
    R1 = '3866346F3539'

class MotorState(Enum):
    IDLE = 0
    CONTROL = 1

FREQUANCY = 50 # Hz
