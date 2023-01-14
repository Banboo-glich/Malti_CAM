import PySimpleGUI as sg
import datetime
import time
import os
import numpy as np
import cv2
import glob
from time import sleep
# import Malti_Cameras as MC
import schedule
import mojimoji
import sys
# import camera_frame as cf


# class 
def cam_2(create_directory1,create_directory2):

    # global create_directory1
    cap1 = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    time.sleep(1)
    cap1.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret1, frame1 = cap1.read()
    print(ret1)
    if ret1 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        os.exit()
    recording = True        
    # cf.camera_frame(frame1)


    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename1 = create_directory1 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename1, frame1)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA1: ' + filename1 + ' => saved!')
    cap1.release()
    time.sleep(1)


    cap2 = cv2.VideoCapture(2,cv2.CAP_DSHOW)
    time.sleep(1)
    cap2.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret2, frame2 = cap2.read()
    print(ret2)
    if ret2 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        sys.exit()

    # imgbytes = cv2.imencode('.png', frame2)[1].tobytes() 
    # window_camframe['image2'].update(data=imgbytes)

    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename2 = create_directory2 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename2, frame2)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA2: ' + filename2 + ' => saved!')
    cap2.release()
    # window_camframe.Close()
    cv2.destroyAllWindows()


def cam_3(create_directory1,create_directory2,create_directory3):
    cap1 = cv2.VideoCapture(1)
    time.sleep(1)
    cap1.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret1, frame1 = cap1.read()
    print(ret1)
    if ret1 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        sys.exit()
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename1 = create_directory1 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename1, frame1)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA1: ' + filename1 + ' => saved!')
    cap1.release()
    time.sleep(1)

    cap2 = cv2.VideoCapture(2)
    time.sleep(1)
    cap2.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret2, frame2 = cap2.read()
    print(ret2)
    if ret2 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        sys.exit()
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename2 = create_directory2 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename2, frame2)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA2: ' + filename2 + ' => saved!')
    cap2.release()
    cv2.destroyAllWindows()

    cap3 = cv2.VideoCapture(3)
    time.sleep(1)
    cap3.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret3, frame3 = cap3.read()
    print(ret3)
    if ret3 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        sys.exit()
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename3 = create_directory3 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename3, frame3)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA3: ' + filename3 + ' => saved!')
    cap3.release()
    cv2.destroyAllWindows()


def cam_4(create_directory1,create_directory2,create_directory3,create_directory4):
    cap1 = cv2.VideoCapture(1)
    time.sleep(1)
    cap1.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret1, frame1 = cap1.read()
    print(ret1)
    if ret1 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        sys.exit()
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename1 = create_directory1 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename1, frame1)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA1: ' + filename1 + ' => saved!')
    cap1.release()
    time.sleep(1)

    cap2 = cv2.VideoCapture(2)
    time.sleep(1)
    cap2.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret2, frame2 = cap2.read()
    print(ret2)
    if ret2 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        sys.exit()
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename2 = create_directory2 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename2, frame2)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA2: ' + filename2 + ' => saved!')
    cap2.release()
    cv2.destroyAllWindows()

    cap3 = cv2.VideoCapture(3)
    time.sleep(1)
    cap3.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret3, frame3 = cap3.read()
    print(ret3)
    if ret3 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        sys.exit()
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename3 = create_directory3 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename3, frame3)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA3: ' + filename3 + ' => saved!')
    cap3.release()

    cap4 = cv2.VideoCapture(4)
    time.sleep(1)
    cap4.set(cv2.CAP_PROP_EXPOSURE,-6)
    ret4, frame4 = cap4.read()
    print(ret4)
    if ret4 == False:
        print('画像の読み込みに失敗しました。Anacondaを再起動してください。')
        sys.exit()
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    filename4 = create_directory4 + '/{:%m-%d_%H%M_%S}.jpg'.format(now)
    # Capture frame-by-frame
    cv2.imwrite(filename4, frame4)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('CAMERA4: ' + filename4 + ' => saved!')
    cap4.release()
    cv2.destroyAllWindows()