""" Google Tech Dev Guide
Former interview question: compression and decompression

In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

The input
3[abc]4[ab]c

Would be output as
abcabcabcababababc

Other rules
Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa
One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab
Characters allowed as input include digits, small English letters and brackets [ ].
Digits are only to represent amount of repetitions.
Letters are just letters.
Brackets are only part of syntax of writing repeated substring.
Input is always valid, so no need to check its validity.

Learning objectives
This question gives you the chance to practice with strings, recursion, algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with better efficiency.
"""
def solution(input, start=0):
    output = ""
    count = 0
    while start < len(input):
        char = input[start]
        start += 1
        if "0" <= char <= "9":
            count = (count * 10) + int(char)
        elif "a" <= char <= "z":
            output += char
        elif char == "[":
            sub = solution(input, start)
            output += (count * sub)
            count = 0
            start += len(sub) + 1
        else:
            return output
    return output
        
print(solution("3[abc]4[ab]c"))
print(solution("10[a]"))
print(solution("2[3[a]b]"))
print(solution("a[]b"))
print(solution("0[abc]"))