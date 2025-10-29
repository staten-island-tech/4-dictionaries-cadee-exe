print("Welcome to the shop! Buy whatever you like.")
best_buy_items = [
    
        {
                "name": "Samsung 55"" 4K UHD TV",
        "price": 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."},

        {
                "name": "French water"" Fancy water",
        "price": 555.99,
        "department": "Water",
        "description": "Water for the rich."},

        {
                "name": "China"" Country",
        "price": 77777777777.99,
        "department": "",
        "description": "Densely populated country"},

        {
            "name": "Baconetta"" Food",
        "price": 6.45,
        "department": "Good food",
        "description": "Make the vegans mad"},

      

]
for index, item in enumerate(best_buy_items):
            print(index, ":" ,(item)["name"])
            best_buy_items[0]["name"]

choice = input("Buy whatever you like!")
cart = []
cart.append(choice)
print(f"Added", choice, "to cart")
while cart != "done":
        