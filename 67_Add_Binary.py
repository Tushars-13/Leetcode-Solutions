class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # appraoch using carry
        i = len(a)-1
        j = len(b)-1
        carry = 0
        ans = ""
        
        while(i>=0 or j>=0 or carry==1):
            total = carry

            if i>=0:
                total += int(a[i])
                i-=1
            if j>=0:
                total += int(b[j])
                j-=1
            
            answer_digit = total%2
            carry = total//2
            
            ans += str(answer_digit)
            
        return ans[::-1] # returning reverse of string i.e. from left to right but we added from right to left
