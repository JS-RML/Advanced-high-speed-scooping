from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import MotorState

def motorState(val):
    state = ScoopingObject(MotorDriverSerialNumber.L0, MotorDriverSerialNumber.L1, MotorDriverSerialNumber.R0, MotorDriverSerialNumber.R1)
    if val == MotorState.CONTROL:
        print("CONTROL state")
        state.SetControlState()

    elif val == MotorState.IDLE:
        print("IDLE state")
        state.SetIdleState()

    else:
        print("Select the control state")
