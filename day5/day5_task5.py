def even_or_odd(num):
    for num in range(1, 11):
        if num % 2:
            return "The number is odd number"
        else:
            return "The number is even number"
    

print(even_or_odd)