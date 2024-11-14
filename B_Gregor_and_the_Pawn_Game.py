import sys
from math import ceil, inf
from collections import defaultdict , Counter
from bisect import bisect_left , bisect_right
mod = pow(10, 9) + 7

def ip():
  return int(input())

def input():
  return sys.stdin.readline().strip()

def readList():
  return list(map(int,input().split()))

def solve():
  n , m = readList()
  graph = defaultdict(list)

  for _ in range(m):
    u , v = readList()
    graph[u].append(v)
    graph[v].append(u)
  
  visited = [0] * n
  total  = 0
  
  def dfs(vertex):

    edges = set()
    counter = Counter()
    vertices = 0
    stack = [vertex]
    visited[vertex - 1] = 1

    while stack:
      vertex = stack.pop()
      
      vertices += 1
      for neighbor in graph[vertex]:
        counter[vertex] += 1
        counter[neighbor] += 1
        edges.add(tuple(sorted([vertex , neighbor])))
        if visited[neighbor - 1] == 0:
          visited[neighbor - 1] = 1
          stack.append(neighbor)

    return vertices == len(edges) and len(set(counter.values())) == 1
    
  for i in range(1 , n + 1):
    if visited[i - 1] == 0:
      total += dfs(i)
      print()
  
  print(total)
    

# T = int(input())
T = 1

for _ in range(T):
  solve()




