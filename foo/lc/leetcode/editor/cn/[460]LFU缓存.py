# Design and implement a data structure for Least Frequently Used (LFU) cache. I
# t should support the following operations: get and put. 
# 
#  get(key) - Get the value (will always be positive) of the key if the key exis
# ts in the cache, otherwise return -1. 
# put(key, value) - Set or insert the value if the key is not already present. W
# hen the cache reaches its capacity, it should invalidate the least frequently us
# ed item before inserting a new item. For the purpose of this problem, when there
#  is a tie (i.e., two or more keys that have the same frequency), the least recen
# tly used key would be evicted. 
# 
#  Note that the number of times an item is used is the number of calls to the g
# et and put functions for that item since it was inserted. This number is set to 
# zero when the item is removed. 
# 
#  
# 
#  Follow up: 
# Could you do both operations in O(1) time complexity? 
# 
#  
# 
#  Example: 
# 
#  
# LFUCache cache = new LFUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#  
# 
#  
#  Related Topics 设计


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Node:
    def __init__(self, key:int, value: int, pre=None, next=None, freq=0):
        self.key = key
        self.value = value
        self.freq = freq
        self.pre = pre
        self.next = next

    # 插入到此节点后面
    def insert(self, next):
        next.pre = self
        next.next = self.next
        self.next.pre = next
        self.next = next

def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.next = tail
    tail.pre = head
    return (head, tail)


class LFUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.size = 0
        self.cur_min_frequency = 0
        self.count_map = collections.defaultdict(create_linked_list) # 默认dict(), 双向链表map，v为双向链表尾部的引用
        self.key_map = dict()

    def delete(self, node):
        # 从key_map中删除
        if node.pre:
            node.pre.next = node.next
            node.next.pre = node.pre
            # 每个双向链表都有一个首尾哨兵节点，此处判断是否除了哨兵节点外无其他节点,则删除此整条双向链表
            if node.pre is self.count_map[node.freq][0] and node.next is self.count_map[node.freq][-1]:
                self.count_map.pop(node.freq)
        return node.key

    def put(self, key: int, value: int) -> None:
        if self.max_capacity != 0:
            if key in self.key_map:
                node = self.key_map[key]
                node.value = value
            else:
                node = Node(key, value)
                # 为什么不用操作count_map, 因为increase方法会处理节点的移动
                self.key_map[key] = node
                self.size += 1
            if self.size > self.max_capacity:
                self.size -= 1
                delete_node = self.delete(self.count_map[self.cur_min_frequency][0].next) # 头部后的是最老使用的
                self.key_map.pop(delete_node)
            self.increase(node)

    def get(self, key: int) -> int:
        if key in self.key_map:
            # 增加使用频率
            self.increase(self.key_map[key])
            return self.key_map[key].value
        return -1

    def increase(self, node):
        node.freq += 1
        # delete node from original freq list, and add to freq+1 list
        self.delete(node)
        # 此dict会默认创建value为首尾节点
        self.count_map[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.cur_min_frequency = 1
        # if node.freq exceed the cur_min
        elif self.cur_min_frequency == node.freq - 1:
            # 取出最小频率的首尾节点
            head, tail = self.count_map[self.cur_min_frequency]
            # if list of min_fre is empty(exclude dummy node), then change the min_cur to node.freq
            if head.next is tail:
                self.cur_min_frequency = node.freq



# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
obj.put(1,1)
obj.put(2,2)
param_1 = obj.get(1)

a = dict()
a[1] = 1
print(a)

# leetcode submit region end(Prohibit modification and deletion)
