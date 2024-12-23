class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []

        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # optimization: if the key just isn't present, return an empty string
        res = ""
        if key not in self.timeMap:
            return res
        
        # Run a binary search on the value array to find
        # the timestamp or the closest one
        value_arr = self.timeMap[key]
        l, r = 0, len(value_arr) - 1

        if value_arr[0][1] > timestamp:
            return res

        # optimization: if even the smallest timestamp is too big,
        # return an empty string
        while r >= l:
            mid = (l + r) // 2
            
            if value_arr[mid][1] == timestamp:
                return value_arr[mid][0]
            elif value_arr[mid][1] > timestamp:
                r = mid - 1
            else: # the value is smaller than timestamp so still valid
                l = mid + 1
                res = value_arr[mid][0]
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)