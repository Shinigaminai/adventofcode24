from collections import namedtuple
from typing import Optional
import numpy as np

input_map = []
Position = namedtuple("PositionYX", "y x")

with open("day6.input.txt", "r") as f:
    while line := f.readline():
        row = list(line.strip())
        input_map.append(row)
input_map = np.array(input_map)
print(input_map)
print(f"recieved map of shape {input_map.shape}")

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


def get_direction_int(direction: Position) -> int:
    if direction.y == 0:
        if direction.x == -1:
            return 0
        return 1
    if direction.y == -1:
        return 2
    return 3


def patrol_guard(
    input_map: np.ndarray, guard_pos, direction
) -> Optional[list[list[chr]]]:
    map_size = (len(input_map[0]), len(input_map))
    max_steps = input_map.size
    walk_dir_map = np.zeros((*input_map.shape, 4))
    step_count = 0
    input_map[guard_pos] = "X"
    while on_map(guard_pos, map_size):
        next_pos = move(guard_pos, direction)
        if not on_map(next_pos, map_size):
            break
        if input_map[next_pos] == "#":
            # print("rotate")
            direction = rotate_direction(direction)
            walk_dir = get_direction_int(direction)
            if walk_dir_map[guard_pos.y, guard_pos.x, walk_dir]:
                print("obstacle found")
                return None
            walk_dir = get_direction_int(direction)
            walk_dir_map[guard_pos.y, guard_pos.x, walk_dir] = 1
        else:
            guard_pos = next_pos
            input_map[guard_pos] = "X"
            walk_dir = get_direction_int(direction)
            walk_dir_map[guard_pos.y, guard_pos.x, walk_dir] = 1
        if step_count >= max_steps:
            print("max step interrupt")
            return None
        step_count += 1
    return input_map


# print(input_map)
direction = get_direction(input_map[guard_pos])
# part 1
guard_patrol = patrol_guard(input_map.copy(), guard_pos, direction)
print(guard_patrol)
res_p1 = np.count_nonzero(guard_patrol == "X")
print(f"part1: {res_p1}")

# part 2
possible_obstacle_positions = np.vstack(np.where(guard_patrol == "X")).T
index = np.where((possible_obstacle_positions == guard_pos).all(axis=1))
possible_obstacle_positions = np.delete(possible_obstacle_positions, index, axis=0)
loop_positions = 0
for p_o in possible_obstacle_positions:
    pos = Position(*p_o)
    assert guard_patrol[pos.y][pos.x] == "X"
    assert input_map[pos.y][pos.x] == "."
    map_with_obstacle = input_map.copy()
    map_with_obstacle[pos.y, pos.x] = "#"
    if patrol_guard(map_with_obstacle, guard_pos, direction) is None:
        loop_positions += 1
print(f"part2: {loop_positions}")
