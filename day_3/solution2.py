def solution():
    f = open("./input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n","").strip() for x in f]
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    equals = []
    current = []
    done = False
    j =0
    letters = []
    for i in range(len(f)):
        if((i+1)%3 ==0):
            equals.append(f[j:i+1])
            j = i+1
    for i in range(len(equals)):
        current = equals[i]
        for j in range(len(current[0])):
            if(current[0][j] in current[1] and current[0][j] in current[2]):
                letters.append(current[0][j])
                break
    soma=0
    for i in range(len(letters)):
        for j in range(len(alphabet)):
            if(letters[i]==alphabet[j]):
                soma+=j+1
    print(soma)

    
        


solution()