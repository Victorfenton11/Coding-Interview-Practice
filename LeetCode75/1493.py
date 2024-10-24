""" Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
class Solution: # Accepted. Runtime: 24ms - O(n) - beats 99.46%, Memory: 19.18MB, O(1) - beats 99.59%
    def longestSubarray(self, nums: List[int]) -> int:
        # Very similar to Max Consecutive Ones III but with k = 1
        # If we wish to actually modify the input array to remove 1 element,
        # we just need to use 2 extra variables to keep track of each 0 we
        # encounter and save the position of the zero when we update the maxRun
        # Then at the end we would simply pop that index, or 0 if index invalid
        k = 1
        ptr1 = 0
        maxRun = 0
        for i in range(len(nums)):
            if not nums[i]:
                k -= 1
                if k < 0:
                    if i - ptr1 - 1 > maxRun:
                        maxRun = i - ptr1 - 1
                    while nums[ptr1]:
                        ptr1 += 1
                    ptr1 += 1
                    k += 1
        return max(maxRun, i - ptr1)
    
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        k = next(inputs)
        print(Solution().longestOnes(nums,k),file=f)
exit(0)