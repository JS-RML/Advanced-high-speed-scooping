from time import sleep
from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import FREQUANCY

def doControlCracker():
    count = 0
    print("[Case cracker is selected]")
    cracker = ScoopingObject(MotorDriverSerialNumber.L0.value, MotorDriverSerialNumber.L1.value, MotorDriverSerialNumber.R0.value, MotorDriverSerialNumber.R1.value)
    cracker.StandbyPosition = -0.051, 0.022, -0.057, 0.269
    cracker.ScoopingPosition = 0.026, 0.005, 0.05, 0.224
    cracker.GrabPosition = 0.032, 0.020, -0.152, 0.289

    cracker.Move2StanbyPosition
    print("standby position")
    sleep(0.5)
    cracker.Move2ScoopingPosition
    print("scooping position")
    sleep(0.5)

    tempEncoderVar = np.zeros(4)
    prevtempEncoderVar = np.zeros(4)
    encoderDifference = np.zeros(4)
    firstRun = True

    while(count < 3):
        # user_input = input("아무 키를 입력하시오")
        # if user_input:
        #     cracker.SetIdleState()
        #     break

        tempEncoderVar = cracker.CurrentMotorEncoderValue

        if firstRun:
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else:
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.005 or encoderDifference[1] > 0.005 :
            cracker.Move2GrabPosition
        else :
            pass

        print(encoderDifference)
        count += 1/FREQUANCY
        sleep(1/FREQUANCY)
        prevtempEncoderVar = tempEncoderVar

    cracker.SetIdleState()
