""" 1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""
class Solution: # Accepted. Runtime: 68ms - O(n) - beats 99.35%, Memory: 17.05MB - O(1) - beats 99.32%
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxVowels = 0
        for i in range(k):
            maxVowels += s[i] in vowels
        cur = maxVowels
        for ptr in range(1, len(s) - k + 1):
            cur = cur - (s[ptr-1] in vowels) + (s[ptr+k-1] in vowels)
            if cur > maxVowels:
                maxVowels = cur
        return maxVowels