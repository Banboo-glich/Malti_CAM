import cv2
import numpy as np
import PySimpleGUI as sg
import datetime
import time
import os
import numpy as np
import glob
from time import sleep
# import Malti_Cameras as MC
import schedule
import mojimoji
import Malti_func as Mf

folder = './CAM1'
if os.path.exists(folder) == False:
    os.mkdir('./CAM1')
    os.mkdir('./CAM2')
    os.mkdir('./CAM3')
    os.mkdir('./CAM4')
else:
    pass


sg.theme('GreenTan')

# layout = [
#         [sg.Text('Check Camera', size=(40, 1), justification='center', font='Helvetica 20',key='-status-')],
#         [sg.Text('All Camera numbers: ', size=(15, 1)), sg.Drop(values=('1', '2','3','4'),key='-camera_num-')],
#         [sg.Image(filename='', key='image')],
#         [sg.Button('Start', size=(10, 1), font='Helvetica 14',key ='-start-'),
#             sg.Button('Stop', size=(10, 1), font='Helvetica 14',key = '-stop-'),
#             sg.Button('Setting', size=(10, 1), font='Helvetica 14', key='-exit-'), ]
#         ]
layout = [
        [sg.Text('Check Camera', size=(40, 1), justification='center', font='Helvetica 20',key='-status-')],
#         [sg.Image(filename='daityan.png', key='')],
        [sg.Text('Camera numbers: ', size=(15, 1)), sg.Drop(values=('1', '2','3','4'),key='-camera_num-')],
        [sg.Image(filename='', key='image')],
        [sg.Button('Start', size=(10, 1), font='Helvetica 14',key ='-start-'),
            sg.Button('Stop', size=(10, 1), font='Helvetica 14',key = '-stop-'),
            sg.Button('Setting', size=(10, 1), font='Helvetica 14', key='-exit-'), ]
        ]


window = sg.Window('Check',layout, location=(25, 75))


recording = False

while True:
    event, values = window.read(timeout=20)
    if event in (None, '-exit-'):
        window.close()
#         sg.popup('コマンドプロンプトでタイムラプスの設定をして下さい。')
       

    # Green & tan color scheme      
        sg.theme('GreenTan')      

        sg.set_options(text_justification='middle')      

        layout = [[sg.Text('TimeLaps Settings', font=('Helvetica', 16))],      
                  [sg.Text('Number of cameras', size=(15, 1),key='-camera_num2-'), sg.In(default_text='4', size=(4,1))],      
                  [sg.Text('Timalapse(hours)', size=(15, 1),key='-timelapse2-'), sg.In(default_text='408', size=(4, 1))],      
                  [sg.Text('interval(minutes)', size=(15, 1),key='-interval2-'), sg.In(default_text='10', size=(4, 1))],
                  [sg.Text('_'  * 100, size=(25, 1))],
                  [sg.Text('TimeLapse!', size=(10,1)),sg.Submit(key='-timelapse-')]
#                   [sg.Image(filename='', key='image',size=(300,300))]
                 ]

        
        if event in (None,'-cancel-'):
            break
    
        window = sg.Window('TimeLaps', layout, font=("Helvetica", 12))      

        event, values = window.read()   
#         print(values)
#         window['-camera_num2-'].Update('-camera_num2-')
#         window['-timelapse2-'].update('Timalapse(hours)')
#         window['-interval2-'].update('interval(minutes)')
        
        camera_num = str(values[0])
        timelaps_hour = int(values[1])
        minutesinterval = int(values[2])
        
        
        if event in '-timelapse-': 
            
#             for i in range(camera_num):
#                 cap = cv2.VideoCapture(i + 1, cv2.CAP_DSHOW)
#                 cap.set(cv2.CAP_PROP_SETTINGS, i+1)
#                 cap = cap.set(cv2.CAP_PROP_SETTINGS, i+1)
#                 while True:
#                    ret, img = capset + str(i+1).read()
#                    cv2.imshow('video image', img)
#                    key = cv2.waitKey(10)
#                    if key == 27:
#                        break

#                 cap.release()
#                 cv2.destroyAllWindows()

