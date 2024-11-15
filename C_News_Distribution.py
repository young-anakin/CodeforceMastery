n, m = list(map(int, input().split(" ")))

class UnionFind:
    def __init__(self, size):
        # Initially, each element is its own parent (self loop) and the rank is 1
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        # Iterative path compression
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        
        # Path compression step: make all nodes on the path point directly to the root
        while x != root:
            next_node = self.parent[x]
            self.parent[x] = root
            x = next_node
        
        return root

    def union(self, x, y):
        # Find the root of the sets that x and y belong to
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank heuristic: attach the shorter tree under the root of the taller tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.rank[rootX] +=self.rank[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.rank[rootY] +=self.rank[rootX]

            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += self.rank[rootY]

    def connected(self, x, y):
        # Check if x and y are in the same subset
        return self.find(x) == self.find(y)

# Example usage:
def solve():
    # Example problem using Union-Find
    uf = UnionFind(n+1)
    
    for _ in range(m):
        arr = list(map(int, input().split(" ")))
        k = arr[0]
        if k < 1:
            continue
        arr = arr[1:]
        first = arr[0]
        for ind in range(1, len(arr)):
            # print(first, arr[ind])
            uf.union(arr[ind-1], arr[ind])
        
    ans = []
    for ind in range(1,n+1):
        x = uf.find(ind)
        ans.append(uf.rank[x])
    print(*ans)
    # print(uf.rank)

    # for _ in range(m):
    #     u, v = map(int, input().split())
    #     uf.union(u, v)
    
    # # Example of checking if two elements are connected
    # x, y = map(int, input().split())
    # if uf.connected(x, y):
    #     print("Yes")
    # else:
    #     print("No")

if __name__ == "__main__":
    solve()
    
