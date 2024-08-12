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

Connect your motor drivers(odriveS1) with your PC and type 'odrivetool' in the terminal.
```shell
odrivetool
```

If the program is intalled and the motor drivers(odriveS1) are connected successfully, then you can see the following messages
```shell
ODrive control utility v0.6.7
Please connect your ODrive
You can also type help() or quit().

Connected to ODrive S1 384D34783539 (firmware v0.6.7) as odrv0
Connected to ODrive S1 383F34723539 (firmware v0.6.7) as odrv1
Connected to ODrive S1 3868345A3539 (firmware v0.6.7) as odrv2
Connected to ODrive S1 3866346F3539 (firmware v0.6.7) as odrv3
```

You have to remember these serial numbers(384D34783539, 383F34723539 ...) to create 'Actuator' objects.

## 3. Run High-Speed Scooping
### Before running the code
You should create 'Actuator' objects and match the created objects and the serial numbers of motor drivers. You can type the following codes directly in the 'GRIPPER/Gripper.py' source file.

(1) Define the internal 'SN_variable' using motor driver's serial numbers.
```python
SN_L0 = '384D34783539'
SN_L1 = '383F34723539'
SN_R0 = '3868345A3539'
SN_R1 = '3866346F3539'
```

(2) Create 'odrive' objects using internal 'SN_variable'
```python
odrv0 = odrive.find_any(serial_number=SN_L0)
odrv1 = odrive.find_any(serial_number=SN_L1)
odrv2 = odrive.find_any(serial_number=SN_R0)
odrv3 = odrive.find_any(serial_number=SN_R1)
```

(3) Create 'Actuator' objects and match the 'Actuator' objects with the 'odrive' objects. The second argument of 'Actuator' is the motor offset.(refer to 'Calibrate Zero Position' of [gripper repo](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips/tree/main)). Let the third and fourth arguments be 1, and 45.(no need to change these values)
```python
LF0 = Actuator(odrv0, 0.966, 1, 45) # left finger
LF1 = Actuator(odrv1, 0.955, 1, 45)
RF0 = Actuator(odrv2, 0.977, 1, 45) # right finger
RF1 = Actuator(odrv3, 0.338, 1, 45)
```

Now you can control the motors. Let's select an obejct to scoop. 

(4) Select an object to scoop.
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

You can operate your own robot arm in the 'thread2'. Just copy and paste the codes to operate your own robot system. For our case, we controlled our robot arm by teaching pendant so we didn't use the 'thread2'.

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

## Maintenance
Hyeonje Cha(guswp3611@gmail.com) and Seunghwa Oh(seunghwa9118@pusan.ac.kr)
