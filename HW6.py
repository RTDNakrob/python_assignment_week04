grades = [55,70,65,40,90,85,50,77]
is_pass = lambda x:x>=60
bonus = lambda x:x*1.05
passed_students = list(filter(is_pass, grades))
passed_with_bonus = list(map(bonus,passed_students))
print(passed_with_bonus)
