class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        alphanumericString = ""
        for character in s:
            if character.lower().isalnum():
                alphanumericString += character.lower()
        
        return alphanumericString == alphanumericString[::-1]