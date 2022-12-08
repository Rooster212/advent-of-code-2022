
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

    highest_scenic_score = int(0)

    # Count the number of visible trees in the interior of the grid
    for row in range(height):
        for col in range(width):
            tree_visible, scenic_score = process_tree(grid, (row, col))
            if (tree_visible):
                num_visible_trees += 1
            if (scenic_score > highest_scenic_score):
                highest_scenic_score = scenic_score

    return num_visible_trees, highest_scenic_score


def process_tree(trees_grid, key: tuple):
    row = key[0]
    col = key[1]
    tree_height = trees_grid[row][col]

    row_count = len(trees_grid)
    col_count = len(trees_grid[0])

    # Edge trees
    # Always visible, and scenic score is 0
    if (row == 0) or (col == 0) or (row == row_count-1) or (row == row_count-1):
        return (True, 0)

    # look left
    left_visible = True
    left_view_dist = 0
    for c in range(col-1, -1, -1):
        left_view_dist += 1
        if trees_grid[row][c] >= tree_height:
            left_visible = False
            break

    # look right
    right_visible = True
    right_view_dist = 0
    for c in range(col+1, col_count):
        right_view_dist += 1
        if trees_grid[row][c] >= tree_height:
            right_visible = False
            break

    up_visible = True
    up_view_dist = 0
    for r in range(row-1, -1, -1):
        up_view_dist += 1
        if trees_grid[r][col] >= tree_height:
            up_visible = False
            break

    down_visible = True
    down_view_dist = 0
    for r in range(row+1, row_count):
        down_view_dist += 1
        if trees_grid[r][col] >= tree_height:
            down_visible = False
            break

    visible = (left_visible or right_visible or up_visible or down_visible)
    scenic_score = left_view_dist * right_view_dist * up_view_dist * down_view_dist

    return (visible, scenic_score)


def main():
    with open("input.txt") as f:
        visible_tree_count, highest_scenic_score = find_visible_trees_count(f)
        print("Visible trees: " + str(visible_tree_count))
        print("Highest scenic score: " + str(highest_scenic_score))


if __name__ == '__main__':
    main()
