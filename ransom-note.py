# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = Solution.getDict(magazine)
        ransomNoteDict = Solution.getDict(ransomNote)

        for x in ransomNoteDict:
            if x not in magazineDict:
                return False

            if x in magazineDict and ransomNoteDict[x] > magazineDict[x]:
                return False

        return True

    # function for creating a dict with the letters as keys with associated count in the string
    def getDict(letters: str) -> dict:
        dict = {}

        for x in list(letters):
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] = dict[x] + 1
        
        return dict
