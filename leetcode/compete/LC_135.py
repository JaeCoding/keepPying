from heapq import heappush


def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    h = []
    # make index + 2 to avoid edge
    candy_allocate = [0 for _ in range(len(ratings) + 2)]
    total_candy = 0
    for i, n in enumerate(ratings):
        heappush(h, (n, i))

    for (score, index) in h:
        # left and right is not allocate
        maxOfLeftAndRight = max(candy_allocate[index], candy_allocate[index + 2])
        
        candy_allocate[index + 1] = maxOfLeftAndRight + 1
        total_candy += candy_allocate[index + 1]

    return total_candy


# print(candy([1, 0, 3]))
print(candy([1, 2, 2]))
