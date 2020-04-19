class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # edge case: if list is empty
        if strs == []: 
            return ""
        
        ## Why sort? b/c it will allow you to do your logic on the first and last word. 
        ## It does this by sort of grouping words that have similar prefixes and putting the shortest
        ## ones at the beginning of its group (not at the start). For example: "flow" will come before
        ## "flower". There is no need to check for "flow" since the prefix is also in "flower".
        strs.sort()
        
        firstWord = strs[0]
        secondWord = strs[-1]
        firstWordSize = len(firstWord)
        lastWordSize = len(secondWord)
        
        
        indexOfFirstWord = 0
        indexOfSecondWord = 0
        commonPrefix = ""
        while (indexOfFirstWord <= firstWordSize-1 and indexOfSecondWord <= lastWordSize-1):
            if (firstWord[indexOfFirstWord] != secondWord[indexOfSecondWord]):
                break
            commonPrefix += (firstWord[indexOfFirstWord])
            indexOfFirstWord += 1
            indexOfSecondWord += 1
            
        return commonPrefix
            
        