""" 1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
class Solution: # Accepted. Runtime: 15ms - O(n) - beats 99.95%, Memory: 16.88MB - O(1) - beats 99.66%
    def longestOnes(self, nums: List[int], k: int) -> int:
        ptr1 = 0
        maxRun = 0
        for i in range(len(nums)):
            if not nums[i]:
                k -= 1
                if k < 0:
                    run = i - ptr1
                    if run > maxRun:
                        maxRun = run
                    while nums[ptr1]:
                        ptr1 += 1
                    k += 1
                    ptr1 += 1
        return max(maxRun, i - ptr1 + 1)

with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        k = next(inputs)
        print(Solution().longestOnes(nums,k),file=f)
exit(0)