"""
1. Read in lines from input.txt
2. Convert values to numbers
3. Count how many numbers are larger than the previous number
4. Count how many numbers are larger than the number three indexes previous
"""


def main():
    # Read in lines from input.txt
    with open("01/input.txt", "r") as f:
        lines = f.readlines()

    # Convert values to numbers
    numbers = [int(line) for line in lines]

    # Count how many numbers are larger than the previous number
    count = 0
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            count += 1

    # Count how many numbers are larger than the number three indexes previous
    count2 = 0
    for i in range(len(numbers) - 3):
        if numbers[i] < numbers[i + 3]:
            count2 += 1

    print(count)
    print(count2)


if __name__ == "__main__":
    main()
