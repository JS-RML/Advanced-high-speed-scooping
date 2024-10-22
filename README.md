# Advanced High-Speed Scooping (2024)

## 1. Overview
<!-- The repository implemented a manipulation technique for picking up flat objects on hard surfaces known as high-speed scooping. Based on the ideas from HKUST's HSS, this method was performed in a variety of environments, not just on flat surfaces but also on inclined planes and the sideway-tilted planes. The experiments conducted demonstrate that this technique can be widely utilized in various settings, not just under limited and specific conditions.-->
This repository contains the latest software implementation of **High-Speed Scooping** using our latest [direct-drive gripper](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips). It can be applied to rapidly and adaptively picking thin objects off from a hard surface, as illustrated below.
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
Our swivel fingertips help scoop objects even when the gripper's workplane is not exactly normal to the ground surface.

<p align = "center">
<img src="media/swivel_card.gif" width="800">
</p>

Fragile objects, such as seaweed and cracker, can also be picked up.

<p align = "center">
<img src="media/swivel_seaweed_gif.gif" width="400">
<img src="media/swivel_cracker_gif.gif" width="400">
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

Git clone our software.
```shell
git clone https://github.com/JS-RML/Advanced-high-speed-scooping.git
```

Install `odrivetool`. If you've already installed this pakage when you calibrate odrive, you can skip this step.
```shell
pip install --upgrade odrivetool
```

Connect your motor drivers (odriveS1) with your PC and run `odrivetool` in the terminal.
```shell
odrivetool
```

If successful, you will see the following output.
```shell
ODrive control utility v0.6.7
Please connect your ODrive
You can also type help() or quit().

Connected to ODrive S1 384D34783539 (firmware v0.6.7) as odrv0
Connected to ODrive S1 383F34723539 (firmware v0.6.7) as odrv1
Connected to ODrive S1 3868345A3539 (firmware v0.6.7) as odrv2
Connected to ODrive S1 3866346F3539 (firmware v0.6.7) as odrv3
```

Record these serial numbers (384D34783539, 383F34723539 ...) to create `Actuator` objects later.

## 3. Run High-Speed Scooping
### Before running the code
<!-- You should create 'Actuator' objects and match the created objects and the serial numbers of motor drivers. You can type the following codes directly in the 'GRIPPER/Gripper.py' source file.-->
Modify `GRIPPER/Gripper.py` as follows.

(1) Define the variables `SN_L0`, `SN_L1`, `SN_R0`, and `SN_R1` using the serial numbers aforementioned.
```python
SN_L0 = '384D34783539'
SN_L1 = '383F34723539'
SN_R0 = '3868345A3539'
SN_R1 = '3866346F3539'
```

(2) Create `odrive` objects using those `SN_L0`, `SN_L1`, `SN_R0`, and `SN_R1`.
```python
odrv0 = odrive.find_any(serial_number=SN_L0)
odrv1 = odrive.find_any(serial_number=SN_L1)
odrv2 = odrive.find_any(serial_number=SN_R0)
odrv3 = odrive.find_any(serial_number=SN_R1)
```

(3) Create `Actuator` objects using the `odrive` objects above. The second argument of each `Actuator` object is the motor offset value (refer to 'Calibrate Zero Position' of [the direct-drive gripper repo](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips/tree/main)). Just let the third and fourth arguments be `1` and `45` (you won't need to change these values).
```python
LF0 = Actuator(odrv0, 0.966, 1, 45) # left finger
LF1 = Actuator(odrv1, 0.955, 1, 45)
RF0 = Actuator(odrv2, 0.977, 1, 45) # right finger
RF1 = Actuator(odrv3, 0.338, 1, 45)
```

<!-- Now you can control the motors. Let's select an obejct to scoop in the 'GRIPPER/mainGripper.py' source file. Also you can type directly in the source file.-->

(4) Set control parameters in `GRIPPER/mainGripper.py`. You can load preset values by selecting one of the options below and commenting out the others.
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

### Let the robot high-speed scoop
Run **main.py**.
```shell
python3 main.py
```

### How to customize control parameters

There are a set of control parameters that you can customize for different objects to scoop.
- ***initialConfiguration*** : Initial configuration (motor angles in degrees).
- ***goalConfiguration*** : Goal configuration (motor angles in degrees).
- ***beforeCollisionStiffness*** : Motor P-gains before collision.
- ***afterCollisionStiffness*** : Motor P-gains after collision.
- ***beforeCollisionVelGain*** : Motor D-gains before collision.
- ***afterCollisionVelGain*** : Motor D-gains after collision.

Each parameter is a four-tuple that specifies the values for the motors L0, L1, R0, and R1, respectively.
<p align = "center">
<img src="images/gripper_labeling.png" width="400">
</p>

Take `GRIPPER/OBJECTS/Card.py` for instance. In the code, the parameters are preset as follows, to scoop a plastic card. 

```python
# Example code
initialConfiguration = [27, 28, 44, -47]
goalConfiguration = [45, 10, -35, -17]
beforeCollisionStiffness = [20, 20, 20, 20]
afterCollisionStiffness = [20, 20, 100, 100]
beforeCollisionVelGain = [0.15,0.15,0.15,0.15]
afterCollisionVelGain = [0.15,0.15,0.15,0.15]
```


## Maintenance
Hyeonje Cha (guswp3611@gmail.com) and Seunghwa Oh (seunghwa9118@pusan.ac.kr)
