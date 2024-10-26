""" 1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
class Solution: # Accepted. Runtime: 0ms - O(n) - beats 100%, Memory: 16.6MB - O(n) - beats 66.5%
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict()
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        if len(set(counts.values())) == len(counts):
            return True
        return False