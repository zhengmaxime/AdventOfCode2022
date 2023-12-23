import argparse

class Node:
    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent: Node = parent
        self.children: dict[str: Node] = dict()

    def is_dir(self):
        return len(self.children) > 0

    def update_size(self):
        self.size = 0
        for child in self.children.values():
            self.size += child.size

    def get_child(self, name):
        return self.children.get(name)

    def add_child(self, name, size=0):
        if self.get_child(name) is None:
            self.children[name] = Node(name, size, self)
        return self.get_child(name)


root_node = Node('/', 0)

n_line = 1

    
def parse_cmd(node: Node):
    global n_line
    if n_line >= len(lines) - 1:
        return

    line = lines[n_line]
    n_line += 1

    if line.startswith('$ cd'):
        dir = line.split()[2]
        if dir == "..":
            node.update_size()
            parse_cmd(node.parent)
        else:
            child = node.add_child(dir)
            parse_cmd(child)

    elif line.startswith('$ ls'):
        line = lines[n_line]
        while not line.startswith('$'):
            tokens = line.split()
            if tokens[0] == "dir":
                dir = tokens[1]
                node.add_child(dir)
            else:
                size, filename = int(tokens[0]), tokens[1]
                node.add_child(filename, size)
            n_line += 1
            if n_line == len(lines):
                break
            line = lines[n_line]
        parse_cmd(node)
        node.update_size()
    
def pretty_print_tree(node: Node, prefix='- '):
    if node is None:
        return

    if node.is_dir():
        print(f"{prefix}{node.name} (dir, size={node.size})")
    else:
        print(f"{prefix}{node.name} (file, size={node.size})")

    if node.is_dir():
        for child in node.children.values():
            pretty_print_tree(child, '  ' + prefix)

def traversal(node: Node, res: list[int], needed_space):
    if node is None:
        return
    
    if node.is_dir():
        if 0 < node.size - needed_space < res[1] - needed_space:
            res[1] = node.size
        if node.size <= 100_000:
            res[0] += node.size
        for child in node.children.values():
            traversal(child, res, needed_space)


def process(input_file, print_tree):
    file_ = open(input_file, 'r')
    global lines
    lines = file_.readlines()
    file_.close()

    parse_cmd(root_node)

    if print_tree:
        pretty_print_tree(root_node)
    print(f"Total size: {root_node.size}")

    total_space = 70_000_000
    update_size = 30_000_000
    unused_space = total_space - root_node.size
    needed_space = update_size - unused_space
    print(f"Needed space: {needed_space}")

    res = [0, total_space]
    traversal(root_node, res, needed_space)
    small_dirs_sum, smallest_dir_to_delete = res
    return small_dirs_sum, smallest_dir_to_delete


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-f', '--filename', default='D07/input')
    args_parser.add_argument('-p', '--print', action='store_true')
    args = args_parser.parse_args()
    res = process(args.filename, args.print)
    print(res)

if __name__ == "__main__":
    main()