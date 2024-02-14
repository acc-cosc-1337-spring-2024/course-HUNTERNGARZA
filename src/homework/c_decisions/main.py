from decisions import get_faculty_rating, get_options_ratio


user_input_for_options: str = input("Options? >>> ")
options = int(user_input_for_options)

user_input_for_total: str = input("Total? >>> ")
total = int(user_input_for_total)

ratio: float = get_options_ratio(options, total)
rating: str = get_faculty_rating(ratio)

print(rating)
