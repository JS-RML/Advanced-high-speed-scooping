import threading
from gripper import mainGripper
from RB5 import mainRB5
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

def threadGripper():
    print("[Gripper thread...]")
    mainGripper.mainGripper()

def threadRB5():
    print("[RB5 thread...]")
    mainRB5.mainRB5()

if __name__ == "__main__":
    thread1 = threading.Thread(target=threadGripper)
    thread2 = threading.Thread(target=threadRB5)

    thread1.start()
    thread2.start()

    # 모든 스레드가 종료될 때까지 기다림
    thread1.join()
    thread2.join()

    print("Program is terminated.")
