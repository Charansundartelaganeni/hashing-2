#TC:O(n) 
#SC:O(n)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        hMap = {} #Creat empty Hash map dictionary
        count = 0 #Creat a counter to count the longest of plaindrome  
        
        for i in s:  
            if i in hMap:
                hMap[i] += 1    
                if hMap[i] == 2:    # if char is in Hashmap and the number of value is 2 
                    count +=2       # add 2 to lonfest of counter 
                    hMap[i] = 0     # change the value of char in map to 0        
            else:
                hMap[i] = 1 #if not found, initiate its value as zero
            
        if 1 in hMap.values(): #if there is 1 for any value, that means we can add 1 for the counter we have as palindrome can have 1 odd occurence
            return count + 1
        else:
            return count