import dictionary


widgets = {}


while True:
    #print("Current Widgets", widgets)
    user_option: str = input("""Inventory Menu

    1-Add or Update Item
    2-Delete Item
    3-Exit
""")

    if user_option == "1":
        widget_name: str = input("Widget Name? ")
        widget_quantity: int = int(input("Widget Quantity? "))
        dictionary.add_inventory(widgets, widget_name, widget_quantity)

    elif user_option == "2":
        widget_name: str = input("Widget Name? ")
        dictionary.remove_inventory(widgets, widget_name)
    
    else:
        break
