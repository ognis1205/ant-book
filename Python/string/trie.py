import sys


class Node:
    def __init__(self, value=None, count=0):
        self.value = value
        self.count = count
        self.children = {}

    def __str__(self):
        return f'Node("{self.value}", {self.count})'

    def __repr__(self):
        return f'Node("{self.value}", {self.count})'


class Trie:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def dfs(node, acc):
        if node.value is not None:
            acc.append(node)
        for c in node.children.values():
            Trie.dfs(c, acc)

    def insert(self, value):
        node = self.root
        for c in value:
            node = node.children.setdefault(c, Node())
        node.value = value
        node.count += 1

    def query(self, value):
        ret, node = [], self.root
        for c in value:
            node = node.children.get(c)
            if node is None:
                return ret
        Trie.dfs(node, ret)
        return ret


if __name__ == '__main__':
    trie = Trie()
    while line := sys.stdin.readline():
        trie.insert(line.strip())
    print(trie.query('wh'))
