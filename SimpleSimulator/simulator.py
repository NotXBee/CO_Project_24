import sys
from helper import *

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f:
    txt = f.read().split("\n")

with open(output_file,"w") as f:
    output = ""
    while True:
        
        i = txt[pc//4]

        # R type
        if type(i) == "add": # verified
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs2] + registers[rs1] if (rd!='00000') else 0
            pc+=4

        if type(i) == "sub" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs1] - registers[rs2] if (rd!='00000') else 0
            pc += 4

        if type(i) == "sll" : # verified
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            temp = registers[rs2] % 32
            registers[rd] = registers[rd]*(2**temp) if (rd!='00000') else 0
            pc += 4

        if type(i) == "slt" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            if registers[rs1] < registers[rs2] :
                registers[rd] = 1 if (rd!='00000') else 0
            pc += 4

        if type(i) == "sltu" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            if (unsigned(registers[rs1]) < unsigned(registers[rs2])) :
                registers[rd] = 1 if (rd!='00000') else 0
            pc += 4

        if type(i) == "xor" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs1] ^ registers[rs2] if (rd!='00000') else 0
            pc += 4

        if type(i) == "srl" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            temp = registers[rs2] % 32
            registers[rd] = registers[rd]//(2**temp) if (rd!='00000') else 0
            pc += 4

        if type(i) == "or" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs1] | registers[rs2] if (rd!='00000') else 0
            pc += 4

        if type(i) == "and" : # verified
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs1] & registers[rs2] if (rd!='00000') else 0
            pc += 4


        # B type
        if type(i) == "beq":
            imm = twos_complement(i[-32]+i[-8]+i[-31:-25]+i[-12:-8]+"0")
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if registers[rs1] == registers[rs2]:
                pc += imm
            else:
                pc += 4

        if type(i) == "bne":  # verified
            imm = twos_complement(i[-32]+i[-8]+i[-31:-25]+i[-12:-8]+"0")
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if registers[rs1] != registers[rs2]:
                pc += imm
            else:
                pc += 4

        if type(i) == "bge":  
            imm = twos_complement(i[-32]+i[-8]+i[-31:-25]+i[-12:-8]+"0")
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if registers[rs1] >= registers[rs2]:
                pc += imm
            else:
                pc += 4

        if type(i) == "bgeu":
            imm = imm = twos_complement(i[-32]+i[-8]+i[-31:-25]+i[-12:-8]+"0")
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if unsigned(registers[rs1]) >= unsigned(registers[rs2]):
                pc += imm
            else:
                pc += 4

        if type(i) == "blt":
            imm = twos_complement(i[-32]+i[-8]+i[-31:-25]+i[-12:-8]+"0")
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if registers[rs1] < registers[rs2]:
                pc += imm
            else:
                pc += 4
                
        if type(i) == "bltu":
            imm = twos_complement(i[-32]+i[-8]+i[-31:-25]+i[-12:-8]+"0")
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if unsigned(registers[rs1]) < unsigned(registers[rs2]):
                pc += imm
            else:
                pc += 4


        #S type
        if type(i) == "s_type":
            
            imm = twos_complement(i[-32:-25]+i[-12:-7])
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            temp = registers[rs1] + binaryToDecimal(int(imm))
            memory["0x"+hexadecimal(temp)] = registers[rs2]
            pc += 4


        # J type
        if type(i) == "j_type" :
            rd = i[-12:-7]
            imm = twos_complement(i[-32] + i[-20:-12] + i[-21] + i[-31:-21] + "0")
            registers[rd] = pc + 4 if (rd!='00000') else 0
            pc += imm   
            pc -= pc%2

        # I type

        if type(i) == "lw": #verified
            
            pc+=4
            rs1 = i[-20:-15]
            imm = twos_complement(i[-32:-20])
            rd = i[-12:-7]
            temp = "0x" + hexadecimal(registers[rs1] + (imm))
            registers[rd] = memory[temp] if (rd!='00000') else 0

        if type(i) == "addi":   #verified
            pc+=4
            rs = i[-20:-15]
            imm = twos_complement(i[-32:-20])
            rd = i[-12:-7]
            registers[rd] = registers[rs] + imm if (rd!='00000') else 0

        if type(i) == "sltiu":  #no test case found to verify
            pc+=4
            rs = i[-20:-15]
            imm = twos_complement(i[-32:-20])
            rd = i[-12:-7]
            if(registers[rs] < imm):
                registers[rd] = 1 if (rd!='00000') else 0

        if type(i) == "jalr":   #partially verified, rd updationyet to be verified
            pc+=4
            rs = i[-20:-15]
            imm = twos_complement(i[-32:-20])
            rd = i[-12:-7]
            
            registers[rd] = pc if (rd!='00000') else 0
            pc = registers[rs] + imm
            pc -= pc%2

        # U type

        if type(i) == "auipc":  #verified
            imm = twos_complement(i[-32:-12])
            rd = i[-12:-7]

            registers[rd] = pc + imm * 2**12 if (rd!='00000') else 0
            pc += 4

        if type(i) == "lui":    #verified
            imm = twos_complement(i[-32:-12])
            rd = i[-12:-7]

            registers[rd] = imm * 2**12 if (rd!='00000') else 0
            pc += 4

        
        # Bonus
        if type(i) == "mul" :
            rd = i[-12:-7]
            rs1 = i[-20:-15]
            rs2 = i[-25:-20]
            registers[rd] = registers[rs1] * registers[rs2] if (rd!='00000') else 0
            pc += 4
        
        if type(i) == "rst" :
            pass
            # left for piyush
        
        if type(i) == "halt" :
            break

        if type(i) == "rvrs" :
            rd = i[-12:-7]
            rs = i[-20:-15]
            t1 = binary(registers[rs])
            t1 = t1[::-1]
            t1 = twos_complement(t1)
            registers[rd] = t1 if (rd!='00000') else 0
            pc += 4


        registers['00000'] = 0
        output += "0b"+binary(pc) + " "
        for j in registers.values():
            output += "0b"+binary(j) + " "
        output += "\n"
        if i == "00000000000000000000000001100011":
            break
        if pc == 0:
            break
    for i,j in memory.items():
        output += f"{i.lower()}:0b{binary(j)}" + "\n"
    
    f.write(output)