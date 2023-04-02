from tkinter import  Canvas, Button, PhotoImage
import os
import sys

def abs_path(file_name):
    file_name = 'assets\\' + file_name
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, file_name)

class Main_UI(Canvas):
    def __init__(self, parent):
        Canvas.__init__(self, parent)
        self.configure(
            #window,
            bg = "#FFFFFF",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        # anhr nen
        self.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=abs_path("image_10.png"))
        self.image_1 = self.create_image(
            500.0,
            300.0,
            image=self.image_image_1
        )
        # cai khung
        self.image_image_2 = PhotoImage(
            file = abs_path("image_2.png"))
        self.image_2 = self.create_image(
            466.0,
            323.0,
            image=self.image_image_2
        )

        # set button
        # btn 1 mac address
        self.button_image_mac_addr = PhotoImage(
            file=abs_path("button_mac_addr.png"))
        self.button_mac_addr = Button(self,
            image=self.button_image_mac_addr,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_mac_addr clicked"),
            relief="flat"
        )
        self.button_mac_addr.place(
            x = 552.0,
            y = 20.0,
            width = 120.0,
            height = 120.0
        )
        # btn 2 keylogger
        self.button_image_keylogger = PhotoImage(
            file=abs_path("button_keylogger.png"))
        self.button_keylogger = Button(self,
            image = self.button_image_keylogger,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: print("button_keylogger clicked"),
            relief="flat"
        )
        self.button_keylogger.place(
            x = 727.0,
            y = 20.0,
            width = 120.0,
            height = 120.0
        )        
        # btn 3 Directory tree
        self.button_image_directory_tree = PhotoImage(
            file=abs_path("button_directory_tree.png"))
        self.button_directory_tree = Button(self,
            image = self.button_image_directory_tree,
            borderwidth = 0,
            highlightthickness=0,
            command = lambda: print("button_directory_tree clicked"),
            relief = "flat"
        )
        self.button_directory_tree.place(
            x = 552.0,
            y = 173.0,
            width = 120.0,
            height = 120.0
        )
        # btn 4 live screen
        self.button_image_livescreen = PhotoImage(
            file = abs_path("button_livescreen.png"))
        self.button_livescreen = Button(self,
            image = self.button_image_livescreen,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: print("button_livescreen clicked"),
            relief = "flat"
        )
        self.button_livescreen.place(
            x = 727.0,
            y = 173.0,
            width = 120.0,
            height = 120.0
        )
        # btn 5 Application/Process
        self.button_image_app_process = PhotoImage(
            file=abs_path("button_app_process.png"))
        self.button_app_process = Button(self,
            image = self.button_image_app_process,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: print("button_app_process clicked"),
            relief = "flat"
        )
        self.button_app_process.place(
            x = 552.0,
            y = 327.0,
            width = 120.0,
            height = 120.0
        )
        # btn 6 registry
        self.button_image_registry = PhotoImage(
            file=abs_path("button_registry.png"))
        self.button_registry = Button(self,
            image = self.button_image_registry,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: print("button_registry clicked"),
            relief = "flat"
        )
        self.button_registry.place(
            x = 727.0,
            y = 327.0,
            width = 120.0,
            height = 120.0
        )
        # btn 7 Shutdown/Logout
        self.button_image_shudown_logout = PhotoImage(
            file = abs_path("button_shudown_logout.png"))
        self.button_shudown_logout = Button(self,
            image = self.button_image_shudown_logout,
            borderwidth = 0,
            highlightthickness = 0,
            command =lambda: print("button_shudown_logout clicked"),
            relief = "flat"
        )
        self.button_shudown_logout.place(
            x = 639.0,
            y = 466.0,
            width = 120.0,
            height = 120.0
        )
        # btn disconnect
        self.button_image_disconnect = PhotoImage(
            file=abs_path("button_disconnect.png"))
        self.button_disconnect = Button(self,
            image = self.button_image_disconnect,
            borderwidth = 0,
            highlightthickness = 0,
            command=lambda: print("button_disconnect clicked"),
            relief="flat"
        )
        self.button_disconnect.place(
            x = 130.2931671142578,
            y = 448.287109375,
            width = 247.55702209472656,
            height = 47.96087646484375
        )
        
        

