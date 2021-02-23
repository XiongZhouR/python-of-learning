from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文
# !本字体路径为本机一款字体路径,运行时可任意替换为系统中的一款中文字体路径,必须为中文字体,系统不限:Windows/macOS/Linux
my_font = font_manager.FontProperties(
    fname='/System/Library/Fonts/Hiragino Sans GB.ttc')

# 设置图片大小
plt.figure(figsize=(15, 5), dpi=80)

# 数据
x = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
d_16 = [15746, 312, 4497, 319]
d_15 = [12357, 156, 2045, 168]
d_14 = [2358, 399, 2358, 362]

# 设置坐标刻度使得可以将三个图画在一个表中
bar_width = 0.15  # 设置条形图宽度
x_14 = list(range(len(x)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width for i in x_15]

#改变坐标刻度使其显示电影名字
plt.xticks(x_15,x,fontproperties=my_font)

#添加坐标描述
plt.ylabel('票房',fontproperties=my_font)

# 画图
plt.bar(x_14, d_14, width=bar_width,label='9月14日')
plt.bar(x_15, d_15, width=bar_width,label='9月15日')
plt.bar(x_16, d_16, width=bar_width,label='9月16日')

#添加图例
plt.legend(prop=my_font,loc='best')

# 展示
plt.show()
