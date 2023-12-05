import odrive
from odrive.enums import *
from actuator import *
from time import sleep
import numpy as np

SN_L0 = '384D34783539'
SN_L1 = '383F34723539'

odrv0 = odrive.find_any(serial_number=SN_L0)
odrv1 = odrive.find_any(serial_number=SN_L1)
leftFinger0 = Actuator(odrv0, 0.48, 1, 45)
leftFinger1 = Actuator(odrv1, -0.37, 1, 45)


leftFingerPosition = np.zeros(2)
rightFingerPosition = np.zeros(2)
prevLeftFingerPosition = np.zeros(2)
prevRightFingerPosition = np.zeros(2)

encoderDifferenceLeft = np.zeros(2)
encoderDifferenceRight = np.zeros(2)

def SetStartingPoint(motorDriverSerialNumber0, motorDriverSerialNumber1):
    serialNumber0 = motorDriverSerialNumber0
    serialNumber1 = motorDriverSerialNumber1
    odrv0 = odrive.find_any(serial_number = serialNumber0)
    odrv1 = odrive.find_any(serial_number = serialNumber1)
    odrv0.axis0.controller.input_pos = 0.45
    odrv1.axis0.controller.input_pos = 0.45

def AttackPoint1(motorDriverSerialNumber0, motorDriverSerialNumber1):
    serialNumber0 = motorDriverSerialNumber0
    serialNumber1 = motorDriverSerialNumber1
    odrv0 = odrive.find_any(serial_number = serialNumber0)
    odrv1 = odrive.find_any(serial_number = serialNumber1)
    odrv0.axis0.controller.input_pos = 0.50
    odrv1.axis0.controller.input_pos = 0.40

def Grap(motorDriverSerialNumber0, motorDriverSerialNumber1):
    serialNumber0 = motorDriverSerialNumber0
    serialNumber1 = motorDriverSerialNumber1
    odrv0 = odrive.find_any(serial_number = serialNumber0)
    odrv1 = odrive.find_any(serial_number = serialNumber1)
    odrv0.axis0.controller.input_pos = 0.62
    odrv1.axis0.controller.input_pos = 0.35


if __name__ == "__main__":
    count = 0
    firstRun = True
    SetStartingPoint(SN_L0, SN_L1)
    sleep(1)
    # AttackPoint1(SN_L0, SN_L1)
    # sleep(1)
    # Grap(SN_L0, SN_L1)
    while(count < 500):
        leftFingerPosition[0] = leftFinger0.encoder
        leftFingerPosition[1] = leftFinger1.encoder
        # rightFingerPosition[0] = rihgtFinger0.encoder
        # rightFingerPosition[1] = rihgtFinger1.encoder

        if(firstRun):
            prevLeftFingerPosition[0] = leftFingerPosition[0]
            prevLeftFingerPosition[1] = leftFingerPosition[1]
            firstRun = False

        encoderDifferenceLeft[0] = abs(leftFingerPosition[0] - prevLeftFingerPosition[0])
        encoderDifferenceLeft[1] = abs(leftFingerPosition[1] - prevLeftFingerPosition[1])

        if(encoderDifferenceLeft[0] > 0.0035 or encoderDifferenceLeft[1] > 0.0035):
            newControlSignal = True
            Grap(SN_L0, SN_L1)

    
        prevLeftFingerPosition[0] = leftFingerPosition[0]
        prevLeftFingerPosition[1] = leftFingerPosition[1]
        

        print(str(encoderDifferenceLeft))
        count = count + 1
        sleep(0.1)