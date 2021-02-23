from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager


x = range(2, 26, 2)
y = [15, 14, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
# *设置图片大小
plt.figure(figsize=(15, 8), dpi=80)

# *绘图
plt.plot(x, y)

#*设置刻度
plt.xticks(x)

# *保存图片
# ?保存图片必须在 plot()之后,在 show()之前
# *plt.savefig(r"/Users/xiongzhou/Desktop/py-test/matplotlib/figure1.png")

# 展示图片
plt.show()
