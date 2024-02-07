def get_options_ratio(option: int, total: int) -> float:
    return option / total


def get_faculty_rating(ratio: int) -> str:
    assert ratio < 1

    if ratio > .9:
        return "Excellent"
    
    elif ratio > .8:
        return "Very Good"
    
    elif ratio > .7:
        return "Good"
    
    elif ratio > .6:
        return "Needs Improvement"
    
    return "Unacceptable"
