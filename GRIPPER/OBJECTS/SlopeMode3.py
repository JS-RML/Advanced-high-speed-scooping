import numpy as np
from time import sleep
from GRIPPER import Gripper
from GRIPPER.Gripper import FREQUENCY

def SlopeGoStone():
    print("   [GRIPPER/ SLOPE-GO-STONE]")

    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [39, 16, 26, -39]
    grabPosition = [45, 10, -35, -17]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,10,30,30])
    Gripper.SetVelocityGain([0.1,0.1,0.1,0.1])

    while(timeStep < 3):
        Gripper.sharedTimeList.append(timeStep)
        Gripper.sharedPositionList.append(Gripper.GetMotorPosition()[0])

        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.005 or encoderDifference[1] > 0.005:
            Gripper.SetStiffness([30,30,30,30])
            Gripper.SetVelocityGain([0.3, 0.3, 0.3, 0.3])

            Gripper.SetMotorPosition(grabPosition)
        else :
            pass

        print(encoderDifference)
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()
