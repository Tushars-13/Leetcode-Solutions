class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        # helper function to swap elements in the array
        def reverse(arr, i, j):
            while(i<j):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i+=1
                j-=1
            return arr


        arr = list(s) # converting the array into the string
        n = len(arr)
        i = 0

        while i<n:
            j = min(i+k-1, n-1) # it is done to prevent the "index out of bound error"  ***
            reverse(arr, i, j) # calling helper function
            i = i + 2*k  # ex:- jumping from i = 0 (swap (0,1)) to i = 4 (swap (4,5)) if k == 2
        return "".join(arr) # converting the list back to string

"""
Why do we use min(i + k - 1, n - 1)?

We want to reverse only the first k characters starting from index i.
Normally, the last index would be:

    i + k - 1

But if fewer than k characters are left at the end of the string,
then i + k - 1 may go beyond the last valid index (n - 1),
which would cause an IndexError.

So we take:

    j = min(i + k - 1, n - 1)

This ensures j never exceeds the last valid index of the array.

Example:
s = "abcdefg", k = 3

Last iteration:
i = 6

i + k - 1 = 8
n - 1 = 6

j = min(8, 6) = 6

So only the remaining character is reversed safely without going
out of bounds.
"""
