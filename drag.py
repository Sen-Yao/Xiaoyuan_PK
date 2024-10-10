import pyautogui
import time

DRAGGING_SCREEN_START_X = 500
DRAGGING_SCREEN_START_Y = 1300
DRAGGING_SCREEN_END_X = 600
DRAGGING_SCREEN_END_Y = 1400

def print_larger_than():
    pyautogui.moveTo(DRAGGING_SCREEN_START_X, DRAGGING_SCREEN_START_Y, duration=0.01)
    pyautogui.mouseDown()  # 按下鼠标
    pyautogui.moveTo(DRAGGING_SCREEN_END_X, (DRAGGING_SCREEN_START_Y + DRAGGING_SCREEN_END_Y) / 2, duration=0.05)
    pyautogui.moveTo(DRAGGING_SCREEN_START_X, DRAGGING_SCREEN_END_Y, duration=0.05)
    pyautogui.mouseUp()  # 松开鼠标

def print_less_than():
    pyautogui.moveTo(DRAGGING_SCREEN_END_X, DRAGGING_SCREEN_START_Y, duration=0.01)
    pyautogui.mouseDown()  # 按下鼠标
    pyautogui.moveTo(DRAGGING_SCREEN_START_X, (DRAGGING_SCREEN_START_Y + DRAGGING_SCREEN_END_Y) / 2, duration=0.05)
    pyautogui.moveTo(DRAGGING_SCREEN_END_X, DRAGGING_SCREEN_END_Y, duration=0.05)
    pyautogui.mouseUp()  # 松开鼠标
