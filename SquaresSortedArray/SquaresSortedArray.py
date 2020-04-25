class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        # initialize variables
        leftPointer = 0
        rightPointer = decrementingCounter = len(A) - 1
        results = [0] * len(A)
        
        # Used two pointer technique where one starts in the beginning and the other at the end
        # Since the list is sorted, the largest (squared) number will either be at the beginning or end
        # The pointers square each number and compare to see which is the largest
        # The largest of the two will be placed at the end of the results list
        # That pointer will either be decremented or incremented based on what side it was
        # thus moving the next number in the input list
        while leftPointer <= rightPointer:
            leftSquaredNumber = A[leftPointer] * A[leftPointer]
            rightSquaredNumber = A[rightPointer] * A[rightPointer]
            if rightSquaredNumber > leftSquaredNumber:
                results[decrementingCounter] = rightSquaredNumber
                rightPointer -= 1
            else:
                results[decrementingCounter] = leftSquaredNumber
                leftPointer += 1
                
            decrementingCounter -= 1
        return results
        
        
        
        