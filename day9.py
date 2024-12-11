from tqdm import tqdm

example_input = "2333133121414131402"
with open("day9.input.txt") as fin:
    real_input = fin.read().strip()
input_nrs = list(map(int, real_input))


def compress_filesystem(blocks: list[int], spaces: list[int], ids: list[int]) -> str:
    checksum = 0
    index = 0
    while len(blocks):
        block = blocks.pop(0)
        id = ids.pop(0)
        for i in range(block):
            checksum += (index + i) * id
        index += block
        if len(spaces):
            space = spaces.pop(0)
            while space > 0 and len(blocks):
                block = blocks.pop()
                remaining_space = space - block
                last_id = ids.pop()
                amount = min(block, space)
                for i in range(amount):
                    checksum += (index + i) * last_id
                index += amount
                if remaining_space < 0:
                    ids.append(last_id)
                    blocks.append(block - space)
                space = remaining_space
    return checksum


spaces = [n for k, n in enumerate(input_nrs) if (k % 2 == 1)]
blocks = [n for k, n in enumerate(input_nrs) if (k % 2 == 0)]
ids = list(range(len(blocks)))

checksum = compress_filesystem(blocks, spaces, ids)
print(checksum)
