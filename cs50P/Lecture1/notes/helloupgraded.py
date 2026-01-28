#def hello(): #najpierw definiujemy. potem nazwa (tutaj hello), a potem nawiasy - jeśli nic w nich nie ma, to znaczy ze funkcja nie potrzebuje nic ode mnie, zeby zadzialac - zanych argumentow, inputow, nic. Dwukropek znaczy, zeby poczekała funkcja na najblizsze wciecie w tekscie bo bedziemy tlumavzyc jej jak dziala
#    print("hello") #no i teraz juz wie ze bedzie drukowac hello

def hello(to="world"): #zamiast ,,to'' moze byc nawet cokolwiek, to jest szablon
#z tym ="world" chodzi o to, ze gdybysmy wywolali potem hello i nic mu nie przekazali, czyli hello(), to funkcja jako deafault bierze, ze jesli nic sie nie przekaze jej to ona wypisze world - tak jak przy =end''bylo np
    print("Hello,", to)
    
hello() #zostawiam puste zeby pokazac to hello world
name = input("What's your name? ")
hello(name) #wywolujemy funkcje i przekazujemy jej zmienna ,,name'' i to wchozi do szablonu

