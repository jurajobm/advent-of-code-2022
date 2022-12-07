FILE_NAME = 'calories.txt'

def data_loader(file_name:str) -> list[str]:
    # Take data from file
    with open(file_name, "r") as f:
        input = f.readlines()
    return input

def input_sum(input:list[str]) -> list[int]:
    # Take strings, retype them into integers and calculate sum
    elves = []
    elf_tmp = []
    for line in input:
        if line != '\n':
            elf_tmp += [int(line)]
        else:
            elves += [sum(elf_tmp)]
            elf_tmp = []
    elves += [sum(elf_tmp)]
    return elves

def task_part_one(elves):
    max_calories = max(elves)
    return max_calories

def task_part_two(elves):
    top_three_carrier = sorted(elves, reverse=True)
    carrier_sum = sum(top_three_carrier[:3])
    return carrier_sum


if __name__ == "__main__":
    calories = data_loader(FILE_NAME)
    elves = input_sum(calories)
    print(task_part_one(elves))
    print(task_part_two(elves))


