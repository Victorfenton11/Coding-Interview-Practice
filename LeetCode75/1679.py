""" 1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
class Solution: # Accepted. Runtime: 95ms - O(n) - beats 99.95%, Memory: 24.44MB - O(n) - beats 99.89%
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        ops = 0
        for num, count in counts.items():
            if k - num in counts:
                ops += min(count, counts[k - num])
        return ops // 2

with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        k = next(inputs)
        print(Solution().maxOperations(nums,k),file=f)
exit(0)