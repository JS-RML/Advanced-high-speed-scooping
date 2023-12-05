import cobot
from math import pi
import signal

cobot.ToCB('10.0.2.7')
cobot.CobotInit()
cobot.SetProgramMode(cobot.PG_MODE.REAL)

cobot.MoveJ(j0=0, j1=0, j2=0, j3=0, j4=0, j5=0, spd=50.0, acc=50.0)




def cleanup_before_exit(signum, frame):
    print("\nCtrl+Z detected. Exiting...")
    cobot.MoveITPL_Clear()
    cobot.MotionHalt()
    cobot.DisConnectToCB()
    # sys.exit(0)


if __name__ == "__main__":
        signal.signal(signal.SIGTSTP, cleanup_before_exit)
