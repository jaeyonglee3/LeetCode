class Solution:

    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                # 1. Form the string that will be repeated
                # 2. Form the number so we know how many times to repeat the string

                new_str = ""
                while stack[-1] != "[":
                    new_str = stack.pop() + new_str
                
                stack.pop() # removed the opening bracket

                num_repeat = ""
                while stack and stack[-1].isnumeric():
                    num_repeat = stack.pop() + num_repeat

                stack.append(new_str * int(num_repeat))
            
            else:
                stack.append(char)
        
        return "".join(stack)