print("Welcome to the shop")
items = [
    
        {
                "name": "Samsung 55"" 4K UHD TV",
        "price" : 429.99,
        "department": "Televisions",
        "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."},

        {
                "name": "French water",
        "price": 555.99,
        "department": "Water",
        "description": "Water for the rich."},

        {
                "name": "China",
        "price": 77777777777.99,
        "department": "",
        "description": "Densely populated country"},

        {
            "name": "Baconetta",
        "price": 6.45,
        "department": "Good food",
        "description": "Make the vegans mad"},

        {
         "name": "Mr. Whalen",
         "price": 0,
         "department": "teacher",
         "description": "will code for $$"},

]

for index, item in enumerate(items):
            print(index, ":" ,(item)["name"])
            items[0]["name"]
choice = int(input("Buy whatever you like!"))
cart = []
cost=0
cart.append(items[choice])
print(f"Added {items[choice]["name"]} into cart")
cost += items[choice]["price"]

while True:
        check=input("Do you wish to keep shopping?")
        if check == "Yes":
                choice = int(input("What else would you liek to buy?"))
        cart.append(items[choice])
        print(f"Added {items[choice]["name"]} into cart")
        cost += items[choice]["price"]
        if check == "No":
                break

for item in cart:
        print(f'{item["name"]}" ${int(item["price"])}')
print(f"Total: ${cost}")
        


""" class calculator():
        def add(x,y):
                print(x+y)
                return x + y
        def add_many(list):
                print(sum(list))
                return sum(list)
        def subtract(list):
                return list
calculator.add(15,5)

class Hero:
        def _init_(self, name, money, inventory):
                self.name = name
                self.money = money
                self.inventory = inventory
        def buy(self, item):
                self.inventory.append(item)
                print(f"{self.name} purchased {item} and has {self.items}")
Nathan = Hero("Nathan", 0, ["Pencil"])
print(Nathan._dict_)
Nathan.buy("Xi Yang")


         """