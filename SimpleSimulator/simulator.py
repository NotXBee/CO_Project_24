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
