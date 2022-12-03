def solution():
    f = open("./input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n","").strip() for x in f]
    input = []
    elf = []
    for i in f:
        if(i == ""):
            input.append(elf)
            elf = []
        else:
            elf.append(int(i))
    input.append(elf)
    somas = [sum(x) for x in input]
    somas.sort()
    soma = 0
    for i in range(1,4):
        soma+= somas[-i]
    print(soma)
    #f = "".join(f)
    #print(f)
solution()