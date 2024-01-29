from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import FREQUANCY

def doControlCard():
    count = 0
    print("[Case card is selected]")
    card = ScoopingObject(MotorDriverSerialNumber.L0, MotorDriverSerialNumber.L1, MotorDriverSerialNumber.R0, MotorDriverSerialNumber.R1)
    card.StandbyPosition(-0.051, 0.022, -0.057, 0.269)
    card.ScoopingPostion(0.026, 0.016, 0.076, 0.266)
    card.GrabPosition(0.032, 0.020, -0.152, 0.289)

    while(count < 1):
        print("Card...",count)
        count += 1/FREQUANCY
        sleep(1/FREQUANCY)

