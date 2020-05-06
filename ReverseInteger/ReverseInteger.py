class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
            
        if x < 0:
            str_x = str(x)
            str_x = str_x.lstrip('-')
            reversed_x = ""
            for i in str_x:
                reversed_x = i + reversed_x
            reversed_x = "-" + reversed_x      
        else:
            str_x = str(x)
            reversed_x = ""
            for i in str_x:
                reversed_x = i + reversed_x     
                    
        if (-2**31) <= int(reversed_x) <= ((2**31)-1):
            return int(reversed_x)
        else:
            return 0