import numpy as np
from time import sleep
from GRIPPER import Gripper
from GRIPPER.Gripper import FREQUENCY
from datetime import datetime

def ScoopingCard():
    print("   [GRIPPER/ CARD]")

    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    initialConfiguration = [27, 28, 44, -47]
    goalConfiguration = [45, 10, -35, -17]
    beforeCollisionStiffness = [20, 20, 20, 20]
    afterCollisionStiffness = [50, 50, 100, 100]
    beforeCollisionVelGain = [0.15, 0.15, 0.15, 0.15]
    afterCollisionVelGain = [0.15, 0.15, 0.15, 0.15]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(initialConfiguration)
    sleep(1.0)
    Gripper.SetStiffness(beforeCollisionStiffness)
    Gripper.SetVelocityGain(beforeCollisionVelGain)

    while(timeStep < 4):
        Gripper.sharedTimeList.append(timeStep)
        Gripper.sharedPositionList.append(Gripper.GetMotorPosition()[0])

        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.01 or encoderDifference[1] > 0.01:
            Gripper.SetStiffness(afterCollisionStiffness)
            Gripper.SetVelocityGain(afterCollisionVelGain)
            Gripper.SetMotorPosition(goalConfiguration)
        else :
            pass

        print(encoderDifference)
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()
