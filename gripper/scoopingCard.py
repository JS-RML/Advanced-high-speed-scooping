import odrive
from odrive.enums import *
from actuator import *
from time import sleep
import numpy as np

# 참고사항
# encoder 0.1 변화는 모터로 치면 36 degree  변화
# encoder 0.01 변화는 모터로 치면 3.6 degee 변화

SN_L0 = '384D34783539'   #OD0 offset : 0.906  -> 240123 position setpoint 0
SN_L1 = '383F34723539'   #OD1 offset : 0.955  -> 240123 position setpoint 0
SN_R0 = '3868345A3539'   #OD2 offset : 0.977  -> 240123 position setpoint 0.076
SN_R1 = '3866346F3539'   #OD3 offset : 0.837  -> 240123 position setpoint 0.21

# odrive 와 작동시킬 모터 mapping
odrv0 = odrive.find_any(serial_number=SN_L0)
odrv1 = odrive.find_any(serial_number=SN_L1)
odrv2 = odrive.find_any(serial_number=SN_R0)
odrv3 = odrive.find_any(serial_number=SN_R1)

# actuator class 이용하여 각 손가락에 대한 객체 생성(odrive 와 손가락 mapping)
# 사실 이 안쪽이 가장 중요함. direction(1) 은 모터가 도는 방향에 알맞게 다시 설정해야함. 당장은 안써도 돼서 1 로 뒀음.
leftFinger0 = Actuator(odrv0, 0.966, 1, 45)
leftFinger1 = Actuator(odrv1, 0.955, 1, 45)
rightFinger0 = Actuator(odrv2, 0.977, 1, 45)
rightFinger1 = Actuator(odrv3, 0.837, 1, 45)

# 각 손가락에 대한 motor 의 position 을 저장하기 위한 array 변수 초기화
leftFingerPosition = np.zeros(2)
rightFingerPosition = np.zeros(2)
prevLeftFingerPosition = np.zeros(2)
prevRightFingerPosition = np.zeros(2)

# 각 손가락에 대한 motor 의 position 변화량을 저장하기 위한 array 변수 초기화
positionDifferenceLeft = np.zeros(2)
positionDifferenceRight = np.zeros(2)

# 카드 테스트 해봄
# 손가락 모양을 초기 상태로 바꿈
def SetStartingPoint(motorDriverSerialNumber0, motorDriverSerialNumber1, motorDriverSerialNumber2, motorDriverSerialNumber3):
    serialNumber0 = motorDriverSerialNumber0
    serialNumber1 = motorDriverSerialNumber1
    serialNumber2 = motorDriverSerialNumber2
    serialNumber3 = motorDriverSerialNumber3

    odrv0 = odrive.find_any(serial_number = serialNumber0)
    odrv1 = odrive.find_any(serial_number = serialNumber1)
    odrv2 = odrive.find_any(serial_number = serialNumber2)
    odrv3 = odrive.find_any(serial_number = serialNumber3)

    odrv0.axis0.controller.input_pos = -0.051
    odrv1.axis0.controller.input_pos = 0.022
    odrv2.axis0.controller.input_pos = -0.057
    odrv3.axis0.controller.input_pos = 0.269

# 손가락 모양을 설정해준 attack point 로 바꿈
def AttackPoint1(motorDriverSerialNumber0, motorDriverSerialNumber1, motorDriverSerialNumber2, motorDriverSerialNumber3):
    serialNumber0 = motorDriverSerialNumber0
    serialNumber1 = motorDriverSerialNumber1
    serialNumber2 = motorDriverSerialNumber2
    serialNumber3 = motorDriverSerialNumber3

    odrv0 = odrive.find_any(serial_number = serialNumber0)
    odrv1 = odrive.find_any(serial_number = serialNumber1)
    odrv2 = odrive.find_any(serial_number = serialNumber2)
    odrv3 = odrive.find_any(serial_number = serialNumber3)

    odrv0.axis0.controller.input_pos = 0.026
    odrv1.axis0.controller.input_pos = 0.016
    odrv2.axis0.controller.input_pos = 0.076
    odrv3.axis0.controller.input_pos = 0.226

# 손가락을 오므리는 모양으로 바꿈
def Grap(motorDriverSerialNumber0, motorDriverSerialNumber1, motorDriverSerialNumber2, motorDriverSerialNumber3):
    serialNumber0 = motorDriverSerialNumber0
    serialNumber1 = motorDriverSerialNumber1
    serialNumber2 = motorDriverSerialNumber2
    serialNumber3 = motorDriverSerialNumber3

    odrv0 = odrive.find_any(serial_number = serialNumber0)
    odrv1 = odrive.find_any(serial_number = serialNumber1)
    odrv2 = odrive.find_any(serial_number = serialNumber2)
    odrv3 = odrive.find_any(serial_number = serialNumber3)

    odrv0.axis0.controller.input_pos = 0.032
    odrv1.axis0.controller.input_pos = 0.020
    odrv2.axis0.controller.input_pos = -0.152
    odrv3.axis0.controller.input_pos = 0.289

if __name__ == "__main__":
    count = 0
    firstRun = True

    SetStartingPoint(SN_L0, SN_L1, SN_R0, SN_R1)
    sleep(0.5)
    AttackPoint1(SN_L0, SN_L1, SN_R0, SN_R1)
    sleep(0.5)

    # 아래 while 문 안에서 gripper 제어코드가 돌아감. 10초 동안 제어기가 작동하고 종료되게 설정했음
    # 추후에 grap 을 하면 종료 또는 다른 종료신호를 줘야 while 문을 탈출하게 만들 수 있음.

    while(count < 100): # count 1 이 0.1 초임

        leftFingerPosition[0] = leftFinger0.encoder
        leftFingerPosition[1] = leftFinger1.encoder
        rightFingerPosition[0] = rightFinger0.encoder
        rightFingerPosition[1] = rightFinger1.encoder

        if(firstRun):
            prevLeftFingerPosition[0] = leftFingerPosition[0]
            prevLeftFingerPosition[1] = leftFingerPosition[1]
            prevRightFingerPosition[0] = rightFingerPosition[0]
            prevRightFingerPosition[1] = rightFingerPosition[1]
            firstRun = False

        positionDifferenceLeft[0] = abs(leftFingerPosition[0] - prevLeftFingerPosition[0])
        positionDifferenceLeft[1] = abs(leftFingerPosition[1] - prevLeftFingerPosition[1])
        positionDifferenceRight[0] = abs(rightFingerPosition[0] - prevRightFingerPosition[0])
        positionDifferenceRight[1] = abs(rightFingerPosition[1] - prevRightFingerPosition[1])

        if(positionDifferenceRight[0] > 0.0035 or
            positionDifferenceRight[1] > 0.0035 or
            positionDifferenceLeft[0] > 0.0035 or
            positionDifferenceLeft[1] > 0.0035):
            #sitffness (p gain) 을 조정할 수 있음.
            leftFinger0.stiffness = 50
            leftFinger1.stiffness = 50
            rightFinger0.stiffness = 50
            rightFinger1.stiffness = 50
            # print(str(rightFinger0.stiffness))
            #vel_gain (v gain) 을 조정할 수 있음.
            # rightFinger0.vel_gain = 0.3
            # print(str(rightFinger0.vel_gain))
            Grap(SN_L0, SN_L1, SN_R0, SN_R1)

        print(str(positionDifferenceRight))

        prevRightFingerPosition[0] = rightFingerPosition[0]
        prevRightFingerPosition[1] = rightFingerPosition[1]

        count = count + 1
        sleep(0.1)


