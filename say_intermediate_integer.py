# say median
# In python, only minheap is provided. If we want to use maxheap, we use minheap with a negative sign 
import sys
from heapq import heappush
from heapq import heappop

def first_setup_heap(maxheap: list, minheap: list, n: int) -> None:
    maxtop = -maxheap[0]
    if n < maxtop:
        minheap.append(-maxheap.pop())
        maxheap.append(-n)
    else: # n >= maxtop
        minheap.append(n)


def setup_heap(maxheap: list, minheap: list, n: int) -> None:
    maxlen = len(maxheap)
    minlen = len(minheap)
    maxtop = -maxheap[0]
    mintop = minheap[0]

    if maxlen > minlen:
        if n < maxtop:
            heappush(minheap, -heappop(maxheap))
            heappush(maxheap, -n)
        else: # n >= maxtop
            heappush(minheap, n)
    else: # maxlen == minlen
        if n > mintop:
            heappush(maxheap, -heappop(minheap))
            heappush(minheap, n)
        else: # n <= mintop
            heappush(maxheap, -n)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    maxheap = list()
    minheap = list()

    for i in range(N):
        n = int(sys.stdin.readline())
        if i == 0:
            maxheap.append(-n)
        elif i == 1:
            first_setup_heap(maxheap, minheap, n)
        else:
            setup_heap(maxheap, minheap, n)

        print(-maxheap[0])
