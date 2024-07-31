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
