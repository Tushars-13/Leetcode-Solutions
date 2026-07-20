class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1

        while(i<j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i+=1
            j-=1

        # used two pointer approach one from start another from last changed their positions of the elements using a temp variable, didn't return any anything and changed the list at its place only
