#!/usr/bin/python3

# read in input

def getInput(filename):
    count = 0
    l = []
    with open(filename) as fp:
        Lines = fp.readlines()
        for line in Lines:
            if not line == "\n":
                l.append((line.strip()))
    return l

def policyTwo(line):

    retval = False
    firstIndex = int(line[0].split('-')[0])
    secondIndex = int(line[0].split('-')[1])
    checkChar = line[1].split(':')[0]
    checkVal = line[2]

    if (checkVal[firstIndex-1] == checkChar) or (checkVal[secondIndex-1] == checkChar):
        retval = True
        if (checkVal[firstIndex-1] == checkChar) and (checkVal[secondIndex-1] == checkChar):
            retval = False
    return retval

def policyOne(line):
    if line == "":
        return False
    retval = True
    minNum = int(line[0].split('-')[0])
    maxNum = int(line[0].split('-')[1])
    checkChar = line[1].split(':')[0]
    checkVal = line[2]
    charCount = checkVal.count(checkChar)
    if charCount < minNum or charCount > maxNum:
        retval = False
    return retval

def process(l):
    count = 0
    for item in l:
        if policyTwo(item.split()):
            count += 1
    return count

def run():
    l = getInput("input_day2.txt")
    print(process(l))

if __name__ == "__main__":
    run()
