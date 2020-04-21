def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        haystackLength = len(haystack)
        needleLength = len(needle)
        i = 0
        while i <= (haystackLength - needleLength):
            if haystack[i:i+needleLength] == needle:
                return i
            i+=1
        return -1