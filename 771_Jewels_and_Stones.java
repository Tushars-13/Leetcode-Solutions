class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count = 0;

        // Check every stone to see if it is a jewel.
        for (int i = 0; i < stones.length(); i++) {
            char stone = stones.charAt(i);

            // Compare the current stone with each jewel.
            for (int j = 0; j < jewels.length(); j++) {
                char jewel = jewels.charAt(j);

                // If the stone matches a jewel, increase the count.
                if (stone == jewel) {
                    count++;
                }
            }
        }

        // Return the total number of jewels found in the stones.
        return count;
    }
}
