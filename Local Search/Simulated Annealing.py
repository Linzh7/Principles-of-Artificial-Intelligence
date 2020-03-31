import numpy as np
# 初始温度
T = 1
x = np.random.uniform(0, 100)
# 终止温度
std = 0.00000001
# 衰减率
a = 0.999
while T > std:
    y = x_function(x)
    x_new = x + np.random.uniform(-1, 1)  # 新值通过扰动产生
    if 0 <= x_new <= 100:
        y_new = x_function(x_new)
        if y_new < y:
            x = x_new
        else:
            p = np.exp((y - y_new) / T)
            r = np.random.uniform(0, 1)
            if p > r:
                x = x_new
                # print(x)
    T = T * a
print(x, x_function(x))
