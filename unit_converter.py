# Unit Converter
#
#   handles temp, currency, volume, mass, etc
#   for now, it rounds to 3rd decimal #
#
#   to-do list:
#     [X] temp:
#       [X] celsius -> fahrenheit
#       [X] fahrenheit -> Celsius
#       [X] Fahrenheit -> Kelvin
#       [X] Kelvin -> Fahrenheit
#       [X] Celsius -> Kelvin
#       [X] Kelvin -> Celsius
#     [] mass:
#       [X] lb -> kg
#       [X] kg -> lb

def tempconv(u_in, u_out, value):
    u_in = u_in.lower()
    u_out = u_out.lower()
    
    if u_in == 'c' and u_out == 'f':
        value_conv = value * 1.8 + 32
        u_in = 'C'
        u_out = 'F'
    
    elif u_in == 'f'and u_out == 'c':
        value_conv = (value - 32) / 1.8
        u_in = 'F'
        u_out = 'C'
    
    elif u_in == 'c' and u_out == 'k':
        value_conv = value + 273.15
        u_in = 'C'
        u_out = 'K'
        
    elif u_in == 'k' and u_out == 'c':
        value_conv = value - 273.15
        u_in = 'K'
        u_out = 'C'

    elif u_in == 'f' and u_out == 'k':
        value_conv = ((value - 32) / 1.8) + 273.15
        u_in = 'F'
        u_out = 'K'
        
    elif u_in == 'k' and u_out == 'f':
        value_conv = (value - 273.15) * 1.8 + 32        
        u_in = 'K'
        u_out = 'F'
        
    else:
        return ("Not valid input/output conversion values")
    
    return str(value) + " " + u_in + " --> " + str(round(value_conv, 3)) + " " + u_out


def massconv(u_in, u_out, value):

    if u_in == 'kg' and u_out == 'lb':
        value_conv = value * 2.2046

    elif u_in == 'pounds' or 'lb' in u_in and u_out == 'kilograms' or 'kg' in u_out:
        value_conv = value / 2.2046

    return round(value_conv, 3)


print (massconv('lb', 'kg', 12345))

