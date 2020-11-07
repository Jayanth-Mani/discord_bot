def k_to_f(kelvins):
    fahrenheit = (kelvins - 273.15)*1.8000 + 32.00
    return fahrenheit

def f_to_k(fahrenheit):
    kelvins = (fahrenheit - 32) / 1.8 + 273.15 
    return kelvins

def f_to_c(fahrenheit):
    celcius = 5/9 * (fahrenheit - 32)
    return celcius

def c_to_f(celcius):
    fahrenheit = 9/5 * celcius + 32
    return fahrenheit

def c_to_k(celcius):
    kelvins = celcius + 273.15
    return kelvins

def k_to_c(kelvins):
    celcius = kelvins - 273.15
    return celcius
