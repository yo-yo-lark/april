"""
    Program to convert Celsius To Fahrenheit
"""
def celsius_to_fahrenheit(celsius):
    """ convert value given to fahrenheit"""
    fah = celsius * 9/5 + 32
    return fah

def fahrenheit_to_celsius(fahrenheit):
    celsius = fahrenheit - 32
    return celsius


celsius = 25
fah = celsius_to_fahrenheit(celsius)
print(f"{celsius} degress is {fah} Fahrenheit")

celsius = fahrenheit_to_celsius(fah)
print(f"{fah} degrees Fahrenheit is {celsius} celsius")
