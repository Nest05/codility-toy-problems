import functools

def split_string(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        



def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greet():
    return "Hi there"

print(greet())

# List Comprehensions
my_students = [{"name":"Naomi", "total_score":450}, {"name":"Naomi", "total_score":500}]

average_total_score = sum([my_student["total_score"] for my_student in my_students]) / len(my_students)

print(average_total_score)

# Generator Expressions
def squares(length):
    for l in range(length):
        yield l**2

for square in squares(6):
    print(square)