page_before: dict[set] = {}
updates = []

with open("day5.input.txt") as fin:
    print("reading rules")
    while line := fin.readline().strip():
        before, after = map(int, line.split("|"))
        if page_before.get(after):
            page_before[after].add(before)
        else:
            page_before[after] = set()
            page_before[after].add(before)

    print("checking updates")
    while line := fin.readline().strip():
        pages = list(map(int, line.split(",")))
        updates.append(pages)


def check_update_correct(update: list) -> bool:
    # print(f"checking update {update}")
    for i, page in enumerate(update[:-1]):
        pages_after = update[i + 1 :]
        page_to_early = [(p_a in (page_before.get(page) or [])) for p_a in pages_after]
        if any(page_to_early):
            # print(f"{page} before {page_to_early}")
            return False
    return True


val = 0
for update in updates:
    if check_update_correct(update):
        middle_index = int(len(update) / 2)
        val += update[middle_index]

print(val)
