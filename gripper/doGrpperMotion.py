from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber

def doGripperMotion():
    print("[Case gripper-motion is selected]")
    motion = ScoopingObject(MotorDriverSerialNumber.L0.value, MotorDriverSerialNumber.L1.value, MotorDriverSerialNumber.R0.value, MotorDriverSerialNumber.R1.value)

    # degree version
    motion.ArbitraryPosition1 = -10.0, 30.0, 10.0, -30.0 # 대기

    motion.Move2ArbitraryPosition1()
    sleep(1.0)

    print(motion.GetMotorPosition)

    print(motion.GetCurrentGains)

    print("Ghanging gains...")

    motion.TunningGain = 20, 20, 20, 20, 0.2, 0.2, 0.2, 0.2

    sleep(1.0)

    print(motion.GetCurrentGains)


    # motion.Move2ArbitraryPosition2
    # sleep(0.7)
    # motion.Move2ArbitraryPosition3
    # sleep(0.7)
    # motion.Move2ArbitraryPosition4
    # sleep(0.7)
    # motion.Move2ArbitraryPosition5
    # sleep(0.7)
    # motion.Move2ArbitraryPosition3
    # sleep(0.7)


    motion.SetIdleState()
