from helper import *

with open("automatedTesting\\tests\\bin\\simple\\s_test1.txt","r") as f:
    txt = f.read().split("\n")

i = txt[0]

if type(i) == "add":
    rs2 = i[-25:-20]
    rs1 = i[-20:-15]
    rd = i[-12:-7]
    registers[rd] = registers[rs2] + registers[rs1]
    pc+=4
print("0b"+binary(pc),end=" ")
for i in registers.values():
    print("0b"+binary(i),end=" ")
print()

if type(i) == "lw":
    pc+=4
    rs1 = i[-20:-15]
    imm = twos_complement(i[-32:-20])
    rd = i[-12:-7]
    registers[rd] = memory[rs1 + imm]

if type(i) == "addi":
    pc+=4
    rs = i[-20:-15]
    imm = twos_complement(i[-32:-20])
    rd = i[-12:-7]
    registers[rd] = registers[rs] + imm

if type(i) == "sltiu":
    pc+=4
    rs = i[-20:-15]
    imm = twos_complement(i[-32:-20])
    rd = i[-12:-7]
    if(registers[rs] < imm):
        registers[rd] = 1

if type(i) == "jalr":
    pc+=4
    rs = i[-20:-15]
    imm = twos_complement(i[-32:-20])
    rd = i[-12:-7]

    registers[rd] = pc
    pc = registers[rs] + imm
    if (pc%2):
        pc -= 1