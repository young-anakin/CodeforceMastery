from collections import defaultdict, deque

dd = defaultdict(deque)

dd[0].append(1)
dd[0].append(3)

print(dd[0].popleft())