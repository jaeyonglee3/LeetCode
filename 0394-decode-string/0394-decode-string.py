class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                # step 1: pop until you hit an open bracket
                curr_str = []
                while stack[-1] != "[":
                    curr_str.append(stack.pop())
                stack.pop()  # pop once more to remove "["

                # step 2: reverse the current string
                curr_str.reverse()
                curr_str = "".join(curr_str)

                # step 3: pop to form the number
                curr_num = []
                while stack and stack[-1].isdigit():
                    curr_num += stack.pop()
                curr_num.reverse()
                curr_num = int("".join(curr_num))

                # step 4: multiply by the number, add back to stack
                stack.append(curr_str * curr_num)
            else:
                stack.append(c)
        
        return "".join(stack)