"""
Program where all the data from the json files
will be extracted and stored in python for ease of access
"""

import json
# import pprint
import string
import os

# Absolute path of the current working directory
abs_path = os.path.split(os.getcwd())[0] + '/' + os.path.split(os.getcwd())[1] + '/'

validChars = set(string.ascii_letters + string.digits + "_")

opcodes = {
    "type-r" : {},
    "type-i" : {},
    "type-s" : {},
    "type-b" : {},
    "type-u" : {},
    "type-j" : {}
}

terms = {}
no_of_register = {}
immediate_values = {}
register_addr = {}
type_structure = {}


#Extracting data from them
with open(abs_path + "CO_Project_24/SimpleAssembler/ISA_Instructions.json") as f:
    temp = json.load(f)["opcode"]

    for i in temp:
        if i[2] == "r":     opcodes["type-r"][i[0]] = i[1]
        elif i[2] == "i":   opcodes["type-i"][i[0]] = i[1]
        elif i[2] == "s":   opcodes["type-s"][i[0]] = i[1]
        elif i[2] == "b":   opcodes["type-b"][i[0]] = i[1]
        elif i[2] == "u":   opcodes["type-u"][i[0]] = i[1]
        elif i[2] == "j":   opcodes["type-j"][i[0]] = i[1]

with open(abs_path + "CO_Project_24/SimpleAssembler/other_constants.json") as f:
    temp = json.load(f)
    terms = temp["terms"]
    no_of_register = temp["no_of_registers"]
    immediate_values = temp["immediate_values"]
    register_addr = temp["register_addr"]
    type_structure = temp["type_structure"]