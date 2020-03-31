import numpy as np
import matplotlib.pyplot as plt
import math

DELTA = 0.01    # 搜索步长
BOUND = [5, 8]  # 定义域x从5到8闭区间
GENERATION = 100  # 随机取乱数100次


def F(x):
    return math.sin(x*x)+2.0*math.cos(2.0*x)


def hillClimbing(x):
    while F(x+DELTA) > F(x) and x+DELTA <= BOUND[1] and x+DELTA >= BOUND[0]:
        x = x+DELTA
    while F(x-DELTA) > F(x) and x-DELTA <= BOUND[1] and x-DELTA >= BOUND[0]:
        x = x-DELTA
    return x, F(x)


def findMax():
    highest = [0, -1000]

    for i in range(GENERATION):
        x = np.random.rand()*(BOUND[1]-BOUND[0])+BOUND[0]
        currentValue = hillClimbing(x)
        print('current value is :', currentValue)

        if currentValue[1] > highest[1]:
            highest[:] = currentValue
    return highest


[x, y] = findMax()

print('highest point is x :{},y:{}'.format(x, y))
