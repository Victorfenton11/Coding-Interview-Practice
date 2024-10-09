""" 605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false 

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
class Solution: # Accepted. Runtime: 129ms - beats 73%, Memory: 16.88MB - beats 77%
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if n == 0:
            return True
        elif l < n:
            return False
        elif l == 1:
            return not flowerbed[0]

        if not flowerbed[0] and not flowerbed[1]:
            n -= 1
            if n == 0:
                return True
            flowerbed[0] = 1
        i = 1
        while i < l - 1:
            if not flowerbed[i]:
                if not flowerbed[i-1] and not flowerbed[i+1]:
                    n -= 1
                    if n == 0:
                        return True
                    flowerbed[i] = 1
            i += 1
        return n == 1 and not flowerbed[i-1] and not flowerbed[i]