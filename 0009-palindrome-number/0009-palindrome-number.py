class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        as_list = [i for i in str(x)] 
        
        new_list = []
        for i in range (len(as_list)-1, -1, -1):
            new_list.append(as_list[i])
            
        if as_list == new_list:
            return True
        
        return False