class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        m = self.m
        # alice not in map
        if key not in m:
            #add alice key to map with empty list
            m[key] = []
        # add value and timestamp at alice key
        m[key].append((value, timestamp))
        

        

    def get(self, key: str, timestamp: int) -> str:
        m = self.m
        # if the timestamp is in the list of values for the key, return value
        #Otherwise, return the most recent timestamp
        #If there ar no values, return ""
        #print(m[key][-1][1])
        # loop through each timestamp until we find the largest timestamp that is less than timestamp vairable
        # m[test] = [one, 10], [two, 20], [3, 30]
        if key not in m:
            return ""
        arr = m[key]
        left = 0
        right = len(arr) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][1] <= timestamp:
                ans = arr[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
        
# Name = key, [emotion, timestamp] = value
# map[alice] = [happy, 1], [sad, 2], [angry, 3]