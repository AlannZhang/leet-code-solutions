# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

list = [2, 2, 1]

def singleNumber(list):
    dict = {}
    count = 1

    for x in list:
        if x not in dict:
            dict[x] = count
        else:
            dict[x] = count + 1

    for key, count in dict.items():
        if dict[key] == 1:
            print(key)
            return key

singleNumber(list)            