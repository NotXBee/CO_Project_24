with open("automatedTesting\\tests\\bin\\simple\\s_test1.txt","r") as f:
    txt = f.read().split("\n")

i = txt[0]

opcode_dict = {"0110011" : "r_type", 
               "1100011" : "b_type", 
               "0100011" : "s_type", 
               "1101111" : "j_type", 
               "0000011" : "lw", 
               "0010011" : "addi/sltiu", 
               "1100111" : "jalr", 
               "0110111" : "lui", 
               "0010111" : "auipc"}

def binary(int, no_of_bits= 32) :
    if int >= 0 :
        return format(int, f'0{no_of_bits}b')
    
    return format((1 << no_of_bits) + int, f'0{no_of_bits}b')

registers = {
    "00000" : 0b00000000000000000000000000000000,
	"00001" : 0b00000000000000000000000000000000,
	"00010" : 0b00000000000000000000000100000000,
	"00011" : 0b00000000000000000000000000000000,
	"00100" : 0b00000000000000000000000000000000,
	"00101" : 0b00000000000000000000000000000000,
	"00110" : 0b00000000000000000000000000000000,
	"00111" : 0b00000000000000000000000000000000,
	"01000" : 0b00000000000000000000000000000000,
	"01001" : 0b00000000000000000000000000000000,
	"01010" : 0b00000000000000000000000000000000,
	"01011" : 0b00000000000000000000000000000000,
	"01100" : 0b00000000000000000000000000000000,
	"01101" : 0b00000000000000000000000000000000,
	"01110" : 0b00000000000000000000000000000000,
	"01111" : 0b00000000000000000000000000000000,
	"10000" : 0b00000000000000000000000000000000,
	"10001" : 0b00000000000000000000000000000000,
	"10010" : 0b00000000000000000000000000000000,
	"10011" : 0b00000000000000000000000000000000,
	"10100" : 0b00000000000000000000000000000000,
	"10101" : 0b00000000000000000000000000000000,
	"10110" : 0b00000000000000000000000000000000,
	"10111" : 0b00000000000000000000000000000000,
	"11000" : 0b00000000000000000000000000000000,
	"11001" : 0b00000000000000000000000000000000,
	"11010" : 0b00000000000000000000000000000000,
	"11011" : 0b00000000000000000000000000000000,
	"11100" : 0b00000000000000000000000000000000,
	"11101" : 0b00000000000000000000000000000000,
	"11110" : 0b00000000000000000000000000000000,
	"11111" : 0b00000000000000000000000000000000    
}

pc = 0b00000000000000000000000000000000

def opcode(i):
    global opcode_dict
    opcode3 = i[-7:]
    return opcode_dict[opcode3]

def r_type(i):
    fun7 = i[-32:-25]
    fun3 = i[-15:-12]
    if fun3 == "000":
        if fun7 == "0000000":
            return "add"
        if fun7 == "0100000":
            return "sub"
    if fun3 == "001":
        return "sll"
    if fun3 == "010":
        return "slt"
    if fun3 == "011":
        return "sltu"
    if fun3 == "100":
        return "xor"
    if fun3 == "101":
        return "srl"
    if fun3 == "110":
        return "or"
    if fun3 == "111":
        return "and"

def b_type(i):
    fun3 = i[-15:-12]
    if fun3 == "000":
        return "beq"
    if fun3 == "001":
        return "bne"
    if fun3 == "100":
        return "blt"
    if fun3 == "101":
        return "bge"
    if fun3 == "110":
        return "bltu"
    if fun3 == "111":
        return "bgeu"
    
def s_type(i):
    fun3 = i[-15:-12]
    if fun3 == "010":
        return "sw"

def j_type(i):
    return "jal"

def lw(i):
    fun3 = i[-15:-12]
    if fun3 == "010":
        return "lw"
def addi_sltiu(i):
    fun3 = i[-15:-12]
    if fun3 == "000":
        return "addi"
    if fun3 == "011":
        return "sltiu"

def jalr(i):
    fun3 = i[-15:-12]
    if fun3 == "000":
        return "jalr"
def lui(i):
    return "lui"

def auipc(i):
    return "auipc"


def type(i):
    
    type =  opcode(i)
    if type == "r_type":
        return r_type(i)
    if type == "b_type":
        return b_type(i)
    if type == "s_type":
        return s_type(i)
    if type == "j_type":
        return j_type(i)
    if type == "lw":
        return lw(i)
    if type == "addi/sltiu":
        return addi_sltiu(i)
    if type == "jalr":
        return jalr(i)
    if type == "lui":
        return lui(i)
    if type == "auipc":
        return auipc(i)

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
