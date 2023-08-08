def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
# How to approach
# 1. We need to get rid of all non-alphanumeric characters
# 2. Convert all uppercase letters to lowercase
# 3. loop through the string and compare each character to its correspondant
    punctuation = "!'#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \""
    s = s.lower()
    for char in punctuation: 
         s = s.replace(char,'')

    for i in range(len(s)):
         if s[i] != s[~i]:
              return False
    return True

    # import string
    # s = "".join(s.split()).lower()
    # print(s)
    # for punctuation in string.punctuation:
    #     s = s.replace(punctuation, '')
    # print(s)
    # for i in range(len(s)):
    #     if s[i] != s[-i-1]:
    #         return False
    # return True

    # import string
    # s = "".join(s.split()).lower()
    # print(s)
    # s = s.translate(str.maketrans('', '', string.punctuation))
    # print(s)
    # for i in range(len(s)):
    #     if s[i] != s[-i-1]:
    #         return False
    # return True
print(isPalindrome("A man, a plan, a canal: Panama"))