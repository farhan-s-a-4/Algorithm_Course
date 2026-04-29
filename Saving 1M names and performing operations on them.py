#This is an example for how to save and then look for names for a dataset of 1M names.
class Node:
    def __init__(self, end):
        self.end = end
        self.next = [None] * 29

class tridata:
    def __init__(self):
        self.Head = Node(0)

    def add(self, name):
        name = name.lower()
        curr = self.Head
        l = len(name) - 1
        for ind, a in enumerate(name):
            if a == " ":
                key = 26
            if a == ".":
                key = 27
            if a == "-":
                key = 28
            else:
                key = ord(a) - ord("a")
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

    def search(self, name):
        name = name.lower()
        curr = self.Head
        l = len(name) - 1
        for ind, a in enumerate(name):
            key = ord(a) - ord("a")
            if curr.next[key] is None:
                print(f"No instances of the name, {name}, was found in the data set!")
                return
            elif ind == l:
                if curr.end == 0:
                    print(f"No instances of the name, {name}, was found in the data set!")
                    return
                print(f"Found {curr.end} instances of the name, {name}, in the data set!")
                return curr.end
            else:
                curr = curr.next[key]

    def delete(self, name):
        name = name.lower()
        curr = self.Head
        l = len(name) - 1
        for ind, a in enumerate(name):
            key = ord(a) - ord("a")
            if curr.next[key] is None:
                print(f"The name, {name}, does not exist in data set!")
                return
            elif ind == l:
                print(f"One instance of the name, {name}, has been deleted from data set!")
                curr.end -= 1
                return
            else:
                curr = curr.next[key]

if __name__ == "__main__":
    NameSet = tridata()
    Names = ["Farhan", "Shariar", "Arnbo", "Farhan", "Farhana", "Sumaya", "Afrin", "Afreen", "Akhtar", "Zaman", "Akhtaruzzaman", "Lipon", "Rikta", "Yeasmin"]
    for name in Names:
        NameSet.add(name)

    while True:
        op = input("What operation would you like to perform? (Search, Delete, Exit)\n").strip().lower()
        if op == "search":
            src = input("What name to look for?\n").strip()
            if src != "-1":
                NameSet.search(src)
            else:
                exit()
        elif op == "delete":
            src = input("What name to delete?\n").strip()
            if src != "-1":
                NameSet.delete(src)
            else:
                exit()
        elif op == "exit":
            exit()