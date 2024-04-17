from helper import *

with open("CO_Project_24/automatedTesting/tests/bin/simple/s_test1.txt","r") as f:
    txt = f.read().split("\n")

i = txt[4]

if type(i) == "add":
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

if type(i) == "sll" :
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


print("0b"+binary(pc),end=" ")
for i in registers.values():
    print("0b"+binary(i),end=" ")
print()