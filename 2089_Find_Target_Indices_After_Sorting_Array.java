import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<Integer> targetIndices(int[] nums, int target) {

        // ---------------------------------------------------------
        // Approach:
        // 1. Count how many elements are smaller than the target.
        //    -> This tells us the first index of target after sorting.
        //
        // 2. Count how many times the target appears.
        //
        // 3. If 'less' elements are smaller than target and target
        //    appears 'equal' times, then after sorting the target
        //    will occupy indices:
        //
        //    less, less + 1, less + 2, ..., less + equal - 1
        //
        // Time Complexity: O(n)
        // Space Complexity: O(1) (excluding the output list)
        // ---------------------------------------------------------

        // Count of elements smaller than target
        int less = 0;

        // Count of occurrences of target
        int equal = 0;

        // Traverse the array once
        for (int num : nums) {

            // Count elements smaller than target
            if (num < target) {
                less++;
            }

            // Count occurrences of target
            else if (num == target) {
                equal++;
            }
        }

        // List to store the answer
        List<Integer> ans = new ArrayList<>();

        // Add all target indices after sorting
        for (int i = 0; i < equal; i++) {
            ans.add(less + i);
        }

        return ans;
    }
}
