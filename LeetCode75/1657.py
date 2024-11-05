""" 1657. Determine if Two Strings Are Close
Two strings are considered close if you can attain one from the other using the following operations:
Operation 1: Swap any two existing characters. For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
"""
class Solution: # Accepted. Runtime: 17ms - O(n) - beats 99.95%, Memory: 17.17MB - O(1) - beats 92.45%
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Strings must have the same length
        if len(word1) != len(word2):
            return False
        # Taking and appending the count of each unique character and then sorting the counts is faster
        # than making an array of length n to contain the count of each character count and not sorting
        # since we are limited to lowercase characters so there is at most 26, which uses less space and
        # takes less time than storing two length n counts and comparing them.
        counts1, counts2 = [], []
        # We count only the characters of word1 in both words since this will also tell
        # us if there are characters that are not shared between word1 and word2.
        for char in set(word1):
            counts1.append(word1.count(char))
            counts2.append(word2.count(char))
        counts1.sort()
        counts2.sort()
        return counts1 == counts2