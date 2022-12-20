#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (not isinstance(roman_string, str)):
        return 0

    nums = []
    for i in roman_string:
        if i == "I":
            nums.append(1)
        elif i == "V":
            nums.append(5)
        elif i == "X":
            nums.append(10)
        elif i == "L":
            nums.append(50)
        elif i == "C":
            nums.append(100)
        elif i == "D":
            nums.append(500)
        elif i == "M":
            nums.append(1000)

    tot = 0
    while nums:
        if len(nums) == 1:
            tot += nums[0]
            break
        if (nums[0] >= nums[1]):
            tot += nums[0]
            nums = nums[1:]
        else:
            tot += nums[1] - nums[0]
            nums = nums[2:]

    return tot
