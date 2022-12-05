### Advent of Code 2022, Day 4
### mr-entropia

def fully_contains(input) -> bool:
    (left, right) = input.split(",")
    (left_min, left_max) = left.split("-")
    (right_min, right_max) = right.split("-")
    if(int(left_min) <= int(right_min) and int(left_max) >= int(right_max)):
        return True
    elif(int(right_min) <= int(left_min) and int(right_max) >= int(left_max)):
        return True
    else:
        return False

def overlapping(input) -> bool:
    (left, right) = input.split(",")
    (left_min, left_max) = left.split("-")
    (right_min, right_max) = right.split("-")
    if(int(left_min) == int(right_min) or int(left_max) == int(right_max)):
        return True
    if(int(left_max) < int(right_max) and int(left_max) > int(right_min)):
        return True
    if(int(right_max) < int(left_max) and int(right_max) > int(left_min)):
        return True
    if(int(left_max) < int(right_min) or int(right_max) < int(left_min)):
        return False
    return True

with open('day4.input') as f:
    lines = f.readlines()

    fullycont = 0
    overlap = 0

    for line in lines:
        if(fully_contains(line.strip())):
            fullycont += 1
        if(overlapping(line.strip())):
            overlap += 1

    print("Fully contained count:", fullycont)
    print("Overlapping count:", overlap)