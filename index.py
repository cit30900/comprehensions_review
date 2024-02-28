from datetime import datetime
import pytz
import re

class MenuItem:
    def __init__(self, name, price, description, start_date=None, end_date=None):
        self.name = name
        self.price = price
        self.description = description
        if start_date != None:
            self.start_date = start_date.astimezone(pytz.utc)
            self.end_date = end_date.astimezone(pytz.utc)
        else:
            self.start_date = None
            self.end_date = None



def setupMenu():
    # Placeholder values for menu items
    menu_items_data = [
        ("Caffè Americano", 2.45, "Espresso shots topped with hot water, creating a light layer of crema"),
        ("Cappuccino", 3.65, "Dark, rich espresso lies in wait under a smoothed and stretched layer of thick milk foam"),
        ("Latte", 3.95, "Rich, full-bodied espresso in steamed milk, lightly topped with foam"),
        ("Mocha", 4.45, "Sweet, rich, full-bodied espresso with bittersweet mocha sauce and steamed milk"),
        ("White Chocolate Mocha", 4.75, "Sweet and creamy white chocolate flavored sauce, steamed milk, and espresso"),
        ("Caramel Macchiato", 4.75, "Freshly steamed milk with vanilla-flavored syrup, marked with espresso and caramel drizzle"),
        ("Flat White", 3.95, "Bold ristretto shots of espresso get the perfect amount of steamed whole milk to create a not-too-strong, not-too-creamy, just-right flavor"),
        ("Caramel Frappuccino", 5.45, "Caramel syrup meets coffee, milk, and ice for a rendezvous in the blender, while whipped cream and caramel sauce layer the love on top"),
        ("Peppermint Mocha", 4.45, "Sweet, rich, full-bodied espresso with a holiday inspired peppermint mocha sauce and steamed milk", datetime(2024, 11, 1, 0, 0, 0, tzinfo=pytz.utc), datetime(2024, 12, 31, 23, 59, 59, tzinfo=pytz.utc)),
        ("Pumpkin Spice Latte", 4.45, "Rich, full-bodied espresso in steamed milk with our famous autumnal pumpkin spice lightly topped with foam", datetime(2024, 9, 1, 0, 0, 0, tzinfo=pytz.utc), datetime(2024, 11, 30, 23, 59, 59, tzinfo=pytz.utc))
    ]

    # Create a list of menu items
    menu_items = []
    for item_data in menu_items_data:
        if len(item_data) > 3:
            item = MenuItem(item_data[0], item_data[1], item_data[2], item_data[3], item_data[4])
        else:
            item = MenuItem(item_data[0], item_data[1], item_data[2])
        menu_items.append(item)

    return menu_items

def main():
    # Get a list of objects of class MenuItem
    menu_items = setupMenu()

    # Use list comprehensions to find menu items that are less than $4
    menu_items_less_than_four_dollars = [item for item in menu_items if item.price < 4.0]

    # Print a header
    print(f'\n\nMENU ITEMS LESS THAN $4')

    # Print the menu items less than four dollars
    for item in menu_items_less_than_four_dollars:
        print(f'{item.name} - ${item.price}')

    # Use list comprehensions to find menu items that contain the word 'Mocha'
    menu_items_with_mocha = [item for item in menu_items if re.search(r'\bMocha\b', item.name)]

    # Print a header
    print(f'\n\nMENU ITEMS CONTAINING "Mocha"')
    
    # Print the menu items that contain the word 'Mocha'
    for item in menu_items_with_mocha:
        print(f'{item.name} - ${item.price}')

    # Use list comprehensions to find seasonal menu items
    menu_items_with_start_date = [item for item in menu_items if item.start_date is not None]

    # Print a header
    print(f'\n\nSEASONAL MENU ITEMS')
    
    # Use list comprehensions to find seasonal menu items
    for item in menu_items_with_start_date:
        print(f'{item.name} - ${item.price}, available {item.start_date.strftime("%m/%d/%Y")}')

if __name__== "__main__":
  main()