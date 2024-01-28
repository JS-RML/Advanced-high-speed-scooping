import odrive
import numpy as np
from odrive.enums import *
from Actuator import *
from time import sleep
import doControlCard
import doControlCracker

######## select control signal ########
controlSignal = 'card'
# controlSignal = 'domino'
# controlSignal = 'goStone'
# controlSignal = 'cracker'
# controlSignal = 'chip'
# controlSignal = 'control_mode'
# controlSignal = 'idle' # 완전 대기 상태
#######################################

SN_L0 = '384D34783539'
SN_L1 = '383F34723539'
SN_R0 = '3868345A3539'
SN_R1 = '3866346F3539'

def switchCase(case):
    if case == 'card':
        doControlCard.doControlCard()

    elif case == 'domino':
        print("[Case domino is selected]")

    elif case == 'goStone':
        print("[Case go-stone is selected]")

    elif case == 'cracker':
        doControlCracker.doControlCracker()

    elif case == 'chip':
        print("[Case chip is selected]")

    elif case == 'control_mode':
        print("[Now you can control the gripper]")

    elif case == 'idle' :
        print("[Idle state, Next time you should turn on the control mode]")

    else:
        print("Default case")


if __name__ == "__main__":

    switchCase(controlSignal)


