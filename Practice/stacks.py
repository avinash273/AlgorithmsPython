stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)

print(*stack,sep="->")

stack.pop(3)

print(*stack,sep="->")