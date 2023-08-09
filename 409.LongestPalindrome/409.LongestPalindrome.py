class Solution:
    def longestPalindrome(self, s: str) -> int:

#Assumptions
# 1. There can bo one char with odd no. to get counted
# 2. else count no. chars that are even
#Constraints
#letters are case sensitive
# s is can't be empty, atleast 1 character

# First Solution
        count = {}
        for char in s:
            count[char] = 1 + count.get(char,0)
        
        center_char = 0
        even_char = 0

        for char in count:
            even_char += count[char] // 2 * 2
            if center_char == 0 and count[char] % 2 == 1:
                center_char = 1
        return center_char + even_char

#second Solution
        # count = {}
        # for char in s:
        #     count[char] = 1 + count.get(char,0)
        
        # odd_found = False
        # result = 0

        # for _,char in count.items():
        #     if char % 2 == 0:
        #         result += char
        #     else:
        #         odd_found = True
        #         result += char -1
        # if odd_found:
        #     result += 1

        # return result
