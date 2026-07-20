class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # helper function
        def ispalindrome(left, right): # normal palindrome check krke boolean result return kr dega
            while(left<right):
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
            
        # main driver
        i, j = 0, len(s)-1

        while(i<j):
            if s[i]!=s[j]: # if character mismatch aaye to ek baar check krega by skipping(deleting, actual me skip hi krenge) either of the two characters ek baar i wala element skip krke check krege aur ek baar j wala if true then true if both false then false
                return( ispalindrome(i+1,j) or ispalindrome(i, j-1))
            i+=1
            j-=1
        return True
      
