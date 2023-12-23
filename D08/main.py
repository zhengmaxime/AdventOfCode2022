input_example = """
30373
25512
65332
33549
35390
"""

import numpy as np

def scenic_score(grid, row, col):
    h = grid[row, col]
    # left
    y = col - 1
    left_score = 0
    while y >= 0:
        left_score += 1
        if h <= grid[row, y]:
            break
        y -= 1
    # right
    y = col + 1
    right_score = 0
    while y < grid.shape[1]:
        right_score += 1
        if h <= grid[row, y]:
            break
        y += 1
    # up
    x = row - 1
    up_score = 0
    while x >= 0:
        up_score += 1
        if h <= grid[x, col]:
            break
        x -= 1
    # down
    x = row + 1
    down_score = 0
    while x < grid.shape[0]:
        down_score += 1
        if h <= grid[x, col]:
            break
        x += 1

    return left_score * right_score * up_score * down_score    
    
    

def search_visible_tree(grid, grid_visible):
    for row in range(grid.shape[0]):
        max_h = -1
        for col in range(grid.shape[1]):
            val = grid[row, col]
            if val > max_h:
                max_h = val
                grid_visible[row, col] = 1

def main():
    with open('input') as f:
        s = f.readlines()

    grid = [list(map(int, list(line.strip()))) for line in s]
    grid = np.array(grid, dtype=np.uint8)
    grid_visible = np.zeros_like(grid, dtype=np.uint8)

    search_visible_tree(grid, grid_visible)
    search_visible_tree(grid[:, ::-1], grid_visible[:, ::-1])
    search_visible_tree(np.transpose(grid), np.transpose(grid_visible))
    search_visible_tree(np.transpose(grid)[:, ::-1], np.transpose(grid_visible)[:, ::-1])
    
    scenic_scores = np.zeros(grid.shape, dtype=int)
    for row, col in np.ndindex(grid.shape):
        if grid_visible[row, col]:
            score = scenic_score(grid, row, col)
            scenic_scores[row, col] = score

    return np.sum(grid_visible), np.max(scenic_scores)

if __name__ == "__main__":
    print(main())