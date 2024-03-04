import numpy as np
from time import sleep
from GRIPPER import Gripper
from GRIPPER.Gripper import FREQUENCY

def ScoopingCard():
    print("   [GRIPPER/ CARD]")

    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [43, 14, 43, -47]
    grabPosition = [45, 10, -45, -5]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    # Gripper.SetStiffness([30,10,30,30])
    # Gripper.SetVelocityGain([0.3,0.1,0.3,0.3])

    Gripper.SetStiffness([5,5,10,10])
    Gripper.SetVelocityGain([0.05,0.05,0.1,0.1])

    while(timeStep < 2):
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
            Gripper.SetStiffness([5,5,10,10])
            Gripper.SetVelocityGain([0.05, 0.05, 0.1, 0.1])

            Gripper.SetMotorPosition(grabPosition)
        else :
            pass

        print(encoderDifference)
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()
