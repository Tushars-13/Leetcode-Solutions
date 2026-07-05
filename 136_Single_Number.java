class Solution {
    public int singleNumber(int[] nums) {

        // Variable to store the XOR result
        int ans = 0;

        // Traverse each element in the array
        for (int num : nums) {

            // XOR the current number with ans
            // Duplicate numbers cancel each other (a ^ a = 0)
            // The unique number remains at the end
            ans = ans ^ num;
        }

        // Return the single number that appears only once
        return ans;
    }
}