# #             print('タイムラプス全体の時間を指定してください。単位は時間です。')
#             print('数字(整数)のみを入力してください。')
#             timelaps_hour = int(input())
#                 #     timelaps_hour = 12
#             print('')
#             #何分に一度か指定してください。例)10分に1度→minutesinterval = 10
#             print('何分に一度のタイムラプスか指定してください。単位は分です。')
#             print('数字(整数)のみを入力してください。')
#             minutesinterval = int(input())
#                 #     minutesinterval = 10
#             # schedule.every(10).minutes.do(cam_2)
#             # schedule.every(1).seconds.do(cam_2)
#             # schedule.every(minutesinterval*60).seconds.do(cam_2)
#                 # timelapse_hourの単位は時間、minutesintervalの単位は分である。
#                 # そのため、フレーム数の計算では、timelapse_hourに60を掛け、インターバルで割った。
            numphotos = int((timelaps_hour*60)/minutesinterval)
            print("撮影する画像は ", numphotos, '枚です')
            print('')

            directory = os.path.abspath(os.curdir)
            
            sg.popup('コマンドプロンプトで保存するフォルダーを設定してください')
            window.close()


            


            if camera_num == '2':
                try:
                    
                    
                    #     dateraw = datetime.datetime.now()
                    #     datetimeformat = dateraw.strftime("%Y-%m-%d_%H%M")
                    #     new_dir_name = datetimeformat

                    print('カメラ1のフォルダー名を入力してください。')
                    # print('please input camera1 folder name')
                    new_dir_name1 = input()
                    create_directory1 = directory + '/CAM1/' + new_dir_name1
#                     create_directory1 = os.mkdir(create_directory1)
                    
                    print('CAERAM1=> ' + create_directory1 + ' フォルダーを作成しました。 ')
                    print('')
                    print('カメラ2のフォルダー名を入力してください。')
                    new_dir_name2 = input()
                    create_directory2 = directory + '/CAM2/' + new_dir_name2
                    # ！保存先のフォルダ(日本語を指定してください！
#                     create_directory2 = os.mkdir(create_directory2)
                
                    print('CAMERA2=> ' + create_directory2 + ' フォルダーを作成しました。')
                    print('')
                    print('タイムラプスは　' + str(timelaps_hour), '時間後に完了します。 Happy Timelapsing:D')
                    print('--------------------------------------------------------------------------------------------')

                    # schedule.every(minutesinterval * 60).seconds.do(cam_2)
                    # frame_1 = sg.Frame('Camera１', [
                    #     [sg.Text('ラベル')],[sg.Image(filename='', key='image1',size=(550,225))],
                    #     [sg.Button('exit', key="Exit")]
                    # ])

                    # frame_2 = sg.Frame('Camera2', [
                    #     [sg.Text('ラベル')],[sg.Image(filename='', key='image2',size=(550,225))],
                    #     [sg.Button('exit', key="Exit")]
                    # ])

                    # frame_3 = sg.Frame('Camera3', [
                    #     [sg.Text('ラベル')],[sg.Image(filename='', key='image3',size=(550,225))],
                    #     [sg.Button('exit', key="Exit")]
                    # ])

                    # frame_4 = sg.Frame('Camera4', [
                    #     [sg.Text('ラベル')],[sg.Image(filename='', key='image4',size=(550,225))],
                    #     [sg.Button('exit', key="Exit")]
                    # ])

                    # layout = [
                    #     [frame_1, frame_2],
                    #     [frame_3, frame_4]
                    # ]

                    # window_camframe = sg.Window('Malti Camera', layout, size=(1100, 550),resizable=True,location=(25, 75))

                    while True:  # Event Loop



                        for i in range(numphotos):
                            # event, values = window_camframe.Read()
                            # schedule.run_pending()
                            print('撮影した枚数: ',i+1)
                            Mf.cam_2(create_directory1,create_directory2)
                            print('-------------------------------------------------------------------------------------------')

                            # imgbytes1 = cv2.imencode('.png', frame_1)[1].tobytes() 
                            # window_camframe['image1'].update(data=imgbytes1)
                            # time.sleep(1)
                            # imgbytes2 = cv2.imencode('.png', frame_2)[1].tobytes() 
                            # window_camframe['image2'].update(data=imgbytes2)

                            time.sleep(minutesinterval*60)
                    #             time.sleep(minutesinterval)
                        if event is None :
                            break
                except OSError as ex:
                    print(ex)
                    print('違うフォルダー名を設定して下さいよ。')

            elif camera_num == '3':
                try:
                    #     dateraw = datetime.datetime.now()
                    #     datetimeformat = dateraw.strftime("%Y-%m-%d_%H%M")
                    #     new_dir_name = datetimeformat

                    # print('保存するフォルダー名を入力してください。')
                    print('カメラ1のフォルダー名を入力してください。')
                    new_dir_name1 = input()
                    create_directory1 = directory + '/CAM1/' + new_dir_name1
                    os.mkdir(create_directory1)
                    print('CAERAM1=> ' + create_directory1 + ' フォルダーを作成しました。 ')
                    print('')
                    print('カメラ2のフォルダー名を入力してください。')
                    new_dir_name2 = input()
                    create_directory2 = directory + '/CAM2/' + new_dir_name2
                    # ！保存先のフォルダ(日本語を指定してください！
                    os.mkdir(create_directory2)
                    print('CAMERA2=> ' + create_directory2 + ' フォルダーを作成しました。 ')
                    print('')
                    print('カメラ3のフォルダー名を入力してください。')
                    new_dir_name3 = input()
                    create_directory3 = directory + '/CAM3/' + new_dir_name3
                    # ！保存先のフォルダ(日本語を指定してください！
                    os.mkdir(create_directory3)
                    print('CAMERA3=> ' + create_directory3 + ' フォルダーを作成しました。 ')
                    print('')
                    print('タイムラプスは　' + str(timelaps_hour), '時間後に完了します。 Happy Timelapsing:D')

                    # schedule.every(minutesinterval * 60).seconds.do(cam_3)
                    # schedule.every(1).seconds.do(cam_3)

                    for i in range(numphotos):
                        # schedule.run_pending()
                        print('撮影した枚数: ',i+1)
                        Mf.cam_3(create_directory1,create_directory2,create_directory3)
                        print('-------------------------------------------------------------------------------------------')
                        time.sleep(minutesinterval*60)
                #         time.sleep(minutesinterval)

                except OSError as ex:
                    print(ex)
                    print('違うフォルダー名を設定して下さい。')

            elif camera_num == '4':
