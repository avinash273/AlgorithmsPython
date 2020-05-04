from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.append(7)

print(*queue, sep="->")
x = queue.popleft()
print(x)
print(*queue, sep="->")