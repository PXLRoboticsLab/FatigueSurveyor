#!/usr/bin/env python3
import calendar
import sys
sys.path.append("./src")
sys.path.append("../UI")
sys.path.append("./")

import imutils
import numpy as np
import cv2

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QImage
import time
from main import *

from ui_mainwindow import *
# from src.main import args


class MainWindow(QWidget):



    def __init__(self, level):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.cap =  cv2.VideoCapture(args["camera"])
        # time.sleep(2.0)
        self.fourcc =None
        self.writer = None
        self.zeros = None
        self.output_file= None
        print(level)
        self.level=level




    # def controlTimer(self):
    #     # if timer is stopped
    #     if not self.timer.isActive():
    #         # create video capture
    #         self.cap =  cv2.VideoCapture(args["camera"])
    #         # time.sleep(2.0)
    #         # start timer
    #         self.timer.start(20)
    #         # update control_bt text
    #         self.ui.control_bt.setText("Stop")
    #     # if timer is started
    #
    #     else:
    #         # stop timer
    #         self.timer.stop()
    #         # release video capture
    #         # self.cap.release()
    #         # update control_bt text
    #         # self.ui.control_bt.setText("Start")

    def showFeed(self):
        # print(level)
        # self.level = mainwindow.level

        ret,frame = self.cap.read()

        # resize frame image
        scaling_factor = 0.8
        height,width, _ = frame.shape

        frame = frame[60:-60+height,120:-120+width ]


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
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
        if self.writer is None:
            # store the image dimensions, initialize the video writer,
            # and construct the zeros array
            (h, w) = gray.shape[:2]
            self.fourcc=cv2.VideoWriter_fourcc(*args["codec"])
            #print(main.level)
            self.output_file='../camCaptures/'+ str(int(calendar.timegm(time.gmtime())))[5:]+"_"+str(self.level)+".mp4"
            self.writer = cv2.VideoWriter(self.output_file, self.fourcc, int(args["fps"]),
                                          (int(w), int(h)), 0)
            # self.zeros = np.zeros((height, width), dtype="uint8")

        output = np.zeros((height, width, 1), dtype="uint8")
        output[:, :,0] = gray
        self.writer.write(output)




