import numpy as np
from time import sleep
from GRIPPER import Gripper
from GRIPPER.Gripper import FREQUENCY

def tiltScooping():
    print("   [GRIPPER/ SLOPE-CARD]")

    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    tempPosition = [0,0,0,0]
    scoopingPosition = [56, 0.0, 36, -54]
    grabPosition = [45, 15, -25, -10]
    # grabPosition = [46, 22, -17, -13]



    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([30,10,30,30]) # 30
    Gripper.SetVelocityGain([0.3,0.1,0.1,0.1]) # 30
    # Gripper.SetStiffness([30,30,30,30]) # 15
    # Gripper.SetVelocityGain([0.3,0.3,0.1,0.1]) # 15

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
            # sleep(0.5)
            # tempPosition = Gripper.GetMotorPosition()
            # tempPosition[3] += 5
            # Gripper.SetMotorPosition(tempPosition)
        else :
            pass

        print(encoderDifference)
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()
