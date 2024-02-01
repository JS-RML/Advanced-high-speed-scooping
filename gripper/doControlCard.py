from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import FREQUANCY

def doControlCard():
    count = 0
    print("[Case card is selected]")
    card = ScoopingObject(MotorDriverSerialNumber.L0.value, MotorDriverSerialNumber.L1.value, MotorDriverSerialNumber.R0.value, MotorDriverSerialNumber.R1.value)
    card.StandbyPosition = -0.089, 0.018, -0.044, 0.294
    card.ScoopingPosition = 0.046, -0.04, 0.12, 0.176
    card.GrabPosition = 0.046, -0.04, -0.136, 0.309

    card.Move2StanbyPosition
    print("standby position")
    sleep(0.5)
    card.Move2ScoopingPosition
    print("scooping position")
    sleep(0.5)

    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)
    firstRun = True

    while(count < 3):
        # user_input = input("아무 키를 입력하시오")
        # if user_input:
        #     card.SetIdleState()
        #     break

        tempEncoderVar = card.CurrentMotorEncoderValue

        if firstRun:
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.005 or encoderDifference[1] > 0.005 :
            card.Move2GrabPosition
        else :
            pass

        print(encoderDifference)
        count += 1/FREQUANCY
        sleep(1/FREQUANCY)
        prevtempEncoderVar = tempEncoderVar

    card.SetIdleState()
