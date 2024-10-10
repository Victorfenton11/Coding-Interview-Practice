""" 345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

 
Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solution: # Accepted. Runtime: 33ms - beats 99%, Memory: 17.58MB - beats 44%
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        ptr1 = 0
        ptr2 = len(s) - 1

        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

        while ptr1 < ptr2:
            if not s[ptr1] in vowels:
                ptr1 += 1
            elif not s[ptr2] in vowels:
                ptr2 -= 1
            else:
                if s[ptr1] != s[ptr2]:
                    s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1

        return ''.join(s)