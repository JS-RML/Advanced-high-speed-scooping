import odrive
import numpy as np
from Actuator import *

class ScoopingObject(object):

    def __init__(self,
                 serialNumberL0,
                 serialNumberL1,
                 serialNumberR0,
                 serialNumberR1):

        self.serialNumberL0 = serialNumberL0
        self.serialNumberL1 = serialNumberL1
        self.serialNumberR0 = serialNumberR0
        self.serialNumberR1 = serialNumberR1

        self.odrv0 = odrive.find_any(serial_number=serialNumberL0)
        self.odrv1 = odrive.find_any(serial_number=serialNumberL1)
        self.odrv2 = odrive.find_any(serial_number=serialNumberR0)
        self.odrv3 = odrive.find_any(serial_number=serialNumberR1)

        self.leftFinger0 = Actuator(self.odrv0, 0.966, 1, 45)
        self.leftFinger1 = Actuator(self.odrv1, 0.955, 1, 45)
        self.rightFinger0 = Actuator(self.odrv2, 0.977, 1, 45)
        self.rightFinger1 = Actuator(self.odrv3, 0.837, 1, 45)

        self.standbyPosition = np.zeros(4)
        self.scoopingPosition = np.zeros(4)
        self.grabPosition = np.zeros(4)


    @property
    def StandbyPosition(self):
        return self.standbyPosition

    @property
    def ScoopingPostion(self):
        return self.scoopingPosition

    @property
    def GrabPosition(self):
        return self.grabPosition

    @StandbyPosition.setter
    def StandbyPosition(self, setPoint):
        for i in range(0,4):
            self.standbyPosition[i] = setPoint[i]

    @ScoopingPostion.setter
    def ScoopingPostion(self, setPoint):
        for i in range(0,4):
            self.scoopingPosition[i] = setPoint[i]

    @GrabPosition.setter
    def GrabPosition(self, setPoint):
        for i in range(0,4):
            self.grabPosition[i] = setPoint[i]

    @property
    def Move2StanbyPosition(self):
        # TODO 검증 필요함
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.leftFinger0.armed(1)
            self.leftFinger1.armed(1)
            self.rightFinger0.armed(1)
            self.rightFinger1.armed(1)

        # TODO 이 부분 actuator class 와 연결시키기
        self.odrv0.axis0.controller.input_pos = self.standbyPosition[0]
        self.odrv1.axis0.controller.input_pos = self.standbyPosition[1]
        self.odrv2.axis0.controller.input_pos = self.standbyPosition[2]
        self.odrv3.axis0.controller.input_pos = self.standbyPosition[3]
        return self.standbyPosition

    @property
    def Move2ScoopingPosition(self):
        # TODO 검증 필요함
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.leftFinger0.armed(1)
            self.leftFinger1.armed(1)
            self.rightFinger0.armed(1)
            self.rightFinger1.armed(1)
        # TODO 이 부분 actuator class 와 연결시키기
        self.odrv0.axis0.controller.input_pos = self.scoopingPosition[0]
        self.odrv1.axis0.controller.input_pos = self.scoopingPosition[1]
        self.odrv2.axis0.controller.input_pos = self.scoopingPosition[2]
        self.odrv3.axis0.controller.input_pos = self.scoopingPosition[3]
        return self.scoopingPosition

    @property
    def Move2GrabPosition(self):
        # TODO 검증 필요함
        if self.leftFinger0.armed == 0 or self.leftFinger0.armed == 0 or self.rightFinger0.armed == 0 or self.rightFinger1.armed == 0:
            self.leftFinger0.armed(1)
            self.leftFinger1.armed(1)
            self.rightFinger0.armed(1)
            self.rightFinger1.armed(1)
        # TODO 이 부분 actuator class 와 연결시키기
        self.odrv0.axis0.controller.input_pos = self.grabPosition[0]
        self.odrv1.axis0.controller.input_pos = self.grabPosition[1]
        self.odrv2.axis0.controller.input_pos = self.grabPosition[2]
        self.odrv3.axis0.controller.input_pos = self.grabPosition[3]
        return self.grabPosition

    @property
    def CurrentMotorEncoderValue(self):
        tempArray = np.zeros(4)
        tempArray[0] = self.leftFinger0.encoder
        tempArray[1] = self.leftFinger1.encoder
        tempArray[2] = self.rightFinger0.encoder
        tempArray[3] = self.rightFinger1.encoder
        return tempArray
