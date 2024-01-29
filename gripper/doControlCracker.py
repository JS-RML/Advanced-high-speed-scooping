from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import FREQUANCY

def doControlCracker():
    count = 0
    print("[Case cracker is selected]")
    cracker = ScoopingObject(MotorDriverSerialNumber.L0, MotorDriverSerialNumber.L1, MotorDriverSerialNumber.R0, MotorDriverSerialNumber.R1)
    cracker.StandbyPosition(-0.051, 0.022, -0.057, 0.269)
    cracker.ScoopingPostion(0.026, 0.005, 0.05, 0.24)
    cracker.GrabPosition(0.032, 0.020, -0.152, 0.289)

    while(count < 1):
        print("Cracker...",count)
        count += 1/FREQUANCY
        sleep(1/FREQUANCY)
