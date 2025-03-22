products = [
    {
        "name": "Dědoles ponožky",
        "price": 50,
    },
    {
        "name": "Kraťasy",
        "price": 120,
    },
    {
        "name": "Černé triko",
        "price": 150,
    },
    {
        "name": "Trenky",
        "price": 70,
    },
    {
        "name": "Kšiltovka",
        "price": 900,
    },
    {
        "name": "Bunda",
        "price": 2000,
    },
    {
        "name": "Rukavice",
        "price": 100,
    },
]

def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}, Cena: {product['price']}Kč")



def search_product(prefix, arr):

    return [product for product in arr if prefix.lower() in product["name"].lower()]


def add_product():
    product_name = input("Název produktu:")
    product_price = int(input("Zadej cenu:"))
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)

def sum_product():
    total = 0
    for product in products:
        total += product['price']

    print(f"Celková částka všech produktů je {total}Kč")

def min_price():
    min_product = products[0]

    for product in products[1:]:

        if product["price"] < min_product["price"]:
            min_product = product

def max_price():
    max_product = products[0]

    for product in products[1:]:

        if product["price"] > max_product["price"]:
            max_product = product

    return max_product

def average_price(products):

    total_price = sum(product["price"] for product in products)
    return total_price / len(products)

def product_edit(products):
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]['name']} - {products[i]['price']} Kč")

    choice = int(input("Zadej číslo produktu, který chceš upravit: "))

    new_name = input("Zadej nový název: ")
    new_price = int(input("Zadej novou cenu: ")) -1

    products[choice]["name"] = new_name
    products[choice]["price"] = new_price

def search_price(products, target_price):
    found_products = [product for product in products if product["price"] == target_price]

    if found_products:
        print("\nNalezené produkty s cenou", target_price, "Kč:")
        for product in found_products:
            print(f"{product['name']} - {product['price']} Kč")
    else:
        print(f"Žádné produkty s cenou {target_price} Kč nebyly nalezeny.")

def menu():
    print("Vítej ve skladu")
    print("------------------")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání položky")
    print("4. Celková suma cen")
    print("5. Produkt s nejnižší cennou")
    print("6. Produkt s nejvyšší cennou")
    print("7. Průměr všech cen")
    print("8. Úprava produktu")
    print("9. Najdi produkt podle ceny")
    print("------------------\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Vyhledej produkt podle názvu")
        user_prefix = input("Zadejte část názvu: ").strip().lower()
        found = search_product(user_prefix, products)
        search_print(found)
        menu()

    elif choice == 4:
        sum_product()
        print("")
        menu()

    elif choice == 5:
        print("Nejlevnější produkt je:")
        min_price()
        min_product = min_price()
        print(f"Produkt s nejnižší cenou je {min_product['name']} za {min_product['price']} Kč.")
        print("")
        menu()

    elif choice == 6:
        print("Nejdražší produkt je:")
        max_price()
        max_product = max_price()
        print(f"Produkt s nejvyšší cenou je {max_product['name']} za {max_product['price']} Kč.")
        print("")
        menu()

    elif choice == 7:
        print("Průměr cen všech produktů:")
        print(average_price(products))
        menu()

    elif choice == 8:
        print("Úprava produktu:")
        product_edit(products)
        menu()

    elif choice == 9:
        print("Nalezení produktu podle ceny:")
        target_price = int(input("Zadej cenu produktu, který hledáš: "))
        search_price(products, target_price)
        menu()

menu()