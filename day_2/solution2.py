def solution():
    f = open("./input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n","").strip() for x in f]
    plays = {"A":"C",
        "B": "A",
        "C":"B"}
    plays2 = {"A":"B",
        "B": "C",
        "C":"A"}
    scores = {
        "A":1,
        "B":2,
        "C":3,
        "Y": 3,
        "X": 0,
        "Z": 6
    }
    translatedPlays = {
        "X":"A",
        "Y":"B",
        "Z": "C"
    }
    score =0
    for i in f:
        score+= scores[i[2]]
        if(i[2]=="Y"):
            score += scores[i[0]]
        elif(i[2]=="X"):
            score += scores[plays[i[0]]]
        else:
            score += scores[plays2[i[0]]]
    print(score)


solution()