def solution():
    f = open("./input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n","").strip() for x in f]
    f = [x.split(",") for x in f]
    pairs = []
    for i in f:
        pair = [x.split("-") for x in i]
        pairs.append(pair)
    over = 0
    for i in pairs:
        first = i[0]
        second = i[1]
        firstString = set((range(int(first[0]),int(first[1])+1)))
        secondString = set((range(int(second[0]),int(second[1])+1)))
        if(firstString.union(secondString) == firstString or secondString.union(firstString) == secondString):
            over+=1

    print(over)
solution()