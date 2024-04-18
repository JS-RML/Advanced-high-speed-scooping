from time import sleep
import numpy as np
import Gripper
from GRIPPER.Gripper import FREQUENCY

def TestMotion():
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

