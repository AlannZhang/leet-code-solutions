# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

def isAnagram(s: str, t: str) -> bool:
    dictOne = {}
    dictTwo = {}

    if len(t) != len(s):
        return False

    for x in s:
        if x not in dictOne:
            dictOne[x] = 1
        else:
            dictOne[x] = dictOne[x] + 1

    for x in t:
        if x not in dictOne:
            return False
        
        if x not in dictTwo:
            dictTwo[x] = 1
        else:
            dictTwo[x] = dictTwo[x] + 1
        
    for key in dictTwo:
        if dictTwo[key] != dictOne[key]:
            return False

    return True

print(isAnagram("anagram", "pangrasasd"))
print(isAnagram("anagram", "anrgaam"))
print(isAnagram("anagram", "pasnagr"))
