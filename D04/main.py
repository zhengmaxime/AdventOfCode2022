INPUT_FILE = 'input'

def read_line(s):
    e1, e2 = s.split(',')
    s_inf1, s_sup1 = e1.split('-')
    s_inf2, s_sup2 = e2.split('-')
    inf1, sup1, inf2, sup2 = int(s_inf1), int(s_sup1), int(s_inf2), int(s_sup2)
    """ 
    Part 1
    return inf1 >= inf2 and sup1 <= sup2 or \
        inf2 >= inf1 and sup2 <= sup1:
    """
    return inf2 <= sup1 <= sup2 or \
        inf1 <= sup2 <= sup1


def read_file():
    with open(INPUT_FILE, 'r') as f:
        return sum(map(read_line, f))


def main():
    return read_file()


if __name__ == "__main__":
    res = main()
    print(res)
