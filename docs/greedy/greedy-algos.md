# Opis

Za pomocą takich algorytmów możemy rozwiązujemy zazwyczaj zadania optymalizacyjne. Przykładowo, mamy jakiś skończony zbiór X, a odpowiedzią jest jakiś podzbiór zbioru X.

Algorytmy zachłanne to na przykład [algorytmy wyznaczające MST](https://aisd-notatki.readthedocs.io/en/latest/mdl/md/).

# Dowody

Poprawność algorytmów zachłannych praktycznie zawsze (nie znam innych przypadków) rozwiązuje się poprzez wzięcie optymalnego rozwiązania (zawsze jakieś istnieje) i porównanie tego, co wypluł nasz algorytm z rozwiązaniem optymalnym. Pokazujemy, że jest to takie samo lub tak samo optymalne rozwiązanie. Intuicja co do wyboru kryterium optymalizacji jest taka, że powinno być ono proste - np. bierzemy tylko najmniejsze elementy, tylko największe, najbardziej opłacalne, coś prostego do sprawdzania.

# Problem wydawania reszty

Przykładem zadania, które pokazuje czym jest strategia zachłanna jest problem wydawania reszty. Rozwiązaniem tego zadania dla zbioru nominałów C = {1, 2, 5, 10, 20, 50, 100} jest wybieranie największego nominału, który nie przekracza kwoty pozostałej do wydania.

Dowód dla sportu:

Fakt:
C[i] >= C[i-1]/2 dla i >= 1 (zbiór indeksowany od 0)

1. pokażemy, że algorytm zawsze zwraca rozwiązanie
2. pokażemy, że rozwiązanie algorytmu jest takie samo/tak samo dobre jak rozwiązanie optymalne

ad 1. W każdym kroku algorytmu, zmniejsza się pozostała do wydania kwota. Algorytm nie zakończy działa, kiedy ta kwota > 0, bo dopchałby jedynkami. Kwota nie spadnie poniżej 0, ponieważ algorytm wybiera nominały <= kwota wydania  
ad 2. Opt = { o1, o2, ... o_k }  
 Alg = { a1, a2, ... a_l }  
 bez straty ogólności, zakładamy że zbiory te są posortowane nierosnąco  
 a) l < k => sprzeczność, Opt nie jest optymalny  
 b) l = k => rozwiązanie algorytmu jest optymalne  
 c) l > k => weźmy pierwszy indeks, na którym rozwiązania się różnią, niech będzie to j.  
 o_j = a_j => sprzeczność, mały się różnić  
 o_j > a_j => sprzeczność, algorytm zawsze wybiera największy mieszczący się nominał, zatem rozwiązanie optymalne byłoby błędne (za dużo wydanej reszty)  
 o_j < a_j => wiemy, że o_j jest co najmniej 2 razy mniejszy od a_j. zakładając, że mamy do wydania Q i możemy użyć do tego a_j, a tego nie robimy, to znaczy że rozwiązanie optymalne używa co najmniej dwóch nominałów, aby pokryć wartość a_j i nie więcej, tj. dwa mniejsze nominały dają nam najwyżej a_j. to znaczy, że rozwiązanie optymalne może być prostsze, używając a_j. próba optymalniejszego pokrycia reszty nie używając a_j byłaby nieoptymalna - dwa nominały dają nam najwyżej a_j, a próbę pokrycia większej wartości, tj. 2 nominały + coś, łatwiej zapisać jako a_j + coś. sprzeczność.  
Zatem l = k, nasze rozwiązanie jest optymalne.

Nie wiem czy ten ostatni podpunkt jest dobrze udowodniony, ale to będzie coś w tym stylu. Musimy użyć jakiejś własności tego zbioru w dowodzie, bo algorytm zachłanny nie zawsze daje optymalne rozwiązanie problemu wydawania reszty, jednak w przypadku naszego zbioru daje. Pewnie dałoby się udowodnić, że dla każdego zbioru, gdzie C[0] = 1 i C[i+1] >= 2\*C[i] ten algorytm daje wynik optymalny. W sumie to chyba nawet ten dowód to udowadnia, jakby ładnie go dupnąć w formie dowodu indukcyjnego.

# Problem szeregowania zadań

Problem 1:  
Mamy taski i hcemy zminimalizować czas przebywania tych tasków w systemie, tzn. wykonać jak najwięcej jak najszybciej. Intuicyjnie, taski wykonujemy od najkrótszego.

Dowód z notatek Lorysia, uwaga bo u niego t oznacza czas wykonania taska, np t1 to czas wykonania 1 zadania.
![](images/szeregowanie-1.png)

Problem 2:
TODO, doczytać

# Problem pokrycia zbioru

NP-trudny! Możemy jednak stworzyć algorytm aproksymacyjny korzystając ze strategii zachłannej, który będzie bliski optymalnemu.
TODO! :)
