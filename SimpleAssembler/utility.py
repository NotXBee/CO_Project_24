'''
This first7 dictionary lists all the funct7 binary codes
for the operations in rtype
complete this one for all operations in rtype
'''
first7 = {
    "add" : "0000000",
    "sub" : "0100000",
    "sll" : "0000000",
    "slt" : "0000000",
    "sltu": "0000000",
    "xor" : "0000000",
    "srl" : "0000000",
    "or"  : "0000000",
    "and" : "0000000",
}

'''
Make this register address dictionary, you will understand by reading what I was doing.
Just complete this
'''
register_address = {     
       
                    'zero': '00000','ra':'00001', 
                    'sp': '00010', 'gp': '00011',
                    'tp': '00100', 't0': '00101', 
                    't1': '00110', 't2': '00111',
                    's0': '01000', 'fp': '01000',
                    's1': '01001', 'a0': '01010',
                    'a1': '01011', 'a2': '01100', 
                    'a3': '01101', 'a4': '01110',
                    'a5': '01111', 'a6': '10000',
                    'a7': '10001', 's2': '10010', 
                    's3': '10011', 's4': '10100', 
                    's5': '10101', 's6': '10110', 
                    's7': '10111', 's8': '11000', 
                    's9': '11001', 's10': '11010', 
                    's11': '11011', 't3': '11100', 
                    't4': '11101', 't5': '11110', 
                    't6': '11111'
                   }

def funct7(operation) :
    return first7[operation]

def rs(register) :
