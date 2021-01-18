#User function Template for python3

class Solution:
    def bfsOfGraph(self, V, adj):
        queue=[0]
        visited=[0]
        res=[]
        while queue:
            c=queue.pop(0)
            res.append(c)
            for neib in adj[c]:
                if neib not in visited:
                    visited.append(neib)
                    queue.append(neib)
        return res       



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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends
