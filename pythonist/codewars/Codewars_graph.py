import string
class Solution:
    def countSubTrees(self, n, edges, labels):
        adj = [[] for _ in range(n)]

        for a, b in edges:
            
            adj[a].append(b)
            adj[b].append(a)

        count = [0]*len(string.ascii_lowercase)
        answer = [0]*n
        print(adj)

        def dfs(node, parent):
            index = ord(labels[node]) - ord('a')
            previous = count[index]
            
            count[index] += 1
            print(adj[node])
            print(index)
            print(count)
            for child in adj[node]:
                if child != parent:
                    dfs(child,node)
            answer[node] = count[index] - previous
        dfs(0,-1)
        return answer

    
def main():
    
    a=Solution()
    print(a.countSubTrees(4,[[0,1],[1,2],[0,3]],"bbbb"))



if __name__ == "__main__":
    main()




#
