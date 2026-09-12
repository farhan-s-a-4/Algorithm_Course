from sys import stdin, stdout

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI():
    return list(map(int, stdin.readline().split()))
def SI():
    return stdin.readline().strip()
def SLI():
    return list(stdin.readline().split())

class Node:
    def __init__(self, end):
        self.end = end
        self.next = [None] * 29

class tridata:
    def __init__(self):
        self.Head = Node(0)

    def get_key(self, a):
        if a == " ":
            return 26
        elif a == ".":
            return 27
        elif a == "-":
            return 28
        else:
            return ord(a) - ord("a")
    def add(self, name):
        name = name.lower()
        curr = self.Head
        l = len(name) - 1
        for ind, a in enumerate(name):
            key = self.get_key(a)
            if curr.next[key] is None:
                curr.next[key] = Node(0)
                if ind == l:
                    curr.end += 1
                else:
                    curr = curr.next[key]
            else:
                if ind == l:
                    curr.end += 1
                else:
                    curr = curr.next[key]

    def delete(self, name):
        name = name.lower()
        curr = self.Head
        l = len(name) - 1
        for ind, a in enumerate(name):
            key = self.get_key(a)
            if curr.next[key] is None:
                return -1
            elif ind == l:
                if curr.end == 0:
                    return -1
                curr.end -= 1
                return 0
            else:
                curr = curr.next[key]
class solution:
    def __init__(self):
        boy, girl = [0]*26, [0]*26
        boys, girls = tridata(), tridata()
        while True:
            data = SLI()
            if data[0] == "0":
                exit()
            elif data[0] == "1":
                initial = data[1][0]
                if data[2] == "1":
                    boys.add(data[1])
                    boy[ord(initial) - ord('A')] += 1
                else:
                    girls.add(data[1])
                    girl[ord(initial) - ord('A')] += 1
            elif data[0] == "2":
                x = boys.delete(data[1])
                if x == 0:
                    boy[ord(data[1][0]) - ord('A')] -= 1
                else:
                    girls.delete(data[1])
                    girl[ord(data[1][0]) - ord('A')] -= 1
            elif data[0] == "3":
                start = ord(data[1][0]) - ord('A')
                end = ord(data[2][0]) - ord('A')
                if data[3] == "0":
                    stdout.write(f"{sum(boy[start:end]) + sum(girl[start:end])} \n")
                elif data[3] == "1":
                    stdout.write(f"{sum(boy[start:end])} \n")
                elif data[3] == "2":
                    stdout.write(f"{sum(girl[start:end])} \n")
if __name__ == "__main__":
    solution()