import repetition


while True:
    user_input: str = input("""Homework 3 Menu
1-Factorial
2-Sum odd numbers
3-Exit
    """)

    if user_input == "1":
        user_number = 0

        while not (user_number > 0 and user_number < 10):
            user_number = int(input())
            repetition.get_factorial(user_number)

    elif user_input == "2":
        user_number = 0

        while not  (user_number > 0 and user_number < 100):
            user_number = int(input())
            repetition.sum_odd_numbers(user_number)

    elif user_input == "3":
        if input("continue? ") == "no":
            break

