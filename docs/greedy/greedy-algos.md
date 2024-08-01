Za pomocą takich algorytmów możemy rozwiązujemy zazwyczaj zadania optymalizacyjne. Przykładowo, mamy jakiś skończony zbiór X, a odpowiedzią jest jakiś podzbiór zbioru X.

Przykładem zadania, które pokazuje czym jest strategia zachłanna jest problem wydawania reszty. Rozwiązaniem tego zadania dla zbioru nominałów C = {1, 2, 5, 10, 20, 50, 100} jest wybieranie największego nominału, który nie przekracza kwoty pozostałej do wydania.

Dowód dla sportu (nie ufać, pierwszy jaki piszę od ponad roku):

Fakt:
C[i] możemy wyrazić przy użyciu co najmniej 2 mniejszych nominałów.

1. pokażemy, że algorytm zawsze zwraca rozwiązanie
2. pokażemy, że rozwiązanie algorytmu jest takie samo/tak samo dobre jak rozwiązanie optymalne

3. W każdym kroku algorytmu, zmniejsza się pozostała do wydania kwota. Algorytm nie zakończy działa, kiedy ta kwota > 0, bo dopchałby jedynkami. Kwota nie spadnie poniżej 0, ponieważ algorytm wybiera nominały <= kwota wydania
4. Opt = { o1, o2, ... o_k }  
   Alg = { a1, a2, ... a_l }  
   bez straty ogólności, zakładamy że zbiory te są posortowane nierosnąco  
   a) l < k => sprzeczność, Opt nie jest optymalny  
   b) l = k => rozwiązanie algorytmu jest optymalne  
   c) l > k => weźmy pierwszy indeks, na którym rozwiązania się różnią, niech będzie to j.  
    o_j = a_j => sprzeczność, mały się różnić  
    o_j > a_j => sprzeczność, algorytm zawsze wybiera największy mieszczący się nominał, zatem rozwiązanie optymalne byłoby błędne (za dużo wydanej reszty)  
    o_j < a_j => suma o_j, ... o_k jest równa sumie a_j, ... a_k. mamy do wydania jeszcze jakieś Q = suma(a_j, ...a_l). weźmy S = Q - a_j. zatem o_j, ... o_k wydaje S + a_j, jednak nie używa wartości a_j - z faktu, do wydania tej wartości musi użyć większej ilości mniejszych nominałów, zatem opt nie jest optymalny, bo mógł użyć a_j minimalizując liczbę wydanych nominałów - **chyba źle** -> S+a_j może być lepiej wydawalne przy użyciu mniejszych wartości, np gdyby C = { 100, 75, 1 } a Q = 150
