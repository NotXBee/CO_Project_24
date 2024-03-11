import os
import pprint
import re
from utility import *

abs_path = os.path.split(os.getcwd())[0] + '/' + os.path.split(os.getcwd())[1] + '/'

with open(abs_path + "CO_Project_24/automatedTesting/tests/assembly/simpleBin/test2.txt") as f :
    # lines = f.readlines()
    lines = ['sltiu s5,a2,10']
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
            
            text = lines[pc].split(' ')
            
            if text[0] in r_type : 
                operation = text[0]
                regs = text[1].split(',')
                if len(regs) < 3 :
                    output = f'Missing comma in line {pc+1}\n'
                else :
                    for i in regs:
                        if i not in register_address:
                            output = f'Invalid register in line {pc+1}\n'
                            error = 1
                            break
                    if not error:
                        dest = regs[0]
                        reg1 = regs[1]
                        reg2 = regs[2]
                        output += funct7(operation)
                        output += rs(reg2)
                        output += rs(reg1)
                        output += funct3(operation)
                        output += rs(dest)
                        output += opcode["r_type"]
                        output += '\n'
                # print(output)

            elif text[0] in i_type :
                operation = text[0]
                if operation == "lw" :
                    addinfo = text[1].split(',')
                    if len(addinfo) < 2 :
                        output = f'Missing comma in line {pc+1}\n'
                    else:
                        temp = addinfo[1].split('(')
                        if len(temp) < 2 :
                            output = f'Missing starting bracket in line {pc+1}\n'
                        else:
                            addinfo[1] = temp[0]
                            if temp[1].rstrip(')') == temp[1] :
                                output = f'Missing ending bracket in line {pc+1}\n'
                            else:
                                addinfo.append(temp[1].rstrip(')'))
                                dest = addinfo[0]
                                imed = addinfo[1]
                                reg1 = addinfo[2]
                                if not imed.isdigit():
                                    output = f'Incorrect type immediate in line {pc+1}\n'
                                elif not crange(int(imed), 12) :
                                    output = f'Illegal Immediate in line {pc+1}\n'
                                else:
                                    imm = binary(int(imed), 12)
                                    output += imm
                                    output += rs(reg1)
                                    output += funct3(operation)
                                    output += rs(dest)
                                    output += opcode["lw"] + '\n'
                                    
                    print(output)
                
                else:
                    addinfo = text[1].split(',')
                    if len(addinfo) < 3 :
                        output = f'Missing comma in line {pc+1}\n'
                    else:
                        dest = addinfo[0]
                        reg1 = addinfo[1]
                        imed = addinfo[2]
                        if not imed.isdigit():
                            output = f'Incorrect type immediate i line {pc+1}\n'
                        elif not crange(int(imed), 12):
                            output = f'Illegal Immediate in line {pc+1}\n'
                        else:
                            imm = binary(int(imed), 12)
                            output += imm
                            output += rs(reg1)
                            output += funct3(operation)
                            output += rs(dest)
                            output += opcode[operation] + '\n'
                                
                    print(output)

            
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
                output = f'Invalid Instruction in line number {pc+1}\n'
        else:
            output = f'Line number {pc+1} is blank\n'

        pc += 1
    
    f.write(output)