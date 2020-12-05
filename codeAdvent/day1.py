#!/usr/bin/python3

# read in input

def getNums(filename):
    count = 0
    l = []
    with open("input_day1.txt") as fp:
        Lines = fp.readlines()
        for line in Lines:
            count += 1
            if not line == "\n":
                l.append(int(line.strip()))
    return l

def process2(goal, l):
    endOfList = len(l)
    for i in range(0, endOfList):
        for j in range(i+1, endOfList):
            mySum = l[i] + l[j]
            if mySum == goal:
                return i, j

def process3(goal, l):
    endOfList = len(l)
    for i in range(0, endOfList):
        for j in range(i+1, endOfList):
            for k in range (j+1, endOfList):
                mySum = l[i] + l[j] + l[k]
                if mySum == goal:
                    return i, j, k

def run():
    goal = 2020
    l = getNums("input_day1.txt")

    a,b = process2(goal, l)
    print(l[a], l[b], l[a] * l[b])

    a,b,c  = process3(goal, l)
    print(l[a], l[b], l[c], l[a] * l[b]*l[c])

if __name__ == "__main__":
    run()
