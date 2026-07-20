class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i, j = 0,0

        while j<len(t): 
            if s[i]==t[j]: # if 't' string me 's' string ka character mil jaae to dono i aur j pointer ko bada do
                i+=1
                j+=1
            else: # agar na mile to sirf 't' string ke j ko pointer ko badao
                j+=1

        if i==len(s): # agar i pointer 's' string ke last character tk pahuch gya mtlb wo 's' string ke barabar ho gya to...
            return True
        else:
            return False
