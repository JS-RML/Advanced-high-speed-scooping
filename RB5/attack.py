import cobot
from math import pi
import signal
from time import sleep

def cleanup_before_exit(signum, frame):
    print("\nCtrl+Z detected. Exiting...")
    cobot.MoveITPL_Clear()
    cobot.MotionHalt()
    cobot.DisConnectToCB()
    # sys.exit(0)

def conectingToRB5():
    print(cobot.ToCB('10.0.2.7'))
    print(cobot.CobotInit())
    cobot.SetProgramMode(cobot.PG_MODE.REAL)
    print(cobot.IsInitialized())

def disconnectngRB5():
    cobot.MoveITPL_Clear()
    cobot.MotionHalt()
    cobot.DisConnectToCB()

def doControl():
    cobot.MoveJ(j0=0.0, j1=0.0, j2=0.0, j3=0.0, j4=0.0, j5=0.0, spd=-1, acc=-1)
    sleep(1)
    cobot.MoveJ(j0=-90.0, j1=0.0, j2=90.0, j3=0.0, j4=60.0, j5=0.0, spd=-1, acc=-1) # starting point
    sleep(0.1)
    cobot.MoveL(x=-110.80, y=-503.59, z=184.54, rx=90, ry=30.0, rz=-0.01, spd=-1, acc=-1)
    sleep(0.1)
    cobot.MoveL(x=-110.80, y=-503.59, z=408.54, rx=90, ry=30.0, rz=-0.01, spd=-1, acc=-1)

if __name__ == "__main__":

    conectingToRB5()

    doControl()
    
    sleep(5)
    disconnectngRB5()

    # signal.signal(signal.SIGTSTP, cleanup_before_exit)
