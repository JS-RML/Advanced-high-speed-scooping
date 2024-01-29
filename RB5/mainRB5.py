from time import sleep
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__)) # 예를들어 부모 디렉토리를 만든다면 parent_dir = os.path.join(current_dir, '..') 이렇게도 가능
sys.path.append(current_dir)
from enums import FREQUANCY

def mainRB5():
    count = 0
    print("[RB5 main...]")
    while(count <= 1):
        count += 1/FREQUANCY
        print("RB5...", count)
        sleep(1/FREQUANCY)

