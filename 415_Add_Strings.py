class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # appraoch using carry
        ans = []
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        
        
        while(i>=0 or j>=0 or carry==1):
            total = carry

            if i>=0:
                total += int(num1[i])
                i-=1
            if j>=0:
                total += int(num2[j])
                j-=1
            
            answer_digit = total%10
            carry = total//10
            
            ans.append(str(answer_digit))
            
        return "".join(ans[::-1])
        



