#import dictionary


#widgets = {}


#while True:
    #print("Current Widgets", widgets)
#    user_option: str = input("""Inventory Menu

#    1-Add or Update Item
#    2-Delete Item
#    3-Exit
#""")

#    if user_option == "1":
 #       widget_name: str = input("Widget Name? ")
  #      widget_quantity: int = int(input("Widget Quantity? "))
   #     dictionary.add_inventory(widgets, widget_name, widget_quantity)

#    elif user_option == "2":
 #       widget_name: str = input("Widget Name? ")
  #      dictionary.remove_inventory(widgets, widget_name)
    
   # else:
    #    break


import sets


prog1 = {'Student1', 'Student2', 'Student3'}
prog2 = {'Student3', 'Student4', 'Student5'}

while True:
    user_option: str = input("""1-Students who took prog1 and prog2
2-Students who took prog2 only
3-Students who took prog1 not prog2
4-Students who took prog2 not prog1
5-Exit""")
    
    if user_option == "1":
        print(sets.get_students_who_took_prog1_and_prog2(prog1, prog2))

    elif user_option == "2":
        print(sets.get_students_who_took_prog2_only(prog1, prog2))
    
    elif user_option == "3":
        print(sets.get_students_who_took_prog1_not_prog_2(prog1, prog2))
    
    elif user_option == "4":
        print(sets.get_students_who_took_prog2_not_prog_1(prog1, prog2))
    
    else:
        break
