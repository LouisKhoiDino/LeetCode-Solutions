class Solution:
    def findMedianSortedArrays(self, A: list[int], B: list[int]) -> float:
        m, n = len(A), len(B)

        if m > n:
            return self.findMedianSortedArrays(B, A)

        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            maxL1 = float("-inf") if i == 0 else A[i - 1]
            minR1 = float("inf") if i == m else A[i]

            maxL2 = float("-inf") if j == 0 else B[j - 1]
            minR2 = float("inf") if j == n else B[j]

            if maxL1 <= minR2 and maxL2 <= minR1:
                if (m + n) % 2:
                    return max(maxL1, maxL2)
                return (max(maxL1, maxL2) + min(minR1, minR2)) / 2

            if maxL1 > minR2:
                right = i - 1
            else:
                left = i + 1

        return 0.0