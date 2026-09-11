class TimeMap:

    def __init__(self):
        self.dic = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ''
        
        n = len(self.dic[key])
        left = 0
        right = n - 1
        res = ''

        while left <= right:
            mid = (left + right) // 2

            if self.dic[key][mid][0] == timestamp:
                return self.dic[key][mid][1]

            elif self.dic[key][mid][0] < timestamp:
                res = self.dic[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res



        
