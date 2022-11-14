# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:

    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

#Darau prielaidą, kad klaida užduoty, nes 100 000 000 milijonų = šimtas bilijonų (ilgojoje skalėje), arba ~25% viso pasaulio bendros ekonominės vertės. Holivudui dar yra kur pasistengt.

    def was_expensive(self):        
        if self.budget > 100000000:
            print(True)
        else:
            print(False)


movie1 = Movie("Pulp Fiction", "Quentin Tarantino", 8500000)

movie1.was_expensive()

movie2 = Movie("Avengers: Endgame", "Russo brothers", 400000000)

movie1.was_expensive()