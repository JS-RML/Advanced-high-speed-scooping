import numpy as np
from time import sleep
from GRIPPER import Gripper

def ScoopingCard():
    print("   [GRIPPER/ CARD]")

    Gripper.SetControlState()
    Gripper.SetMotorPosition([-36, 97, 49, -111])
    sleep(0.5)
    Gripper.SetMotorPosition([44, 23, -41, -16])
    sleep(0.5)
    Gripper.SetMotorPosition([-36, 97, 49, -111])
    sleep(0.5)
    Gripper.SetMotorPosition([44, 23, -41, -16])
    sleep(0.5)
    Gripper.SetMotorPosition([-36, 97, 49, -111])
    sleep(0.5)
    Gripper.SetMotorPosition([44, 23, -41, -16])
    sleep(0.5)

    # 44, 23, -41, -16 모음
    # -36, 97, 49, -111 벌림

    Gripper.SetIdleState()
