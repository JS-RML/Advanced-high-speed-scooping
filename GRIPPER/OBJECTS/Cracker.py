import numpy as np
from time import sleep
from GRIPPER import Gripper

def ScoopingCrackerSwivel():
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    initialConfiguration = [11, 21, 35, -40]
    goalConfiguration = [50, 15, -55, -10]
    beforeCollisionStiffness = [20, 20, 20, 20]
    afterCollisionStiffness = [20, 20, 20, 20]
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
