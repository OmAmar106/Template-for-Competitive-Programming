import subprocess
import random
import os
import msvcrt

current_dir = os.path.dirname(os.path.abspath(__file__))
AC = os.path.join(current_dir, "wa.py")

local = True
if local:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)

def check(input, output):
    L = list(map(int, output.split(' ')))
    input = int(''.join(input[2:]))
    return True

def generate_random_input_temp():
    n = random.randint(1, 10)
    arr = [random.randint(1, n) for _ in range(n)]
    input_data = "1\n" + f"{n}\n" + " ".join(map(str, arr))
    return input_data

def generate_random_input():
    n = random.randint(1, 10)
    input_data = "1\n" + f"{n}\n"
    return input_data

random_input = True
val = 1
count = 0
while True:
    if msvcrt.kbhit() and msvcrt.getch() == b'\r':
        break
    if random_input:
        input_data = generate_random_input()
    else:
        input_data = str(val)
        val += 1

    input_file = "input.txt"

    result_ac = subprocess.run(
        ["python", AC],
        input=input_data,
        text=True,
        capture_output=True
    )

    if result_ac.returncode != 0:
        if count:
            print()
        if local:
            print(Back.YELLOW + " Your code encountered an error! ")
        else:
            print("Your code encountered an error!")
        print("Input Data:")
        print(input_data.strip())
        print("Error Message:\n", result_ac.stderr)
        exit()

    output_ac = result_ac.stdout.strip()
    if not check(input_data, output_ac):
        if count:
            print()
        if local:
            print(Back.RED + " Test Case Failed! ")
        else:
            print("Test Case Failed!")
        print("Input Data:")
        print(input_data.strip())
        print("Received Output: ", output_ac)
        with open(input_file, 'w') as file:
            file.write(input_data)
        exit()
    else:
        count += 1
        if local:
            print(f"\r{Back.GREEN}Test Cases Passed: {count} ", end="", flush=True)
        else:
            print(f"\rTest Cases Passed: {count}", end="", flush=True)