#                 schedule.every(minutesinterval * 60).seconds.do(cam_4)
                try:
                    #     dateraw = datetime.datetime.now()
                    #     datetimeformat = dateraw.strftime("%Y-%m-%d_%H%M")
                    #     new_dir_name = datetimeformat

                    # print('保存するフォルダー名を入力してください。')
                    print('カメラ1のフォルダー名を入力してください。')
                    new_dir_name1 = input()
                    create_directory1 = directory + '/CAM1/' + new_dir_name1
                    os.mkdir(create_directory1)
                    print('CAERAM1=> ' + create_directory1 + 'フォルダーを作成しました。')
                    print('')
                    print('カメラ2のフォルダー名を入力してください。')
                    new_dir_name2 = input()
                    create_directory2 = directory + '/CAM2/' + new_dir_name2
                    # ！保存先のフォルダ(日本語を指定してください！
                    os.mkdir(create_directory2)
                    print('CAMERA2=> ' + create_directory2 + 'フォルダーを作成しました。')
                    print('')
                    print('カメラ3のフォルダー名を入力してください。')
                    new_dir_name3 = input()
                    create_directory3 = directory + '/CAM3/' + new_dir_name3
                    # ！保存先のフォルダ(日本語を指定してください！
                    os.mkdir(create_directory3)
                    print('CAMERA3=> ' + create_directory3 + 'フォルダーを作成しました。')
                    print('')
                    print('カメラ4のフォルダー名を入力してください。')
                    new_dir_name4 = input()
                    create_directory4 = directory + '/CAM4/' + new_dir_name4
                    # ！保存先のフォルダ(日本語を指定してください！
                    os.mkdir(create_directory4)
                    print('CAMERA4=> ' + create_directory4 + 'フォルダーを作成しました。')
                    print('')
                    print('タイムラプスは' + str(timelaps_hour), '時間後に完了します。 Happy Timelapsing:D')

                    # schedule.every(minutesinterval * 60).seconds.do(cam_4)

                    for i in range(numphotos):
                        print('撮影した枚数: ',i+1)
                        # schedule.run_pending()
                        Mf.cam_4(create_directory1,create_directory2,create_directory3,create_directory4)
                        print('-------------------------------------------------------------------------------------------')
#                         Mf.main(numphotos)
                        time.sleep(minutesinterval*60)
                #         time.sleep(minutesinterval)

                except OSError as ex:
                    print(ex)
                    print('違うフォルダー名を設定して下さい。')

            else:
                print('対応してないっす。')
                
    elif event == '-start-':
        time.sleep(0.2)
        window['-status-'].update('Live')
        camera_number = int(values['-camera_num-'])
        cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
        recording = True
        
        if event == '-camera_num-':
#             cap.release()
            time.sleep(0.2)
            window['-status-'].update('Live')
            camera_number = int(values['-camera_num-'])
            cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
            recording = True

        # cap = cv2.VideoCapture(camera_number)

#         cap.release()

    elif event == '-stop-':
        time.sleep(0.2)
        # cap.release()
        window['-status-'].update("Stop")
        recording = False
        # 幅、高さ　戻り値Float
        W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print(H,W)
        img = np.full((H, W), 0)
        # ndarry to bytes
        imgbytes = cv2.imencode('.png', img)[1].tobytes()
        window['image'].update(data=imgbytes)
        cap.release()
        cv2.destroyAllWindows()

    if recording:
        ret, frame = cap.read()
        if ret is True:
            imgbytes = cv2.imencode('.png', frame)[1].tobytes() 
            window['image'].update(data=imgbytes)

window.close()
