import random
import math
from operator import itemgetter


#
def Splitdata(data, M, k, seed):
    test = dict()
    train = dict()
    random.seed(seed)
    for user, item in data:
        rdm = random.randint(0, M)
        # 等于k时 加入到数据集
        if rdm == k:
            if user not in test:
                test[user] = set()
            test[user].add(item)

            # test.append([user, item])
        else:
            if user not in train:
                train[user] = set()
            train[user].add(item)

            # train.append([user, item])
    return train, test


def Recall(train, test, N, K):
    hit = 0
    all = 0
    W = UserSimilarity(train)

    for user in train.keys():
        if user in test:
            tu = test[user]
            rank = Recommend(user, train, W, K)
            rk = sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]
            for item, pui in rk:
                if item in tu:
                    hit += 1
            all += len(tu)
    return hit / (all * 1.0)


def Precision(train, test, N, K):
    hit = 0
    all = 0
    W = UserSimilarity(train)

    for user in train.keys:
        tu = test[user]
        rank = Recommend(user, train, W, K)
        rk = sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]
        for item, pui in rk:
            if item in tu:
                hit += 1
        all += N
    return hit / (all * 1.0)


def Coverage(train, test, N, K):
    recommend_items = set()
    all_items = set()
    W = UserSimilarity(train)
    for user in train.keys:
        for item in train[user]:
            all_items.add(item)
        rank = Recommend(user, train, W, K)
        rk = sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]
        for item, pui in rk:
            recommend_items.add(item)
    return len(recommend_items) / (len(all_items) * 1.0)


def popularity(train, test, N, K):
    item_popularity = dict()
    for user, items in train.items():
        for item in items:
            if item not in item_popularity:
                item_popularity[item] = 0
            item_popularity[item] += 1
    ret = 0
    n = 0
    W = UserSimilarity(train)
    for user in train.keys():
        rank = Recommend(user, train, W, K)
        rk = sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]
        for item, pui in rk:
            ret += math.log(1 + item_popularity[item])
            n += 1
    ret /= n * 1.0
    return ret


def UserSimilarity(train):
    item_users = dict()
    # print(train.items())
    for u, items in train.items():
        for i in items:
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

    C = dict()
    N = dict()
    for i, users in item_users.items():
        for u in users:
            if u not in N:
                N[u] = 0
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                if u not in C:
                    C[u] = dict()
                if v not in C[u]:
                    val = 1 / math.log(1 + len(users))
                    C[u].update({v: val})
                else:
                    val = C[u][v] + 1 / math.log(1 + len(users))
                    C[u].update({v: val})

    W = dict()
    for u, related_users in C.items():
        if u not in W:
            W[u] = dict()
        for v, cuv in related_users.items():
            if v not in W[u]:
                val = cuv / math.sqrt(N[u] * N[v])
                W[u].update({v: val})
    return W


def Recommend(user, train, W, K):
    rank = dict()
    interacted_items = train[user]
    li = W[user].items()
    for v, wuv in sorted(W[user].items(), key=itemgetter(1), reverse=True)[0:K]:
        for i in train[v]:
            if i not in interacted_items:
                if (i in rank):
                    rank[i] += wuv
                else:
                    rank[i] = wuv
    return rank


def ItemSimilarity(train):
    C = dict()
    N = dict()
    for u, items in train.items():
        for i in items:
            if i not in N:
                N[i] = 0
            N[i] += 1
            for j in items:
                if i == j:
                    continue
                if i not in C:
                    C[i] = dict()
                if j not in C[i]:
                    val = 1 / math.log(1 + len(items) * 1.0)
                    C[i].update({j: val})
                else:
                    val = C[i][j] + 1 / math.log(1 + len(items) * 1.0)
                    C[i].update({j: val})
    W = dict()
    for i, related_items in C.items():
        for j, cij in related_items.items():
            if i not in W:
                W[i] = dict()

            val = cij / math.sqrt(N[i] * N[j])
            W[i].update({j: val})

    return W


def ItemCFRecommend(train, user_id, W, K):
    rank = dict()
    ru = train[user_id]
    for i in ru:
        for j, wj in sorted(W[i].items(), key=itemgetter(1), reverse=True)[0:K]:
            if j in ru:
                continue
            if j not in rank:
                rank[j] = wj
            else:
                rank[j] += wj
    return rank


def RandomSelectNegativeSample(self, items):
    ret = dict()
    for i in items.keys():
        ret[i] = 1
    n = 0
    # for i in range(0, len(items) * 3):
    #     item = items_


path = 'C:\\Users\\Jae\\Desktop\\高一丹作业\\ratings.csv'
datalines = open(path)
data = []
for line in datalines.readlines():
    arr = line.split(',')
    print(arr)
    data.append((arr[0], arr[1]))

# dict结构 k:userId v:itemId
trn, tst = Splitdata(data, 10, 1, 10)
print(len(trn))
print(len(tst))
itemW = ItemSimilarity(trn)
rk = ItemCFRecommend(trn, '1', itemW, 5)
print(rk)

#
# recall = Recall(trn, tst, 100, 80)
# print('recall: ', recall)
# print 'recall: '+ recall
# Wtmp = UserSimilarity(trn)
# rk = Recommend('1', trn, Wtmp, 3)
# print(rk)

# t = dict()
# t['A'] = 1
# t['B'] = 2
# print(t)
# r = sorted(t.items(), key=itemgetter(1),reverse=True)
# print(r)
# for a1, a2 in r:
#     print(a1,a2)