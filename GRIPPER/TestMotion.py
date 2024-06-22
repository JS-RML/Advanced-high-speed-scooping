from time import sleep
import numpy as np
import Gripper
from GRIPPER.Gripper import FREQUENCY

def TestGetEncoder():
    print("   [GRIPPER/ TEST MOTION]")



    Gripper.SetControlState()
    print(Gripper.GetMotorPosition())

    # 44, 23, -41, -16 모음
    # -36, 97, 49, -111 벌림

    Gripper.SetIdleState()

def TestCurrent():
    print("   [GRIPPER/ TEST CURRENT]")
    timeStep = 0.0
    readyPosition = [17, 27, -15, -24]
    Gripper.SetControlState()
    Gripper.SetMotorPosition(readyPosition)
    sleep(1.0)

    Gripper.SetStiffness([30,30,30,30])
    Gripper.SetVelocityGain([0.3,0.3,0.3,0.3])

    while(timeStep < 30):

        # print(Gripper.GetCurrent())
        # Gripper.sharedData = 3

        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)

    Gripper.SetIdleState()

def TestMotion():
    print("   [GRIPPER/ TEST MOTION]")

    position1 = [14, 25, -16, -20]
    position2 = [-36, 100, 37, -100]
    position3 = [-35, 44, 39, -45]
    position4 = [35, 24, 5, -14]
    position5 = [-9, 23, -40, -15]

    Gripper.SetControlState()

    Gripper.SetStiffness([50,50,50,50])
    Gripper.SetVelocityGain([0.2,0.2,0.2,0.2])

    sleep(0.5)

    Gripper.SetMotorPosition(position1)
    sleep(0.5)

    Gripper.SetMotorPosition(position2)
    sleep(0.5)

    Gripper.SetMotorPosition(position1)
    sleep(0.5)

    Gripper.SetMotorPosition(position3)
    sleep(0.5)

    Gripper.SetMotorPosition(position1)
    sleep(0.5)

    Gripper.SetMotorPosition(position4)
    sleep(0.5)

    Gripper.SetMotorPosition(position5)
    sleep(0.5)

    Gripper.SetMotorPosition(position1)
    sleep(10.0)

    Gripper.SetIdleState()

def TestMotionStop():
    print("   [GRIPPER/ TEST MOTION]")

    position1 = [14, 25, -16, -20]
    position2 = [-36, 100, 37, -100]
    position3 = [-35, 44, 39, -45]
    position4 = [35, 24, 5, -14]
    position5 = [-9, 23, -40, -15]

    Gripper.SetControlState()

    Gripper.SetStiffness([50,50,50,50])
    Gripper.SetVelocityGain([0.15,0.15,0.15,0.15])

    Gripper.SetMotorPosition(position1)

    # 44, 23, -41, -16 모음
    # -36, 97, 49, -111 벌림

    # Gripper.SetIdleState()
