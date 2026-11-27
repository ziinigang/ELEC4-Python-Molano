def calculate_average(grades):
    return sum(grades) / len(grades)

def determine_result(average):
    if average >= 75:
        return "PASSED"
    return "FAILED"

def get_highest_grade(grades):
    return max (grades)

def get_lowest_grade(grades):
    return min (grades)