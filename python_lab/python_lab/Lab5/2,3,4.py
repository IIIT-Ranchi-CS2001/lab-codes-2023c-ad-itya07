# Q2: List of Tuples with Student Details and Sorting by Marks
names = input("Enter student names separated by commas: ").split(',')
roll_numbers = input("Enter roll numbers separated by commas: ").split(',')
marks = list(map(float, input("Enter marks separated by commas: ").split(',')))

students = list(zip(names, roll_numbers, marks))
sorted_students = sorted(students, key=lambda x: x[2], reverse=True)
print("Sorted Student Details:", sorted_students)


students = [(names[i], roll_numbers[i], marks[i]) for i in range(len(names))]

for i in range(len(students) - 1):
    for j in range(len(students) - i - 1):
        if students[j][2] < students[j + 1][2]:
            students[j], students[j + 1] = students[j + 1], students[j]
print("Manually Sorted Student Details:", students)


# Q4: Employee Salaries Sorted by Descending Order
employees = {}
for _ in range(5):
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    employees[name] = salary

sorted_employees = sorted(employees.items(), key=lambda x: x[1], reverse=True)
for rank, (name, salary) in enumerate(sorted_employees, start=1):
    print(f"{rank}. {name}: Rs. {salary}")