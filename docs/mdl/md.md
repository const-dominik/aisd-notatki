Niestety, do AiSDu potrzebujemy zagadnień z matematyki dyskretnej. Ta sekcja skupi się na podsumowaniu ważniejszych rzeczy z MD, które są potrzebne na AiSD.

##

Oznaczenia:  
G = (V, E; c) - graf nieskierowany, gdzie V to zbiór wierzchołków, E to zbiór krawędzi, a c to funkcja wagowa (tj. c(edge) => number).

# Minimalne drzewo rozpinające (MST)

Formalnie:  
Drzewem rozpinającym grafu G = (V, E; c) nazywamy dowolne drzewo T = (V, E'),
takie, że E' ⊆ E. Drzewo rozpinające T nazywamy minimalnym, je±li ma minimalną wagę spośród
wszystkich drzew rozpinających grafu G.

Nieformalnie:
Drzewo rozpianające G to takie poddrzewo, że z każdego wierzchołka, po krawędziach możemy dotrzeć do każdego innego wierzchołka.
Minimalne drzewo rozpinające to takie drzewo rozpinające, że suma wag na krawędziach jest najmniejsza wśród poddrzew będących rozpinającymi.

Algorytmy wyznaczania MST:  
sprowadzają się do znalezienia podzbioru krawędzi, są to algorytmy zachłanne

1. algorytm Kruskala  
   W każdym kroku algorytmu do zbioru E' dodajemy krawędź z najmniejszą wagą, o ile dodanie jej nie powoduje powstania cyklu. Kończymy kiedy G = (V, E') jest drzewem rozpinającym. Tak stworzony G jest MST.

2. algorytm Prima  
   Wybieramy jakiś wierzchołek v i dodajemy do E' najlżejszą krawędź incydentną z v. Następnie rozważamy pozostałe krawędzie, wybieramy minimalną z tych, które są incydentne z którąś z krawędzi z E', o ile drugi jej koniec nie znajduje się także w E'.

3. algorytm Boruvki  
   Dla każdego wierzchołka z V, do E' dodajemy najlżejszą krawędź incydentną do tego wierzchołka. W ten sposób otrzymujemy graf, który nie musi być spójny. Jeżeli jest spójny, to mamy MST. Jeśli nie, to spójne składowe możemy potraktować jako superwierzchołek (tj. z składowej robimy pojedynczy wierzchołek, który ma incydentne wszystkie krawędzie, które są incydentne z wierzchołkami należącymi do tej spójnej składowej). Dla tych superwierzchołków powtarzamy krok 1 algorytmu, tj. do E' dodajemy najlżejsze krawędzie incydentne z tymi superwierzchołkami.

# Liczba Catalana

Wzór jawny:  
!!c_n = \frac{1}{n+1} {2n \choose n} = \frac{(2n!)}{(n+1)!n!}!!

Wzór rekurencyjny:
!!c_0 = 1; c_n = c_0 \cdot c\_{n-1} + c_1 \cdot c{n-2} + ... + c\_{n-2} \cdot c_1 + c\_{n-1} \cdot c_0 = \sum\_{i=0}^{n-1} c_i \cdot c\_{n-1-i}!!

Co opisuje ta liczba? Na przykład liczbę poprawnych rozmieszczeń nawiasów. Na AiSD chyba wystarczy wiedzieć, że jak coś ma złożoność liczby Catalana, to nie jest kolorowo.

# Algorytm Floyda-Warshalla

Znajduje najkrótsze ścieżki pomiędzy wszystkimi wierzchołkami w grafie.
Korzysta z faktu, że jeśli ścieżka pomiędzy dwoma wierzchołkami prowadzi przez wierzchołek !!u!!, to jest ona połączeniem najkrótszych scieżek pomiędzy pierwszym wierzchołkiem a !!u!! i !!u!! do drugiego wierzchołka.

Zaczynamy od zwykłej macierzy, gdzie M[v1,v2] = 0 jeśli v1=v2, jeżeli istnieje między nimi krawędź to wstawiamy jej wagę, a jeśli nie istnieje to dajemy nieskończoność. Następnie dynamicznie wypełniamy naszą macierz, zakładając że przechodzimy przez !!i!!-ty wierzchołek. Np. w macierzy !!A^1!!, szukając najkrótszej drogi z 2 do 3, sprawdzimy czy krótsza jest obecna droga, czy może przejście z 2 do 1, a z 1 do 3. Powtarzamy aż skończą nam się wierzchołki.

Filmik: [Abdul Bari](https://www.youtube.com/watch?v=oNI0rf2P9gE)

# Słowniczek

Drzewo - acykliczny graf spójny  
Las - acykliczny graf, którego spójnymi składowymi są drzewa  
Drzewo rozpinające - drzewo, które zawiera wszystkie wierzchołki grafu, a krawędzie są podzbiorem krawędzi grafu  
Digraf - graf skierowany
