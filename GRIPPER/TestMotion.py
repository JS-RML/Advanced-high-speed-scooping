from time import sleep
import numpy as np
import Gripper

def TestMotion():
    print("   [GRIPPER/ TEST MOTION]")

    Gripper.SetControlState()
    print(Gripper.GetMotorPosition())

    # 44, 23, -41, -16 모음
    # -36, 97, 49, -111 벌림


    Gripper.SetIdleState()




