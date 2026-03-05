name  = input("What's your name? ")

file = open("names.txt", "a") 
#ta funkcja pythonowa - dajemy nazwę pliku, w którym chcemy zeby byly przechowywane rzeczy, a skoro tam będzie tylko tekst, no to dajemy rozszerzenie .txt.
#"w" mówi funkcji, e będziemy tez chcieli cos pisac w tym pliku
#"a" to append
#jezeli plik jeszcze nie istnieje, to open jest super cool bo stworzy ten plik
#open zwraca ,,file handler" - wartość, ktora pozwala dostac sie konkretnie do tego pliku pozniej, dlatego przypisujemy to co open zwraca do zmiennej file

file.write(f"{name}\n")
#.write to metoda do funkcji open
file.close()
#.close zapisuje i zamyka plik