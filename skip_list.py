import random


class SkipListNode:
    def __init__(self, value=None, level=1):
        self.value = value
        self.forward = [None] * level


class SkipList:
    def __init__(self, max_level=16, probability=0.2):
        self.max_level = max_level
        self.probability = probability
        self.header = SkipListNode(level=max_level)
        self.level = 1

    def random_level(self):
        level = 1
        while random.random() < self.probability and level < self.max_level:
            level += 1
        return level

    def skip_list_insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current is None or current.value != value:
            new_level = self.random_level()
            if new_level > self.level:
                for i in range(self.level, new_level):
                    update[i] = self.header
                self.level = new_level
            node = SkipListNode(value, new_level)
            for i in range(new_level):
                node.forward[i] = update[i].forward[i]
                update[i].forward[i] = node

    def skip_list_search(self, value):
        current = self.header
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.value == value:
            return True
        return False

    def skip_list_delete(self, value):
        update = [None] * self.max_level
        current = self.header
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.value == value:
            for i in range(self.level):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while self.level > 1 and self.header.forward[self.level - 1] is None:
                self.level -= 1
