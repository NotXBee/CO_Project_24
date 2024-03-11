import sys
from utility import *

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f :
    lines = f.readlines()
    total_lines = len(lines)
    emptylines = []
    labels = {}
    labellines = []
    for i in range(len(lines)) :
        lines[i] = lines[i].lstrip()
        if lines[i] == '\n' :
            emptylines.append(i+1)
        lines[i] = lines[i].rstrip('\n')
        labeltemp = lines[i].split(': ')
        if len(labeltemp) == 2:
            labels[labeltemp[0]] = 4*i
            lines[i] = labeltemp[1]
        

with open(output_file, "w") as f :
    output = ""
    pc = 0
    
    while pc < total_lines :
        error = 0
        
        if pc+1 not in emptylines :
            
            text = lines[pc].split(' ')
            
            if text[0] in r_type : 
                operation = text[0]
                regs = text[1].split(',')
                if len(regs) != 3 :
                    print(f'Missing comma in line {pc+1}')
                    output = ''
                    break
                else :
                    for i in regs:
                        if i not in register_address:
                            print(f'Invalid register in line {pc+1}')
                            output = ''
                            error = 1
                            break
                    if error:
                        break
                    
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

            elif text[0] in i_type :
                operation = text[0]
                if operation == "lw" :
                    addinfo = text[1].split(',')
                    if len(addinfo) != 2 :
                        print(f'Missing comma in line {pc+1}')
                        output = ''
                        break
                    else:
                        temp = addinfo[1].split('(')
                        if len(temp) != 2 :
                            print(f'Missing starting bracket in line {pc+1}')
                            output = ''
                            break
                        else:
                            addinfo[1] = temp[0]
                            if temp[1].rstrip(')') == temp[1] :
                                print(f'Missing ending bracket in line {pc+1}')
                                output = ''
                                break
                            else:
                                addinfo.append(temp[1].rstrip(')'))
                                dest = addinfo[0]
                                imed = addinfo[1]
                                reg1 = addinfo[2]
                                if dest not in register_address or reg1 not in register_address:
                                    print(f'Invalid register in line {pc+1}')
                                    output = ''
                                    break
                                elif not imed.lstrip('-').isdigit():
                                    print(f'Incorrect type immediate in line {pc+1}')
                                    output = ''
                                    break
                                elif not crange(int(imed), 12) :
                                    print(f'Illegal Immediate in line {pc+1}')
                                    output = ''
                                    break
                                else:
                                    imm = binary(int(imed), 12)
                                    output += imm
                                    output += rs(reg1)
                                    output += funct3(operation)
                                    output += rs(dest)
                                    output += opcode["lw"] + '\n'
                                    
                elif operation == 'jalr':
                    addinfo = text[1].split(',')
                    if len(addinfo) != 3 :
                        print(f'Missing comma in line {pc+1}')
                        output = ''
                        break
                    else:
                        dest = addinfo[0]
                        reg1 = addinfo[1]
                        if dest not in register_address or reg1 not in register_address:
                            print(f'Invalid register in line {pc+1}')
                            output = ''
                            break
                        if addinfo[2] not in labels and not addinfo[2].lstrip('-').isdigit():
                            print(f'Invalid Label in line {pc+1}')
                            output = ''
                            break
                        elif addinfo[2] in labels:
                            imed = 4*pc - labels[addinfo[2]]
                        else :
                            if not crange(int(addinfo[2]), 12):
                                print(f'Illegal immediate in line {pc+1}')
                                output = ''
                                break
                            else:
                                imed = addinfo[2]
                        imm = binary(int(imed), 12)
                        output += imm
                        output += rs(reg1)
                        output += funct3(operation)
                        output += rs(dest)
                        output += opcode['jalr'] + '\n'


                else:
                    addinfo = text[1].split(',')
                    if len(addinfo) != 3 :
                        print(f'Missing comma in line {pc+1}')
                        output = ''
                        break
                    else:
                        dest = addinfo[0]
                        reg1 = addinfo[1]
                        imed = addinfo[2]
                        if not imed.lstrip('-').isdigit():
                            print(f'Incorrect type immediate in line {pc+1}')
                            output = ''
                            break
                        elif dest not in register_address or reg1 not in register_address:
                            print(f'Invalid register in line {pc+1}')
                            output = ''
                            break
                        elif not crange(int(imed), 12):
                            print(f'Illegal Immediate in line {pc+1}')
                            output = ''
                            break
                        else:
                            imm = binary(int(imed), 12)
                            output += imm
                            output += rs(reg1)
                            output += funct3(operation)
                            output += rs(dest)
                            output += opcode[operation] + '\n'

            
            elif text[0] in s_type :
                operation = text[0]
                addinfo = text[1].split(',')
                if len(addinfo) != 2 :
                    print(f'Missing comma in line {pc+1}')
                    output = ''
                    break
                else:
                    temp = addinfo[1].split('(')
                    if len(temp) != 2 :
                       print(f'Missing starting bracket in line {pc+1}')
                       output = ''
                       break
                    else:
                        addinfo[1] = temp[0]
                        if temp[1].rstrip(')') == temp[1] :
                            print(f'Missing ending bracket in line {pc+1}')
                            output = ''
                            break
                        else:
                            addinfo.append(temp[1].rstrip(')'))
                            reg2 = addinfo[0]
                            imed = addinfo[1]
                            reg1 = addinfo[2]
                            if not imed.lstrip('-').isdigit():
                                print(f'Incorrect type immediate in line {pc+1}')
                                output = ''
                                break
                            elif not crange(int(imed), 12) :
                                print(f'Illegal Immediate in line {pc+1}')
                                output = ''
                                break
                            elif dest not in register_address or reg1 not in register_address:
                                print(f'Invalid register in line {pc+1}')
                                output = ''
                                break
                            else:
                                imm = binary(int(imed), 12)
                                output += imm[0:7]
                                output += rs(reg2)
                                output += rs(reg1)
                                output += funct3(operation)
                                output += imm[7:]
                                output += opcode["s_type"] + '\n'
                                    
            
            elif text[0] in b_type : 
                addinfo = text[1].split(',')
                if len(addinfo) != 3 :
                    print(f'Missing comma in line {pc+1}')
                    output = ''
                    break
                else:
                    if addinfo[2] not in labels and not addinfo[2].lstrip('-').isdigit():
                        print(f'Invalid Label in line {pc+1}')
                        output = ''
                        break
                    elif addinfo[2] in labels:
                        imed = 4*pc - labels[addinfo[2]]
                    else :
                        if not crange(int(addinfo[2]), 12):
                            print(f'Illegal immediate in line {pc+1}')
                            output = ''
                            break
                        else:
                            imed = addinfo[2]
                    reg1 = addinfo[0]
                    reg2 = addinfo[1]
                    if reg1 not in register_address or reg2 not in register_address:
                            print(f'Invalid register in line {pc+1}')
                            output = ''
                            break
                    imm = binary(int(imed), 13)
                    output += imm[0] + imm[2:8]
                    output += rs(reg2)
                    output += rs(reg1)
                    output += funct3(operation)
                    output += imm[8:12] + imm[1]
                    output += opcode["b_type"]
                    output += '\n'

            elif text[0] in u_type :
                operation = text[0]
                addinfo = text[1].split(',')
                if len(addinfo) != 2 :
                    print(f'Missing comma in line {pc+1}')
                    output = ''
                    break
                else:
                    if addinfo[0] not in register_address :
                        print(f'Invalid register in line {pc+1}')
                        output = ''
                        break
                    elif not addinfo[1].lstrip('-').isdigit():
                        print(f'Invalid immmediate in line {pc+1}')
                        output = ''
                        break
                    elif not crange(int(addinfo[1]), 32):
                        print(f'Illegal immediate in line {pc+1}')
                        output = ''
                        break
                    else:
                        dest = addinfo[0]
                        imm = binary(int(addinfo[1]), 32)
                        output += imm[0:20]
                        output += rs(dest)
                        output += opcode[operation] + "\n"
            
            elif text[0] in j_type :
                operation = text[0]
                addinfo = text[1].split(',')
                if len(addinfo) != 2 :
                    print(f'Missing comma in line {pc+1}')
                    output = ''
                    break
                else:
                    if addinfo[0] not in register_address :
                        print(f'Invalid register in line {pc+1}')
                        output = ''
                        break
                    if addinfo[1] not in labels and not addinfo[1].lstrip('-').isdigit():
                        print(f'Invalid Label in line {pc+1}')
                        output = ''
                        break
                    elif addinfo[1] in labels:
                        imed = 4*pc - labels[addinfo[1]]
                    else :
                        if not crange(int(addinfo[1]), 21):
                            print(f'Illegal immediate in line {pc+1}')
                            output = ''
                            break
                        else:
                            imed = addinfo[1]
                    dest = addinfo[0]
                    imm = binary(int(imed), 21)
                    output += imm[0] + imm[10:20] + imm[9] + imm[1:9]
                    output += rs(dest)
                    output += opcode["j_type"] + "\n"

            else :
                print(f'Invalid Instruction in line number {pc+1}')
                output = ''
                break
            
        else:
            print(f'Line number {pc+1} is blank')
            output = ''
            break

        pc += 1
    
    output = output.rstrip('\n')
    f.write(output)