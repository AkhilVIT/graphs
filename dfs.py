#User function Template for python3

class Solution:
    visited=[]
    stk=[0]
    res=[]
    def dfsOfGraph(self, V, adj):
        while self.stk:
            c = self.stk.pop()
            self.visited.append(c)
            self.res.append(c)
            for neib in adj[c]:
                if neib not in self.visited:
                    self.stk.append(neib)
                self.dfsOfGraph(V,adj)
        return self.res





#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
        ob = Solution()
		ans = ob.dfsOfGraph(V, adj)
		for i in range(len(ans)):
			print(ans[i], end = " ")
		print()
        

# } Driver Code Ends
