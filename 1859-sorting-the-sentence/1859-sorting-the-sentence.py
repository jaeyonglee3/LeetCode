class Solution:
    def sortSentence(self, s: str) -> str:
        result = []
        s_list = s.split()

        for i in range(1, s.count(" ") + 2):
            for word in s_list:
                if word[-1] == str(i):
                    result.append(word[:-1])

        return(' '.join(result))