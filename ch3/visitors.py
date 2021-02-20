visitors = ['Jack', 'Bill', 'Bob']
#print(visitors[0] + ", welcome dinner with me")
#print(visitors[1] + ", welcome dinner with me")
#print(visitors[-1] + ", welcome dinner with me")
#print(visitors[-1] + " can't have dinner with me")
visitors[-1] = 'Curry'
print("I have a new big table")
visitors.insert(0, 'Jhon')
visitors.append('Jordan')
print(visitors[0] + ", welcome dinner with me")
print(visitors[1] + ", welcome dinner with me")
print(visitors[2] + ", welcome dinner with me")
print(visitors[3] + ", welcome dinner with me")
print(visitors[-1] + ", welcome dinner with me")
print("I just can invite two friends have dinner with me")
sorry1 = visitors.pop(0)
print("sorry " + sorry1 + ", I can't have dinner with you")
sorry2 = visitors.pop(0)
print("sorry " + sorry2 + ", I can't have dinner with you")
sorry3 = visitors.pop(0)
print("sorry " + sorry3 + ", I can't have dinner with you")
print("\n" + visitors[0] + ", you stay have dinner with me")
print("\n" + visitors[1] + ", you stay have dinner with me")
del visitors[0]
del visitors[0]
print("\n")
print(visitors)

print("\nDinner End")
