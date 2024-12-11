from tqdm import tqdm

test_str = "125 17"
input_str = "475449 2599064 213 0 2 65 5755 51149"
stones = list(map(int, test_str.strip().split()))
print(f"input: {stones}")


def blink(stones: list[int]) -> list[int]:
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
            continue
        stone_str = str(stone)
        length = len(stone_str)
        if length % 2 == 0:
            half_length = int(length / 2)
            left_stone = int(stone_str[:half_length])
            right_stone = int(stone_str[half_length:])
            # print(f"{stone} -> {left_stone},{right_stone}")
            new_stones.append(left_stone)
            new_stones.append(right_stone)
        else:
            new_stones.append(stone * 2024)
    return new_stones


for i in tqdm(range(25)):
    stones = blink(stones)
# print(stones)
print(len(stones))
