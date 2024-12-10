from tqdm import tqdm


def check_equation(result: float | int, values: list[int]) -> bool:
    if len(values) <= 2:
        summation = values[0] + values[1]
        product = values[0] * values[1]
        return result == summation or result == product
    last_value = values.pop()
    return check_equation(result / last_value, values.copy()) or check_equation(
        result - last_value, values
    )


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
