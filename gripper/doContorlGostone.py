from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import FREQUANCY

def doControlGoStone():
    count = 0
    print("[Case go-stone is selected]")
    # TODO 아래의 값들 go-stone 값으로 변경
    goStone = ScoopingObject(MotorDriverSerialNumber.L0, MotorDriverSerialNumber.L1, MotorDriverSerialNumber.R0, MotorDriverSerialNumber.R1)
    goStone.StandbyPosition(-0.051, 0.022, -0.057, 0.269)
    goStone.ScoopingPostion(0.026, 0.016, 0.076, 0.266)
    goStone.GrabPosition(0.032, 0.020, -0.152, 0.289)

    while(count < 1):
        print("Go-stone...",count)
        count += 1/FREQUANCY
        sleep(1/FREQUANCY)

