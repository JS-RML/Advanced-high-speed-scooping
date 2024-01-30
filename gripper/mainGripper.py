import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir)
import doControlCard
import doControlCracker
import doContorlDomino
import doContorlGostone
import motorState
from enums import MotorState

######## select control signal ########
controlSignal = 'card'
# controlSignal = 'domino'
# controlSignal = 'goStone'
# controlSignal = 'cracker'
# controlSignal = 'chip'
# controlSignal = 'control_mode'
# controlSignal = 'idle' # 완전 대기 상태
#######################################


def switchCase(case):
    if case == 'card':
        doControlCard.doControlCard()

    elif case == 'domino':
        doContorlDomino.doControlDomino()

    elif case == 'goStone':
        doContorlGostone.doControlGoStone()

    elif case == 'cracker':
        doControlCracker.doControlCracker()

    elif case == 'chip':
        print("[Case chip is selected]")

    elif case == 'control_mode':
        motorState.motorState(MotorState.CONTROL)
        print("Now you can control the gripper...")

    elif case == 'idle' :
        motorState.motorState(MotorState.IDLE)
        print("For the operation, ensure the state is set to CONTROL mode...")

    else:
        print("Check the controlSignal")

# Gripper main is started
def mainGripper():
    print("[Gripper main...]")
    switchCase(controlSignal)
