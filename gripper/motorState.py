from ScoopingObject import *
from enums import MotorDriverSerialNumber
from enums import MotorState

def motorState(val):
    print(val)
    state = ScoopingObject(MotorDriverSerialNumber.L0.value, MotorDriverSerialNumber.L1.value, MotorDriverSerialNumber.R0.value, MotorDriverSerialNumber.R1.value)
    if val == MotorState.CONTROL:
        print("CONTROL state")
        state.SetControlState()

    elif val == MotorState.IDLE:
        print("IDLE state")
        state.SetIdleState()

    else:
        print("Select the control state")
