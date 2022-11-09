# Wybieranie produktów
def shopping(section=[]):
    goods = len(section)
    basket = []
    watching_goods = 0
    while watching_goods < goods:
        print("\nYou take it in your hand: {}".format(section[watching_goods]))
        decision = input("Do you want to put this product in the basket: ")
        if decision == "YES":
            basket.append(section[watching_goods])
            section[watching_goods] = ""
        watching_goods += 1
    return basket

# Wykładanie produktów na taśmę
def cash_register(*argv):
    if argv is not None:
        for iarg in argv:
            for good in iarg:
                print(good, end=", ")
                
    print("")

# Produkty na półkach
shop_shelf1 = ["Cygaro", "Grzechotka", "Cytryna", "TV"]
shop_shelf2 = ["Pokemon", "Jabłko", "Kolejka"]
shop_shelf3 = ["Cukier", "Mąka", "Ziemniaki"]

basket1 = shopping(shop_shelf1)
basket2 = shopping(shop_shelf2)
basket3 = shopping(shop_shelf3)

print("------------------------------------------")
print("Your choice: ")
cash_register(basket1, basket2, basket3)

