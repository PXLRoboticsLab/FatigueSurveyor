import argparse
import calendar
import datetime
import glob
import os
import threading
import sys

import cv2
import imutils

import numpy as np
sys.path.append("../UI")
sys.path.append("../src")
sys.path.append("./")

from ui_updated import *


from PyQt5.QtCore import QTimer, QByteArray
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap, QImage, QMovie, QIcon
import time

import drive_list

# from Mainwindow import *
# from PopUp import *


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default=('../camCaptures/'
                                                     + str(int(calendar.timegm(time.gmtime())))[5:]),
                # +str(level)+'.mp4'),
                help="path to output video file")
ap.add_argument("-C", "--camera", type=int, default=0,
                help="whether or not the Raspberry Pi camera should be used")
ap.add_argument("-f", "--fps", type=int, default=50,
                help="FPS of output video")
ap.add_argument("-c", "--codec", type=str, default="mp4v",
                help="codec of output video")
args = vars(ap.parse_args())

# timer
timer = QTimer()
recording_timer = QTimer()
reset_timer = QTimer()
time_left = 0
level = 5
seconds_untill_reset =1200


# pop-up
def update_slider_val():
    global level
    global mainwindow
    get_slider_val()

    mainwindow.output_file = '../camCaptures/' + str(datetime.datetime.now().timestamp()).split('.')[0] + "_" + str(
        level) + ".mp4"
    # print(mainwindow.output_file)
    set_slider_text(mainwindow.ui.energy_label_slider_value, level)


def get_slider_val():
    global level
    global mainwindow
    level = mainwindow.ui.horizontalSlider.value()
    #print("level: " + str(level))
    #print("slider: " + str(mainwindow.ui.horizontalSlider.value()))
    return level


def set_slider_text(label, value):
    global mainwindow
    label.setText(str(value))


def ok_btn_clicked():
    global mainwindow
    #print("mainwindow param: " + str(level))
    # mainwindow.gif.stop()
    mainwindow.ui.image_label.setText("0")
    # mainwindow.ui.image_label.setMovie(None)
    mainwindow.ui.frame.hide()

    mainwindow.height = Mainwindow.minimumHeight(mainwindow.ui.Dialog)
    set_cam_timer_init()
    # mainwindow.show()


def showFeed():
    # print(level)
    # self.level = mainwindow.level
    global level
    global mainwindow
    # mainwindow.gif.stop()

    ret, frame = mainwindow.cap.read()

    # resize frame image
    scaling_factor = 0.8
    height, width, _ = frame.shape

    frame = frame[60:-60 + height, 120:-120 + width]

    # frame = cv2.resize(frame,(300,int(frame.shape[0]*scaling_factor)), interpolation=cv2.INTER_AREA)
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor,
                       interpolation=cv2.INTER_AREA)
    gray = imutils.resize(frame, width=300)
    # convert frame to GRAY format
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    # print(gray.shape)
    # frame = cv2.flip(frame, 1)
    # cv2.imshow('my webcam', img)
    # height, width, channel = frame.shape
    height, width = gray.shape
    step = 0 * width

    # create QImage from RGB frame
    qImg = QImage(gray.data, width, height, step, QImage.Format_Grayscale8)
    mainwindow.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
    if mainwindow.writer is None:
        # store the image dimensions, initialize the video writer,
        # and construct the zeros array
        (h, w) = gray.shape[:2]
        mainwindow.fourcc = cv2.VideoWriter_fourcc(*args["codec"])
        #print(level)
        # mainwindow.output_file = '../camCaptures/' + str(int(calendar.timegm(time.gmtime())))[5:] + "_" + str(level) + ".mp4"
        print(mainwindow.output_file)
        mainwindow.writer = cv2.VideoWriter(mainwindow.output_file, mainwindow.fourcc, int(args["fps"]),
                                            (int(w), int(h)), 0)
        # self.zeros = np.zeros((height, width), dtype="uint8")

    output = np.zeros((height, width, 1), dtype="uint8")
    output[:, :, 0] = gray
    mainwindow.writer.write(output)


def mainwindow_init():
    global level
    global mainwindow
    mainwindow.show()
    level = get_slider_val()

    slider = mainwindow.ui.horizontalSlider
    slider_label = mainwindow.ui.energy_label_slider_value
    #print("main_init level val: " + str(level))
    set_slider_text(slider_label, get_slider_val())

    slider.valueChanged['int'].connect(update_slider_val)

    mainwindow.ui.buttonBox.accepted.connect(ok_btn_clicked)


