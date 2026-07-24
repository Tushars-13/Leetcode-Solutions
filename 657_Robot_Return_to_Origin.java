class Solution {
    public boolean judgeCircle(String moves) {
        // (x, y) represents the robot's current position.
        // Robot starts at the origin (0, 0).
        int x = 0;
        int y = 0;

        // Process each move in the given string.
        for (int i = 0; i < moves.length(); i++) {
            char move = moves.charAt(i);

            // Update the robot's position based on the current move.
            if (move == 'U') {
                y++;        // Move Up
            } else if (move == 'D') {
                y--;        // Move Down
            } else if (move == 'R') {
                x++;        // Move Right
            } else {
                x--;        // Move Left
            }
        }

        // Robot returns to the origin only if both coordinates are zero.
        return x == 0 && y == 0;
    }
}
