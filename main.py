class Solution: #class named Solution 
    def sortedSquares(self, nums):
        squares = [num * num for num in nums] #Iterates over each element num in the input list and squares them to later aprend them to the new list
        squares.sort() #a function that sorts the list in asecnding order                      
        return squares
