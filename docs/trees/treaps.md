# Opis

o_O taki kopco-BST. Ma jakieś dwie wartości: klucz i priorytet. Po kluczach jest drzewem BST, po priorytetach kopcem. Nie jest to drzewo zbalansowane, jednak losowanie priorytetów daje nam dużą szansę na to, że takie będzie. Nie wiem kto i po co wymyślił taką strukturę, ale przynajmniej zrozumienie jej jest trywialne.

# Operacje

#### search

Jak w drzewie BST.

#### insert

Tworzymy nowy węzeł, gdzie klucz to nasza wartość którą chcemy wstawić i losujemy mu priorytet. Na początku wstawiamy węzeł jak do BST, a później robim co możem żeby przywrócić mu własność kopca, przy pomocy rotacji.

#### delete

Jeżeli jest to liść, usuwamy go. Jeżeli nie, to dajemy mu priorytet nieskończoność (przy kopcu minimalnym), przywrcamy własność kopca (nasz węzeł na pewno trafi do liścia) i usuwamy go.
