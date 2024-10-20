""" 11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
class Solution: # Accepted: Runtime: 37ms - O(n) - beats 100%, Memory: 27.60MB - O(1) - beats 99.54%
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        maxArea = 0
        while start < end:
            if height[start] > height[end]:
                h = height[end]
                end -= 1
            else:
                h = height[start]
                start += 1
            area = h * (end - start + 1)
            if area > maxArea:
                maxArea = area
        return maxArea