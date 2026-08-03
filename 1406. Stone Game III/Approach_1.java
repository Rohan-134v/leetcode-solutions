class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        int[] dp = new int[n + 1];
        for (int i = 0; i < n; i++) {
            dp[i] = -1000000000; 
        }
        dp[n] = 0; 
        
        for (int i = n - 1; i >= 0; i--) {
            int take_sum = 0;
            for (int k = 1; k <= 3 && i + k <= n; k++) {
                take_sum += stoneValue[i + k - 1];
                dp[i] = Math.max(dp[i], take_sum - dp[i + k]);
            }
        }
        
        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }
}