#  提供一个  a=b b=c a=c
#          a=b b=c a!=c
# input: [ "a=b" "b=c" "a!=c"]
# output: 是否成立


def checkConfilct(input):

    parent = {}
    def findRoot(x):
        # find the root of x and y
        if x not in parent:
            parent[x] = x
        if x != parent[x]:
            parent[x] = findRoot(parent[x])
        return parent[x]
        # A -> B , B ->B

    # Check the condition of "="
    for item in input:
        if item[1] == '=':
            x = item[0]
            y = item[-1]
            rootX = findRoot(x)
            rootY = findRoot(y)
            if rootX != rootY:
                parent[rootX] = rootY

    # Check the condition of "!="
    for item in input:
        if item[1] == '!':
            x = item[0]
            y = item[-1]
            rootX = findRoot(x)
            rootY = findRoot(y)
            if rootX == rootY:
                return False
    return True

input = ["A=B", "B=C", "A!=C"]
print(checkConfilct(input))
input2 = ["A=B", "B=C", "A=C"]
print(checkConfilct(input2))




    # Check the condition of "!="






