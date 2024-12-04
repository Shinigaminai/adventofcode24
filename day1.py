import numpy as np

# read input
list1 = []
list2 = []
with open("day1.input.txt", "r") as f:
	while line := f.readline():
		nr1, nr2 = line.split()
		list1.append(int(nr1))
		list2.append(int(nr2))
print("input read")
print(f"length list1: {len(list1)}")
print(f"       list2: {len(list2)}")

# convert to numpy array and sort
sort1 = np.sort(np.array(list1))
sort2 = np.sort(np.array(list2))

# calculate distance
distances = np.absolute(np.subtract(sort1, sort2))
total_distance = np.sum(distances)
print(total_distance)
