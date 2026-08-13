class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # binary search implementation
        l, r = 0, len(self.data[key]) - 1
        res=""

        while(l <= r):
            m =l + (r-l)//2
            curTimestamp, curValue = self.data[key][m]

            if(curTimestamp <= timestamp):
                res = curValue
                l=m+1
            else:
                r=m-1
            
        
        return res