from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager
# 设置中文显示
my_font = font_manager.FontProperties(
    fname='/System/Library/Fonts/Hiragino Sans GB.ttc')

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 生成数据
x = range(11, 31)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 绘图
# color:颜色 十六进制 linestyle:线条风格 linewidth:线条宽度 alpha:透明度
plt.plot(x, y_1, color='m', linestyle='--', linewidth=2, alpha=0.5, label='自己')
plt.plot(x, y_2, color='b', linestyle='-.', linewidth=2, alpha=0.5, label='同桌')

# 设置坐标刻度
_xticks_ = ['{}岁'.format(i) for i in x]
plt.xticks(x, _xticks_, fontproperties=my_font)
plt.yticks(range(0,9))

# 设置图例:plot 中添加 label 参数 legend:图例 prop:指定中文字体 loc:指定图例在图的位置,默认右上角
plt.legend(prop=my_font, loc='best')

# 设置坐标轴描述
plt.xlabel('岁数', fontproperties=my_font)
plt.ylabel('个数', fontproperties=my_font)
plt.title('11岁到30岁每年交男朋友的数量走势', fontproperties=my_font)

#绘制网格
plt.grid(alpha=0.5)

# 展示图片
plt.show()
