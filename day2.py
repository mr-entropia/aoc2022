### Advent of Code 2022, Day 2
### mr-entropia

def i_win(plays):
    (opponent, player) = plays
    if(opponent == "A"):
        if(player == "Y"):
            return 6
        elif(player == "X"):
            return 3
        else:
            return 0
    elif(opponent == "B"):
        if(player == "Y"):
            return 3
        elif(player == "X"):
            return 0
        else:
            return 6
    else:
        if(player == "Y"):
            return 0
        elif(player == "X"):
            return 6
        else:
            return 3

def score(play):
    if(play == "X"):
        return 1
    elif(play == "Y"):
        return 2
    else:
        return 3

def change_play(plays):
    (opponent, play) = plays
    if(play == "X"):
        # need to lose
        if(opponent == "A"):
            return "Z"
        elif(opponent == "B"):
            return "X"
        else:
            return "Y"
    elif(play == "Y"):
        # need to draw
        if(opponent == "A"):
            return "X"
        elif(opponent == "B"):
            return "Y"
        else:
            return "Z"
    else:
        # need to win
        if(opponent == "A"):
            return "Y"
        elif(opponent == "B"):
            return "Z"
        else:
            return "X"

with open('day2.input') as f:
    lines = f.readlines()
 
total_score_p1 = 0
total_score_p2 = 0

for line in lines:
    (elf, me) = line.strip().split(" ")
    total_score_p1 += i_win((elf, me)) + score(me)
    me = change_play((elf, me))
    total_score_p2 += i_win((elf, me)) + score(me)

print("Total score (part 1):", total_score_p1)
print("Total score (part 2):", total_score_p2)