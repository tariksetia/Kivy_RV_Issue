import os, sys, json
import os.path
import kivy
from kivy.core.window import Window
from kivy.config import Config 
from kivy.metrics import sp, dp


def set_windows_config():
    Window.clearcolor = (1,1,1,1)   
    Window.maximize()
    w,h = Window.width, Window.height
    if kivy.utils.platform == 'win':
        Window.minimum_height = h
        Window.minimum_width = w
    else:
        #Window.minimum_height = dp(h/4)
        Window.minimum_width = dp(w/4)  
    

def get_path(file_path):
    if hasattr(sys, "_MEIPASS"):
        path = os.path.join(sys._MEIPASS, file_path)
    else:
        path = file_path

    return path