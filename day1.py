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

# calculate similarity score
list2_counted = {}
for i in list2:
	if nr := list2_counted.get(i):
		list2_counted[i] = nr + 1
	else:
		list2_counted[i] = 1
counts = [list2_counted.get(i) * i for i in list1 if list2_counted.get(i) is not None]
similarity_score = np.nansum(counts)
print(similarity_score)
