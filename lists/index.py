str = "hello there dudes"

str2 = str.split(' ')

print(str2)

fib1 = [1,1,2,3,5,8,13]

print(fib1[2], fib1[5], fib1[-1], fib1[-3])

print(fib1[0:4])

fib2 = [21, 34, 55]

fib3 = fib1  + fib2

print(fib3)

fib1[0] = 100

print(fib1)

fib3.append(999)

print(fib3)

fib3.pop()

print(fib3)

fib3.remove(55)

print(fib3)

del(fib3[5])

print(fib3)


chars = ['mario', 'luigi', 'bowser']

chars.append(5)

print(chars)

nums = [chars, fib3, [1,2,3,4]]

print(nums)