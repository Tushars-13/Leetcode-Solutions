class Solution {
    public String toLowerCase(String s) {

        // Convert the input string into a character array
        char[] arr = s.toCharArray();

        // Traverse each character
        for (int i = 0; i < arr.length; i++) {

            // Check if the current character is an uppercase letter (A-Z)
            if (arr[i] >= 'A' && arr[i] <= 'Z') {

                // Convert uppercase to lowercase using ASCII difference (32)
                arr[i] = (char) (arr[i] + 32);
            }
        }

        // Convert the modified character array back to a String
        return new String(arr);
    }
}
