# Opis

Dla mnie kopiec (heap) to coś jak BST, ale zamiast być lewo-prawo (lewo - małe, prawo - duże), jest góra-dół (korzeń - duży, liść - mały, lub odwrotnie). Przykładowo, przy kopcu minimalnym, jeśli w korzeniu jest wartość x, to na niższym poziomie będą tylko wartości większe (bądź równe) od x.

Fotka z wikipedii:  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Max-Heap-new.svg/800px-Max-Heap-new.svg.png" width="300px">

Rzeczy do zapamiętania - struktura:

d - wysokość drzewa

-   liście są albo na poziomie d, albo d-1
-   wszystkie liście na poziomie d-1 są najbardziej lewymi węzłami na tym poziomie  
    (oznacza to: poziom x x x x \_ \_ \_ _ jest poprawny, _ x x x x \_ \_ \_ nie jest poprawny, ponieważ mamy przestrzeń z lewej strony)
-   najbardziej prawy węzeł na poziomie d-1 może mieć syna.

Układ:  
Załóżmy, że używamy tablicy K do zapamiętania naszego kopca z n węzłami.  
K[0] -> korzeń  
K[floor(i/2)] -> rodzic  
K[2i+1] -> lewe dziecko  
K[2i+2] -> prawe dziecko

# Kluczowe operacje

Zakładamy kopiec minimalny, tj. w korzeniu jest najmniejszy element kopca.

### Dodawanie elementów (insert):

Kiedy dodajemy nowy element do kopca, umieszczamy go na końcu drzewa (w ostatnim wolnym miejscu w tablicy).
Następnie przesuwamy ten element w górę drzewa, zamieniając go z rodzicem, aż znajdzie się na właściwej pozycji (tzn. nie jest mniejszy od swojego rodzica).

### Usuwanie elementów (delete):

Usuwamy element z korzenia (najmniejszy element w kopcu minimalnym).
Ostatni element w tablicy przesuwamy na miejsce usuniętego elementu.
Następnie przesuwamy ten element w dół drzewa, zamieniając go z mniejszym z jego dzieci, aż znajdzie się na właściwej pozycji.

### Poruszanie się po drzewie (move_up i move_down):

move_up: Przesuwa element w górę drzewa, zamieniając go z rodzicem, jeśli jest mniejszy.
move_down: Przesuwa element w dół drzewa, zamieniając go z mniejszym z jego dzieci, jeśli jest większy.

### Heapify:

heapify_slow: Buduje kopiec dodając i przesuwając każdy element w górę (wolniejsze, ale prostsze podejście).
heapify_fast: Buduje kopiec od dołu (szybsze podejście).

# Heap sort

Szybki algorytm sortujący przy użyciu kopca, O(n log n). Na chłopski rozum - robimy kopiec z tablicy (O(n)), a później usuwamy z niego korzeń i dodajemy go do tablicy posortowanych. Usunięcie zakłada przywrócenie własności kopca (log n). Tak robimy aż skończy nam sie kopiec.

# Implementacja

Moja implementacja kopca (min) i heap sorta:

```python
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
```
