import numpy as np

def validate_difference(difference: int, direction: int) -> int:
	dist = abs(difference)
	if dist < 1 or dist > 3:
		return 0
	same_dir = difference * direction
	if same_dir < 1:
		return 0
	return 1

def is_report_safe(levels: list[int], dampen: int = 0) -> bool:
	differences = [levels[i-1] - levels[i] for i in range(1, len(levels))]
	direction = differences[0]
	for i, difference in enumerate(differences):
		if validate_difference(difference, direction):
			continue
		if dampen > 0:
			for j in range(len(levels)):
				new_levels = levels.copy()
				new_levels.pop(j)
				if is_report_safe(new_levels, dampen-1):
					print(f"dampened {levels[j]} in {levels} => {new_levels}")
					return 1
		return 0
	return 1

# read input
safe_reports = 0
nr_reports = 0
with open("day2.input.txt", "r") as f:
	while line := f.readline():
		nr_reports += 1
		levels = list(map(int, line.split()))
		if safe := is_report_safe(levels, dampen=1):
			safe_reports += 1
			# print(f"{levels} -> {safe}")
print(f"read {nr_reports} reports")
print(safe_reports)
