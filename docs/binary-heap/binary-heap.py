# Key arrangement: node(parent) <= node(child)
from typing import List


class Heap:
    def __init__(self, n: int):
        self.heap = [None]*n
        self.size = 0

    def get_parent(self, i: int):
        return ((i - 1) // 2, self.heap[(i - 1) // 2])

    def get_left_child(self, i: int):
        return (2 * i + 1, self.heap[2 * i + 1])

    def get_right_child(self, i: int):
        return (2 * i + 2, self.heap[2 * i + 2])

    def insert(self, x: int):
        self.heap[self.size] = x
        self.move_up(self.size)
        self.size += 1

    def delete(self, i: int):
        self.size -= 1
        self.heap[i] = self.heap[self.size]
        self.heap[self.size] = None
        self.move_down(i)

    def move_up(self, i: int):
        if i > 0:
            i_parent, parent_val = self.get_parent(i)
            if parent_val > self.heap[i]:
                self.heap[i_parent], self.heap[i] = (
                    self.heap[i], self.heap[i_parent]
                    )
                self.move_up(i_parent)

    def move_down(self, i: int):
        while 2 * i + 1 < self.size:
            i_left, left_val = self.get_left_child(i)
            i_smallest = i_left
            if 2 * i + 2 < self.size:
                _, right_val = self.get_right_child(i)
                if right_val < left_val:
                    i_smallest = 2 * i + 2

            if self.heap[i_smallest] >= self.heap[i]:
                break

            self.heap[i], self.heap[i_smallest] = (
                self.heap[i_smallest], self.heap[i]
                )
            i = i_smallest

    # O(n log n)
    def heapify_slow(self, tab: List[int]):
        self.heap = tab
        self.size = len(tab)
        for i in range(1, len(tab)):
            self.move_up(i)

    # O(n)
    def heapify_fast(self, tab: List[int]):
        self.heap = tab
        self.size = len(tab)
        for i in range(len(tab) // 2 - 1, -1, -1):
            self.move_down(i)

    def extract_min(self):
        if self.size == 0:
            raise IndexError("Heap is empty")
        min_val = self.heap[0]
        self.delete(0)
        return min_val

    def heap_sort(self, tab: List[int]) -> List[int]:
        self.heapify_fast(tab)
        sorted_list = []
        original_size = self.size
        for _ in range(original_size):
            sorted_list.append(self.extract_min())
        return sorted_list

    def heap_sort_2(self, tab: List[int]) -> List[int]:
        self.heapify_fast(tab)
        for i in range(len(tab) - 1, 0, -1):
            tab[0], tab[i] = tab[i], tab[0]
            self.size -= 1
            self.move_down(0)
        return tab
