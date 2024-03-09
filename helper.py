def registeraddress(register):
    '''
    binary representation of the address the specified register.
    register:input string for the name(ABI) of the register.-1 in case of 
    an invalid register
    '''
    registers = {
                    'zero': '00000', 'ra': '00001', 'sp': '00010', 'gp': '00011',
                    'tp': '00100', 't0': '00101', 't1': '00110', 't2': '00111',
                    's0': '01000', 's1': '01001', 'a0': '01010', 'a1': '01011',
                    'a2': '01100', 'a3': '01101', 'a4': '01110', 'a5': '01111',
                    'a6': '10000', 'a7': '10001', 's2': '10010', 's3': '10011',
                    's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111',
                    's8': '11000', 's9': '11001', 's10': '11010', 's11': '11011',
                    't3': '11100', 't4': '11101', 't5': '11110', 't6': '11111'
                }

    if(register in registers.keys()):
        return registers[register]
    return -1
    
def instructiontype(instruction):
    '''
    Returns from {r,i,s,b,u,j} depending on the type of the instruction 
    If the instruction is not part of the ISA, the function returns -1
    '''
    type=   {
                'R': ["add", "sub", "sll", "slt", "sltu","xor","srl","or","and"],
                'I': ["lw","addi","sltiu","jalr"],
                'S': ["sw"],
                'B': ["beq","bne","blt","bge","bltu","bgeu"],
                'U': ["lui","auipc"],
                'J': ["jal"]
            } 
    
    for i in type.keys():
        if instruction in type[i]:
            return i
    return -1
