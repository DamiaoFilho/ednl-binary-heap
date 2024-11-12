class BinaryItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}:{self.value}"

class BinaryHeap:

    def __init__(self):
        self.array: list[BinaryItem] = []
        self.array.append(float("inf"))

    def insert(self, key, value) -> None:
        self.array.append(BinaryItem(key, value))
        self.up(len(self.array) - 1)
        self.display_heap()

    def remove(self):
        self.array[1] = self.array.pop()
        self.down(1)

    def change_priority(self, index, new_priority):
        self.array[index].key = new_priority
        self.arrange(len(self.array) - 1)

    def get_high_priority(self):
        return self.array[1]
    
    def up(self, i) -> None:

        j = i // 2

        if j >= 1:
            if self.array[i].key > self.array[j].key:
                self.swap(i, j)
                self.up(j)

    def down(self, i) -> None:

        j = i * 2

        if j <= len(self.array) - 1:

            if j < len(self.array) - 1:
                if self.array[j+1].key > self.array[j].key:
                    j += 1
            
            if self.array[i].key < self.array[j].key:
                self.swap(i, j)
                self.down(j)

    def arrange(self, n):
        i = n // 2
        while i != 0:
            self.down(i)
            i -= 1

    def heap_sort(self, n=None):
        if not n:
            n = len(self.array) - 1

        self.arrange(n)
        m = n
        while m > 1:
            print(f"{m-1} organizações a serem feitas")

            self.swap(1, m)
            m -= 1
            self.down(1)

            self.display_heap()

    def display_heap(self):
        for i in self.array:
            if type(i) != float:
                print(i.key)

    def swap(self, element, parent):
        aux = self.array[element]
        self.array[element] = self.array[parent]
        self.array[parent] = aux

