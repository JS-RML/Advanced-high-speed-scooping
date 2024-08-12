# Advanced High-Speed Scooping (2024)

## 1. Overview
<!-- The repository implemented a manipulation technique for picking up flat objects on hard surfaces known as high-speed scooping. Based on the ideas from HKUST's HSS, this method was performed in a variety of environments, not just on flat surfaces but also on inclined planes and the sideway-tilted planes. The experiments conducted demonstrate that this technique can be widely utilized in various settings, not just under limited and specific conditions.-->
This repository contains the latest software implementation of **High-Speed Scooping** using our latest [direct-drive gripper](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips). It can be applied to rapidly and adaptively picking thin objects off from a hard surface, which would be quite challenging with a straightforward approach aiming at directly obtaining a pinch grasp.
### *High-Speed Scooping*
<p align = "center">
<img src="media/card_.gif" width="400"> 
<img src="media/envelope_.gif" width="400"> 
</p>

<!--
### *High-Speed Scooping(slope)*
<p align = "center">
<img src="media/slope_card_.gif" width="400">
<img src="media/slope_envelope_.gif" width="400">
</p>

### *High-Speed Scooping(slope-diffrent angles)*
<p align = "center">
<img src="media/slope_card_15degree_.gif" width="400">
<img src="media/slope_card45.gif" width="400">
</p>

### *High-Speed Scooping(slope-sideway)*
<p align = "center">
<img src="media/sideway_card.gif" width="400">
<img src="media/sideway_domino.gif" width="400">
</p>
-->

### *Adaptive High-Speed Scooping*
The passive swivel fingertips help pick the object even when the workplane of the gripper is not normal to the ground surface.
<p align = "center">
<img src="media/tilted_card.gif" width="400">
<img src="media/tilted_domino.gif" width="400">
</p>

**Related repos**
- [**Direct-Drive Gripper (2024)**](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips)
- [**High-Speed Scooping (2022)**](https://github.com/JS-RML/high_speed_scooping)
- [**Direct-Drive Gripper (2022)**](https://github.com/JS-RML/ddh_hardware)

## 2. Prerequisites
### Hardware
- [**Rainbow robotics RB5-850**](https://www.rainbow-robotics.com/rb?gad_source=1&gclid=CjwKCAiAq4KuBhA6EiwArMAw1H8wNPbhSO7W_gAv-8gQMxyxffJRlo_nOqRpkLgsJm7VGlkmAHT8xRoChH0QAvD_BwE): Industrial Robot Arm 
- [**Direct-Drive Gripper**](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips/tree/main)

### Software
Our software is implemented with **python3** and tested on **Ubuntu 20.04**.

Clone our *Advanced-high-speed-scooping* software.
```shell
git clone https://github.com/JS-RML/Advanced-high-speed-scooping.git
```

Install `odrivetool`. If you've already installed this pakage when you calibrate odrive, you can skip this step.
```shell
pip install --upgrade odrivetool
```
## 3. Run High-Speed Scooping
### Before running the code
You should match the 'Actuator object' and the serial number of motor driver in the 'GRIPPER/Gripper.py' source file. $\color{red}{\textsf{This sounds more like a high-level goal to achieve. Explain more explicitly the list of low-level action items that your user needs to perform.}}$

```python
# example code
# Define the internal 'SN_variable' using motor driver's serial number.
SN_L0 = '384D34783539'
SN_L1 = '383F34723539'
SN_R0 = '3868345A3539'
SN_R1 = '3866346F3539'

# Create 'odrive' objects using internal 'SN_variable'
odrv0 = odrive.find_any(serial_number=SN_L0)
odrv1 = odrive.find_any(serial_number=SN_L1)
odrv2 = odrive.find_any(serial_number=SN_R0)
odrv3 = odrive.find_any(serial_number=SN_R1)

# Create 'Actuator' objects and match these with the 'odrive' objects.
LF0 = Actuator(odrv0, 0.966, 1, 45) # left finger
LF1 = Actuator(odrv1, 0.955, 1, 45)
RF0 = Actuator(odrv2, 0.977, 1, 45) # right finger
RF1 = Actuator(odrv3, 0.338, 1, 45)
```

### Run with real robot
Run **main.py**.
```shell
python3 main.py
```
Then two threads run simultaneously.
```python
thread1 = threading.Thread(target=threadGripper) # for gripper
thread2 = threading.Thread(target=threadRB5) # for robot arm
```
$\color{red}{\textsf{Not clear when to select an option below.}}$
In the 'GRIPPER/mainGripper.py', you can select control signal choosing obejcts which will be scooped.

```python
controlSignal = 'card'
# controlSignal = 'domino'
# controlSignal = 'goStone'
# controlSignal = 'cracker'
# controlSignal = 'chip'
# controlSignal = 'envelope'
# controlSignal = 'seaweed'
# controlSignal = 'testMotion'
```

### Changing execution parameters
In the 'GRIPPER/OBJECTS/Card.py', there are some parameters you can adjust to scoop the card. The same code exist in the each object source file(domino.py, goStone.py, cracker.py ...)
(They are all a one-dimensional array with four elements L0, L1, R0 and R1 in order.)
- ***scoopingPosition*** : Ready position of the finger and thumb(degree).
- ***grabPosition*** : Grab position of the finger and thumb(degree).
- ***setStiffness*** : Each motor's position gain.
- ***setVelocityGain*** : Each motor's velocity gain.
```python
# Example code
scoopingPosition = [27, 28, 44, -47]
grabPosition = [45, 10, -35, -17]
Gripper.SetStiffness([30,30,30,30])
Gripper.SetVelocityGain([0.15,0.15,0.15,0.15])
```

Repeat the collision destection condition in the while loop until a change in the motor's position due to a collision is detected.
```python
while(timeStep < 4):
        tempEncoderVar = Gripper.GetEncoderValue()
        if(firstRun):
            prevtempEncoderVar = tempEncoderVar
            firstRun = False
        else :
            pass

        encoderDifference = abs(tempEncoderVar - prevtempEncoderVar)

        if encoderDifference[0] > 0.01 or encoderDifference[1] > 0.01:
            Gripper.SetStiffness([30,30,40,40])
            Gripper.SetVelocityGain([0.3, 0.3, 0.3, 0.3])
            Gripper.SetMotorPosition(grabPosition)
        else :
            pass
        timeStep += 1/FREQUENCY
        sleep(1/FREQUENCY)
        prevtempEncoderVar = tempEncoderVar
```

## Maintenance
Hyeonje Cha(guswp3611@gmail.com) and Seunghwa Oh(seunghwa9118@pusan.ac.kr)
