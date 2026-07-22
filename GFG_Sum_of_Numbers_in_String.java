class Solution {
    public static int findSum(String str) {
        int sum = 0;
        int num = 0;

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (Character.isDigit(ch)) {
                num = num * 10 + (ch - '0');
            } else {
                sum += num;
                num = 0;
            }
        }

        sum += num; // Last number agar string digit par end ho

        return sum;
    }
}
