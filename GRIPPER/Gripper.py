import sys
import os
current_dir_gripper = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir_gripper)
import numpy as np
import odrive
from Actuator import *

FREQUENCY = 50 #Hz

SN_L0 = '384D34783539'
SN_L1 = '383F34723539'
SN_R0 = '3868345A3539'
SN_R1 = '3866346F3539'

odrv0 = odrive.find_any(serial_number=SN_L0)
odrv1 = odrive.find_any(serial_number=SN_L1)
odrv2 = odrive.find_any(serial_number=SN_R0)
odrv3 = odrive.find_any(serial_number=SN_R1)

LF0 = Actuator(odrv0, 0.966, 1, 45) # left finger
LF1 = Actuator(odrv1, 0.955, 1, 45)
RF0 = Actuator(odrv2, 0.977, 1, 45) # right finger
RF1 = Actuator(odrv3, 0.338, 1, 45)

sharedTimeList = []
sharedPositionList = []

def ClearErrors():
    LF0.clearErrors()
    LF1.clearErrors()
    RF0.clearErrors()
    RF1.clearErrors()

def GetMotorPosition():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.motor_pos
    tempArray[1] = LF1.motor_pos
    tempArray[2] = RF0.motor_pos
    tempArray[3] = RF1.motor_pos
    return tempArray

def GetStiffness():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.stiffness
    tempArray[1] = LF1.stiffness
    tempArray[2] = RF0.stiffness
    tempArray[3] = RF1.stiffness
    return tempArray

def GetVelocityGains():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.vel_gain
    tempArray[1] = LF1.vel_gain
    tempArray[2] = RF0.vel_gain
    tempArray[3] = RF1.vel_gain
    return tempArray

def GetEncoderValue():
    tempArray = np.zeros(4)
    tempArray[0] = LF0.encoder
    tempArray[1] = LF1.encoder
    tempArray[2] = RF0.encoder
    tempArray[3] = RF1.encoder
    return tempArray

def SetMotorPosition(motorAngles):
    LF0.motor_pos = motorAngles[0]
    LF1.motor_pos = motorAngles[1]
    RF0.motor_pos = motorAngles[2]
    RF1.motor_pos = motorAngles[3]

# stiffness = position gain
def SetStiffness(stiffness):
    LF0.stiffness = stiffness[0]
    LF1.stiffness = stiffness[1]
    RF0.stiffness = stiffness[2]
    RF1.stiffness = stiffness[3]

def SetVelocityGain(velGains):
    LF0.vel_gain = velGains[0]
    LF1.vel_gain = velGains[1]
    RF0.vel_gain = velGains[2]
    RF1.vel_gain = velGains[3]

def SetControlState():
    ClearErrors()
    LF0.armed = True
    LF1.armed = True
    RF0.armed = True
    RF1.armed = True
    SetStiffness([30, 30, 30, 30])
    SetVelocityGain([0.3, 0.3, 0.3, 0.3])
    print("      [GRIPPER/ CONTROL STATE]")

def SetIdleState():
    ClearErrors()
    LF0.armed = False
    LF1.armed = False
    RF0.armed = False
    RF1.armed = False
    print("      [GRIPPER/ IDLE STATE]")


