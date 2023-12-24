class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        curr_char = None
        curr_len = 0

        while r < len(chars):
            if chars[r] != curr_char:  # New character encountered
                if curr_len >= 2:
                    len_str = []
                    while curr_len:
                        len_str.append(str(curr_len % 10))
                        curr_len = curr_len // 10
                    for lstr in len_str[::-1]:
                        chars[l] = lstr
                        l += 1
                chars[l] = chars[r]
                l += 1
                curr_char = chars[r]
                curr_len = 1
            else:  # Same character encountered
                curr_len += 1
            r += 1
        
        if curr_len >= 2:
            len_str = []
            while curr_len:
                len_str.append(str(curr_len % 10))
                curr_len = curr_len // 10
            for lstr in len_str[::-1]:
                chars[l] = lstr
                l += 1
        
        return l
                    