# Opis

Jest to struktura danych służąca do pamiętania danych, nie będziemy mieć operacji !!insert!! i !!delete,!! tylko !!find!!. Zbiór !!n!! kluczy chcemy pamiętać tak, by:

1. struktura zajmowała !!n!! komórek pamęci,
2. czas konstrukcji był wielomianowy względem !!n!!
3. !!find!! był w czasie stałym.

# Idea

Po pierwsze, stosujemy haszowanie dwupoziomowe. Funkcje haszujące wybieramy losowy z uniwersalnej rodziny.
Na pierwszym poziomie funkcja haszująca rozrzuca klucze do kubełków, tak żeby !!\sum\_{i=0}^{n-1} n_i^2 = O(n)!!, gdzie !!n_i!! to liczba kluczy wrzuconych do kubełka !!i!!.  
Na poziomie drugim, haszujemy klucze w każdym kubełku niezależnie, używając tablicy o rozmiarze !!n_i^2!! - haszowanie bezkolizyjne.

Tworzenie tablicy to !!O(n)!!, find w !!O(1)!!. Są tu jakieś dowody, ale to zbyt algebraiczno/rpisowe żeby było warte naszego czasu.
