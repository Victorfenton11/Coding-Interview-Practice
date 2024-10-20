""" 643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
 

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
class Solution: # Accepted. Runtime: 45ms - O(n) - beats 99.82%, Memory: 26.5MB - O(1) - beats 97.73%
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        for i in range(k):
            maxSum += nums[i]
        currSum = maxSum
        for ptr1 in range(1, len(nums) - k + 1):
            currSum = currSum - nums[ptr1-1] + nums[ptr1+k-1]
            if currSum > maxSum:
                maxSum = currSum
        return maxSum / k