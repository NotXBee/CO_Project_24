def binary(int, no_of_bits) :
    if int >= 0 :
        return format(int, f'0{no_of_bits}b')
    
    return format((1 << no_of_bits) + int, f'0{no_of_bits}b')


x1 = 0b00000000000000000000000000000100
print('0b' + binary(x1, 32))
