class Solution:

    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                # 1. Form the string that will be repeated
                new_str = ""
                while stack[-1] != "[":
                    new_str = stack.pop() + new_str
                
                # 2. Remove the opening bracket
                stack.pop()

                # 3. Form the number so we know how many times to repeat the string
                num_repeat = ""
                while stack and stack[-1].isdigit():
                    num_repeat = stack.pop() + num_repeat

                stack.append(new_str * int(num_repeat))
            
            else:
                stack.append(char)
        
        # By the end, the stack contains the entire decoded string
        return "".join(stack)