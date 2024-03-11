import os
import pprint
import re
from utility import *

abs_path = os.path.split(os.getcwd())[0] + '/' + os.path.split(os.getcwd())[1] + '/'

with open(abs_path + "CO_Project_24/automatedTesting/tests/assembly/simpleBin/test2.txt") as f :
    lines = f.readlines()
    total_lines = len(lines)
    emptylines = []
    for i in range(len(lines)) :
        if lines[i] == '\n' :
            emptylines.append(i+1)

with open(abs_path + "CO_Project_24/automatedTesting/tests/assembly/user_bin_s/output2.txt", "w") as f :
    output = ""
    pc = 0
    
    while pc < total_lines :
        error = 0
        
        if pc+1 not in emptylines :
            
            text = re.split("\(|\)|\s|,|\n", lines[pc])
            
            if text[0] in r_type : 
                operation = text[0]
                dest = text[1]
                reg1 = text[2]
                reg2 = text[3]
                output += funct7(operation)
                output += rs(reg2)
                output += rs(reg1)
                output += funct3(operation)
                output += rs(dest)
                output += opcode["r_type"]
                output += '\n'

            elif text[0] in i_type :
                if text[0] == "lw" :
                    operation = text[0]
                    dest = text[1]
                    imm = binary(int(text[2]), 12)
                    reg1 = text[3]
                    output += imm
                    output += rs(reg1)
                    output += funct3(operation)
                    output += rs(dest)
                    output += opcode["lw"] + '\n'
                
                elif text[0] == "addi" :
                    operation = text[0]
                    dest = text[1]
                    imm = binary(int(text[3]), 12)
                    reg1 = text[2]
                    output += imm
                    output += rs(reg1)
                    output += funct3(operation)
                    output += rs(dest)
                    output += opcode["addi"] + '\n'
                
                elif text[0] == "sltiu" :
                    operation = text[0]
                    dest = text[1]
                    imm = binary(int(text[3]), 12)
                    reg1 = text[2]
                    output += imm
                    output += rs(reg1)
                    output += funct3(operation)
                    output += rs(dest)
                    output += opcode["sltiu"] + '\n'
                
                elif text[0] == "jalr" : # Note that this instruction has reg1 as x6 fixed. Please check this out while caring for errors
                    operation = text[0]
                    dest = text[1]
                    imm = binary(int(text[3]), 12)
                    reg1 = text[2]
                    output += imm
                    output += rs(reg1)
                    output += funct3(operation)
                    output += rs(dest)
                    output += opcode["jalr"] + '\n'
            
            elif text[0] in s_type :
                operation = text[0]
                reg2 = text[1]
                imm = binary(int(text[2]), 12)
                reg1 = text[3]
                output += imm[0:7]
                output += rs(reg2)
                output += rs(reg1)
                output += funct3(operation)
                output += imm[7:]
                output += opcode["s_type"] + '\n'
            
            elif text[0] in b_type : # Please ask the TA how the immediate part is parsed. I am still not sure I am doing it the right way although the output is correct.
                operation = text[0]
                reg1 = text[1]
                reg2 = text[2]
                imm = binary(int(text[3]), 13)
                output += imm[0] + imm[2:8]
                output += rs(reg2)
                output += rs(reg1)
                output += funct3(operation)
                output += imm[8:12] + imm[1]
                output += opcode["b_type"]
                output += '\n'

            elif text[0] in u_type :
                operation = text[0]
                dest = text[1]
                imm = binary(int(text[2]), 32)
                output += imm[0:20]
                output += rs(dest)
                output += opcode[operation] + "\n"
            
            elif text[0] in j_type :
                operation = text[0]
                dest = text[1]
                imm = binary(int(text[2]), 21)
                output += imm[0] + imm[10:20] + imm[9] + imm[1:9]
                output += rs(dest)
                output += opcode["j_type"] + "\n"

            else :
                output = f'Instruction out of range in line number {pc+1}'
        else:
            output = f'Line number {pc+1} is blank'

        pc += 1
    
    f.write(output)