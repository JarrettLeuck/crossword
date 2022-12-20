import csv


# Checks if crossword square is a clue start
def should_be_numbered(r, c, grid):
    if (r == 0 or c == 0) and grid[r][c] != 'x':
        return True
    elif (grid[r-1][c] == 'x' or grid[r][c-1] == 'x') and grid[r][c] != 'x':
        return True
    else:
        return False


def number_grid(grid):
    grid_width = len(grid[0])
    numbered_grid = []
    cur_num = 1

    for row in range(len(grid)):
        numbered_grid.append(['']*grid_width)
        for col in range(len(grid[0])):
            if should_be_numbered(row, col, grid):
                numbered_grid[row][col] = cur_num
                cur_num += 1
    
    return numbered_grid


def save_grid_csv(grid, grid_name):
    with open(grid_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(grid)

def save_reference_csv(reference_list, reference_list_name):
    with open(reference_list_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(reference_list)

def read_grid(grid_name):
    with open(grid_name, 'r') as f:
        reader = csv.reader(f)
        grid = list(reader)
    
    return grid


def get_column_letter(num):
    A = 65
    carry = num // 26
    letter = num % 26 + A
    col_str = ''

    if carry > 0:
        col_str += chr(A + carry - 1)
    return col_str + chr(letter)

def map_number_to_cell(numbered_grid):
    coord_list = []
    for row in range(len(numbered_grid)):
        for col in range(len(numbered_grid[0])):
            if numbered_grid[row][col]:
                coord_list.append(f'{get_column_letter(col)}{row+1}')

    return coord_list


def main():
    grid = read_grid('basic_grid.csv')
    print(grid)
    numbered_grid = number_grid(grid)
    save_grid_csv(numbered_grid, 'numbered_grid.csv')


def main_2():
    numbered_grid = read_grid('numbered_grid.csv')
    coord_list = map_number_to_cell(numbered_grid)
    print(coord_list)
    save_reference_csv(coord_list, 'coord_ref.csv')


if __name__ == '__main__':
    main_2()




