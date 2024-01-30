from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import FREQUANCY

def doControlDomino():
    count = 0
    print("[Case domino is selected]")
    # TODO 아래의 값들 domino 값으로 변경
    domino = ScoopingObject(MotorDriverSerialNumber.L0, MotorDriverSerialNumber.L1, MotorDriverSerialNumber.R0, MotorDriverSerialNumber.R1)
    domino.StandbyPosition(-0.051, 0.022, -0.057, 0.269)
    domino.ScoopingPostion(0.026, 0.016, 0.076, 0.266)
    domino.GrabPosition(0.032, 0.020, -0.152, 0.289)

    while(count < 1):
        print("Domino...",count)
        count += 1/FREQUANCY
        sleep(1/FREQUANCY)

