prices = [150.0, 22.0, 12.75, 50.99]
names = ["Cell Phone", "Fancy Pen", "Energy Drink", "Flash Drive"]
totalProducts = 0
totalSold = 0.0

print("Welcome to the Program")

while True:
    for i in [0, 1, 2, 3]:
        print (i+1, " ", names[i])
    option = input("Select a product: ")
    if option:
        try:
            optionNumber = int(option)
        except ValueError as err:
            print(err)
            continue
        print("You have selected: ", names[i-1], " with price: ", prices[i-1])
        totalProducts += 1
        totalSold += prices[i-1]
    else:
        break

print("Thanks for using")
print("Number of products sold ", totalProducts)
print("Total income ", totalSold)

# Create a new program that shows how many of each product was sold
