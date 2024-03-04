import threading

import GRIPPER.Gripper
from GRIPPER import mainGripper
from RB5 import mainRB5
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
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

    # 모든 스레드가 종료될 때까지 기다림
    thread1.join()
    thread2.join()

    # 데이터프레임 생성
    df = pd.DataFrame({'Time': GRIPPER.Gripper.sharedTimeList, 'Value': GRIPPER.Gripper.sharedPositionList})

    plt.figure(figsize=(10, 6))  # 그래프 크기 설정
    plt.plot(df['Time'], df['Value'], marker='o', linestyle='-', color='b')  # 라인 차트 생성

    # 그래프 제목 및 축 라벨 설정
    plt.title('test')
    plt.xlabel('Time')
    plt.ylabel('Value')

    # plt.show()

    with open('time_data_seconds.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time (seconds)', 'Data'])  # 헤더 작성
        for time, value in zip(GRIPPER.Gripper.sharedTimeList, GRIPPER.Gripper.sharedPositionList):
            writer.writerow([time, value])  # 시간(초)과 데이터 값 쓰기

    print("Program is terminated.")
