import mainGripper
from ScoopingObject import *

def doControlCracker():
    print("[Case cracker is selected]")
    cracker = ScoopingObject(mainGripper.SN_L0, mainGripper.SN_L1, mainGripper.SN_R0, mainGripper.SN_R1)
    cracker.StandbyPosition(-0.051, 0.022, -0.057, 0.269)
    cracker.ScoopingPostion(0.026, 0.005, 0.05, 0.24)
    cracker.GrabPosition(0.032, 0.020, -0.152, 0.289)
