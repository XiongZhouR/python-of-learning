# 版本 1 使用 if...else...结构
alien_color = 'green'
if alien_color == 'green':
    print("You get 5 points\n")
else:
    print('You get 10 points\n')

# 版本2 使用多个 if 语句
alien_color = 'yellow'
if alien_color == 'green':
    print('You get 5 points\n')
if alien_color != 'green':
    print('You get 10 points\n')

# 使用 if...elif...else....结构
alien_color = 'green'
if alien_color == 'green':
    print('You get 10 points\n')
elif alien_color == 'yellow':
    print('You get 10 points\n')
else:
    print('You get 15 points\n')

# 使用 if...elif...elif...结构
alien_color = 'yellow'
if alien_color == 'green':
    print('You get 10 points\n')
elif alien_color == 'yellow':
    print('You get 10 points\n')
elif alien_color == 'red':
    print('You get 15 points\n')

# 使用多个 if...语句
alien_color = 'red'
if alien_color == 'green':
    print('You get 10 points\n')
if alien_color == 'yellow':
    print('You get 10 points\n')
if alien_color == 'red':
    print('You get 15 points\n')