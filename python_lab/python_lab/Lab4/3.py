# Q3: Combine course code and course name into a list
course_codes = input("Enter course codes separated by commas: ").split(',')
course_names = input("Enter course names separated by commas: ").split(',')
course_list = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]
print("Combined Course List:", course_list)