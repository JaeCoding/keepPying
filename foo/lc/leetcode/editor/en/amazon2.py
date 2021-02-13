class Solution:
    def routerPairs(self, maxTraveDist, forwardRouteList, returnRouter):
        forwardRouteList.sort()
        returnRouter.sort()
        for item in forwardRouteList:
            toFind = maxTraveDist - item
            if returnRouter[0] >= toFind >= returnRouter[-1]:
                biSearch(toFind, returnRouter)


a = Solution().combinationSum2([2,5,2,1,2], 5)
print(a)