import numpy as np
from time import sleep
from GRIPPER import Gripper
from GRIPPER.Gripper import FREQUENCY

def ScoopingDominoBlock():
    print("   [GRIPPER/ CARD]")

    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [17, 22, 43, -45]
    grabPosition = [24, 15, -59, -5]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,20,30,30])
    Gripper.SetVelocityGain([0.2,0.2,0.1,0.1])

    while(timeStep < 5):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.01 or encoderDifference[1] > 0.01:
            Gripper.SetStiffness([20,20,50,50])
            Gripper.SetVelocityGain([0.2, 0.2, 0.3, 0.3])

            Gripper.SetMotorPosition(grabPosition)
        else :
            pass

        print(encoderDifference)
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingDominoBlockTilted():
    print("   [GRIPPER/ CARD]")

    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [17, 22, 43, -45]
    grabPosition = [24, 15, -59, -5]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,20,30,30])
    Gripper.SetVelocityGain([0.2,0.2,0.1,0.1])

    while(timeStep < 5):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.01 or encoderDifference[1] > 0.01:
            Gripper.SetStiffness([20,20,50,50])
            Gripper.SetVelocityGain([0.2, 0.2, 0.3, 0.3])

            Gripper.SetMotorPosition(grabPosition)
        else :
            pass


        # print(encoderDifference)
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()
