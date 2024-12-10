from tqdm import tqdm


def check_equation(result: int, values: list[int]) -> bool:
    def next_step(index, cur_result):
        if index == len(values):
            return cur_result == result
        return (
            next_step(index + 1, cur_result + values[index])
            or next_step(index + 1, cur_result * values[index])
            or next_step(index + 1, int(str(cur_result) + str(values[index])))
        )

    return next_step(1, values[0])


total_calibration_result = 0
with open("day7.input.txt") as fin:
    lines = fin.readlines()

amount_possible_callibrations = 0
for line in tqdm(lines):
    result, values_str = line.strip().split(":")
    result = int(result)
    values = list(map(int, values_str.strip().split()))
    if check_equation(result, values):
        total_calibration_result += result
        amount_possible_callibrations += 1
print(f"{amount_possible_callibrations}/{len(lines)} succesfull calibrations")
print(total_calibration_result)
