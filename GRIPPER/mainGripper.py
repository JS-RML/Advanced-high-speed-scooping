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
import TestMotion


######## select control signal ########
controlSignal = 'card'
# controlSignal = 'domino'
# controlSignal = 'goStone'
# controlSignal = 'cracker'
# controlSignal = 'chip'
# controlSignal = 'envelope'
# controlSignal = 'seaweed'
# controlSignal = 'testMotion'
######################################

def switchCase(case):
    if case == 'card':
        OBJECTS.Card.ScoopingCard0()
        
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
        TestMotion.TestGetEncoder()
        # TestMotion.TestMotion()
        # TestMotion.TestMotionStop()

    else:
        print("Check the controlSignal")

# Gripper main is started
def mainGripper():
    switchCase(controlSignal)
