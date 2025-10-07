def students_info(grades, school):
    result = []     
    stud_school = {}
    for school_num, stud_list in school.items():
        for stud_name in stud_list:
            stud_school[stud_name] = school_num
    for stud_name, marks in grades.items():
        average = sum(marks) / len(marks)
        average2 = round(average)
        school_number = stud_school.get(stud_name)
        info_string = f"{stud_name} учится в школе номер {school_number} и имеет средний балл {average2}"
        result.append(info_string) 
    return result
grades = {
    "Алиса": [85, 90, 78],
    "Никита": [92, 89, 94], 
    "Иван": [70, 65, 72]
    }
school = {
    1: ["Алиса", "Никита"],
    2: ["Иван"]
    }
result = students_info(grades, school)
for line in result:

    print(line)
