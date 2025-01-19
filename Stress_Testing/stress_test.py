import subprocess
import random
import os

Brute = "Stress_Testing/brute.py"
AC = "Stress_Testing/ac.py"

def generate_random_input_temp():
    n = random.randint(1, 100)
    arr = [random.randint(1, n) for _ in range(n)]
    input_data = "1\n" + f"{n}\n" + " ".join(map(str, arr))
    return input_data
def generate_random_input():
    n = random.randint(1, 100)
    arr = [random.randint(1, n) for _ in range(n)]
    input_data = "1\n" + f"{n}\n" + " ".join(map(str, arr))
    return input_data
count = 0
while True:
    input_data = generate_random_input()
    input_file = "input.txt"
    result_brute = subprocess.run(
        ["python", Brute],
        input=input_data,
        text=True,
        capture_output=True
    )
    result_ac = subprocess.run(
        ["python", AC],
        input=input_data,
        text=True,
        capture_output=True
    )
    output_brute = result_brute.stdout.strip()
    output_ac = result_ac.stdout.strip()
    if output_brute != output_ac:
        print()
        print(input_data)
        print("Actual Output: ",output_brute)
        print("Received Output: ",output_ac)
        with open(input_file, 'w') as file:
            file.write(input_data)
        exit()
    else:
        count += 1
    print(f"Cases Passed: {count}", end="\r")
