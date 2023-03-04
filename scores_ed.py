student_dict = {}
count = 0
average_grade = 0.0
letter_grade = 'Not assigned'

with open("DATA/testscores.dat") as test_in:
    for raw_line in test_in:
        line = raw_line.rstrip()
        student_name, grade = line.split(':')
        count += 1
        if float(grade) >= 95:
            letter_grade = 'A'
        elif float(grade) >= 89:
            letter_grade = 'B'
        elif float(grade) >= 83:
            letter_grade = 'C'
        elif float(grade) >= 75:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        average_grade = float(average_grade) + float(grade)
        student_dict[student_name] = grade, letter_grade
#        print("{:<20s} {} {}".format(student_name, grade, letter_grade))

    average_grade = average_grade / count
    print(student_dict)
    for student_name, student_data in sorted(student_dict.items(),reverse=True,key=lambda e: e[1][0]):
        print("{:<20s} {} {}".format(student_name,student_data[0],student_data[1]))
    print("The average test grade for examine was {:.1f}".format(average_grade))

