class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        maxLength = max(len(a), len(b))

        a = a.zfill(maxLength)
        b = b.zfill(maxLength)

        result = ""
        carry = 0
        addToResult = ""

        for index in range(maxLength-1, -1, -1):
            r = carry
            r+=1 if a[index] == '1' else 0
            r+=1 if b[index] == '1' else 0
            addToResult = ('0' if r%2==0 else '1')
            result = addToResult + result
            carry = (0 if r < 2 else 1)

        if carry != 0:
            result = '1' + result

        return result.zfill(maxLength)