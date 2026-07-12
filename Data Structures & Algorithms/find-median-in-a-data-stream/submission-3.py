class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        if not self.left: 
            heapq.heappush(self.left,-num)
            return
        if num<=-self.left[0]:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        if abs(len(self.left)-len(self.right))>=2:
            if len(self.left)>len(self.right):
                s=-heapq.heappop(self.left)
                heapq.heappush(self.right,s)
            else:
                s=heapq.heappop(self.right)
                heapq.heappush(self.left,-s)
        

    def findMedian(self) -> float:
        if len(self.left)==len(self.right):
            m=(-self.left[0]+self.right[0])/2.0
        elif len(self.left)>len(self.right):
            m=-self.left[0]
        else:
            m=self.right[0]
        return m
        
        