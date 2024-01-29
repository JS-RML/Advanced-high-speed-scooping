import threading
from gripper import mainGripper

def gripperControl():
    print("[Gripper thread...]")
    mainGripper.mainGripper()

def RB5Contorl():
    print("[RB5 thread...]")

if __name__ == "__main__":
    thread1 = threading.Thread(target = gripperControl())
    thread2 = threading.Thread(target = RB5Contorl())

    thread1.start()
    thread2.start()
