from dataclasses import dataclass
import numpy as np


input_test = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".strip()


@dataclass
class clawmachine:
    a: np.ndarray
    b: np.ndarray
    prize: np.ndarray


def splitNamedCoordinate(text: str) -> np.ndarray:
    name, coordinates = text.split(": ")
    x_cord, y_cord = coordinates.split(", ")
    x = int(x_cord.replace("=", "").replace("X", "").replace("Y", ""))
    y = int(y_cord.replace("=", "").replace("X", "").replace("Y", ""))
    return np.array([x, y])


def findCheapestWin(machine: clawmachine) -> int | None:
    a_presses = 0
    b_presses = 100
    while a_presses <= 100 and b_presses > 0:
        cur_pos = machine.a * a_presses + machine.b * b_presses
        distance = machine.prize - cur_pos
        # print(
        # f"pressing a {a_presses} times and b {b_presses} times is {cur_pos} instead of {machine.prize} -> distance {distance}"
        # )
        if not distance.any():
            print(
                f"Found solution for {machine.prize} using {a_presses}*a and {b_presses}*b"
            )
            return a_presses * 3 + b_presses
        if (distance[0] < 0 and distance[1] < 0) or a_presses >= 100:
            b_presses -= 1
            continue
        a_presses += 1
        if a_presses > 100:
            a_presses -= 1
    return None


with open("day13.input.txt") as fin:
    input_text = fin.read().strip()

input_groups = input_text.split("\n\n")
clawmachines = []
for input in input_groups:
    input = [splitNamedCoordinate(text) for text in input.split("\n")]
    clawmachines.append(clawmachine(*input))

cheapest_wins = []
for machine in clawmachines:
    cheapest_win = findCheapestWin(machine)
    if cheapest_win:
        cheapest_wins.append(cheapest_win)

print(sum(cheapest_wins))
