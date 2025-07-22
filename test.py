import module1
bye = lambda: print("Goodbye!")
double = lambda x: x*2
is_even = lambda x: x%2==0
module1.hi("World")
module1.hi("Alice", "Welcome")
bye()
print(double(4))
print(is_even(4))
print(is_even(5))
numbers = [1,2,3,4,5]
double_numbers = list(map(double, numbers))
even_nums = list(filter(is_even,numbers))
print(double_numbers)
print(even_nums)

students = [
    {"name": "Gene", "grade": 62},
    {"name": "Konek", "grade": 81},
    {"name": "Nakrob", "grade": 95},
]
grade_criteria = lambda student: student["grade"] >= 80
filtered_students = list(filter(grade_criteria, students))
print(filtered_students)

sorted_students = sorted(filtered_students,
                         key=lambda x:x["grade"],
                         reverse=True)
print(sorted_students)