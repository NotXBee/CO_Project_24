opcode = {
    "r_type" : "0110011"
}

'''
This first7 dictionary lists all the funct7 binary codes
for the operations in rtype
complete this one for all operations in rtype
'''
first7 = {
    "sub" : "0100000"
}

'''
Make this register address dictionary, you will understand by reading what I was doing.
Just complete this
'''
register_address = {     
        "zero" : "00000", # x0
        "ra" : "00001",   # x1
        "sp" : "00010",   # x2
        "gp" : "00011",   # x3
        "tp" : "00100",   # x4
        "t0" : "00101",   # x5
        "t1" : "00110",   # x6
        "t2" : "00111",   # x7
        "s0" : "01000",   # x8
        "fp" : "01000",   # x8
        "s1" : "01001",   # x9
        "" : "01010",
        "x11" : "01011",
        "x12" : "01100",
        "x13" : "01101",
        "x14" : "01110",
        "x15" : "01111",
        "x16" : "10000",
        "x17" : "10001",
        "x18" : "10010",
        "x19" : "10011",
        "x20" : "10100",
        "x21" : "10101",
        "x22" : "10110",
        "x23" : "10111",
        "x24" : "11000",
        "x25" : "11001",
        "x26" : "11010",
        "x27" : "11011",
        "x28" : "11100",
        "x29" : "11101",
        "x30" : "11110",
        "x31" : "11111"
}

def funct7(operation) :
    return first7[operation]

def rs(register) :
    pass