class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        word_list = s.split()
        new_word = ""
        final_sentence = ""
        
        for word in word_list:
            new_word = " "
            for x in range(len(word)-1, -1, -1):
                new_word = new_word + word[x]
            final_sentence = final_sentence + new_word
        
        
        return final_sentence[1:len(final_sentence)]