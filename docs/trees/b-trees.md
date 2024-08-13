# Opis

Do przechowywania małych słowników, tj. struktury danych umożliwiającej pamiętanie zbioru elementów, na których można wykonywać operacja wstawiania/wyszukiwania/usuwania elementów nadają się drzewa AVL, czerwono-czarne (o których jeszcze będzie) oraz tablice haszujące. Do implementowania dużych słowników idealnie nadają się B-drzewa. Są to zbalansowane drzewa przeszukiwań, zaprojektowane tak, aby operacje były efektywnie wykonywane, gdy są one przechowywane w plikach dyskowych (bo są duże i w jakichś RAMach się nie mieszczą).

Nie wiem od czego jest to B w B-drzewach, ale możemy założyć, że jest to drzewo **B**. dobre dla operacji dyskowych :)

**Przed kontynuacją, warto obejrzeć sobie fajny filmik, żeby mieć ogólne pojęcie czym są B-drzewa, tym samym znacznie!! ułatwiając zrozumienie dalszej części notatki: [filmik](https://www.youtube.com/watch?v=K1a2Bk8NrYQ).**

Warto wiedzieć, a nawet trzeba:

-   wszystkie liście B-drzew leżą na tej samej głębokości,
-   każdy węzeł zawiera wiele elementów zbioru (te są uporządkowane),
-   Michał Anioł nie cierpiał malować Kaplicy Sykstyńskiej i napisał o tym wiersz,
-   nowe elementy zawsze zapamiętywane są w liściach,
-   drzewo rośnie od liści do korzenia - jeśli jakiś węzeł jest pełny, to tworzymy mu brata, który dostaje połowę jego elementów, a środkowy element wędruje ze wskaźnikiem na brata do ojca. Jeżeli zostanie podzielony korzeń, to tworzony jest nowy korzeń, a stary będzie jednym z dwóch jego synów. To jedyny moment, kiedy wysokość B-drzewa wzrasta.

# Formalny opis

Raczej mało ważny, intuicja ważniejsza.

B-drzewo o minimalnym stopniu !!t!! (tzn. że ilość kluczy na węzeł to !![t-1, 2t-1]!!) posiada następujące własności:

1. każdy węzeł !!x!! ma następujące pola
    - !!n!! - ile kluczy jest aktualnie pamiętanych w tym węźle
    - !!2t-1!! pól na klucze, posortowane niemalejąco
    - !!leaf!! - pole logiczne, które mówi czy węzeł jest liściem
    - !!c!! - opcjonalnie, patrz punkt 2., są to wskaźniki do dzieci
2. jeżeli !!x!! jest węzłem wewnętrznym, to ma też !!2t!! pól na wskaźniki do swoich dzieci
3. klucze pamiętane w poddrzewie o korzeniu !!root!! są nie mniejsze od kluczy pamiętanych w drzewie o korzeniu !! < root !! i nie większe od kluczy pamiętanych w poddrzewie o korzeniu !! > root !!
4. Wszystkie liście mają tę sama głębokość, jest to też wysokość drzewa
5. !!t \geq 2!! określa dolną i górną granicę na liczbę kluczy pamiętanych w węzłach:
    - każdy węzeł (oprócz korzenia) musi pamiętać **co najmniej** !!t-1!! kluczy (musi więc mieć co najmniej !!t!! dzieci). Jeżeli drzewo jest niepuste, to korzeń musi pamiętać co najmniej jeden klucz.
    - każdy węzeł może pamiętać co najwyżej !!2t-1!! kluczy (ma zatem co najwyżej !!2t!! dzieci). Węzeł jest pełny gdy ma !!2t-1!! kluczy.

# Operacje na B-drzewach

Musimy o czymś wiedzieć. B-drzewa służą do pamiętania danych na dysku, bo są duże, a przynajmniej istnieją do bycia dużymi. Z ask/so/syk wiemy, że odczytanie danych z dysku nie jest magiczną operacją która wykonuje się w mgnieniu oka, choć może tak być dla niedoświadczonego obserwatora. Dlatego rozważając operacje na B-drzewach, będziemy zwracać uwagę na pamięć wewnętrzną/dyskową. Każdorazowo w pamięci wewnętrznej znajduje się niewielka liczba węzłów i tylko te mogą być przez nas modyfikowane. Po modyfikacji musimy węzeł zapisać na dysku. Przjmujemy też, że próba odczytania danych z dysku nie powoduje żadnej akcji, jeżeli dane które chcemy odczytać są zapakowane do pamięci wewnętrznej.

Liczba operacji na dysku, które są kosztowne, dla przeszukiwania, dodawania oraz usuwania to !!O(h)!!, a dla tworzenia i splitowania !!O(1)!!. To znaczy, że jest super - pamiętajmy, że ze względu na ilość danych w pojedynczym węźle, !!h!! nie jest wcale dużą liczbą w porównaniu do wysokości innych drzew.

Operacje które tutaj przedstawiam to pseudo-python-kod.

### Przeszukiwanie

```python
def B_Tree_Search(x, k):
    # x - węzeł
    # k - szukana wartość
    i = 1
    # dopóki i nie wychodzi poza ilość kluczy w węźle, a k jest większe od klucza, to szukamy dalej
    # dla dużych x.n możemy zastosować binary searcha do tego żeby zoptymalizować
    while i <= x.n and k > x.key[i]:
        i += 1
    # jeżeli nie wyszliśmy poza ilość kluczy w węźle, to sprawdzamy czy klucz się zgadza, jak tak to zwracamy
    if i <= x.n and k == x.key[i]:
        return (x, i)
    else:
        return B_Tree_Search(DISC_READ(x.c[i]), k)

```

!!O(h)!!

### Tworzenie pustego B-drzewa

```python
def B-Tree-Create(T):
    # no wiadomo w C nie jestesmy ale możemy udawać:
    x = ALLOCATE_NODE()
    # jest liściem, nie ma kluczy
    x.leaf = True
    x.n = 0
    # zapisujemy to na dysku i podpinamy korzeń do drzewa
    DISC_WRITE(x)
    T.root = x
```

### Rozdzielenie węzła

Czasem jest potrzebne, jak się przepełni. Przypominam, że przy przepełnieniu węzła, dzielimy gnoja na pół i robimy se takie poddrzewo, że środkowy element staje się ojcem i idzie do góry, a jego dzieci to lewa połowa i prawa połowa, prawie jak lewy i prawy Twix, ale gdybyśmy wiedzieli że lewy Twix jest mniejszy a prawy większy.

```python
def B_Tree_Split_Child(x, i, y):
    # x - ojciec y
    # y - pełny węzeł
    # i - mówi, którym synem x jest y
    z = ALLOCATE_NODE()
    # jeżeli y jest liściem, to jego brat też będzie,
    # a jak nie jest, to jego brat nie będzie
    z.leaf = y.leaf
    # węzeł jest pełny, gdy ma 2t-1 kluczy
    z.n = t -1
    # pętla po [1, t-1] - tak działa range w pythonie
    for j in range(1, t):
        # indeksowanie się kićka bo wiadomo normalnie od 0, w pseudo od 1,
        # chodzi o to, że klucze w nowym węźle to druga połowa kluczy y
        z.key[j] = y.key[j+t]
    if not y.leaf:
        for j in range(1, t+1):
            # jak z to nie liść, to dostaje też drugą połowę wskaźników na dzieci
            z.c[j] = y.c[j+t]
    y.n = t-1
    # shiftujemy wskaźniki na prawo od i, żeby zrobić miejsce na środkowy element y - nowego ojca
    for j in range(x.n + 1, -1, i):
        x.c[j+1] = x.c[j]
    # z staje się i+1-ym dzieckiem w x, i-ty jest y
    x.c[i+1] = z
    # shiftujemy też klucze
    for j in range(x.n, -1, i-1):
        x.key[j+1] = x.key[j]
    # no i i-tym ojcem staje się środkowy gnojek z y-ka
    x.key[i] = y.key[t]
    # x ma klucz więcej! :)
    x.n += 1
    DISC_WRITE(y)
    DISC_WRITE(x)
    DISC_WRITE(z)
```

### Dodawanie klucza

Tą procedurkę dzielimy sobie na dwie - jedna z nich to taki wrapper zapewniający, że drzewo nie jest pełne, a druga to właściwe dodanie. Zakładam w pseudo-python-kodzie że lecimy indeksami od 1.

```python
def B_Tree_Insert(T, k):
    r = T.root
    # dodajemy do korzenia, jeżeli jest on pełny to tworzymy nowego roota
    if r.n == 2*t - 1:
        s = ALLOCATE_NODE()
        T.root = s
        s.leaf = False
        s.n = 0
        s.c[1] = r
        B_Tree_Split_Child(s, 1, r)
        B_Tree_Insert_Nonfull(s, k)
    # a jak nie jest to po prostu dodajemy
    else:
        B_Tree_Insert_Nonfull(r, k)
```

Właściwa procedura:

```python
def B_Tree_Insert_Nonfull(x, k):
    i = x.n
    # wstawiamy tylko do liści
    if x.leaf:
        # przesuwamy klucze od końca, żeby zrobić miejsce dla nowego klucza
        while i >= 1 and k < x.key[i]:
            x.key[i+1] = x.key[i]
            i -= 1
        x.key[i+1] = k
        x.n += 1
        DISC_WRITE(x)
    else:
        # nie jesteśmy w liściu, szukamy ojca który będzie miał wskaźnik
        # tam gdzie powinien się znajdować nowy klucz
        while i >= 1 and k > x.key[i]:
            i -= 1
        i += 1
        DISC_READ(x.c[i])
        # jeżeli węzeł do którego mamy wstawić k jest pełny
        if x.c[i].n == 2*t - 1:
            B_Tree_Split_Child(x, i, x.c[i])
            # jeżeli po podziale k powinno trafić do prawego syna
            if k > x.key[i]:
                i += 1
        B_Tree_Insert_Nonfull(x.c[i], k)

```

### Usuwanie

Oczywiście najgorsze trzeba zrobić samemu. Po pierwsze, będziemy potrzebować procedury która merguje węzły. :( Po drugie, będziemy musieli rozważać różne przypadki. Jest to zadanie które można rozwiązać na przykład podczas rozmrażania zupy, czyli potrzebujemy chwili żeby pomyśleć.

Przypadki:

1. usuwanie liścia:
    - jeśli w węźle jest przynajmniej t kluczy, super, usuwamy
    - jeżeli ma t-1 kluczy, wykonujemy merge i usuwamy ze zmergowanego
2. usuwanie z węzła wewnętrznego:
    - jeżeli ma co najmniej t (dla roota: co najmniej 2):
        - jeżeli lewy/prawy syn mają !!\geq t!! kluczy, to replace maksem lewego lub minimum prawego
        - jeżeli dwójka synów ma !!t-1!! kluczy, to robimy merge lewego i usuwamy z niego co trzeba
    - jeżeli ma t-1 (dla roota: 1) kluczy, wykonujemy merge i usuwamy ze zmergowanego

Implementację merge/replace wrzucę robiąc zadanka na ćwiczenia, bo pewnie trzeba było.
