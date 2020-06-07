# Given two words (beginWord and endWord), and a dictionary's word list, find th
# e length of shortest transformation sequence from beginWord to endWord, such tha
# t: 
# 
#  
#  Only one letter can be changed at a time. 
#  Each transformed word must exist in the word list. 
#  
# 
#  Note: 
# 
#  
#  Return 0 if there is no such transformation sequence. 
#  All words have the same length. 
#  All words contain only lowercase alphabetic characters. 
#  You may assume no duplicates in the word list. 
#  You may assume beginWord and endWord are non-empty and are not the same. 
#  
# 
#  Example 1: 
# 
#  
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog
# " -> "cog",
# return its length 5.
#  
# 
#  Example 2: 
# 
#  
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible trans
# formation.
#  
# 
#  
#  
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
import queue
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # 通过建立单词之间的关系图，可以转化图的最短路问题
        step = 1
        all = set(wordList)
        if beginWord in all:
            all.remove(beginWord)

        visited = set()
        visited.add(beginWord)

        q: queue.Queue[str] = queue.Queue()  # queue used to save handing node
        q.put(beginWord)

        while not q.empty():

            for word in list(q.queue):
                for i in range(0, len(word)):

                    for z in range(ord("a"), ord("z") + 1):
                        # replace char at i, to generate the new word, and look whether it in allSet
                        new_word = word[:i] + chr(z) + word[i+1:]
                        if word == new_word:
                            continue
                        if new_word in all:
                            if new_word == endWord: # find the target
                                return step + 1
                            if new_word not in visited:
                                q.put(new_word)
                                visited.add(new_word)
            step += 1
        return 0  # has not find the path


a = Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(a)

        
# leetcode submit region end(Prohibit modification and deletion)
