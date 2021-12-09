"""
1. Read comma-separated numbers from input.txt
2. Determine the value that is the minimum distance from all the numbers
"""

import math


def read_numbers():
    """Read comma-separated numbers from input.txt"""
    with open("07/input.txt") as f:
        numbers = f.read().split(",")
    return numbers


def get_min_distance(numbers):
    """Determine the value that is the minimum distance from all the numbers"""
    min_distance = math.inf
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(int(numbers[i]) - int(numbers[j]))
            if distance < min_distance:
                min_distance = distance
    return min_distance


def main():
    """Main function"""
    numbers = read_numbers()
    min_distance = get_min_distance(numbers)
    print(min_distance)


if __name__ == "__main__":
    main()
