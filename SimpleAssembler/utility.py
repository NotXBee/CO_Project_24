opcode = {
    "r_type" : "0110011",
    "b_type" : "1100011",
    "s_type" : "0100011",
    "j_type" : "1101111",
    "lw"     : "0000011",
    "addi"   : "0010011",
    "sltiu"  : "0010011",
    "jalr"   : "1100111",
    "lui"    : "0110111",
    "auipc"  : "0010111"
        
}

r_type = [
    "add",
    "sub",
    "sll",
    "slt",
    "sltu",
    "xor",
    "srl",
    "or",
    "and"
]

b_type = [
    "beq",
    "bne",
    "blt",
    "bge",
    "bltu",
    "bgeu"
]

i_type = [
    "lw",
    "addi",
    "sltiu",
    "jalr"
]

s_type = [
    "sw"
]

u_type = [
    "lui",
    "auipc"
]

j_type = [
    "jal"
]

f7 = {
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

f3 = {
    "add" : "000",
    "sub" : "000",
    "sll" : "001",
    "slt" : "010",
    "sltu": "011",
    "xor" : "100",
    "srl" : "101",
    "or"  : "110",
    "and" : "111",
    "beq" : "000",
    "bne" : "001",
    "blt" : "100",
    "bge" : "101",
    "bltu": "110",
    "bgeu": "111",
    "lw"  : "010",
    "addi": "000",
    "sltiu":"011",
    "jalr": "000",
    "sw"  : "010",
    
}


register_address = {     
       
        'zero': '00000',
        'ra':'00001',   
        'sp': '00010', 
        'gp': '00011',
        'tp': '00100', 
        't0': '00101', 
        't1': '00110', 
        't2': '00111',
        's0': '01000', 
        'fp': '01000',
        's1': '01001', 
        'a0': '01010',
        'a1': '01011', 
        'a2': '01100', 
        'a3': '01101', 
        'a4': '01110',
        'a5': '01111', 
        'a6': '10000',
        'a7': '10001', 
        's2': '10010', 
        's3': '10011', 
        's4': '10100', 
        's5': '10101', 
        's6': '10110', 
        's7': '10111', 
        's8': '11000', 
        's9': '11001', 
        's10': '11010', 
        's11': '11011', 
        't3': '11100', 
        't4': '11101', 
        't5': '11110', 
        't6': '11111'
}

def funct7(operation) :
    return f7[operation]

def funct3(operation) :
    return f3[operation]

def rs(register) :
    return register_address[register]
