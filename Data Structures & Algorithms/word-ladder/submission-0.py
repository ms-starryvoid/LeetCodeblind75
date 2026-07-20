class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns=defaultdict(list)
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                patterns[pattern].append(word)
        q=deque([beginWord])
        visited={beginWord}
        steps=1
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return steps
                for i in range(len(word)):
                    pattern=word[:i]+"*"+word[i+1:]
                    for nei in patterns[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            steps+=1
        return 0

