import numpy as np
from time import sleep
from GRIPPER import Gripper
from GRIPPER.Gripper import FREQUENCY
from datetime import datetime

import keyboard

def ScoopingCard(): # for test
    print("   [GRIPPER/ CARD]")

    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    # scoopingPosition = [41, 16, 24, -37]
    scoopingPosition = [27, 28, 44, -47]
    grabPosition = [45, 10, -35, -17]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([30,30,30,30])
    Gripper.SetVelocityGain([0.15,0.15,0.15,0.15])

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
            Gripper.SetStiffness([30,30,40,40])
            Gripper.SetVelocityGain([0.3, 0.3, 0.3, 0.3])

            Gripper.SetMotorPosition(grabPosition)
        else :
            pass

        print(encoderDifference)
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingCardSlopeCurrent():
    print("   [GRIPPER/ CARD-SLOPE]")

    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    # scoopingPosition = [27, 20, 5, -26]
    # scoopingPosition = [38, 17, 10, -30]
    scoopingPosition = [24, 26, 25, -32]
    grabPosition = [45, 10, -35, -17]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([30,30,30,30])
    Gripper.SetVelocityGain([0.3,0.1,0.1,0.1])

    while(timeStep < 6):
        if Gripper.GetCurrent()[0] > 0.2 :
            Gripper.SetStiffness([30,30,5,5])
            Gripper.SetVelocityGain([0.3, 0.3, 0.3, 0.3])
            Gripper.SetMotorPosition(grabPosition)
        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)

    Gripper.SetIdleState()

def ScoopingCard_photo():#position: (130,70)
    print("   [GRIPPER/ CARD]")
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    # scoopingPosition = [23, 26, 49, -51]
    # grabPosition = [50, 15, -55, -10] # new grab
    scoopingPosition = [23, 26, 40, -40] # new ready
    grabPosition = [61, 7, -62, -3] # all new grab, if you use this point you have to set the velocity integral gain as 0.


    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,20,30,30])
    Gripper.SetVelocityGain([0.1,0.1,0.2,0.2])

    while(timeStep < 5.5):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.02 or encoderDifference[1] > 0.02:
            Gripper.SetStiffness([20,20,40,40])
            Gripper.SetVelocityGain([0.1, 0.1, 0.2, 0.2])
            Gripper.SetMotorPosition(grabPosition)

        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingCard0():#position: (130,70)
    print("   [GRIPPER/ CARD]")
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    # scoopingPosition = [23, 26, 49, -51]
    # grabPosition = [50, 15, -55, -10] # new grab
    scoopingPosition = [23, 26, 40, -40] # new ready
    grabPosition = [61, 7, -62, -3] # all new grab, if you use this point you have to set the velocity integral gain as 0.


    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,20,30,30])
    Gripper.SetVelocityGain([0.1,0.1,0.2,0.2])

    while(timeStep < 5.5):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.02 or encoderDifference[1] > 0.02:
            Gripper.SetStiffness([40,40,40,40])
            Gripper.SetVelocityGain([0.1, 0.1, 0.2, 0.2])
            Gripper.SetMotorPosition(grabPosition)

        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingCard1():  #AOA test. smaller aoa (position: 105,70)
    print("   [GRIPPER/ CARD]")
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [50, 9, 49, -52] # for lower aoa
    grabPosition = [61, 7, -62, -3]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,20,40,40])
    Gripper.SetVelocityGain([0.1,0.1,0.1,0.1])

    while(timeStep < 5):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.005 or encoderDifference[1] > 0.005:
            Gripper.SetStiffness([20,20,40,40])
            Gripper.SetVelocityGain([0.1,0.1,0.1,0.1])
            Gripper.SetMotorPosition(grabPosition)

        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingCard2():  #AOA test. bigger aoa (position: 150,70)
    print("   [GRIPPER/ CARD]")
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [-3, 39, -14, -15]
    grabPosition = [61, 7, -62, -3]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,20,50,50])
    Gripper.SetVelocityGain([0.1,0.1,0.1,0.1])

    while(timeStep < 4):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.02 or encoderDifference[1] > 0.02:
            Gripper.SetStiffness([20,20,100,100])
            Gripper.SetVelocityGain([0.1,0.1,0.1,0.1])
            Gripper.SetMotorPosition(grabPosition)

        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()


