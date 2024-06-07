from enum import Enum

class TransportEnum(Enum):
    UNDEFINE = 0
    AFOOT = 1
    BICYCLE = 2
    SCOOTER = 3
    PUBLICTRAN = 4
    CAR = 5

class TranSpeedEnum(Enum):
    UNDEFINE = 0
    AFOOT = 4.0
    BICYCLE = 8.0
    SCOOTER = 15.0
    PUBLICTRAN = 30.0
    CAR = 70.0