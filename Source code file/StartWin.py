try :
    import time
    import os
    import cv2
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

def Record_Sund_and_Screen_File(Time):
    duration = Time  # time record
    audio_filename = "C:/LOG_Program_Cactus_Black/recorded_audio_"+str(time.strftime( "%Y_%m_%d_T_%H_%M_%S"))+".wav"  # name and path file

    video_filename = "C:/LOG_Program_Cactus_Black/screen_recording_" + str(time.strftime("%Y_%m_%d_T_%H_%M_%S")) + ".mp4"
    fps = 10.0  # FPS
    resolution = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(video_filename, fourcc, fps, resolution)
    def record_audio():
        audio = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
        sd.wait()
        sf.write(audio_filename, audio, 44100) # Save File
    def record_screen():
        start_time = time.time()
        while time.time() - start_time < duration:
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

def Record_Camera_File():
    # Open Camera
    cap = cv2.VideoCapture(0)
    Activ = False
    if not cap.isOpened():
        pass
    else:
        # read canera
        ret, frame = cap.read()

        if ret:
            # show camera
            cv2.imshow('Camera', frame)
            # Save Image
            cv2.imwrite("C:/LOG_Program_Cactus_Black/Camera_"+str(time.strftime( "%Y_%m_%d_T_%H_%M_%S"))+".jpg", frame)
            Activ = True
        else:
            pass

        # exit the camera
        cap.release()
        cv2.destroyAllWindows()
    if Activ == True :
        return "No Error :)"
    else :
        return "Get Erorr!!!"


# Create Back Data
SystemAdress = "C:/LOG_Program_Cactus_Black"
Back_FILE_T = ""
Back_FILE_E = ""
E = ""
# Get Back Data Start Windows
try:
    file = open("C:/LOG_Program_Cactus_Black"+"/TimeLog.Cactus_Black","r")
    Back_FILE_T = file.read()
except :
    Create = open(SystemAdress+"/TimeLog.Cactus_Black","w")
    Create.close()
try:
    file = open(SystemAdress+"/ErrorLog.Cactus_Black","r")
    Back_FILE_E = file.read()
except :
    Create = open(SystemAdress+"/ErrorLog.Cactus_Black","w")
    Create.close()

# Get Setting
# SOON
# Save Log
W_file = open("C:/LOG_Program_Cactus_Black"+"/TimeLog.Cactus_Black","w")
W_file.write(Back_FILE_T+"time start Sys is : "+str(time.strftime( "%Y / %m / %d , %H:%M:%S"))+"\n")
W_file.close()
# Get Data
Camera = Record_Camera_File()
Screen_and_sund  = Record_Sund_and_Screen_File(180)
FOLDER = [f for f in os.listdir("C:/Windows/Temp/")
            if os.path.isfile(os.path.join("C:/Windows/Temp/", f))]
for i in FOLDER :
    try:
        os.remove("C:/Windows/Temp/"+i)
        E = "No Error :)"
    except :
        E = "Get Error!!"
# Save Errors
Errors = (f"Errors {str(time.strftime( "%Y / %m / %d , %H:%M:%S"))} is : \nErrors Record Camera : {Camera}\nErrors Record Screen & Sund : {Screen_and_sund}\nnErrors Remove Temp Files : {E}")
W_file = open(SystemAdress+"/ErrorLog.Cactus_Black","r")
W_file.write(Back_FILE_T+Errors)
W_file.close()
# Show Notife End
toast = ToastNotifier()
masege = ("Hi Welcom King!")
toast.show_toast("Welcome!",masege,duration = 5,threaded = True)
