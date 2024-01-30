from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import FREQUANCY

def doControlCard():
    count = 0
    print("[Case card is selected]")
    card = ScoopingObject(MotorDriverSerialNumber.L0.value, MotorDriverSerialNumber.L1.value, MotorDriverSerialNumber.R0.value, MotorDriverSerialNumber.R1.value)
    card.StandbyPosition = -0.089, 0.018, -0.044, 0.294
    card.ScoopingPosition = 0.026, 0.016, 0.076, 0.226
    card.GrabPosition = 0.032, 0.020, -0.152, 0.289

    # print(card.CurrentMotorEncoderValue)

    card.Move2StanbyPosition
    sleep(0.5)
    # card.Move2ScoopingPosition
    # sleep(0.5)
    # card.Move2GrabPosition
    # sleep(0.5)
    # card.Move2ScoopingPosition

    while(count < 5):
        # print("Card...",count)
        # user_input = input("아무 키를 입력하시오")
        # if user_input:
        #     break
        count += 1/FREQUANCY
        sleep(1/FREQUANCY)

    card.SetIdleState()
