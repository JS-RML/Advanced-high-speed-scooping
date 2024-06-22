import threading
import GRIPPER.Gripper
from GRIPPER import Gripper
from GRIPPER import mainGripper
from RB5 import mainRB5

def threadGripper():
    print("[GRIPPER THREAD]")
    mainGripper.mainGripper()

def threadRB5():
    print("[RB5 THREAD]")
    # mainRB5.mainRB5()

if __name__ == "__main__":
    thread1 = threading.Thread(target=threadGripper)
    thread2 = threading.Thread(target=threadRB5)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Program is terminated.")
