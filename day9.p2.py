from dataclasses import dataclass
from tqdm import tqdm

example_input = "2333133121414131402"
with open("day9.input.txt") as fin:
    real_input = fin.read().strip()
input_nrs = list(map(int, real_input))


@dataclass
class Entry:
    id: int
    is_block: int
    length: int
    index: int


def compress_filesystem(filesystem: list[Entry]) -> str:
    first_space_pointer = 0
    back_pointer = len(filesystem) - 1
    pbar = tqdm(total=len(filesystem) - 1)
    while (
        first_space_pointer < len(filesystem)
        and back_pointer > 0
        and first_space_pointer <= back_pointer
    ):
        pbar.update(len(filesystem) - back_pointer - 1 - pbar.n)
        if filesystem[first_space_pointer].is_block:
            first_space_pointer += 1
            continue
        block = filesystem[back_pointer]
        if not block.is_block:
            back_pointer -= 1
            continue
        pointer = first_space_pointer
        while pointer < back_pointer:
            space = filesystem[pointer]
            if space.is_block or space.length < block.length:
                pointer += 1
                continue
            if space.length == block.length:
                space.is_block = 1
                block.is_block = 0
                space.id = block.id
                break
            if space.length > block.length:
                space.length -= block.length
                space.index += block.length
                block.is_block = 0
                filesystem.insert(
                    pointer, Entry(block.id, 1, block.length, space.index)
                )
                break
        else:
            # no fitting space found
            back_pointer -= 1
    pbar.close()
    return filesystem


def get_checksum(filesystem: list[Entry]):
    checksum = 0
    index = 0
    for entry in filesystem:
        if entry.is_block:
            for i in range(entry.length):
                checksum += (index + i) * entry.id
        index += entry.length
    return checksum


def print_filesystem(filesystem: list[Entry]):
    for entry in filesystem:
        symbol = str(entry.id) if entry.is_block else "."
        print(symbol * entry.length, end="")
    print()


filesystem = []
index = 0
for i, x in enumerate(input_nrs):
    new_entry = Entry(int(i / 2), (i + 1) % 2, length=x, index=index)
    filesystem.append(new_entry)
    index += x

# print_filesystem(filesystem)
compressed_filesystem = compress_filesystem(filesystem)
# print_filesystem(compressed_filesystem)
checksum = get_checksum(compressed_filesystem)
print(checksum)
