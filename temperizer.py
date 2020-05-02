"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c




def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_f = (temperature_c * 1.8) + 32
    return temperature_f


## CREATE THE ADDITIONAL FUNCTIONS BELOW


# convert_c_to_k
def convert_c_to_k(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_k = (temperature_c +273.15)
    return temperature_k


# convert_f_to_k
def convert_f_to_k(temperature_f):
    """Convert Celsius to Fahrenheit."""
    temperature_k = (temperature_f - 32) * (5/9) + 273.15
    return temperature_k


# convert_k_to_c
def convert_k_to_c(temperature_k):
    """Convert Celsius to Fahrenheit."""
    temperature_c = (temperature_k - 273.15)
    return temperature_c


# convert_k_to_f
def convert_k_to_f(temperature_k):
    """Convert Celsius to Fahrenheit."""
    temperature_f = (temperature_k - 273.15) * (9/5) + 32
    return temperature_f



## LEVEL UP

# convert_f_to_all
def convert_f_to_all(temperature_f):
    temperature_k = (temperature_f - 32) * (5/9) + 273.15
    temperature_c = (temperature_f - 32) * (5/9)
    print(f'The temperature {temperature_f} F is: \n {round(temperature_c,2)} in C \n {round(temperature_k,2)} in K')