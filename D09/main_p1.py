head_pos = 0, 0
prev_head_pos = 0, 0
tail_pos = 0, 0
tail_pos_list = []

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

f = open('input')
for line in f:
    d, n = line.split()
    n = int(n)
    for _ in range(n):
        tail_pos_list.append(tail_pos)
        prev_head_pos = head_pos
        head_pos = get_new_pos(head_pos, dirs[d])
        if no_touch(head_pos, tail_pos):
            tail_pos = prev_head_pos
print(len(set(tail_pos_list)))
