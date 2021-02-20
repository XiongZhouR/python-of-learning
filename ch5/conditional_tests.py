cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='subaru':
        print('The car is ',car,', I predict True')
    elif car=='audi':
        print('The car is ',car,', I predict False')
    else:
        print(car.title())

# 以下代码为测试一些常用的条件测试
print('\n')

#No1:检查两个数字是否相等
a=2
b=3
print(a==b)
print("\n")

#No2:使用函数 lower() 进行测试
car='Audi'
print(car.lower()=='audi')
print('\n')

#No3:检查两个数字是否相等,不等,大于,小于,大于等于,小于等于
a=3
b=4
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print()

#No4:使用关键字 and 和 or 进行测试
a=4
b=5
print(a>=4 and b<=5)
print(a>4 or b<=5)
print('\n')

#No5:测试特定的值是否包含在列表中
for car in cars:
    if car=='bmw' in cars:
        print(car.upper())
print('\n')

#No6:测试特定的值不包含在列表中
car='yiqi'
if car not in cars:
    print("The %s is not in cars" %car)