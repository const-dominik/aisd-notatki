# Opis

Ta notatka podsumowuje najpopularniejsze algorytmy sortujące, ze szczególnym pochyleniem na algorytmy, nad którymi Loryś szczególnie się pochylił prowadząc wykład.

# Algorytmy !!O(n^2)!!

Nie są dla nas zbyt ważne.

### Sortowanie bąbelkowe (bubble sort)

Najprostszy istniejący algorytm sortujący. Polega na przechodzeniu po zbiorze, porównując ze sobą każde dwa elementy i zamieniając je, jeśli są w złej kolejności.

```python
def bubble_sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)- i - 1):
            if (tab[j] > tab[j+1]):
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

```

### Sortowanie przez wstawianie (insertion sort)

Polega na przechodzeniu po kolejnych elementach, a będac na indeksie i+1-ym, wszystko do i powinno być posortowane. Zatem rozważając i+1-y element, idziemy z nim do tyłu, szukając dla niego odpowiedniego miejsca (takiego że tab[k-1] <= tab[i] i tab[k+1] >= tab[i]).

```python
def insertion_sort(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i - 1
        for k in range(i, 0, -1):
            if tab[k-1] > key:
                tab[k] = tab[k-1]
                j = k - 1
            else:
                break
        tab[j + 1] = key
    return tab
```

### Sortowanie przez selekcję (selection sort)

Polega na przechodzeniu po tablicy i znajdowaniu minimum (lub maximum, ale zakładam że bierzemy sobie minimum), które po zakończeniu przejścia wstawiamy na początek tablicy. Wtedy zawsze początku mamy już posortowane elementy i skupiamy się na nieposortowanej części.

```python
def selection_sort(tab):
    for i in range(len(tab)):
        for j in range(i, len(tab)-1):
            if tab[j+1] < tab[i]:
                tab[i], tab[j+1] = tab[j+1], tab[i]

    return tab
```

# Algorytmy !!O(n \log n)!!

Są dla nas ważne.

### Sortowanie przez kopcowanie (heap sort)

Jak napisałem w notatce o kopcach, gdzie dostępna jest także cała implementacja kopca:

Szybki algorytm sortujący przy użyciu kopca, O(n log n). Na chłopski rozum - robimy kopiec minimalny z tablicy (O(n)), a później usuwamy z niego korzeń i dodajemy go do tablicy posortowanych. Usunięcie zakłada przywrócenie własności kopca (log n). Tak robimy aż skończy nam sie kopiec.

```python
    def heap_sort(self, tab: List[int]) -> List[int]:
        self.heapify_fast(tab)
        sorted_list = []
        original_size = self.size
        for _ in range(original_size):
            sorted_list.append(self.extract_min())
        return sorted_list
```

### Sortowanie przez scalanie (merge sort)

Używa strategii dziel i zwyciężaj, został wspomniany w notatce na temat tej metody. Polega na dzieleniu tablicy na połówki, tak długo aż dojdziemy do tablicy 1-elementowej, która już jest posortowana. Następnie musimy ją zmergować.

```python
# żywcem z geeksforgeeks
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
```

Dzielenie tablicy to !!\log n !!, scalamy w !!n!!, wychodzimy !!O(n \log n)!!

### Sortowanie szybkie (quicksort)

[filmik Computerphile, fajny, 3min](https://www.youtube.com/watch?v=XE4VP_8Y0BU)  
Także korzysta ze strategii dziel i zwyciężaj. Żeby uniknąć najgorszego przypadku, musimy dobrze wybierać pivota, a także dobrze dzielić naszą tablicę. W notatkach pana Lorysia jest to fajnie opisane, więc posłużę się jego pseudokodami, a jak ogarniemy jak dobrze dzielić/wybierać pivota to wrzucę działającą implementację w Pythonie.

Więc generalnie tak będzie wyglądać nasza procedura quicksort:
![alt text](images/qs1.png)

A tak partition:
![alt text](images/qs2.png)  
Co się tutaj dzieje? Otóż: dla prostoty zapisujemy w !!x!! wartość pivota, a następnie analizujemy !!A[p \dots r]!!. W każdym obrocie pętli while, szukamy elementu który jest mniejszy od pivota a jest po jego prawej stronie oraz elementu, który jest od pivota większy, a jest po lewej. Jeżeli takie elementy znaleźliśmy, to zamieniamy je miejscami. Jeśli !!i \geq j!!, to zwracamy !!j!!. Wiemy, że w !!A[p \dots j]!! znajdują się elementy !!\leq A[p]!!, a w !!A[j+1 \dots r]!! elementy !! \geq A[p]!!.

Teraz ważne pytanie, na które nie ma jednoznacznej odpowiedzi - w jaki sposób wybierać pivota? Dla prostoty możemy wybierać zawsze pierwszy/ostatni element, ale wtedy, tak jak było pokazane w filmiku Computerphile, algorytm może nam się zkwadracić.

Warto wspomnieć, że każda z wybranych metod ma swoje wady i zalety.

Metoda 1 to wybór deterministyczny, czyli pierwszy/ostatni element.  
Zalety: prostota  
Wady: dla posortowanych w jakimś stopniu danych łatwo się kwadraci

Metoda 2 to wybór losowy.  
Zalety: prostota, nie obchodzi nas w jakim stanie przychodzą dane  
Wady: nadal może się zkwadracić, ale szansa jest zaniedbywalnie mała

Metoda 3 to mediana.  
Jednak nie z całego zbioru - wyliczenie tego jest nieopłacalne złożonościowo w algorytmie. Wybieramy 3 losowe elementy i wybieramy ich medianę. To znacząco zmniejsza szansę na zkwadracenie się algorytmu - musielibyśmy trafić np. na 3 bardzo małe wartości w sortowanej tablicy, szansa na zkwadracenie jest tym mniejsza im większy jest zbiór, a tym samym tym większa im mniejszy jest zbiór - ale jak zbiór jest mały, to bardzo nie ucierpimy na tym kwadracie.

Teraz implementacja, a później niestety analiza złożoności.

```python
import random

def quicksort(tab):
    # używamy metody 3
    def choose_pivot(tab, p, r):
        p1, p2, p3 = list(map(lambda _: random.randint(p, r), [None]*3))
        if p1 > p2 and p2 > p3:
            return p2
        if p2 > p1 and p1 > p3:
            return p1
        return p3

    def partition(tab, p, r, pivot):
        x = tab[pivot]
        i = p - 1
        j = r + 1

        while i < j:
            while True:
                j -= 1
                if tab[j] <= x:
                    break
            while True:
                i += 1
                if tab[i] >= x:
                    break
            if i < j:
                tab[i], tab[j] = tab[j], tab[i]
            else:
                return j


    def quicksort2(tab, p, r):
        if p < r:
            pivot = choose_pivot(tab, p, r)
            q = partition(tab, p, r, pivot)
            quicksort2(tab, p, q)
            quicksort2(tab, q+1, r)

    quicksort2(tab, 0, len(tab)-1)
```

#### Analiza złożoności

Dla uproszczenia zakładamy, że elementy tablicy są różne.
!!n = r - p + 1!! - liczba elementów w !!A[p \dots r]!!. Definiujemy też funkcję:
$$ rank(x, A[p \dots r]) = | \\{j \colon p \leq j \leq r \text{ i } A[j] \leq x\\}|$$
Funkcja ta mówi nam, ile elementów w !!A[p \dots r]!! jest mniejszych bądź równych !!x!!.
