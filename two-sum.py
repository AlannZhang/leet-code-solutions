# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

target = 9
nums = [2, 7, 11, 15]
dict = {}

def twoSum():
    for i, num, in enumerate(nums):
        if num in dict:
            print("Index 1: ", dict[num])
            print ("Index 2: ", i)

            return [dict[num], i]
        dict[target - num] = i

print(twoSum())