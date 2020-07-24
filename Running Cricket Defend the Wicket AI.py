import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pyautogui
from PIL import ImageGrab
import time
scaler1 = MinMaxScaler(feature_range = (0, 1))
scaler2 = MinMaxScaler(feature_range = (0, 1))
scaler3 = MinMaxScaler(feature_range = (0, 1))
scaler4 = MinMaxScaler(feature_range = (0, 1))
temp = [[938, 642], [913, 642], [879, 644], [942, 642], [851, 642], [895, 643], [860, 643], [914, 645], [880, 645], [916, 642], [863, 644], [891, 642], [939, 642], [884, 643], [941, 643], [850, 642], [874, 642], [942, 644], [898, 644], [911, 643], [932, 645], [868, 642], [951, 642], [919, 642], [907, 642], [898, 642], [882, 642], [882, 642], [924, 645], [883, 642], [900, 642], [863, 645], [920, 642], [918, 645], [875, 642], [922, 642], [868, 644], [883, 646], [955, 644], [895, 643], [918, 642], [919, 645], [950, 643], [927, 642], [950, 642], [908, 645], [881, 642], [854, 643], [888, 643], [939, 643]]
ball_pos_list = []
for i in range(len(temp)):
    ball_pos_list.append(temp[i][0])
ball_pos_list = np.array(ball_pos_list)
ball_pos_list = ball_pos_list.reshape(-1, 1)
ball_pos_list = scaler1.fit_transform(ball_pos_list)
pos_diff_list = [[525, -33], [427, -17], [418, -41], [365, -67], [380, -32], [370, -55], [278, -60], [351, -28], [328, -21], [310, -41], [345, 11], [333, -8], [333, -24], [330, -48], [408, -19], [360, 6], [332, -35], [384, -9], [368, -26], [271, -81], [236, -41], [322, -43], [336, -72], [415, -2], [428, 28], [321, -36], [351, 36], [316, 13], [335, 30], [261, -10], [336, 21], [364, 33], [326, 25], [321, -19], [334, 19], [317, 34], [228, -4], [374, 31], [301, 29], [367, 33], [307, 52], [308, 39], [370, 11], [468, -29], [428, -19], [368, 33], [331, 10], [425, 30], [388, 32], [401, 7]]
x_pos_diff_list = []
for j in range(len(pos_diff_list)):
    x_pos_diff_list.append(pos_diff_list[j][0])
x_pos_diff_list = np.array(x_pos_diff_list)
x_pos_diff_list = x_pos_diff_list.reshape(-1, 1)
x_pos_diff_list = scaler2.fit_transform(x_pos_diff_list)
y_pos_diff_list = []
for k in range(len(pos_diff_list)):
    y_pos_diff_list.append(pos_diff_list[k][1])
y_pos_diff_list = np.array(y_pos_diff_list)
y_pos_diff_list = y_pos_diff_list.reshape(-1, 1)
y_pos_diff_list = scaler3.fit_transform(y_pos_diff_list)
time_diff_list = [1.1, 1.1, 1.2, 1.4, 1.2, 1.3, 1.1, 1.2, 1.1, 1.4, 1.2, 1.4, 1.3, 1.2, 1.5, 1.2, 1.1, 1.4, 1.1, 1.0, 1.0, 1.1, 1.4, 1.3, 1.0, 1.7, 1.4, 1.2, 1.0, 1.1, 1.0, 0.9, 1.3, 1.3, 1.0, 1.0, 1.1, 1.0, 1.3, 1.0, 1.3, 1.5, 1.3, 1.4, 1.3, 1.4, 1.0, 1.0, 1.1, 1.2]
time_diff_list = np.array(time_diff_list)
time_diff_list = time_diff_list.reshape(-1, 1)
time_diff_list = scaler4.fit_transform(time_diff_list)
model_1 = tf.keras.models.load_model("model_1.h5")
model_2 = tf.keras.models.load_model("model_2.h5")
model_3 = tf.keras.models.load_model("model_3.h5")
while (i<5000):
    image = ImageGrab.grab()
    while (j >= 642) and (j <= 973):
        while (k >= 642) and (k <= 646):
            temp = image.getpixel((j, k))
            a = temp[0]
            b = temp[1]
            c = temp[2]
            if ((a>=120) and (a<=144) and (b>=39) and (b<=75) and (c>=37) and (c<=57)):
                temporary = [j]
                temporary = np.array(temporary)
                temporary = temporary.reshape(-1, 1)
                scaled_ball_coord = scaler1.fit_transform(temporary)
                x_pos_diff = model_1.predict(scaled_ball_coord)
                x_pos_diff = scaler2.inverse_transform(x_pos_diff)
                x_pos_diff = x_pos_diff[0][0]
                y_pos_diff = model_2.predict(scaled_ball_coord)
                y_pos_diff = scaler3.inverse_transform(y_pos_diff)
                y_pos_diff = y_pos_diff[0][0]
                time_diff = model_3.predict(scaled_ball_coord)
                time_diff = scaler4.inverse_transform(time_diff)
                time_diff = time_diff[0][0]
                random_temp = pyautogui.position()
                X = random_temp[0] + x_pos_diff
                Y = random_temp[1] + y_pos_diff
                time.sleep(0.2)
                pyautogui.moveTo(X, Y, duration = time_diff) #can be 0.35 is not trained well
                pyautogui.moveTo(490, 595, duration = 0)  #y coordinate can be 650 if not trained well
                j = 974
                k = 647
            k +=1
        k = 642
        j += 1
    j = 642
    i += 1
