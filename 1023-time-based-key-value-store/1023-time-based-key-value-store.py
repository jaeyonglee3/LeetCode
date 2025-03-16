from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        
        if key not in self.dict: 
            return res
        
        values = self.dict[key]
        l, r = 0, len(values) - 1
        
        while r >= l:
            mid = (l + r) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Main ds: dictionary, where keys are the keys and the values are arrays containing multiple values for each key
# as tuples of (value, timestamp)

# set method: will simply add a new entry to our dictionary

# get method: will use the given key to fetch the array of associated values from our dictionary
# and use binary search to fetch the value equal to the timestamp or closest to it without going over.