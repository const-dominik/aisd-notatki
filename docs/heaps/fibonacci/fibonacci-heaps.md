# Opis

Są to kopce dwumianowe, ale takie OP - !!deletemin!! będzie się tu wykonywać w zamortyzowanym czasie stałym !!O(1)!!! Co więcej, dodamy sobie operację _decrement_, która podobno czasem się przydaje, polega ona na zmniejszeniu jakiegoś klucza o jakąś wartość. Na kopcach dwumianowych taka procedura zajmowałaby !!\log n!! czasu, co jest absolutnie nieakceptowalne gdy wykonujemy dużo *decrement*ów. Jest to ultimate kopiec, gdzie prawie wszystko dzieje się w !!O(1)!!.

# Struktura

Kopce Fibonacciego są zbiorami drzew, których wierzchołki pamiętają elementy w porządku kopcowym. Jednak tym razem nie muszą to być drzewa dwumianowe. Drzewa pamiętamy tak jak w kopcach dwumianowych (lazy meld), tak samo minimum. Dodatkowo, każdy wewnętrzny wierzchołek kopca pamięta, czy starcił syna przez operację !!cut!!.

# Operacje

#### !!cut(h, p)!!

Operacja odcina !!p!! od swojego ojca !!p'!! i dołącza (meld) poddrzewo zakorzenione w !!p!! do listy drzew kopca. Jeżeli !!p'!! już wcześniej utracił syna, wycinamy go. Robimy to tak długo, aż dotrzemy do wierzchołka który jeszcze nie utracił syna. Jeżeli !!p'!! jeszcze nie utracił syna, no to już utracił i sobie to zapisujemy.

#### !!decrement(h, p, \Delta)!!

Zmniejszamy wartość klucza w wierzchołku !!p!!. Jeżeli nowa wartość klucza zakłóca porządek kopcowy, to odcinamy p przez !!cut(h, p)!!. Oszczędzamy tym czas naprawiania własności kopca.

#### !!deletemin(h)!!

Tak jak w kopcach dwumianowych. Redukując łączymy drzewa o jednakowym rzędzie, otrzymując drzewo o stopniu jeden wyższym. Drzewa jednak nie są dwumianowe, więc nie możemy oczekiwać, że łączone drzewa będą miały identyczną strukturę.

Żeby wykazać, że !!O(\log n)!! nadal ogranicza naszą procedurę, musimy dowieść, że stopień wierzchołków drzew występujących w kopcach Fibonacciego jest ograniczony przez !!O(\log n)!!. Będzie to też ograniczenie na liczbe różnych rzędów drzew.

Lemat: Dla każdego wierzchołka !!x!! kopca Fibonacciego o rzędzie !!k!!, drzewo zakorzenione w !!x!! ma rozmiar wykładniczy względem !!k!!.

Dowód: Niech !!x!! będzie dowolnym wierzchołkiem kopca, a !!y_1, \dots, y_k!! jego synami (uporządkowane w kolejności przyłączania do !!x!!). Kiedy !!y_i!! był przyłączany, !!x!! miał co najmniej !!i-1!! synów. Stąd !!y_i!! też miał co najmniej !!i-1!! synów, bo łączymy tylko drzewa o jednakowym rzędzie. Od tego momentu !!y_i!! mógł stracić tylko jednego syna, inaczej byśmy go odcięli (!!cut!!). Zatem w !!i!!-tym momencie syn każdego wierzchołka ma rząd **co najmniej** !!i - 2!!.  
!!F_i!! - najmniejsze drzewo o rzędzie !!i!!, spełniające powyższą zależność.  
!!F_0!! - jeden wierzchołek  
!!F_i!! - ma korzeń oraz poddrzewa: !!F_0!!, !!F_0!!, !!F_1!!, !!F_2!!, ... , !!F\_{i-2}!!.
Liczba wierzchołków !!|F_i| \geq 1 + \sum\_{j=0}^{i-2} |F_j|!!, co jest równe !!i!!-tej liczbie Fibonacciego. Zatem liczba wierzchołków w drzewie o rzędzie !!k!! jest nie mniejsza niż !!{((1+\sqrt{5})/2)}^k!!.

Wniosek: Każdy wierzchołek w !!n!!-elementowym kopcu Fibonacciego ma stopień ograniczony przez !!O(\log n)!!.

#### !!delete(h, p)!!

Możemy to zrobić poprzez ustawienie w !!p!! minimum kopca (używając !!decrement!!) a następnie usuwając minimum. Zamortyzowany koszt to !!O(\log n)!!
