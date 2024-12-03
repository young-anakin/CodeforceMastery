# n, m , k = list(map(int, input().split(" ")))
# colors = list(map(int, input().split(" ")))
from collections import Counter
class UnionFind:
    def __init__(self, size):
        # Initially, each element is its own parent (self loop) and the rank is 1
        
        self.parent = list(range(size))
        self.rank = [1] * size
        # self.counter = cp
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

    def union(self, x, y, bool):
        # Find the root of the sets that x and y belong to
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank heuristic: attach the shorter tree under the root of the taller tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                if bool == True:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1
                else:
                    self.parent[rootX] = rootY
                    self.rank[rootY] +=1
        print(self.parent)

    def connected(self, x, y):
        # Check if x and y are in the same subset
        return self.find(x) == self.find(y)

# Example usage:
def solve():
    # Example problem using Union-Find
    n, m, k = list(map(int, input().split(" ")))  # Number of elements and number of union operations
    arr = list(map(int, input().split(" ")))
    uf = UnionFind(n+1)

    count = Counter(arr)
    # for ind, val in enumerate(arr):
    #     uf.union()

    cp = 0
    for _ in range(m):
        u, v = map(int, input().split())
        if arr[u-1] == arr[v-1]:
            cp +=0
        else:
            x, y = uf.find(u), uf.find(v)
            if not uf.connected(u, v):
                cp +=1    

        # if uf.rank[x] == uf.rank[y]:
            # F T
            if count[arr[u-1]] <= count[arr[v-1]]:
                uf.union(u, v, False)
            else:
                uf.union(u, v, True)
            x = count[arr[u-1]] + count[arr[v-1]]
            count[arr[u-1]] = x
            count[arr[v-1]] = x



        # uf.union(u, v)
    print(cp)
    # Example of checking if two elements are connected
    # x, y = map(int, input().split())
    # if uf.connected(x, y):
    #     print("Yes")
    # else:
    #     print("No")

if __name__ == "__main__":
    solve()


# for _ in range(m):
#     u, v  = list(map(int, input().split(" ")))
    