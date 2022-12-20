import csv


import csv

def read_clues_csv(clues_csv_filename):
    with open(clues_csv_filename, 'r') as f:
        reader = csv.reader(f)
        clues = list(reader)
    return clues[0]

def write_clues_csv(clues_list, clues_list_name):
    with open(clues_list_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(clues_list)

def space_clues(clues_list):
    print(clues_list)
    spaced_clues = []
    prev_num = 0
    for clue in clues_list:
        num = int(clue.split()[0])
        spaced_clues.extend(['']*(num-prev_num-1))
        prev_num = num
        spaced_clues.append(clue)
    return spaced_clues
        

def across(across_csv_name):
    across_csv = read_clues_csv(across_csv_name)
    spaced_clues_list = space_clues(across_csv)
    write_clues_csv(spaced_clues_list, 'spaced_across.csv')

def down(down_csv_name):
    down_csv = read_clues_csv(down_csv_name)
    spaced_clues_list = space_clues(down_csv)
    write_clues_csv(spaced_clues_list, 'spaced_down.csv')


if __name__ == '__main__':
    down('down.csv')