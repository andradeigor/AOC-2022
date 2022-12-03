def solution():
    f = open("./input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n","").strip() for x in f]
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    equals = []
    current = []
    done = False
    for i in f:
        current = []
        for j in range(len(i)//2):
            if(done): 
                done=False
                continue
            letter = i[j]
            for k in range(len(i)//2):
                if(letter == i[(len(i)//2)+k]):
                    if(letter not in current):
                        equals.append(letter)
                        current.append(letter)
                        done=True
                        break
    soma = 0
    for i in range(len(equals)):
        for j in range(len(alphabet)):
            if(equals[i]==alphabet[j]):
                soma+=j+1
    print(soma)
    
        


solution()