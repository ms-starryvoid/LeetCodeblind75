class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            graph[course].append(pre)

        state=[0]*numCourses
        order=[]
        def dfs(course):
            if state[course]==1:
                return True
            if state[course]==2:
                return False
            state[course]=1
            for pre in graph[course]:
                if dfs(pre):
                    return True
            state[course]=2
            order.append(course)
        for course in range(numCourses):
            if  dfs(course):
                return []
        return order
        
