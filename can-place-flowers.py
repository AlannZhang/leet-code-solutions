# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
# and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        prev = ""
        next = ""
        count = 0

        for i, x in enumerate(flowerbed):
            if i != 0:
                prev = flowerbed[i - 1]

            if i != len(flowerbed) - 1:
                next = flowerbed[i + 1]

            # case where an available plot is the first element
            if i == 0 and x == 0 and next == 0:
                flowerbed[i] = 1
                count += 1
            
            # case where an available plot is the last element
            if i == len(flowerbed) and x == 0 and prev == 0:
                flowerbed[i] = 1
                count += 1

            # general case
            if x == 0 and prev == 0 and next == 0:
                flowerbed[i] = 1
                count += 1
        
        if n == 0:
            return True
        
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return False

        if n > count:
            return False

        return True