def start_timer(seconds):
    global time_left
    global timer
    timer = QTimer()
    time_left = seconds

    timer.start(1000)
    timer.timeout.connect(timer_timeout_warmup_cam)


def update_timer_test_label(t):
    mainwindow.ui.image_label.setText(str(t))


def timer_timeout_warmup_cam():
    global time_left
    global mainwindow
    if time_left == 0:
        # time_left=0
        recording_timer.singleShot(10000, stop_recording_timer)
        # recording_timer.timeout.connect()
        # recording_timer.
        timer.stop()
        timer.start(20)
        timer.timeout.connect(showFeed)
    if time_left >= 0:
        update_timer_test_label(time_left)
        time_left = time_left - 1


def upload_vid():
    list_of_files = glob.glob('../camCaptures/*mp4')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    #print(latest_file)
    drive_list.uploadFile(latest_file)


def stop_recording_timer():
    timer.timeout.disconnect(showFeed)
    recording_timer.stop()


    if mainwindow is not None:
        mainwindow.cap.release()
        mainwindow.writer = None
        mainwindow.ui.frame.hide()
        mainwindow.ui.timeout_frame.show()
        # mainwindow.ui.image_label.setMovie(mainwindow.gif)
        mainwindow.ui.buttonBox.setEnabled(False)
        # mainwindow.gif.start()
        mainwindow.ui.image_label.setPixmap(QPixmap.fromImage(QImage('../res/notUsingCam.png')))

    cleanup()


def reset_app():
    global app
    # global dialog_box
    global mainwindow
    # if mainwindow is not None:
    #     mainwindow.destroy()

    # print("reset_app"+threading.enumerate().__str__())
    main()

    # timer.timeout.connect(showFeed)
    upload_vid()


# TODO  rename meth
def set_cam_timer_init():
    global time_left
    update_timer_test_label(time_left)
    start_timer(2)


def cleanup():
    global mainwindow
    global timer
    global recording_timer
    global app
    global seconds_untill_reset
    seconds_untill_reset=1200
    reset_timer.start(1000)
    reset_timer.timeout.connect(timer_timeout_countdown)
    # reset_app()


    dialog_box = None
    # mainwindow = None


def update_timeout_frame_label(seconds_untill_reset):
    global mainwindow
    mainwindow.ui.timeout_frame_label.setText(f'Time untill next recording \n{int(seconds_untill_reset/60)}:{seconds_untill_reset%60}')



def timer_timeout_countdown():
    global seconds_untill_reset
    global mainwindow
    if seconds_untill_reset == 0:
        # time_left=0
        reset_timer.stop()
        mainwindow.ui.timeout_frame.hide()
        close_and_reset()
        # recording_timer.timeout.connect()
        # recording_timer.

    if seconds_untill_reset >= 0:
        update_timeout_frame_label(seconds_untill_reset)
        seconds_untill_reset = seconds_untill_reset - 1



def close_and_reset():
    global mainwindow
    mainwindow.close()
    reset_app()


class Mainwindow(QMainWindow):

    def __init__(self):
        global level
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.cap = cv2.VideoCapture(args["camera"])
        # self.gif = QMovie('../res/whitenoise.gif', QByteArray(), self)
        # self.gif.setCacheMode(QMovie.CacheAll)
        # self.gif.setSpeed(100)
        # self.ui.image_label.setMovie(self.gif)
        self.ui.image_label.setScaledContents(True)
        self.ui.image_label.setPixmap(QPixmap.fromImage(QImage('../res/notUsingCam.png')))
        # self.gif.start()
        # time.sleep(2.0)
        self.fourcc = None
        self.writer = None
        self.zeros = None
        self.output_file = None
        # print(level)


def main():
    # print(threading.enumerate())
    global app
    global mainwindow

    if not app:
        app = QApplication(sys.argv)

    mainwindow = Mainwindow()

    # dialog_box = PopUp()
    # mainwindow = None
    mainwindow_init()


if __name__ == '__main__':
    global mainwindow
    global app
    print("running")
    app = QApplication(sys.argv)


    try:

        reset_app()

    finally:

        sys.exit(app.exec_())
