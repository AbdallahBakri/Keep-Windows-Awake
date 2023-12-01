# Application Name: Keep Windows Awake                            
# Description: Keep Windows Awake by Abdallah Bakri.
# Version: 1.0 (Deployment)
# Author: Abdallah Bakri
# GitHub: https://github.com/AbdallahBakri/Keep-Windows-Awake

import pyautogui
import time
import sys
import logging
from datetime import datetime
import tkinter as tk
from tkinter import ttk

DEFAULT_MINUTES = 3
MOVEMENT_INTERVAL = 60
NUM_MOVEMENTS = 200
pyautogui.FAILSAFE = False

def move_cursor():
    for i in range(NUM_MOVEMENTS):
        pyautogui.moveTo(0, i * 4)
    pyautogui.moveTo(1, 1)
    for _ in range(3):
        pyautogui.press("shift")
        
def start_keep_windows_awake():
    while True:
        try:
            for _ in range(DEFAULT_MINUTES):
                time.sleep(MOVEMENT_INTERVAL)
            move_cursor()
            print(f"Movement made at {datetime.now().time()}")
        except KeyboardInterrupt:
            print(f"Script Disabled")
            break
        except Exception as e:
            logging.error("An error occurred: %s", str(e))
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("=== Keep Windows Awake by Abdallah Bakri ===")
    print("GitHub: https://github.com/AbdallahBakri/Keep-Windows-Awake")
    logging.basicConfig(level=logging.INFO)
    start_keep_windows_awake()
