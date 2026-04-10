class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = {}

        def solve(i, j):
            if i == 0 or j == 0:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if text1[i-1] == text2[j-1]:
                dp[(i, j)] = 1 + solve(i-1, j-1)
            else:
                dp[(i, j)] = max(solve(i-1, j), solve(i, j-1))

            return dp[(i, j)]

        return solve(len(text1), len(text2))
