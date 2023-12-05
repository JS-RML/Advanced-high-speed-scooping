import odrive
from odrive.enums import *
from actuator import *
from time import sleep

SN_L0 = '384D34783539'
SN_L1 = '383F34723539'


def Docalibration(motorDriverSerialNumber):
    serialNumber = motorDriverSerialNumber
    odrv = odrive.find_any(serial_number = serialNumber)
    odrv.clear_errors()
    odrv.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE


def ControlMode(motorDriverSerialNumber):
    serialNumber = motorDriverSerialNumber
    odrv = odrive.find_any(serial_number = serialNumber)
    odrv.clear_errors()
    odrv.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

def SetMotorOffset(motorDriverSerialNumber):
    serialNumber = motorDriverSerialNumber
    odrv = odrive.find_any(serial_number = serialNumber)
    if(serialNumber == SN_L0):
        odrv.axis0.controller.input_pos = 0.48
    elif(serialNumber == SN_L1):
        odrv.axis0.controller.input_pos = 0.34

def GetMotorPosition(motorDriverSerialNumber):
    serialNumber = motorDriverSerialNumber
    odrv = odrive.find_any(serial_number = serialNumber)
    return odrv.encoder_estimator1.pos_estimate

if __name__ == "__main__":

    # Docalibration(SN_L0)
    # sleep(11)
    # ControlMode(SN_L0)
    # sleep(1)
    # SetMotorOffset(SN_L0)

    # Docalibration(SN_L1)
    # sleep(1)
    ControlMode(SN_L1)
    # sleep(1)
    # SetMotorOffset(SN_L1)
    # print(GetMotorPosition(SN_L1))
