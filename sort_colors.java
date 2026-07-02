/*
Approach: Dutch National Flag Algorithm

Idea:
- Maintain three pointers:
  low  -> next position for 0
  mid  -> current element being processed
  high -> next position for 2

Rules:
1. If nums[mid] == 0:
   - Swap nums[low] and nums[mid]
   - Increment both low and mid

2. If nums[mid] == 1:
   - It is already in the correct region
   - Increment mid

3. If nums[mid] == 2:
   - Swap nums[mid] and nums[high]
   - Decrement high
   - Do NOT increment mid because the swapped element
     from the end has not been processed yet

Time Complexity: O(n)
Space Complexity: O(1)
*/

class Solution {
    public void sortColors(int[] nums) {

        // Pointer for placing the next 0
        int low = 0;

        // Current element under consideration
        int mid = 0;

        // Pointer for placing the next 2
        int high = nums.length - 1;

        // Traverse until mid crosses high
        while (mid <= high) {

            if (nums[mid] == 0) {
                // Place 0 at the beginning
                swap(nums, low, mid);

                // Move both pointers forward
                low++;
                mid++;
            }
            else if (nums[mid] == 1) {
                // 1 is already in the correct region
                mid++;
            }
            else {
                // Place 2 at the end
                swap(nums, mid, high);

                // Reduce the right boundary
                high--;

                // Do not increment mid here because
                // the swapped element needs to be checked
            }
        }
    }

    // Helper function to swap two elements
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

    }
}
