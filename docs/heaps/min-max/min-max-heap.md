# Opis

Kopiec min-maxowy to kopiec, w którym możemy jednocześnie znaleźć/usunąć minimlany i maksymalny element. Giga się nadaje do stworzenia kolejki priorytetowej. Istnieją dwa rodzaje kopców min-maxowych.

## Rodzaj pierwszy: szczepione dupami

Jak wskazuje nazwa tego rodzaju, są to dwa kopce - minimalny i maksymalny, "sklejone" liśćmi.

![](images/min-max-heap.png)

<div style="text-align: center;">
<sup>Obrazek ze skryptu KLo</sup>
</div>

W takim kopcu:

-   kopiec L uporządkowany jest malejąco, a H rosnąco
-   dodatkowy warunek: klucze wszystkich ścieżek z L do H są uporządkowane niemalejąco.

insert(x):  
Ogólnie to zakładając że kopiec jest na n elementów i jest miejsce, to nawet proste. Jeśli nasz kopiec zawiera nieparzystą liczbę elementów, to wstawiamy go do kopca H, a jak nie to do L, na takiej zasadzie jak dodajemy do normalnego kopca. Decyzja czy element przesuwamy niżej czy wyżej. Zatem, jak wstawialiśmy do kopca H, to x jest jakimś elementem na ścieżce. Ścieżka musi być uporządkowana niemalejąco, więc jeśli x jest większy bądź równy następnemu elementowi ścieżki, to przesuwamy go wyżej w stronę korzenia H. Inaczej zamieniamy x z następnym elementem na ścieżce i przesuwamy go wyżej w stronę korzenia L. Chodzi o to, żeby po dodaniu nowego elementu zachowany był dodatkowy warunek (tj. klucze wszystkich ścieżek z L do H są uporządkowane niemalejąco).

usuwanie minimalnego (maks analogicznie):  
Wiadomo, że minimalny element jest w korzeniu L. Usuwamy minimalny i wstawiamy w jego miejsce y - ostatni element kopca L, jeżeli L i H były równoliczne, albo ostatni element kopca H, jeśli był on większy. y przesuwamy niżej. Jeśli przesunęliśmy go aż do liścia, to musimy sprawdzić czy nie powinien być on wyżej - jeśli tak, tj. liść z H, kolejny element ścieżki, jest mniejszy niż y, to zamieniamy y z tym liściem i w kopcu H przesuwamy y wyżej.

## Rodzaj drugi: w jednym kopcu

Tutaj przechowujemy w jednym kopcu zarówno kopiec minimalny i maksymalny.

![alt text](images/min-max-heap-2.png)

Na piętrach parzystych (tj. 0, 2..) będziemy mieć wartości minimalne, a na piętrach nieparzystych (1, 3, 5...) wartości maksymalne. Zakładamy, że korzeń znajduje się na piętrze 0. W roocie nadal mamy wartość najmniejszą. Wartość największa to jeden z wierzchołków na 1 poziomie. Taki kopiec nadal zachowuje własność kopca - jeżeli jesteśmy we wierzchołku !!x!! na poziomie parzystym (minimalnym), to !!x.key!! jest mniejszy od wszystkich wartości w poddrzewie którego korzeniem jest !!x!!. Jeżeli jesteśmy we wierzchołku !!y!! na poziomie nieparzystym (maksymalnym), to !!y.key!! jest największą wartością w poddrzewie którego korzeniem jest !!y!!.
