class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for i in range(1, n + 1):
            to_add = []

            if i % 3 == 0:
                to_add.append("Fizz")
            if i % 5 == 0:
                to_add.append("Buzz")
            
            if not to_add: 
                to_add = str(i)
            
            res.append("".join(to_add))
        
        return res
