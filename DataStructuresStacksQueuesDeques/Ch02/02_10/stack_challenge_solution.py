class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def match_symbols(symbol_str):
    symbols = {'(': ')', '{': '}', '[': ']'}
    size = len(symbol_str)
    symbolStack = []
    i = 0
    if size == 0:
        return False
    else:
        while i < size:
            if symbol_str[i] in symbols:
                symbolStack.append(symbols[symbol_str[i]])
                print("L:", symbol_str[i])
                print("R:", symbols[symbol_str[i]])
            elif symbolStack[-1] == symbol_str[i]:
                print("Pop: ", symbolStack.pop())
            i += 1

    if (len(symbolStack) == 0):
        return True
    else:
        return False


print(match_symbols('[([{}])]'))
print(match_symbols('{(([{}])]}'))
