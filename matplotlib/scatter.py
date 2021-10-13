from matplotlib import pyplot as plt
from matplotlib import font_manager
# 设置中文
# !本字体路径为本机一款字体路径,运行时可任意替换为系统中的一款中文字体路径,必须为中文字体,系统不限:Windows/macOS/Linux
my_font = font_manager.FontProperties(
    fname='C:\Windows\Fonts\STFANGSO.TTF')  
# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 数据
x_3 = range(1, 32)
x_10 = range(51, 82)
y_1 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18,
       21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]  # 3月份
y_2 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20,
       21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]  # 10月份

# 设置坐标刻度
_x = list(x_3)+list(x_10)  # 将两个横坐标转化为列表相加,列表的值刚好中间缺少值,形成和坐标点的对应
_xticks_ = ['3月{}日'.format(i) for i in range(1, 32)]
_xticks_ += ['10月{}日'.format(i) for i in range(1, 32)]
plt.xticks(_x[::3], _xticks_[::3], fontproperties=my_font,
           rotation=45)  # _xticks_和_x一一对应 坐标刻度太密集可以将列表取步长

# 设置坐标轴描述
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度(℃)", fontproperties=my_font)
plt.title("3月和10月温度比较图", fontproperties=my_font)


# 绘图
plt.scatter(x_3, y_1, label="3月", color='r')
plt.scatter(x_10, y_2, label="10月")

# ?添加图例 添加图例必须在画图之后!!!!!!
plt.legend(prop=my_font, loc='upper left')
# 展示
plt.show()