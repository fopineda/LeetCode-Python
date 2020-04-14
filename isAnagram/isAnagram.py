class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        ## Anagrams must have equal length
        if len(s) != len(t):
            return False
        
        for letter in s:
            if letter in t:
                t = t.replace(letter, '', 1)
            else:
                return False
        return True
        
        
        