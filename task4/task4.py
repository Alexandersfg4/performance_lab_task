import sys


def min_steps(nums):
    value_to_be_driven_in = nums[len(nums) // 2]
    return sum(abs(v - value_to_be_driven_in) for v in nums)


if __name__ == "__main__":
    file_with_numbers = sys.argv[1]
    with open(file_with_numbers, "r") as f:
        numbers = f.readlines()
    int_numbers = [int(num) for num in numbers]
    int_numbers.sort()
    steps = min_steps(int_numbers)
    print(steps)
