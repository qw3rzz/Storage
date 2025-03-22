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

6

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
        print("Vyhledej produkt podle názvu")
        user_prefix = input("Zadejte část názvu: ").strip().lower()
        found = search_product(user_prefix, products)
        search_print(found)
        menu()

    elif choice == 3:
        print("Přidání položky:")
        add_product()
        print("")
        menu()

menu()