import class_a


while True:
    die_object = class_a.die()
    die_object.roll()

    user_input: str = input("""
MENU:
1-continue? y/n
""")
    if user_input == "n":
        break

    print(die_object.get_rolled_value())
