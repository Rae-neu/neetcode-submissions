class TimeMap:

    def __init__(self):
        self.dic = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value))        

    def get(self, key: str, timestamp: int) -> str:
        ans = self.dic[key]
        left = 0
        right = len(ans) - 1
        res = 0

        if key not in self.dic:
            return ""
        
        while left <= right:
            mid = (right + left) // 2

            if ans[mid][0] < timestamp:
                res = ans[mid][1]
                left = mid + 1

            elif ans[mid][0] > timestamp:
                right = mid - 1

            else:
                return ans[mid][1]
        
        return res

        
