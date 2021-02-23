from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文显示
# !本字体路径为本机一款字体路径,运行时可任意替换为系统中的一款中文字体路径,必须为中文字体,系统不限:Windows/macOS/Linux
my_font = font_manager.FontProperties(
    fname='/System/Library/Fonts/Hiragino Sans GB.ttc')

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 数据
x = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归",
     "生化危机6：终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

y = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28,
     11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]

# 坐标刻度
#todo: plt.xticks(range(len(x)),x,fontproperties=my_font,rotation=45)
plt.yticks(range(len(x)), x, fontproperties=my_font, rotation=45)

# 坐标描述
#todo: plt.xlabel('单位：亿元',fontproperties=my_font)
plt.xlabel('单位：亿元', fontproperties=my_font)
plt.title('电影票房', fontproperties=my_font, loc='center')

# 网格
plt.grid(alpha=0.5)

# 画图
#todo: plt.bar(range(len(x)),y,width=0.3,color='orange')
plt.barh(range(len(x)), y, height=0.3, color='orange')  # 绘制横着的条形图

# 展示
plt.show()
