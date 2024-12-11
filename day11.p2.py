from tqdm import tqdm

test_str = "125 17"
input_str = "475449 2599064 213 0 2 65 5755 51149"
stones = list(map(int, input_str.strip().split()))
print(f"input: {stones}")


def recursive_blink(stone: int, steps: int) -> int:
    if steps <= 0:
        return 1
    if res := memory.get((stone, steps)):
        # print(f"{(stone, steps)} -> {res}")
        return res
    res = 0
    if stone == 0:
        res = recursive_blink(2024, steps - 2)
    elif stone == 1:
        res = recursive_blink(2024, steps - 1)
    else:
        stone_str = str(stone)
        length = len(stone_str)
        if length % 2 == 0:
            half_length = int(length / 2)
            left_stone = int(stone_str[:half_length])
            right_stone = int(stone_str[half_length:])
            res = recursive_blink(left_stone, steps - 1) + recursive_blink(
                right_stone, steps - 1
            )
        else:
            res = recursive_blink(stone * 2024, steps - 1)
    # print(f"memory added {(stone, steps)} -> {res}")
    memory[(stone, steps)] = res
    return res


memory = {}
total = 0
for stone in tqdm(stones):
    total += recursive_blink(stone, 75)
print(f"saved {len(memory)} (stone,steps) datapoints in memory")
print(total)
