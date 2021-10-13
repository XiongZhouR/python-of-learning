import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import trace

data_dict = {-1: np.array([[1, 7], [2, 8], [3, 8], ]),
             1: np.array([[5, 1], [6, -1], [7, 3], ])
             }
colors = {1: 'r', -1: 'g'}

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
[[ax.scatter(x[0], x[1], s=100, color=colors[i])
  for x in data_dict[i]] for i in data_dict]

# plt.show()

# 定义线性可分支持向量机的模型主体


def train(data):
    # 参数字典 {||w||:[w,b]}
    opt_dict = {}
    # 数据转换列表
    transforms = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

    # 从字典中获取所有的数据

    all_data = []
    for yi in data:
        for featureset in data[yi]:
            for feature in featureset:
                all_data.append(feature)

    # 获取最大最小值
    max_feature_value = max(all_data)
    min_feature_value = min(all_data)
    all_data = None

    # 定义一个步长列表
    step_sizes = [max_feature_value * 0.1,
                  max_feature_value * 0.01,
                  max_feature_value * 0.001]

    # 参数b的范围设置
    b_range_mutiple = 2
    b_mutiple = 5
    latest_optimum = max_feature_value * 10

    # 基于不同的步长训练优化
    for step in step_sizes:
        w = np.array([latest_optimum, latest_optimum])

        # 凸优化

        optimized = False

        while not optimized:
            for b in np.arange(-1*(max_feature_value*b_range_mutiple),
                               max_feature_value*b_range_mutiple,
                               step*b_mutiple):
                for transformation in transforms:
                    w_t = w*transformation
                    found_option = True
                    for i in data:
                        for xi in data[i]:
                            yi = i
                            if not yi*(np.dot(w_t, xi)+b) >= 1:
                                found_option = False
                    if found_option:
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]
            if w[0] < 0:
                optimized = True
                print('Optimized a step!')
            else:
                w = w - step
        norms = sorted([n for n in opt_dict])
        # ||w|| : [w,b]
        opt_choice = opt_dict[norms[0]]
        w = opt_choice[0]
        b = opt_choice[1]
        latest_optimum = opt_choice[0][0]+step*2

    for i in data:
        for xi in data[i]:
            yi = i
            print(xi, ':', yi*(np.dot(w, xi)+b))
    return w, b


w, b = train(data_dict)
