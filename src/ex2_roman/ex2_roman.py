import math


def roman(number):
    if type(number) != int:
        raise TypeError('Number must be an integer')
    elif number < 4000:
        symbols = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
        symbols_10s = []
        for symbol in symbols.keys():
            if math.log10(symbol).is_integer():
                symbols_10s.append(symbol)
        temp = number
        roman_number = ''
        while temp > 0:
            for key, value in symbols.items():
                if temp - key >= 0:
                    roman_number += value
                    temp -= key
                    break
                else:
                    flag = False
                    for key_10s in symbols_10s:
                        if key_10s < temp and temp + key_10s - key >= 0:
                            roman_number += (symbols.get(key_10s) + value)
                            temp -= (key - key_10s)
                            flag = True
                            break
                    if flag:
                        break
        return roman_number
    else:
        raise ValueError('Number too big')
