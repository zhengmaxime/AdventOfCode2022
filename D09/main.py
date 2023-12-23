head_pos = 0, 0
prev_head_pos = 0, 0
tail_pos = 0, 0
tail_pos_list = []

pos = [(0, 0)] * 10
prev_pos = [(0, 0)] * 10

dirs = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (1, 0),
    'D': (-1, 0),
}

def no_touch(head_pos, tail_pos):
    return abs(head_pos[0] - tail_pos[0]) > 1 or \
        abs(head_pos[1] - tail_pos[1]) > 1

def get_new_pos(pos, move):
    return pos[0] + move[0], pos[1] + move[1]

f = open('input2')
for line in f:
    d, n = line.split()
    n = int(n)
    for _ in range(n):
        tail_pos_list.append(pos[-1])
        prev_pos = pos[:]
        pos[0] = get_new_pos(pos[0], dirs[d])
        for i in range(1, 10):
            if no_touch(pos[i - 1], pos[i]):
                pos[i] = prev_pos[i - 1]
print(len(set(tail_pos_list)))

#5071 is too high
