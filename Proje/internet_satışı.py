#------------------------------TASK 1----------------------------

def regester_login(username):           # Task 1 de İnput yerine ad yaş mail bilgisini fonksiyonun parametresine mi gireceğiz
    with open("users.txt","r") as file_users:
        listu = []
        for line in file_users:
            line = line.strip()
            liste = line.split(",")
            users = liste[0]
            listu.append(users)
    print("Existing Users:",listu[1:])

    with open("users.txt","a") as users:
        global login
        if username not in listu[1:]:
            name = input("Enter your username for register: ")
            age_input = input("Enter your age: ")
            email_input = input("Enter your email: ")
            users.write(f"\n{name}, {age_input}, {email_input}")
            print("User successfully registered!")
            login = input("Enter username to login: ")
            if login == username:
                print(f"Login successful! Welcome {login}")
        
        else:
            print(f"{username} alrady regester !!!")
            print(f"Login successful! Welcome {login}")

#------------------------------TASK 2----------------------------

def product_catalog():               
    with open("products.txt","r") as products:
        print("Original Products:")
        for line in products:
            line = line.strip()
            liste = line.split()
            print(*(liste))

    while True:

            procedure = input("1: Add Product. (press 1)\nExit:(Press Q)\n")

            if procedure == "1":
                with open("products.txt","a") as products:
                    id = (input("Enter product ID: "))
                    name = input("Enter product name: ")
                    price = (input("Enter product price: "))
                    stock = (input("Enter product stock: "))
                    products.write(f"\n{id}, {name}, {price}, {stock}")
                    print("Products successfully added!")

            elif procedure == "q":
                with open("products.txt","r") as products:
                    print("New Products:")
                    lines = products.readlines()
                    for line in lines[int(21): ]:
                            line = line.strip()
                            liste = line.split()
                            print(*liste)
                break

#------------------------------TASK 3----------------------------

def shopping_cart():            # Task 3 de eklenen ve silinen listenin sıralaması ne olacak her ekeleme çıkarmadan sonra mı en son mı
    with open("products.txt","r") as products:
        print("Products list:")
        global basket,listproduct,listprice,liststock,sum
        basket = []
        listproduct = []
        listprice = []
        liststock = []
        sum = 0
        for line in products:
            line = line.strip()
            liste = line.split(",")
            product = liste[1]
            listproduct.append(product)
            price = liste[2]
            listprice.append(price)
            stock = liste[3]
            liststock.append(stock)
            print(*liste)
        while True:

            procedure = input("1: Add Product to Shopping Card. (press 1)\n2: Remove Product from Shopping Card. (Press 2)\nExit:(Press Q)\n")

            if procedure == "1":
                productID = int(input("Enter product ID which want to add: "))
                basket.append(listproduct[productID])
                sum += int(listprice[productID])
                print("Adding Succesful!")
                print(f"Your Shopping Card: {basket}, Total Price: {sum}")
            elif procedure == "2":
                productID = int(input("Enter product ID which want to remove: "))
                basket.remove(listproduct[productID])
                print("Removing Succesful!")
                sum -= int(listprice[productID])
                print(f"Your Shopping Card: {basket}, Total Price: {sum}")
            else:
                print("Cart after adding products:")
                for i in set(basket):
                    piece = int(basket.count(i))
                    price = int(listprice[listproduct.index(i)])*piece
                    print((f"-{i} x{piece}: {price}"))
                print((f"Total: {sum}"))
                break
    return sum,basket,listproduct,listprice

#------------------------------TASK 4----------------------------

def discound_promotion():               
    global fintot
    if "Laptop" or "Monitor" in basket:
        count_lptp = basket.count("Laptop")
        price_lptp = count_lptp * int(listprice[listproduct.index("Laptop")])
        discound_lptp = price_lptp * 0.85
        count_mntr = basket.count("Monitor")
        price_mntr = count_mntr * int(listprice[listproduct.index("Monitor")])
        discound_mntr = price_mntr * 0.85
        #fintot = sum - ((sum-discoundten) + (price_lptp-discound_lptp) + (price_mntr-discound_mntr))
        fintot = (sum - (price_lptp * 0.15)-(price_mntr * 0.15)) * 0.9
    else:
        print("There is no spesific products in your shopping card")
        fintot = sum - (sum * 0.1)

    print(f"\nOriginal Total: {sum}")
    print(f"After %15 discount on specific products:\nLaptop: Original price {price_lptp}, Discound price {discound_lptp}\nMonitor: Original price {price_mntr}, Discound price {discound_mntr}")
    print(f"After %10 discound: {fintot}\n")
    print("Final Total: ",fintot)

#------------------------------TASK 5----------------------------

def transaction_summary():          # Task 1 ve Task4 ile çalışır
    with open("transaction_summary.txt.","w") as sum:
        sum.write(f"User: {login}\nProducts:\n")
        for i in set(basket):
            piece = int(basket.count(i))
            price = int(listprice[listproduct.index(i)])*piece
            sum.write(f"-{i} x{piece}: {price}\n")
        sum.write(f"Final Total: {fintot}")  
        sum.close()

#------------------------------TASK 6----------------------------

def update_products(i):      # (shopping_card()ile çalıştırılıyor)
    global pf,sf
    if i == len(listproduct):
        return "Products Successfully Updated!"
    else:
        if i == 1:
            pf = float(input("Enter price factor.(factor like 1.10 for a %10 increase or 0.90 for a %10 decrease)"))
            sf = float(input("Enter stock factor.(factor like 1.20 for a %20 increase or 0.80 for a %20 decrease)"))
            print("Updated Products:")
        if listproduct[i] in ["Phone","Tablet","Laptop Stand","Smart Watch","Wireless Earbuds"]:
            new_price = int(listprice[i]) * pf
            new_stock = int(int(liststock[i]) * sf)  # I put two int because stock cannot be float
            listprice[i] = new_price
            liststock[i] = new_stock
            print(f"{i}, {listproduct[i]}, {new_price}, {new_stock}")
            return update_products(i+1)
        else:
            return update_products(i+1)
    
#------------------------------TASK 7----------------------------

def product_search_filter():           # (shopping_card()ile çalıştırılıyor)
    top_rance = int(input("Enter the top price range: "))
    bottom_range = int(input("Enter the bottom price range: "))
    isstock = int(input("Enter the  minimum stock number: "))
    search = (input("Enter the  product name: "))
    print(f"\nSearch by Price Range ({bottom_range}-{top_rance}):")
    for i in set(listprice[1:]):
        if bottom_range <= int(i) <= top_rance:
            print(f"{listprice.index(i)}, {listproduct[listprice.index(i)]}, {listprice[listprice.index(i)]}, {liststock[listprice.index(i)]}")
    print(f"\nFilter by Stock Availability (>={isstock}):")
    for i in set(liststock[1:]):
        if int(i) >= isstock:
            print(f"{liststock.index(i)}, {listproduct[liststock.index(i)]}, {listprice[liststock.index(i)]}, {liststock[liststock.index(i)]}")
    print(f"\nSearch by Product Name (contains {search}):")
    for i in set(listproduct):
        if search in i:
            print(f"{listproduct.index(i)}, {listproduct[listproduct.index(i)]}, {listprice[listproduct.index(i)]}, {liststock[listproduct.index(i)]}")

# Task 2
# Task 4
# Task 5
# Task 6
# Task 7


shopping_cart()





