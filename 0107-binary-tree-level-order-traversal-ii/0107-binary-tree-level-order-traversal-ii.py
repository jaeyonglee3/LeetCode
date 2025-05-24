from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = deque()
        q = deque([root])

        while q:
            curr_lvl = []

            for _ in range(len(q)):
                curr = q.popleft()

                if curr:
                    curr_lvl.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)

            if curr_lvl:
                res.appendleft(curr_lvl)

        return list(res)
