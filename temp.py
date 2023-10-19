"""
    Program to convert Celsius To Fahrenheit
"""
def celsius_to_fahrenheit(celsius):
    """ convert value given to fahrenheit"""
    fah = celsius * 9/5 + 32
    return fah


celsius = 25
fah = celsius_to_fahrenheit(celsius)
print(f"{celsius} degress is {fah} Fahrenheit")
