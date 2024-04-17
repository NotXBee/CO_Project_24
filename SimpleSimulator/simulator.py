from helper import *

with open("automatedTesting/tests/bin/simple/s_test1.txt","r") as f:
    txt = f.read().split("\n")

with open("automatedTesting/tests/user_traces/s_test1.txt","w") as f:
    output = ""
    while True:
        i = txt[pc//4]

        # R type
        if type(i) == "add": # verified
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs2] + registers[rs1]
            pc+=4

        if type(i) == "sub" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs1] - registers[rs2]
            pc += 4

        if type(i) == "sll" : # verified
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            temp = registers[rs2] % 32
            registers[rd] = registers[rd]*(2**temp)
            pc += 4

        if type(i) == "slt" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            if registers[rs1] < registers[rs2] :
                registers[rd] = 1
            pc += 4

        if type(i) == "sltu" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            if (unsigned(registers[rs1]) < unsigned(registers[rs2])) :
                registers[rd] = 1
            pc += 4

        if type(i) == "xor" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs1] ^ registers[rs2]
            pc += 4

        if type(i) == "srl" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            temp = registers[rs2] % 32
            registers[rd] = registers[rd]/(2**temp)
            pc += 4

        if type(i) == "or" :
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs1] | registers[rs2]
            pc += 4

        if type(i) == "and" : # verified
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            rd = i[-12:-7]
            registers[rd] = registers[rs1] & registers[rs2]
            pc += 4


        # B type
        if type(i) == "beq":
            imm = i[-32]+i[-8]+i[-31:-25]+i[-12:-8]
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if registers[rs1] == registers[rs2]:
                pc += int(imm)*2
            else:
                pc += 4

        if type(i) == "bne":  # verified
            imm = i[-32]+i[-8]+i[-31:-25]+i[-12:-8]
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if registers[rs1] != registers[rs2]:
                pc += int(imm)*2
            else:
                pc += 4

        if type(i) == "bge":  
            imm = i[-32]+i[-8]+i[-31:-25]+i[-12:-8]
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if registers[rs1] >= registers[rs2]:
                pc += int(imm)*2
            else:
                pc += 4

        if type(i) == "bgeu":
            imm = i[-32]+i[-8]+i[-31:-25]+i[-12:-8]
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if unsigned(registers[rs1]) >= unsigned(registers[rs2]):
                pc += int(imm)*2
            else:
                pc += 4

        if type(i) == "blt":
            imm = i[-32]+i[-8]+i[-31:-25]+i[-12:-8]
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if registers[rs1] < registers[rs2]:
                pc += int(imm)*2
            else:
                pc += 4
                
        if type(i) == "bltu":
            imm = i[-32]+i[-8]+i[-31:-25]+i[-12:-8]
            rs2 = i[-25:-20]
            rs1 = i[-20:-15]
            if unsigned(registers[rs1]) < unsigned(registers[rs2]):
                pc += int(imm)*2
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
            imm = twos_complement(i[-32] + i[-22:-12] + i[-23] + i[-31:-23] + 0)
            registers[rd] = pc + 4
            pc += imm
            pc *= 2

        # I type

        if type(i) == "lw": #verified
            
            pc+=4
            rs1 = i[-20:-15]
            imm = twos_complement(i[-32:-20])
            rd = i[-12:-7]
            temp = "0x" + hexadecimal(registers[rs1] + (imm))
            registers[rd] = memory[temp]

        if type(i) == "addi":   #verified
            pc+=4
            rs = i[-20:-15]
            imm = twos_complement(i[-32:-20])
            rd = i[-12:-7]
            registers[rd] = registers[rs] + imm

        if type(i) == "sltiu":  #no test case found to verify
            pc+=4
            rs = i[-20:-15]
            imm = twos_complement(i[-32:-20])
            rd = i[-12:-7]
            if(registers[rs] < imm):
                registers[rd] = 1

        if type(i) == "jalr":   #partially verified, rd updationyet to be verified
            pc+=4
            rs = i[-20:-15]
            imm = twos_complement(i[-32:-20])
            rd = i[-12:-7]

            registers[rd] = pc
            pc = registers[rs] + imm
            pc = pc * 2

        # U type

        if type(i) == "auipc":  #verified
            imm = twos_complement(i[-32:-12])
            rd = i[-12:-7]

            registers[rd] = pc + imm * 2**12
            pc += 4

        if type(i) == "lui":    #verified
            imm = twos_complement(i[-32:-12])
            rd = i[-12:-7]

            registers[rd] = imm * 2**12
            pc += 4

        print("0b"+binary(pc),end=" ")
        for j in registers.values():
            print("0b"+binary(j),end=" ")
        print()
        if i == "00000000000000000000000001100011":
            break
        if pc == 0:
            break
