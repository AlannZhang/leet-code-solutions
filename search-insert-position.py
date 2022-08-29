# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        currIndex = 0

        for i, x in enumerate(nums):
            prevNum = 0
            nextNum = 0

            if i != 0:
                prevNum == nums[i - 1]

            if i != len(nums) - 1:
                nextNum == nums[i + 1]    
            
            if x == target:
                return i

            if target > nums[len(nums) - 1]:
                return len(nums)

            if target < x and target >= prevNum :
                return i

            if target > x and target <= nextNum:
                currIndex = i + 1

        return currIndex

print(Solution.searchInsert(Solution, [1,3,5,6], 7))
