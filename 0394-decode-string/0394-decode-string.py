class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                # step 1: get the char to repeat by popping until "["
                str_to_repeat = []
                while stack and stack[-1] != "[":
                    str_to_repeat.append(stack.pop())
                stack.pop()  # pop once more to rid of "["
                str_to_repeat.reverse()  # reverse to obtain the correct order after popping

                # step 2: obtain the number to repeat
                num_to_repeat = []
                while stack and stack[-1].isdigit():
                    num_to_repeat.append(stack.pop())
                num_to_repeat.reverse()  # reverse to get the digits in right order

                # step 3: repeat the string, then push back to stack
                new_str = "".join(str_to_repeat) * int("".join(num_to_repeat))
                stack.append(new_str)
            else:
                stack.append(c)

        return "".join(stack)