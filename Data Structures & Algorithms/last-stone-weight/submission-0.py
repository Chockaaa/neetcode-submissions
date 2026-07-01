class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]= -stones[i]
        for x in range(len(stones)):
            heapq.heapify(stones)
        

        while stones:
            print(stones)
            y = -heapq.heappop(stones)
            if stones:
                x = -heapq.heappop(stones)
                print(y,x)
                if(y-x ==0):
                    res = 0
                else:
                    heapq.heappush(stones,-(y-x))
            else:
                res = y

        return res
        


