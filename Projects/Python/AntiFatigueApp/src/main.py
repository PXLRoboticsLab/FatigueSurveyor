import argparse
import glob
import os
import threading
import sys
sys.path.append("../UI")
sys.path.append("../src")
sys.path.append("./")
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import time

import drive_list
from Mainwindow import *
from PopUp import *


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
time_left=0
level=5


# pop-up
def get_slider_val():
    global level
    level=dialog_box.ui.horizontalSlider.value()
    print("level: "+str(level))
    print("slider: "+str(dialog_box.ui.horizontalSlider.value()))
    return level



def set_slider_text(label,value):
    label.setText(str(value))

def ok_btn_clicked():
    global mainwindow
    print("mainwindow param: "+str(level))
    mainwindow=MainWindow(level)
    dialog_box.hide()
    mainwindow_init()
    mainwindow.show()


def dialog_box_init():
    global dialog_box
    dialog_box.show()
    # level = get_slider_val()
    slider = dialog_box.ui.horizontalSlider
    slider_label = dialog_box.ui.energy_label_slider_value
    set_slider_text(slider_label, get_slider_val())

    slider.valueChanged['int'].connect(get_slider_val)

    dialog_box.ui.buttonBox.accepted.connect(ok_btn_clicked)

def start_timer(seconds):
    global time_left
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
        recording_timer.singleShot(10000,reset_app)
        # recording_timer.timeout.connect()
        # recording_timer.
        timer.stop()
        timer.start(20)
        timer.timeout.connect(mainwindow.showFeed)
    if time_left >=0:
        update_timer_test_label(time_left)
        time_left = time_left-1

def upload_vid():
    list_of_files = glob.glob('../camCaptures/*mp4')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    drive_list.uploadFile(latest_file)


def reset_app():
    global app
    global dialog_box
    global mainwindow
    # print("reset_app"+threading.enumerate().__str__())

    main()
    upload_vid()

def mainwindow_init():
    global time_left
    update_timer_test_label(time_left)
    start_timer(2)


def cleanup():
    global mainwindow
    global timer
    global recording_timer
    global app

    global dialog_box

    timer.disconnect()


    recording_timer.disconnect()

    if mainwindow is not None:

        mainwindow.cap.release()
        mainwindow.writer=None

    dialog_box = None
    mainwindow = None

def main():

    print(threading.enumerate())
    global app
    global mainwindow
    global dialog_box

    if not app:
        app = QApplication(sys.argv)
    dialog_box = PopUp()
    mainwindow = None
    dialog_box_init()



if __name__ == '__main__':

    global mainwindow
    global app
    global dialog_box
    app = QApplication(sys.argv)


    try:
        reset_app()
    finally:

        sys.exit(app.exec_())





