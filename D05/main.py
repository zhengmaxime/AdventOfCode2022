INPUT_FILE = 'input'

M = [[]]

# Part 1
def move_lifo(nb, src, dst):
    for _ in range(nb):
        crate = M[src].pop(0)
        M[dst].insert(0, crate)

# Part 2
def move_fifo(nb, src, dst):
    crates = M[src][:nb]
    del M[src][:nb]
    M[dst] = crates + M[dst]


def read_file():
    f = open(INPUT_FILE, 'r')
    lines = f.readlines()
    f.close()

    nb_stacks = len(lines[0]) // 4
    for _ in range(nb_stacks):
        M.append([])

    for n_line, l in enumerate(lines):
        if l.startswith(" 1"):
            break

        for i in range(0, len(l), 4):
            c = l[i + 1]
            if c != ' ':
                M[(i // 4) + 1].append(c)

    n_line += 2 # Skip line with indexes and blank line

    while n_line < len(lines):
        l = lines[n_line]
        tokens = l.split()
        nb, src, dst = int(tokens[1]), int(tokens[3]), int(tokens[5])
        move_fifo(nb, src, dst)
        n_line += 1

    res = []
    M.pop(0)
    for i in range(len(M)):
        res.append(M[i][0])
    return "".join(res)

def main():
    return read_file()


if __name__ == "__main__":
    res = main()
    # print(M)
    print(res)
