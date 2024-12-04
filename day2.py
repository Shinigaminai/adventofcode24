import numpy as np

def is_report_safe(levels: list[int]):
	dir = levels[0] - levels[1]
	for i in range(len(levels) - 1):
		diff = levels[i] - levels[i+1]
		dist = abs(diff)
		if dist < 1 or dist > 3:
			return 0
		same_dir = diff * dir
		if same_dir < 1:
			return 0
	return 1

# read input
safe_reports = 0
with open("day2.input.txt", "r") as f:
	while line := f.readline():
		levels = list(map(int, line.split()))
		safe = is_report_safe(levels)
		safe_reports += safe
		# print(f"{levels} -> {safe}")

# calculate distance
print(safe_reports)
