from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import FREQUANCY

def doGripperMotion():
    print("[Case gripper-motion is selected]")
    motion = ScoopingObject(MotorDriverSerialNumber.L0.value, MotorDriverSerialNumber.L1.value, MotorDriverSerialNumber.R0.value, MotorDriverSerialNumber.R1.value)
    motion.ArbitraryPosition1 = 0.042, 0.022, -0.08, 0.278 # 대기
    motion.ArbitraryPosition2 = -0.164, 0.266, 0.121, 0.023 # 쫙 펼친거
    motion.ArbitraryPosition3 = 0.09, 0.014, -0.13, 0.28 # 11자
    motion.ArbitraryPosition4 = 0.046, 0.013, 0.0, 0.286  # R 만 구부리기
    motion.ArbitraryPosition5 = -0.027, 0.0, -0.063, 0.277 # L 만 구부리기


    motion.Move2ArbitraryPosition1
    sleep(0.7)
    motion.Move2ArbitraryPosition2
    sleep(0.7)
    motion.Move2ArbitraryPosition3
    sleep(0.7)
    motion.Move2ArbitraryPosition4
    sleep(0.7)
    motion.Move2ArbitraryPosition5
    sleep(0.7)
    motion.Move2ArbitraryPosition3
    sleep(0.7)

    # motion.TunningGain = 10, 10, 10, 10, 0.1, 0.1, 0.1, 0.1

    user_input = input("아무 키를 입력하시오")
    if user_input:
        motion.SetIdleState()
