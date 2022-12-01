### Advent of Code 2022, Day 1
### mr-entropia
 
with open('day1.input') as f:
    lines = f.readlines()
 
curr_elf_energy = 0
best_elves = [0, 0, 0]
 
for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == "":
        if curr_elf_energy > best_elves[0]:
            best_elves[2] = best_elves[1]
            best_elves[1] = best_elves[0]
            best_elves[0] = curr_elf_energy
        elif curr_elf_energy > best_elves[1]:
            best_elves[2] = best_elves[1]
            best_elves[1] = curr_elf_energy
        elif curr_elf_energy > best_elves[2]:
            best_elves[2] = curr_elf_energy
        curr_elf_energy = 0
    else:
        curr_elf_energy += int(line)
 
print("Part one:")
print(" * Best elf:", best_elves[0])
print("\nPart two:")
print(" * Energy carried by top three elves:", str(best_elves[0] + best_elves[1] + best_elves[2]))