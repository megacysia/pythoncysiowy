def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")
    
    
def get_student():
    n = input("Name: ")
    h = input("House: ")
    return (n, h) #tuple --> typ danych w pythonie, który zbiera rózne wartosci: x, y albo x, y, z --> te wartości są niezmienne (w odroznieniu od list). Nawiasy () są opcjonalne jak coś, dla czytelności. ALE jak damy nawiasy [] to funkcja zwraca listę, i tu juz mozna robić modyfikacje pozniej i przypisywac do innych wartosci elementy z listy

if __name__ == "__main__":
    main()
    
