from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        for i in range(0, len(votes)):
            s = votes[i]
            for j in range(0, len(s)):
                a = s[j]




