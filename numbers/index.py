

# <class 'int'>

print(type(5))


# <class 'float'>

print(type(3.142))


print(5 + 2)        # 7
print(5 - 2)        # 3
print(5 * 2)        # 10
print(5 / 2)        # 2.5
print(5 // 5)       # 1
print(5 ** 5)       # 3125
print(10 % 3)       # 1
print(5 + 5 * 3)    # 20
print((5 + 5) * 3)  # 30

age = 25
age = age + 5
print(age)          # 30
age += 5
print(age)          # 35
age -= 5
print(age)          # 30
age /= 2
print(age)          # 15.0


wages = 1000
bills = 200
rent  = 500
food  = 200

savings = wages - bills - rent - food
print(savings)      # 100