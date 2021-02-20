from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 14, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 设置图片大小
plt.figure(figsize=(15, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 展示图片
plt.show()
