# PNU-Advanced-High-Speed-Scooping

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
- [**PNU Direct-Drive Gripper**](https://github.com/chahyeonje/PNU-Direct-Drive-Gripper)

## 2. Prerequisites
### 2.1 Hardware
- [**Rainbow robotics RB5-850**](https://www.rainbow-robotics.com/rb?gad_source=1&gclid=CjwKCAiAq4KuBhA6EiwArMAw1H8wNPbhSO7W_gAv-8gQMxyxffJRlo_nOqRpkLgsJm7VGlkmAHT8xRoChH0QAvD_BwE): Industrial Robot Arm 
- [**Direct-Drive Gripper (DDG)**](https://github.com/chahyeonje/PNU-Direct-Drive-Gripper)

### 2.2 Software
Our software is implemented with **python3** and tested on **Ubuntu 20.04**.
  
## 3. Run High-Speed Scooping
### 3.1 Run with real robot
1. You can run **main.py**.
```shell
python3 main.py
```
2. If you want to operate the RB5 and the gripper seperately
```shell
python3 RB5/mainRB5.py
```
or
```shell
python3 gripper/mainGripper.py
```

### 3.2 Changing execution parameters

**Gripper Dimensions**
(They are all a one-dimensional array with 4 elements L0, L1, R0 and R1 in order.)
- ***standbyPosition*** : Waiting position of the finger and thumb(degree).
- ***scoopingPosition*** : Prescoop position of the finger and thumb(degree).
- ***grapPosition*** : Grab position of the finger and thumb(degree).
- ***prescoopStiffness*** : Position p-gain of finger and thumb before scoop.
- ***scoopingStiffness*** : Position p-gain of finger and thumb for scooping.
- ***graspingStiffness*** : Position p-gain of finger and thumb for grasping).

## Maintenance
Hyeonje Cha(guswp3611@gmail.com) and Seunghwa Oh(seunghwa9118@pusan.ac.kr)
