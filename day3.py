### Advent of Code 2022, Day 3
### mr-entropia

def divide_in_half(input) -> tuple:
    return (input[:int(len(input) / 2)], input[int(len(input) / 2):])

def find_similarity(input) -> str:
    (left, right) = input
    for i in range(0, len(left)):
        for j in range(0, len(right)):
            if(left[i] == right[j]):
                return left[i]
    return None

def find_similarity_2(input) -> str:
    (left, middle, right) = input
    for i in range(0, len(left)):
        for j in range(0, len(middle)):
            for k in range(0, len(right)):
                if(left[i] == middle[j] and middle[j] == right[k]):
                    return left[i]
    return None

def get_priority(input) -> int:
    prio = int(ord(input.swapcase()) - 64)
    if(prio > 26):
        return prio - 6
    else:
        return prio

with open('day3.input') as f:
    lines = f.readlines()

    prio_sum_1 = 0
    for line in lines:
        prio_sum_1 += get_priority(find_similarity(divide_in_half(line)))
    print("Part 1:", prio_sum_1)

    prio_sum_2 = 0
    for i in range(0, len(lines), 3):
        prio_sum_2 += get_priority(find_similarity_2((lines[i], lines[i + 1], lines[i + 2])))
    print("Part 2:", prio_sum_2)