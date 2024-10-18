""" 392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
class Solution: # Accepted. Runtime: 0ms - O(n) - beats 100%, Memory: 16.55MB - O(1) - beats 71%
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        elif len(s) == 0:
            return True

        ptrs = 0
        for i in range(len(t)):
            if t[i] == s[ptrs]:
                ptrs += 1
                if ptrs == len(s):
                    return True
        return False
    
# Follow up question response: If we knew there were multiple incoming s to check, I would change the code to do a preprocessing step
# where a dictionary (hash map) is created with the indices of each charater of t. This way, for each incoming s to check, we would not have to iterate
# through all of t, but only through the characters of s and check their position (if any) in t by accessing the dictionary (constant time).