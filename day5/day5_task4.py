def c_to_f(celsius):
    return(celsius * 9/5) + 32

def f_to_c(farenheit):
    return(farenheit - 32) * 5/9

temperature1 = c_to_f(30)
temperature2 = f_to_c(89)
print(temperature1)
print(temperature2)
