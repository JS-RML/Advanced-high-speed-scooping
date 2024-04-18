import threading

import GRIPPER.Gripper
from GRIPPER import Gripper
from GRIPPER import mainGripper
from RB5 import mainRB5

import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta


# class MyMplCanvas(FigureCanvas):
#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MyMplCanvas, self).__init__(fig)
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.canvas = MyMplCanvas(self, width=5, height=4, dpi=100)
#         self.setCentralWidget(self.canvas)
#
#         self.max_points = 300
#         self.x_data = []
#         self.y_data = []
#         self.y_limit = 0.5  # 초기 y축 범위 설정
#
#         self.animation = FuncAnimation(self.canvas.figure, self.update_plot, interval=20)
#         self.canvas.mpl_connect('scroll_event', self.on_scroll)  # 마우스 휠 이벤트 연결
#
#     def update_plot(self, frame):
#
#         y_value = Gripper.GetCurrent()[0]
#         print(y_value)
#         self.x_data.append(datetime.now())
#         self.y_data.append(y_value)  # y값 범위 변경
#
#         if len(self.x_data) > self.max_points:
#             self.x_data = self.x_data[-self.max_points:]
#             self.y_data = self.y_data[-self.max_points:]
#
#         self.canvas.axes.clear()
#         if self.x_data:
#             self.canvas.axes.plot(self.x_data, self.y_data)
#             self.canvas.axes.figure.autofmt_xdate()
#             self.canvas.axes.set_ylim(-self.y_limit, self.y_limit)  # y축 범위 설정
#         self.canvas.draw()
#
#     def on_scroll(self, event):
#         # 마우스 휠 이벤트에 따라 y축 범위 조절
#         if event.button == 'up':
#             self.y_limit = max(0.1, self.y_limit - 0.1)  # 확대
#         else:  # 'down'
#             self.y_limit += 0.1  # 축소
#         self.canvas.axes.set_ylim(-self.y_limit, self.y_limit)
#         self.canvas.draw_idle()

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(10, 8), dpi=100)
        self.axes1 = self.fig.add_subplot(221, title="L0")
        self.axes2 = self.fig.add_subplot(222, title="L1")
        self.axes3 = self.fig.add_subplot(223, title="R0")
        self.axes4 = self.fig.add_subplot(224, title="R1")
        self.fig.suptitle("Motor Current", fontsize=16)
        super(MyMplCanvas, self).__init__(self.fig)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.canvas = MyMplCanvas(self)
        self.setCentralWidget(self.canvas)

        self.start_time = datetime.now()
        self.max_points = 50
        self.x_data = [[] for _ in range(4)]
        self.y_data = [[] for _ in range(4)]
        self.y_limit = [0.5] * 4  # 초기 y축 범위 설정

        self.animation = FuncAnimation(self.canvas.fig, self.update_plot, interval=50)
        self.canvas.mpl_connect('scroll_event', self.on_scroll)

    def update_plot(self, frame):
        current_time = datetime.now()
        elapsed_time = (current_time - self.start_time).total_seconds()
        for i in range(4):
            y_value = Gripper.GetCurrent()[i]  # 임의의 y값 생성
            self.x_data[i].append(elapsed_time)
            self.y_data[i].append(y_value)

            if len(self.x_data[i]) > self.max_points:
                self.x_data[i] = self.x_data[i][-self.max_points:]
                self.y_data[i] = self.y_data[i][-self.max_points:]

        for ax, x, y, ylim in zip(self.canvas.fig.get_axes(), self.x_data, self.y_data, self.y_limit):
            ax.clear()
            ax.plot(x, y)
            ax.set_ylim(-ylim, ylim)
            ax.figure.autofmt_xdate()

        self.canvas.draw()

    def on_scroll(self, event):
        zoom_factor = 0.1  # 확대/축소 인자
        for i, ax in enumerate(self.canvas.fig.get_axes()):
            if event.button == 'up':  # 확대
                self.y_limit[i] = max(0.1, self.y_limit[i] - zoom_factor)
            else:  # 축소
                self.y_limit[i] += zoom_factor
            ax.set_ylim(-self.y_limit[i], self.y_limit[i])
        self.canvas.draw_idle()

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

    app = QApplication(sys.argv)
    window = MyWindow()
    # window = MultiGraphWindow()
    window.show()
    app.exec_()
    # sys.exit(app.exec_())

    # 모든 스레드가 종료될 때까지 기다림
    thread1.join()
    thread2.join()

    print("Program is terminated.")