def ScoopingCard_noF0(): # for one-digit exp (130,70)
    print("   [GRIPPER/ CARD]")
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [-56, 96, 40, -40]
    grabPosition = [-56, 96, -62, -3]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([50,50,100,100])
    Gripper.SetVelocityGain([0.1,0.1,0.1,0.1])

    while(timeStep < 4):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[2] > 0.002 or encoderDifference[3] > 0.002:
            Gripper.SetStiffness([50,50,100,100])
            Gripper.SetVelocityGain([0.1, 0.1, 0.1, 0.1])
            Gripper.SetMotorPosition(grabPosition)
            break

        # if Gripper.GetCurrent()[0] > 0.1 or Gripper.GetCurrent()[1] > 0.1:
        #     Gripper.SetStiffness([20,20,55,55])
        #     Gripper.SetVelocityGain([0.15, 0.15, 0.05, 0.05])

        #     Gripper.SetMotorPosition(grabPosition)

        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingCard_noF1(): # for one-digit aoa exp.
    print("   [GRIPPER/ CARD]")
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [-56, 96, 49, -52]
    grabPosition = [-56, 96, -62, -3]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([30,30,30,30])
    Gripper.SetVelocityGain([0.1,0.1,0.1,0.1])

    while(timeStep < 4):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[2] > 0.005 or encoderDifference[3] > 0.005:
            Gripper.SetStiffness([50,50,25,25])
            Gripper.SetVelocityGain([0.1, 0.1, 0.1, 0.1])
            Gripper.SetMotorPosition(grabPosition)

        # if Gripper.GetCurrent()[0] > 0.1 or Gripper.GetCurrent()[1] > 0.1:
        #     Gripper.SetStiffness([20,20,55,55])
        #     Gripper.SetVelocityGain([0.15, 0.15, 0.05, 0.05])

        #     Gripper.SetMotorPosition(grabPosition)

        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingCard_noF2(): # for one-digit aoa exp big
    print("   [GRIPPER/ CARD]")
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [-56, 96, -14, -15]
    grabPosition = [-56, 96, -62, -3]

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([50,50,30,30])
    Gripper.SetVelocityGain([0.1,0.1,0.1,0.1])

    while(timeStep < 4):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[2] > 0.002 or encoderDifference[3] > 0.002:
            Gripper.SetStiffness([50,50,25,25])
            Gripper.SetVelocityGain([0.1, 0.1, 0.1, 0.1])
            Gripper.SetMotorPosition(grabPosition)

        # if Gripper.GetCurrent()[0] > 0.1 or Gripper.GetCurrent()[1] > 0.1:
        #     Gripper.SetStiffness([20,20,55,55])
        #     Gripper.SetVelocityGain([0.15, 0.15, 0.05, 0.05])

        #     Gripper.SetMotorPosition(grabPosition)

        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingCardRollOnly(): # for fixed fingertip, position(90,90)
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [16, 25, 33, -38]
    grabPosition = [50, 15, -55, -10] # new grab

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,20,30,30])
    Gripper.SetVelocityGain([0.1,0.1,0.3,0.3])

    while(timeStep < 50):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.01 or encoderDifference[1] > 0.01:
            Gripper.SetStiffness([50,50,60,60])
            Gripper.SetVelocityGain([0.1, 0.1, 0.2, 0.2])

            Gripper.SetMotorPosition(grabPosition)
        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()

def ScoopingCardRollOnlySwivel(): # for swivel fingertip (70,120)
    timeStep = 0.0
    firstRun = True
    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)

    scoopingPosition = [11, 21, 35, -40]
    grabPosition = [50, 15, -55, -10] # new grab

    Gripper.SetControlState()
    Gripper.SetMotorPosition(scoopingPosition)
    sleep(1.0)
    Gripper.SetStiffness([20,20,30,30])
    Gripper.SetVelocityGain([0.1,0.1,0.3,0.3])

    while(timeStep < 5):
        tempEncoderVar = Gripper.GetEncoderValue()

        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.01 or encoderDifference[1] > 0.01:
            Gripper.SetStiffness([50,50,100,100])
            Gripper.SetVelocityGain([0.1, 0.1, 0.1, 0.1])
            Gripper.SetMotorPosition(grabPosition)
        else :
            pass

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar

    Gripper.SetIdleState()
