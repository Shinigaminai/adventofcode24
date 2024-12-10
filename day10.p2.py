from tqdm import tqdm

with open("day10.input.txt") as fin:
    grid = fin.read().splitlines()


def is_reachable(j, i, last_val: int) -> bool:
    if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[0]):
        return False
    new_val = int(grid[j][i])
    return new_val == last_val + 1


def reachable_peaks(j, i):
    cur_val = int(grid[j][i])
    peaks = 0
    if cur_val == 9:
        peaks += 1
    for dir in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        if is_reachable(j + dir[0], i + dir[1], cur_val):
            peaks += reachable_peaks(j + dir[0], i + dir[1])
    return peaks


def get_number_of_reachable_peaks(j, i) -> int:
    nr_of_peaks_reachable = reachable_peaks(j, i)
    # print(f"can reach {nr_of_peaks_reachable} from {j},{i}")
    return nr_of_peaks_reachable


total = 0
start_pos_amount = 0
for j, line in enumerate(tqdm(grid)):
    for i, x in enumerate(line):
        height = int(x)
        if height == 0:
            start_pos_amount += 1
            total += get_number_of_reachable_peaks(j, i)
print(f"evaluated {start_pos_amount} start positions")
print(total)
