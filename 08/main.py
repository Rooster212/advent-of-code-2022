
def find_visible_trees_count(input_lines):
    # Parse the input and create a grid of trees
    grid = []
    for line in input_lines:
        if not line.strip():
            break
        input_line = str(line).removesuffix('\n')

        row = []
        for c in input_line:
            row.append(int(c))
        grid.append(row)

    num_visible_trees = 0

    # Count the number of trees along the edge of the grid
    height = len(grid)
    width = len(grid[0])

    # Width - 2 to avoid double counting corner trees
    num_visible_trees += (height * 2) + ((width - 2) * 2)

    # Count the number of visible trees in the interior of the grid
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            if (process_tree(grid, (row, col))):
                num_visible_trees += 1
    return num_visible_trees


def process_tree(trees_grid, key: tuple):
    row = key[0]
    col = key[1]
    tree_height = trees_grid[row][col]

    row_count = len(trees_grid)
    col_count = len(trees_grid[0])

    # look left
    left_visible = True
    for c in range(col-1, -1, -1):
        if trees_grid[row][c] >= tree_height:
            left_visible = False
            break

    # look right
    right_visible = True
    for c in range(col+1, col_count):
        if trees_grid[row][c] >= tree_height:
            right_visible = False
            break

    up_visible = True
    for r in range(row-1, -1, -1):
        if trees_grid[r][col] >= tree_height:
            up_visible = False
            break

    down_visible = True
    for r in range(row+1, row_count):
        if trees_grid[r][col] >= tree_height:
            down_visible = False
            break

    visible = (left_visible or right_visible or up_visible or down_visible)
    return visible


def main():
    with open("input.txt") as f:
        print(find_visible_trees_count(f))


if __name__ == '__main__':
    main()
