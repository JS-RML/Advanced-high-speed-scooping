# High-Speed Scooping 2024

## 1. Overview
The repository implemented a manipulation technique for picking up flat objects on hard surfaces known as high-speed scooping. Based on the ideas from HKUST's HSS, this method was performed in a variety of environments, not just on flat surfaces but also on inclined planes and the sideway-tilted planes. The experiments conducted demonstrate that this technique can be widely utilized in various settings, not just under limited and specific conditions.
### *High-Speed Scooping*
<p align = "center">
<img src="media/card_.gif" width="400"> 
<img src="media/envelope_.gif" width="400"> 
</p>


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

### *High-Speed Scooping(slope-tilted + passive joint finger tip)*
<p align = "center">
<img src="media/tilted_card.gif" width="400">
<img src="media/tilted_domino.gif" width="400">
</p>

**Related materials**
- [**HKRML High-Speed-Scooping**](https://github.com/HKUST-RML/high_speed_scooping)
- [**HKRML Direct-Drive Hand**](https://github.com/HKUST-RML/ddh_hardware)
- [**Direct-Drive Gripper with Swivel Fingertips**](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips)

## 2. Prerequisites
### 2.1 Hardware
- [**Rainbow robotics RB5-850**](https://www.rainbow-robotics.com/rb?gad_source=1&gclid=CjwKCAiAq4KuBhA6EiwArMAw1H8wNPbhSO7W_gAv-8gQMxyxffJRlo_nOqRpkLgsJm7VGlkmAHT8xRoChH0QAvD_BwE): Industrial Robot Arm 
- [**Direct-Drive Gripper (DDG)**](https://github.com/chahyeonje/PNU-Direct-Drive-Gripper)

### 2.2 Software
Our software is implemented with **python3** and tested on **Ubuntu 20.04**.

Cloning our *Advanced-high-speed-scooping* software.
```shell
git clone https://github.com/JS-RML/Advanced-high-speed-scooping.git
```
## 3. Run High-Speed Scooping
### 3.0 Before running the code
You sholud match the 'Actuator object' and the serial number of motor driver in the 'GRIPPER/Gripper.py' source file.

```python
# exmaple code
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

### 3.1 Run with real robot
1. You can run **main.py**.
```shell
python3 main.py
```
2. Then two threads are run automatically.
```python
thread1 = threading.Thread(target=threadGripper) # for gripper
thread2 = threading.Thread(target=threadRB5) # for robot arm
```
3. In the 'GRIPPER/mainGripper.py', you can select control siganl choosing obejcts which will be scooped.
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

### 3.2 Changing execution parameters
In the 'GRIPPER/OBJECTS/Card.py', there are some parameters you can adjust to scoop the card.
(They are all a one-dimensional array with 4 elements L0, L1, R0 and R1 in order.)
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
