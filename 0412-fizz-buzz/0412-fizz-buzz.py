class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_so_far = []
        
        for i in range(1, n + 1):
            s = ""

            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if s == "":
                s += str(i)
            
            list_so_far.append(s)
        
        return list_so_far
