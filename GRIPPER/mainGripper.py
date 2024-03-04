import sys
import os
current_dir_gripper = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir_gripper)
import OBJECTS.Card
import OBJECTS.Chip
import OBJECTS.Cracker
import OBJECTS.DominoBlock
import OBJECTS.Gostone
import OBJECTS.Seaweed
import OBJECTS.Envelope
import OBJECTS.SlopeMode1
import OBJECTS.SlopeMode2
import OBJECTS.SlopeMode3
import OBJECTS.SlopeMode4
import OBJECTS.SlopeMode5
import OBJECTS.SlopeMode6
import OBJECTS.SlopeMode7
import OBJECTS.SlopeMode45degree
import OBJECTS.tilted
import TestMotion

######## select control signal ########
controlSignal = 'card'
# controlSignal = 'domino'
# controlSignal = 'goStone'
# controlSignal = 'cracker'
# controlSignal = 'chip'
# controlSignal = 'envelope'
# controlSignal = 'seaweed'
# controlSignal = 'slopeCard'
# controlSignal = 'slopeDomino'
# controlSignal = 'slopGoStone'
# controlSignal = 'slopeCracker'
# controlSignal = 'slopeChip'
# controlSignal = 'slopeSeaweed'
# controlSignal = 'slopeEnvelope'
# controlSignal = 'slope45degree'
# controlSignal = 'testMotion'
# controlSignal = 'tilted' #domino test 중
# controlSignal = 'control_mode'
# controlSignal = 'idle' # 완전 대기 상태
#######################################

def switchCase(case):
    if case == 'card':
        OBJECTS.Card.ScoopingCard()

    elif case == 'domino':
        OBJECTS.DominoBlock.ScoopingDominoBlock()

    elif case == 'goStone':
        OBJECTS.Gostone.ScoopingGostone()

    elif case == 'cracker':
        OBJECTS.Cracker.ScoopingCracker()

    elif case == 'chip':
        OBJECTS.Chip.ScoopingChip()

    elif case == 'seaweed':
        OBJECTS.Seaweed.ScoopingSeaweed()

    elif case == 'envelope':
        OBJECTS.Envelope.ScoopingEnvelope()

    elif case == 'testMotion':
        TestMotion.TestMotion()

    elif case == 'slopeCard':
        OBJECTS.SlopeMode1.SlopeCard() #todo 파일명에 card 들어가면 경로를 card.py  잡음...

    elif case == 'slopeDomino':
        OBJECTS.SlopeMode2.SlopeDomino()

    elif case == 'slopGoStone':
        OBJECTS.SlopeMode3.SlopeGoStone()

    elif case == 'slopeCracker':
        OBJECTS.SlopeMode4.SlopeCracker()

    elif case == 'slopeChip':
        OBJECTS.SlopeMode5.SlopeChip()

    elif case == 'slopeSeaweed':
        OBJECTS.SlopeMode6.SlopeSeaweed()

    elif case == 'slopeEnvelope':
        OBJECTS.SlopeMode7.SlopeEnvelope()

    elif case == 'slope45degree':
        OBJECTS.SlopeMode45degree.ScoopingCard()

    elif case == 'tilted':
        OBJECTS.tilted.tiltScooping()

    else:
        print("Check the controlSignal")

# Gripper main is started
def mainGripper():
    switchCase(controlSignal)
