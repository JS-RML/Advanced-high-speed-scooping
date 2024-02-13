import odrive
import numpy as np
from Actuator import *

class ScoopingObject(object):

    def __init__(self,
                 serialNumberL0,
                 serialNumberL1,
                 serialNumberR0,
                 serialNumberR1):

        self.odrv0 = odrive.find_any(serial_number=serialNumberL0)
        print(serialNumberL0)
        self.odrv1 = odrive.find_any(serial_number=serialNumberL1)
        print(serialNumberL1)
        self.odrv2 = odrive.find_any(serial_number=serialNumberR0)
        print(serialNumberR0)
        self.odrv3 = odrive.find_any(serial_number=serialNumberR1)
        print(serialNumberR1)

        self.leftFinger0 = Actuator(self.odrv0, 0.966, 1, 45)
        self.leftFinger1 = Actuator(self.odrv1, 0.955, 1, 45)
        self.rightFinger0 = Actuator(self.odrv2, 0.977, 1, 45)
        self.rightFinger1 = Actuator(self.odrv3, 0.338, 1, 45)

        self.standbyPosition = np.zeros(4)
        self.scoopingPosition = np.zeros(4)
        self.grabPosition = np.zeros(4)

        self.arbitraryPosition1 = np.zeros(4)
        self.arbitraryPosition2 = np.zeros(4)
        self.arbitraryPosition3 = np.zeros(4)
        self.arbitraryPosition4 = np.zeros(4)
        self.arbitraryPosition5 = np.zeros(4)
        self.arbitraryPosition6 = np.zeros(4)

        print("Object is created")


    @property
    def StandbyPosition(self):
        return self.standbyPosition

    @property
    def ScoopingPosition(self):
        return self.scoopingPosition

    @property
    def GrabPosition(self):
        return self.grabPosition

    @property
    def ArbitraryPosition1(self):
        return self.arbitraryPosition1
    @property
    def ArbitraryPosition2(self):
        return self.arbitraryPosition2
    @property
    def ArbitraryPosition3(self):
        return self.arbitraryPosition3
    @property
    def ArbitraryPosition4(self):
        return self.arbitraryPosition4
    @property
    def ArbitraryPosition5(self):
        return self.arbitraryPosition5
    @property
    def ArbitraryPosition6(self):
        return self.arbitraryPosition6

    @StandbyPosition.setter
    def StandbyPosition(self, setDegree):
        for i in range(0,4):
            self.standbyPosition[i] = setDegree[i]

    @ScoopingPosition.setter
    def ScoopingPosition(self, setDegree):
        for i in range(0,4):
            self.scoopingPosition[i] = setDegree[i]

    @GrabPosition.setter
    def GrabPosition(self, setDegree):
        for i in range(0,4):
            self.grabPosition[i] = setDegree[i]

    @ArbitraryPosition1.setter
    def ArbitraryPosition1(self, setDegree):
        for i in range(0,4):
            self.ArbitraryPosition1[i] = setDegree[i]
    @ArbitraryPosition2.setter
    def ArbitraryPosition2(self, setDegree):
        for i in range(0,4):
            self.ArbitraryPosition2[i] = setDegree[i]
    @ArbitraryPosition3.setter
    def ArbitraryPosition3(self, setDegree):
        for i in range(0,4):
            self.ArbitraryPosition3[i] = setDegree[i]
    @ArbitraryPosition4.setter
    def ArbitraryPosition4(self, setDegree):
        for i in range(0,4):
            self.ArbitraryPosition4[i] = setDegree[i]
    @ArbitraryPosition5.setter
    def ArbitraryPosition5(self, setDegree):
        for i in range(0,4):
            self.ArbitraryPosition5[i] = setDegree[i]
    @ArbitraryPosition6.setter
    def ArbitraryPosition6(self, setDegree):
        for i in range(0,4):
            self.ArbitraryPosition6[i] = setDegree[i]

    def Move2StandbyPosition(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()

        self.leftFinger0.motor_pos = self.standbyPosition[0]
        self.leftFinger1.motor_pos = self.standbyPosition[1]
        self.rightFinger0.motor_pos = self.standbyPosition[2]
        self.rightFinger1.motor_pos = self.standbyPosition[3]

    def Move2ScoopingPosition(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()

        self.leftFinger0.motor_pos = self.scoopingPosition[0]
        self.leftFinger1.motor_pos = self.scoopingPosition[1]
        self.rightFinger0.motor_pos = self.scoopingPosition[2]
        self.rightFinger1.motor_pos = self.scoopingPosition[3]

    def Move2GrabPosition(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()
        # TODO 이 부분 actuator class 와 연결시키기
        self.leftFinger0.motor_pos = self.grabPosition[0]
        self.leftFinger1.motor_pos = self.grabPosition[1]
        self.rightFinger0.motor_pos = self.grabPosition[2]
        self.rightFinger1.motor_pos = self.grabPosition[3]

    def Move2ArbitraryPosition1(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()

        self.leftFinger0.motor_pos = self.arbitraryPosition1[0]
        self.leftFinger1.motor_pos = self.arbitraryPosition1[1]
        self.rightFinger0.motor_pos = self.arbitraryPosition1[2]
        self.rightFinger1.motor_pos = self.arbitraryPosition1[3]

    def Move2ArbitraryPosition2(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()

        self.leftFinger0.motor_pos = self.arbitraryPosition2[0]
        self.leftFinger1.motor_pos = self.arbitraryPosition2[1]
        self.rightFinger0.motor_pos = self.arbitraryPosition2[2]
        self.rightFinger1.motor_pos = self.arbitraryPosition2[3]

    def Move2ArbitraryPosition3(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()

        self.leftFinger0.motor_pos = self.arbitraryPosition3[0]
        self.leftFinger1.motor_pos = self.arbitraryPosition3[1]
        self.rightFinger0.motor_pos = self.arbitraryPosition3[2]
        self.rightFinger1.motor_pos = self.arbitraryPosition3[3]

    def Move2ArbitraryPosition4(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()

        self.leftFinger0.motor_pos = self.arbitraryPosition4[0]
        self.leftFinger1.motor_pos = self.arbitraryPosition4[1]
        self.rightFinger0.motor_pos = self.arbitraryPosition4[2]
        self.rightFinger1.motor_pos = self.arbitraryPosition4[3]

    def Move2ArbitraryPosition5(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()

        self.leftFinger0.motor_pos = self.arbitraryPosition5[0]
        self.leftFinger1.motor_pos = self.arbitraryPosition5[1]
        self.rightFinger0.motor_pos = self.arbitraryPosition5[2]
        self.rightFinger1.motor_pos = self.arbitraryPosition5[3]

    def Move2ArbitraryPosition6(self):
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.SetControlState()

        self.leftFinger0.motor_pos = self.arbitraryPosition6[0]
        self.leftFinger1.motor_pos = self.arbitraryPosition6[1]
        self.rightFinger0.motor_pos = self.arbitraryPosition6[2]
        self.rightFinger1.motor_pos = self.arbitraryPosition6[3]

    @property
    def CurrentMotorEncoderValue(self):
        tempArray = np.zeros(4)
        tempArray[0] = self.leftFinger0.encoder
        tempArray[1] = self.leftFinger1.encoder
        tempArray[2] = self.rightFinger0.encoder
        tempArray[3] = self.rightFinger1.encoder
        return tempArray

    def SetControlState(self):
        self.ClearErrors()
        self.leftFinger0.armed = True
        self.leftFinger1.armed = True
        self.rightFinger0.armed = True
        self.rightFinger1.armed = True

    def SetIdleState(self):
        self.ClearErrors()
        self.leftFinger0.armed = False
        self.leftFinger1.armed = False
        self.rightFinger0.armed = False
        self.rightFinger1.armed = False

    def ClearErrors(self):
        self.leftFinger0.clearErrors()
        self.leftFinger1.clearErrors()
        self.rightFinger0.clearErrors()
        self.rightFinger1.clearErrors()

    @property
    def TunningGain(self):
        return 0

    @TunningGain.setter
    #todo 동작 안함 확인해야함
    def TunningGain(self,
                    left0Stiffness,
                    left1Stiffness,
                    right0Stiffness,
                    right1Stiffness,
                    left0VelGain,
                    left1VelGain,
                    right0VelGain,
                    right1VelGain):

        self.leftFinger0.stiffness = left0Stiffness
        self.leftFinger1.stiffness = left1Stiffness
        self.rightFinger0.stiffness = right0Stiffness
        self.rightFinger1.stiffness = right1Stiffness

        self.leftFinger0.vel_gain = left0VelGain
        self.leftFinger1.vel_gain = left1VelGain
        self.rightFinger0.vel_gain = right0VelGain
        self.rightFinger1.vel_gain = right1VelGain
