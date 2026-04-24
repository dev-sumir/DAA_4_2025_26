class Solution:
    def minDifference(self, arr):
        total = sum(arr)
        n = len(arr)
        
        dp = [False] * (total + 1)
        dp[0] = True
        
        for num in arr:
            for j in range(total, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        for s1 in range(total // 2, -1, -1):
            if dp[s1]:
                return total - 2 * s1
