import matplotlib.pyplot as plt
import random
import matplotlib
from matplotlib import font_manager
import numpy as np
# 设置图片大小及像素
plt.figure(figsize=(20, 8), dpi=80)

# 设置中文
my_font = font_manager.FontProperties(
    fname='/System/Library/Fonts/Hiragino Sans GB.ttc')
# 生成数据
x = range(0, 120)
random.seed(10)  # 生成随机种子,不同时候得到的随机结果都一样
y = [random.randint(20, 35) for i in range(120)]

# 画图
plt.plot(x, y)

# 设置坐标轴刻度
_xticks_lables = ['10点{}分'.format(i) for i in x if i<60 ]
_xticks_lables += ['11点{}分'.format(i-60) for i in x if i>=60]
# 取步长和数字和字符串一一对应,数据的长度一样.rotation:旋转度数
plt.xticks(x[::3], _xticks_lables[::3],
           rotation=45, fontproperties=my_font)

# 添加坐标轴描述信息
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度 单位(℃)', fontproperties=my_font)
plt.title('10点到11点每分钟的气温变化情况', fontproperties=my_font)
# 展示
plt.show()