from time import perf_counter as pfc

def find_top_1(f):
    cur_elf_nb_calories = 0
    max_elf_nb_calories = 0

    for line in f:
        if line == "\n":
            max_elf_nb_calories = max(max_elf_nb_calories, cur_elf_nb_calories)
            cur_elf_nb_calories = 0
        else:
            cur_elf_nb_calories += int(line)

    return max_elf_nb_calories

def find_top_n(f, n):
    cur_elf_nb_calories = 0
    elf_nb_calories = []

    for line in f:
        if line == "\n":
            elf_nb_calories.append(cur_elf_nb_calories)
            cur_elf_nb_calories = 0
        else:
            cur_elf_nb_calories += int(line)

    elf_nb_calories.sort()
    return sum(elf_nb_calories[-n:])

def oneliners(n):
    list_ = [l for l in open('input', 'r').read().strip().split("\n\n")]
    calories_by_elf = [sum(map(int, elf_items.splitlines())) for elf_items in list_]
    return sum(sorted(calories_by_elf)[-n:])

def main():
    input_file = 'input'
    with open(input_file, 'r') as f:
        max_elf_nb_calories = find_top_n(f, 3)
    return max_elf_nb_calories

if __name__ == "__main__":
    start_t = pfc()
    res = oneliners(3)
    print(f"{res}, t={pfc() - start_t}")
    start_t = pfc()
    res = main()
    print(f"{res}, t={pfc() - start_t}")

