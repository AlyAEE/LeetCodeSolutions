class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# Assumptions:
#1. the two Srting should be the same length
#2. to be an anagram each character should appear the same no. of times in each string

#First Solution
        s = sorted(s)
        t = sorted(t)
        return s == t
    
# Second Solution to work with unicode letters

        # count = [0] * 26
        
        # # Count the frequency of characters in string s
        # for x in s:
        #     count[ord(x) - ord('a')] += 1
        
        # # Decrement the frequency of characters in string t
        # for x in t:
        #     count[ord(x) - ord('a')] -= 1
        
        # # Check if any character has non-zero frequency
        # for val in count:
        #     if val != 0:
        #         return False
        
        # return True

# third solution using hash map

        # count = defaultdict(int)
        
        # # Count the frequency of characters in string s
        # for x in s:
        #     count[x] += 1
        
        # # Decrement the frequency of characters in string t
        # for x in t:
        #     count[x] -= 1
        
        # # Check if any character has non-zero frequency
        # for val in count.values():
        #     if val != 0:
        #         return False
        
        # return True

# Forth Solution
        # if len(s) != len(t):
        #     return False

        # s_freq = {}
        # t_freq = {}
        # for char in s:
        #     s_freq[char] = s_freq.get(char, 0) + 1
        # for char in t:
        #     t_freq[char] = t_freq.get(char, 0) + 1

        # return s_freq == t_freq