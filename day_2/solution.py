def solution():
    f = open("./input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n","").strip() for x in f]
    plays = {"A":"Y",
        "B": "Z",
        "C":"X"}
    scores = {
        "A":1,
        "B":2,
        "C":3,
        "Y": 2,
        "X": 1,
        "Z": 3
    }
    translatedPlays = {
        "X":"A",
        "Y":"B",
        "Z": "C"
    }
    score =0
    for i in f:
        if(i[2] == plays[i[0]]):
            score+=6
        elif(translatedPlays[i[2]] == i[0]):
            score+=3
        score+= scores[i[2]]
    print(score)


solution()