class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # sorted function calls are O(n log n)
        # s_sorted = sorted(s)
        # t_sorted = sorted(t)

        # for i in range(len(t_sorted)):
        #     if i == len(t_sorted) - 1:
        #         return t_sorted[-1]

        #     if t_sorted[i] != s_sorted[i]:
        #         return t_sorted[i]

        for c in t:
            if t.count(c) != s.count(c):  # count function takes O(n) time
                return c
    