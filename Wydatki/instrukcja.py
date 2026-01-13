# Uzytkownik wprowadza wydatki w osobnym pliku
    # w pliku z wydatkami przy kazdym wydatku jest: Kwota, data, kategoria (zakupy spozywcze/drogeryjne/media/ubrania --- cokolwiek na razie)

# Wczytujemy plik z wydatkami
    #jezeli w kolumnie kwota wartosc nie jest liczba to wiersz jest pomijany

#program:
    # 0. Początkowo pyta o zakres dat, który Cię interesuje? (np. ostatnie 7 / 30 dni, ostatnie 6 miesięcy, konkretny zakres dat)
    # 1. Następnie pyta, jaka kategoria wydatków Cię interesuje (jedna, kilka, albo wszystkie)
    # 2. Następnie pyta, czego chciałbyś się dowiedzieć o swoich wydatkach z tego okresu?
    # 2a. Uzytkownik wybiera z listy:
        # A. Ile srednio wydaję w tej / tych kategoriach? - wylicza średnią wartosc wydatku w tej / kazdej kategorii w danym okresie
        # B. Ile najwiecej a ile najmniej wydałem w tej / tych kategoriach? - Pokazuje najwyzszy i najnizszy wydatek z tej / tych kategorii w danym okresie
        # C. Ile łącznie wydałem w tej / tych kategoriach? Pokazuje sumę wydatków z tej / tych kategoriach w danym okresie
        # D. Suma wszystkich wydatków - Pokazuje sumę wszystkich wydatków z tej / tych kategorii w danym okresie 
            # 4a. Pokazuje sumę wszystkich wydatków wraz z podziałem na kategorie na wykresie kołowym
        # E. Porównaj z innym okresem - Porównuje wydatki z zakresu dat X z tym samym okresem rok wcześniej (albo z innym wybranym okresem, np. porównaj sierpień z lipcem) (input z jakim okresem porównać)
