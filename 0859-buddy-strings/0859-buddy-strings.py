class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # iterate through s
        # anytime s[i] != goal[i], do s.index(goal[i])
        # if -1, return false
        # otherwise, perform swap 

        # Attempt #1 (close, but wrong)
        # for i in range(len(s)):
        #     if s == goal:
        #         return any((count >= 2) for count in {s.count(c) for c in s})

        #     if s[i] != goal[i] and s.find(goal[i]) != -1:
        #         indx = s.find(goal[i])
        #         sList = list(s.strip())
        #         sList[i], sList[indx] = sList[indx], sList[i]
        #         print("".join(sList))
        #         return "".join(sList) == goal

        # Attempt #2 (correct)
        c1 = Counter(s)
        c2 = Counter(goal)

        if c1 != c2:
            return False
        
        num_diffs = sum(1 for i in range(len(s)) if s[i] != goal[i])

        if num_diffs == 2:
            return True
        elif num_diffs == 0:
            return any((count > 1) for count in {s.count(c) for c in s})
        else:
            return False