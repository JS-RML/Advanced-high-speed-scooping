from . import mainGripper
from .ScoopingObject import *

def doControlCard():
    count = 0
    print("[Case card is selected]")
    card = ScoopingObject(mainGripper.SN_L0, mainGripper.SN_L1, mainGripper.SN_R0, mainGripper.SN_R1)
    card.StandbyPosition(-0.051, 0.022, -0.057, 0.269)
    card.ScoopingPostion(0.026, 0.016, 0.076, 0.266)
    card.GrabPosition(0.032, 0.020, -0.152, 0.289)

    while(count <200) :

        count += 1
