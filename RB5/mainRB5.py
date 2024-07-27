from time import sleep
import sys
import os
current_dir_rb = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir_rb)
# from enums import FREQUANCY
import cobot
import signal

###### mode
controlSignal = 'horizontal'
# controlSignal = 'slope'
######

def switchCase(case):
    if case == 'horizontal':
        horizontal()
    elif case == 'slope':
        slope()
    else:
        print("Check the RB5 controlSignal")

def cleanup_before_exit(signum, frame):
    print("\nCtrl+Z detected. Exiting...")
    cobot.MoveITPL_Clear()
    cobot.MotionHalt()
    cobot.DisConnectToCB()
    # sys.exit(0)

def disconnectngRB5():
    cobot.MoveITPL_Clear()
    cobot.MotionHalt()
    cobot.DisConnectToCB()

def mainRB5():
    count = 0
    print("[RB5 main...]")
    cobot.ToCB('10.0.2.7')
    cobot.CobotInit()
    cobot.SetProgramMode(cobot.PG_MODE.REAL)

    # test()

    switchCase(controlSignal)
    sleep(2.5)

    disconnectngRB5()

def horizontal():
    cobot.MoveL(x=32.09, y=-443.82, z=334.38, rx=-166.24, ry=10.05, rz=53.12, spd=-1, acc=-1)
    cobot.MoveL(x=32.10, y=-443.82, z=190, rx=-166.24, ry=10.05, rz=53.11, spd=-1, acc=-1)
    cobot.MoveL(x=32.09, y=-443.82, z=334.38, rx=-166.24, ry=10.05, rz=53.12, spd=-1, acc=-1)

def slope():
    cobot.MoveL(x=123.76, y=-448.94, z=304.20, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    cobot.MoveL(x=123.76, y=-448.94, z=403.26, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    cobot.MoveL(x=123.76, y=-448.94, z=304.20, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    cobot.MoveL(x=123.76, y=-448.94, z=403.26, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)
    cobot.MoveL(x=123.76, y=-448.94, z=304.20, rx=-139.6, ry=22.8, rz=67.3, spd=-1, acc=-1)

def test():

    cobot.MoveJ(j0=0, j1=0, j2=0, j3=0, j4=0.0, j5=0.0, spd=-1, acc=-1)
    sleep(2.5)
    cobot.MoveJ(j0=-68, j1=-4.97, j2=0, j3=0, j4=0.0, j5=0.0, spd=-1, acc=-1)
    cobot.MoveL(x=32.09, y=-443.82, z=334.38, rx=-166.24, ry=10.05, rz=53.12, spd=-1, acc=-1)
    sleep(2.5)
    cobot.MoveL(x=32.10, y=-443.82, z=190, rx=-166.24, ry=10.05, rz=53.11, spd=-1, acc=-1)
    sleep(2.5)
    cobot.MoveL(x=32.09, y=-443.82, z=334.38, rx=-166.24, ry=10.05, rz=53.12, spd=-1, acc=-1)
    sleep(2.5)
    cobot.MoveITPL_Clear()
    cobot.MotionHalt()
    cobot.DisConnectToCB()




