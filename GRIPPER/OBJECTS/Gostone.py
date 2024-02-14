import numpy as np
from time import sleep
from GRIPPER import Gripper
from GRIPPER.Gripper import FREQUENCY
# 44, 23, -41, -16 모음
# -36, 97, 49, -111 벌림
def ScoopingGostone():
    print("   [GRIPPER/ GO-STONE]")
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)
    scoopingPosition = [46, 21, 10, -46]
    grabPosition = [17, 16, -16, -15]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(0.5)

    while(timeStep < 10):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.005 or encoderDifference[1] > 0.005:
            Gripper.SetMotorPosition(grabPosition)
        else :
            pass

        print(encoderDifference)
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()
