import tensorflow as tf
import pyautogui
from PIL import ImageGrab
import time
import win32api
i = 0
j = 642
k = 642
ball_pos_list = []
pos_diff_list = []
time_diff_list = []
def is_click():
    if (win32api.GetKeyState(0x01) < 0):
        return True
def mouse():
    initial_pos = pyautogui.position()
    initial_time = time.time()
    x = 0
    while (x < 10000):
        if (is_click() == True):
            final_time = time.time()
            time_diff = final_time - initial_time
            time_diff = round(time_diff, 1)
            final_pos = pyautogui.position()
            temp_array = []
            x_pos_diff = final_pos[0] - initial_pos[0]
            y_pos_diff = final_pos[1] - initial_pos[1]
            temp_array.append(x_pos_diff)
            temp_array.append(y_pos_diff)
            return time_diff, temp_array
        else:
            time.sleep(0.001)
            x += 1
while (i<5000):
    image = ImageGrab.grab()
    while (j >= 642) and (j <= 973):
        while (k >= 642) and (k <= 646):
            temp = image.getpixel((j, k))
            a = temp[0]
            b = temp[1]
            c = temp[2]
            if ((a>=120) and (a<=144) and (b>=39) and (b<=75) and (c>=37) and (c<=57)):
                print("BALL DETECTED!!!!!")
                temp_list = []
                temp_list.append(j)
                temp_list.append(k)
                ball_pos_list.append(temp_list)
                output = mouse()
                temp_1 = output[0]
                time_diff_list.append(temp_1)
                temp_2 = output[1]
                pos_diff_list.append(temp_2)
                j = 974
                k = 647
            k +=1
        k = 642
        j += 1
    j = 642
    i += 1
