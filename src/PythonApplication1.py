import re

def TestSplitString():
    string = "test3-test2-test1"
    splitString = string.split("-")
    print(str(splitString.sort()))
# TestSplitString()

def Bin2Dec():
    binary = input("binary: ")
    decimal = 0
    for i in range(0,len(binary)):
        if int(binary[i]) != 0 and int(binary[i]) != 1:
            print("error nonbinary input")
            return
        else:
            print(str(decimal) + "+" + str(binary[i]) + "*" + str(2 ** (len(binary)-i-1)))
            decimal += int(binary[i]) * (2 ** (len(binary)-i-1))
    print(int(decimal))
# Bin2Dec()

def Base2Dec():
    base = input("base: ")
    if re.search(base,'\d'):
        print("error non supported base")
        return
    value = input("value: ")
    decimal = 0
    for i in range(0,len(value)):
        if int(base == 2) and int(value[i]) != 0 and int(value[i]) != 1:
            print("error nonbinary input")
            return
        else:
            print(str(decimal) + "+" + str(value[i]) + "*" + str(2 ** (len(value)-i-1)))
            decimal += int(value[i]) * (int(base) ** (len(value)-i-1))
    print(int(decimal))
Base2Dec()