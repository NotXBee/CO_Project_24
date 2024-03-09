import os
import pprint
import re
from utility import *

abs_path = os.path.split(os.getcwd())[0] + '/' + os.path.split(os.getcwd())[1] + '/'

with open(abs_path + "CO_Project_24/automatedTesting/tests/assembly/simpleBin/test1.txt") as f :
    lines = f.readlines()
    lines = [i for i in lines if i != '\n'] # removing empty lines

with open(abs_path + "CO_Project_24/automatedTesting/tests/assembly/user_bin_s/output1.txt", "w") as f :
    output = ""
    for i in lines :

        text = re.split("\s|,|\n", i)
    
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

        if text[0] in b_type :
            operation = text[0]
            reg1 = text[1]
            reg2 = text[2]
            imm = format(int(text[3]), '013b')
            output += imm[0] + imm[2:8]
            output += rs(reg2)
            output += rs(reg1)
            output += funct3(operation)
            output += imm[8:12] + imm[1]
            output += opcode["b_type"]
            output += '\n'
            
        
            


        





