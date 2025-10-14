num = int(input("Enter a number: "))


count = 1

for i in range(1, 11): # this will repeat 10 times
    result = num * i
    print(f"{num} x {i} = {result}")