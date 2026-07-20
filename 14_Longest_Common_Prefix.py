class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        reference = strs[0] # strs ke first word ko reference bna lenge
        ans = ""            # ek empty string initialize kr lenge jo ki humara answer bnegi

        for i in range(len(reference)):  # hum first word ki length tk traverse krenge

            for s in strs[1:]: # yahan pe list ke bache hue saare elements pe jaaenge for checking of index i
                if i == len(s) or reference[i]!=s[i]: # if koi word khatam ho jaata hai ya words ke character match na kre to answer return kr denge
                    return ans
                
                # ek index ke liye saare words check krne ke baad inner loop se bahar nikal aaenge
                
            ans += reference[i] # answer string me first word jo reference uska compared character add kr denge then next index pe jaaenge

        return ans # answer return kr denge

        
        
        # first point to think should be ki common prefix humesha start se shuru hota hai beech ya end se nahi
