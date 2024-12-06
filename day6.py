from collections import namedtuple
import numpy as np

input_map = []
Position = namedtuple("PositionYX", "y x")

with open("day6.input.txt", "r") as f:
    while line := f.readline():
        row = list(line.strip())
        input_map.append(row)
input_map = np.array(input_map)
print(input_map)
print(f"recieved map of size {input_map.size}")

obstacles = []
guard_pos = None
for iy, ix in np.ndindex(input_map.shape):
    if input_map[iy][ix] == "#":
        obstacles.append(Position(iy, ix))
    elif input_map[iy][ix] in ("<", "^", ">", "v"):
        guard_pos = Position(iy, ix)
print(f"guard at {guard_pos}, dir: {input_map[guard_pos]}")
print(f"found {len(obstacles)} obstacles")


def on_map(guard_pos: Position, map_size) -> bool:
    for dim in range(len(guard_pos)):
        if guard_pos[dim] >= map_size[dim]:
            return False
        if guard_pos[dim] < 0:
            return False
    return True


def move(guard_pos: Position, direction: Position) -> Position:
    new_pos = Position(guard_pos.y + direction.y, guard_pos.x + direction.x)
    # print(f"{guard_pos} + {direction} -> {new_pos}")
    return new_pos


def rotate_direction(direction: Position) -> Position:
    new_y = direction.x * 1
    new_x = direction.y * -1
    return Position(new_y, new_x)


def get_direction(guard_char) -> Position:
    if guard_char == "<":
        return Position(0, -1)
    elif guard_char == ">":
        return Position(0, 1)
    elif guard_char == "v":
        return Position(1, 0)
    return Position(-1, 0)  # y, x


map_size = (len(input_map[0]), len(input_map))
direction = get_direction(input_map[guard_pos])
input_map[guard_pos] = "X"
while on_map(guard_pos, map_size):
    next_pos = move(guard_pos, direction)
    if not on_map(next_pos, map_size):
        break
    if input_map[next_pos] == "#":
        direction = rotate_direction(direction)
    else:
        guard_pos = next_pos
        input_map[guard_pos] = "X"

print(input_map)
print(np.count_nonzero(input_map == "X"))
