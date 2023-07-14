class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

# The maximum digit in the string n decides how many 1's will be present.
# The total number of 1's required to sum up to form the max digit 
# is deciding how many numbesr required for the total sum. 