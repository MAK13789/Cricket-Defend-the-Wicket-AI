from sklearn.preprocessing import MinMaxScaler
import numpy as np
import tensorflow as tf
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
#make 3 seperate models
#first predicting x_pos_diff_list based on ball_pos_list:
model_1 = tf.keras.Sequential()
model_1.add(tf.keras.layers.Dense(1, activation = 'relu'))
model_1.add(tf.keras.layers.Dense(1, activation = 'sigmoid'))
model_1.compile(loss = 'mean_squared_error', optimizer = 'adam')
model_1.fit(ball_pos_list, x_pos_diff_list, batch_size = 1, epochs = 20, verbose = 1)
model_1.save("model_1.h5")
#next predicting y_pos_diff_list based on ball_pos_list:
model_2 = tf.keras.Sequential()
model_2.add(tf.keras.layers.Dense(1, activation = 'relu'))
model_2.add(tf.keras.layers.Dense(1, activation = 'sigmoid'))
model_2.compile(loss = 'mean_squared_error', optimizer = 'adam')
model_2.fit(ball_pos_list, y_pos_diff_list, batch_size = 1, epochs = 20, verbose = 1)
model_2.save("model_2.h5")
#finally predicting time_diff_list based on ball_pos_list
model_3 = tf.keras.Sequential()
model_3.add(tf.keras.layers.Dense(1, activation = 'relu'))
model_3.add(tf.keras.layers.Dense(1, activation = 'sigmoid'))
model_3.compile(loss = 'mean_squared_error', optimizer = 'adam')
model_3.fit(ball_pos_list, time_diff_list, batch_size = 1, epochs = 20, verbose = 1)
model_3.save("model_3.h5")
