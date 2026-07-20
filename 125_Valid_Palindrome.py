class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum(): # agar alphanumeric nahi hai to wo wala character skip kr denge aur pointer move krenge
                i += 1
                continue

            if not s[j].isalnum(): # yahan bhi same kaam
                j -= 1
                continue

            if s[i].lower() != s[j].lower(): # yaahan actual comparison krenge aur agar match ni hua to turant false return kr denge aur agar match kr gye to ye wala if ni chlega
                return False

            i += 1
            j -= 1
        return True

        # we will use two pointers one from start and one from last
        # we will check if both the elements are alphabets or numeric characters then compare s[i] and s[j]
        # if not alphanumeric then continue and move the pointer by one
