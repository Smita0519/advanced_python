#Part 2

'''
Question 1: Data Types and Input Handling
Take student name, roll number, age, and marks as input.
Display each value with its data type.
Convert age to float and marks to int before displaying.
'''
user_input = input("Enter name, roll number, age, and marks (separated by spaces): ")
name, roll, age, marks = user_input.split()
age = int(age)
marks = float(marks)
roll = int(roll)

print(f"Name: {name} | Data Type: {type(name)}")
print(f"Roll Number: {roll} | Data Type: {type(roll)}")
print(f"Age : {age} | Data Type: {type(age)}")
print(f"Total Marks : {marks} | Data Type: {type(marks)}")

'''
Output:
Enter name, roll number, age, and marks (separated by spaces): Smita 39 20 91

Name: Smita | Data Type: <class 'str'>
Roll Number: 39 | Data Type: <class 'int'>
Age : 20 | Data Type: <class 'int'>
Total Marks : 91.0 | Data Type: <class 'float'>
'''
'''
Question 2: Conditional Logic
Accept marks (0-100) and display:

Excellent (≥80)
Good (≥60)
Pass (≥40)
Fail (<40)
'''
marks = input("Enter your marks: ")
marks = int(marks)

if marks > 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >=40:
    print("Pass")
else:
    print("Fail")

'''
Output:
Enter your marks: 45
Pass
'''

'''
Question 3: Looping with Conditions
Print numbers between 1 and 100 that are divisible by 4 but not divisible by 8.
'''

result= []
for num in range(1, 101):
    if num % 4 == 0:
        if num % 8 != 0 :
            result.append(num)
print(*result, sep=" ")   # The *results unpacks the list, and sep=" " sets the separator.Each item remains an integer type when printed.

'''
Output:
4 12 20 28 36 44 52 60 68 76 84 92 100
'''

'''
Question 4: List Operations
Given:
marks = [55, 72, 48, 90, 67, 72, 90]
Find max, min, count of 72, and marks ≥ 60.
'''

marks = [55, 72, 48, 90, 67, 72, 90]
max_mark = max(marks)
min_mark = min(marks)

count_72 = marks.count(72)

marks_60 = [mark for mark in marks if mark >= 60]
#marks_60= []
#for mark in marks:
#    if mark >= 60:
#marks_60.append(mark)

count_60 = len(marks_60)

print(f"1. Maximum Mark: {max_mark}")
print(f"2. Minimum Mark: {min_mark}")
print(f"3. Count of mark 72: {count_72}")
print(f"4. Marks greater than or equal to 60 (≥ 60): {marks_60}")
print(f"5. Count of marks ≥ 60: {count_60}")

'''
Output:
1. Maximum Mark: 90
2. Minimum Mark: 48
3. Count of mark 72: 2
4. Marks greater than or equal to 60 (≥ 60): [72, 90, 67, 72, 90]
5. Count of marks ≥ 60: 5
'''

'''
Question 5: Tuple and Immutability
Create a tuple of 5 subjects and attempt modification.
Explain result using comments.
'''
tuple = ("Math", "Science", "History", "Art", "English")
print(type(tuple))
tuple[2] = "Geography"

print("Modified Tuple:", tuple)

'''
Output:
<class 'tuple'>
Traceback (most recent call last):
  File "C:\Users\Dell\Desktop\python_5th_sem\assignment\assignment 1\part2.py", line 116, in <module>
    tuple[2] = "Geography"
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment

Explanation: This means Tuples are immutable (cannot be changed after creation)
'''

'''
Question 6: List Sanitization and Metrics
Given:
marks = [45, -3, 88, "NA", 102, None, 67]
Write a function that:
Removes invalid entries
Returns:
Cleaned list
Number of invalid entries
Percentage of valid marks
Return values using a tuple.
'''
def sanitize_marks(marks):
    tot_entries = len(marks)
    cleaned = []
    
    for mark in marks:
        if isinstance(mark, (int, float)) and 0 <= mark <= 100: #is instance checks if the specific mark in the tuple matches the instance(int or float)
            cleaned.append(mark)

    invalid_cnt = tot_entries - len(cleaned)
    
    valid_per = round((len(cleaned) / tot_entries) * 100, 2)

    return (cleaned, invalid_cnt, valid_per)

marks = [45, -3, 88, "NA", 102, None, 67]
result= sanitize_marks(marks)
cleaned_list, invalid_count, valid_percentage = result

print("\n--- Sanitization Metrics ---")
print(f"Cleaned List of Valid Marks: {cleaned_list}")
print(f"Total Invalid Entries Found: {invalid_count}")
print(f"Percentage of Valid Marks: {valid_percentage}%")

'''
Output:
--- Sanitization Metrics ---
Cleaned List of Valid Marks: [45, 88, 67]
Total Invalid Entries Found: 4
Percentage of Valid Marks: 42.86%
'''

'''
Question 7: Dictionary Usage
Create a dictionary of roll number and name.
Implement add, update, and display operations using functions.
'''
#Initializing the global dictionary (Roll Number: Name)
student_records = {
    12: "Derry",
    13: "Merry",
    14: "Gerry"
}

def add_student(roll, name):
    student_records[roll] = name

def update_student_name(roll, new_name):
    if roll in student_records:
        student_records[roll] = new_name

def display_records():
    print("\n--- Student Records ---")
    if not student_records:   #empty dict
        print("No records found.")
        return
        
    for roll, name in student_records.items():
        print(f"Roll No: {roll}, Name: {name}")

# Display initial records
display_records()

#Add Operation
add_student(20, "Jack")
print("\nStudent Added")

#Update Operation
update_student_name(12, "Harry")
print("\nStudent Updated")

#dictionary after updating
display_records()

'''
Output:
--- Student Records ---
Roll No: 12, Name: Derry
Roll No: 13, Name: Merry
Roll No: 14, Name: Gerry

Student Added

Student Updated

--- Student Records ---
Roll No: 12, Name: Harry
Roll No: 13, Name: Merry
Roll No: 14, Name: Gerry
Roll No: 20, Name: Jack
'''

'''Question 8: Prime Number Function
Write is_prime(n) and display prime numbers between 1 and 50.
'''

def is_prime(n):
    if n <= 1:
        return False
        
    # Check for divisors from 2 up to the square root of n; loop goes up to the square root (n**0.5) + 1 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    # No divisors found, so it is prime
    return True

prime_numbers = []

for number in range(1, 51):
    if is_prime(number):
        prime_numbers.append(number)

print("Prime Numbers between 1 and 50:")
print(prime_numbers)

'''
Output:
Prime Numbers between 1 and 50:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''

'''
Question 9: Function Composition
Write functions to:
Calculate total marks
Calculate average
Classify result (Distinction / Pass / Fail)
Then write a function that combines them and returns:
(name, total, average, result)
Explain why modular design is beneficial.
'''
#total marks
def calculate_total(marks):
    return sum(marks)

#average
def calculate_average(total_marks, num_subjects):
    return round(total_marks / num_subjects, 2)

#classifying the result
def classify_result(average):
    if average >= 80:
        return "Distinction"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"
    
#Composition Function
def process_student(name, marks):
    num_subjects = len(marks)
    total = calculate_total(marks)
    average = calculate_average(total, num_subjects)
    result = classify_result(average)
    return (name, total, average, result)


student1 = process_student("Derry", [90, 85, 70])
student2 = process_student("Merry", [55, 30, 65])
student3 = process_student("Gerry", [25, 35, 30])

print("Studentno.: ('Name', total marks, average, 'remarks')")
print(f"Student 1: {student1}")
print(f"Student 2:   {student2}")
print(f"Student 3: {student3}")

'''
Output:
Studentno.: ('Name', total marks, average, 'remarks')
Student 1: ('Derry', 245, 81.67, 'Distinction')
Student 2:   ('Merry', 150, 50.0, 'Pass')
Student 3: ('Gerry', 90, 30.0, 'Fail')
'''

'''
Question 10: Defensive Input Parsing
Write a function that accepts a raw input string in the format:
"Ram|101|22|78, 88, 91"
Hint: Parse student data from string format: "Name|Roll|Age|Mark1, Mark2, Mark3"
Tasks:
Extract name, roll number, age, and marks
Convert them into appropriate data types
Validate age (≥16) and marks (0-100)
Return the result as a dictionary using roll number as the key
The function must not crash for malformed input.
'''

def parse_student_data(raw_input_string):

# Parses and validates student data. Returns: A dictionary {roll_number: {data}} if successful, or None if validation fails.
# 1. Structural Check: Split by '|'
    parts = raw_input_string.split('|')
    
    if len(parts) != 4:
        print(f"ERROR: Input string '{raw_input_string}' has incorrect number of parts (expected 4).")  #invalid input
        return None

    name = parts[0].strip()      #separately store the input
    raw_roll = parts[1].strip()
    raw_age = parts[2].strip()
    raw_marks = parts[3].strip()

    # Roll Number Validation
    # .isdigit() checks if the string contains only digits.
    if raw_roll.isdigit():
        roll_num = int(raw_roll)
    else:
        print(f"VALIDATION FAILED: Roll number '{raw_roll}' is not an integer.")
        return None

    # Age Validation (>= 16)
    if raw_age.isdigit():
        age = int(raw_age)
        if age < 16:
            print(f"VALIDATION FAILED: Age {age} is below 16.")
            return None
    else:
        print(f"VALIDATION FAILED: Age '{raw_age}' is not an integer.")
        return None
        
    # Marks Validation (0-100)
    marks = []
    mark_list = raw_marks.split(',')
    
    for raw_mark in mark_list:
        raw_mark = raw_mark.strip()
        
        # Check if the mark string contains only digits
        if not raw_mark.isdigit():
            print(f"VALIDATION FAILED: Mark '{raw_mark}' is not a valid integer.")
            return None
        
        mark = int(raw_mark)
        if 0 <= mark <= 100:
            marks.append(mark)
        else:
            print(f"VALIDATION FAILED: Mark {mark} is outside the valid range (0-100).")
            return None

    student_record = {  #assemble
        'name': name,
        'age': age,
        'marks': marks,
    }
    
    return {roll_num: student_record}

Student1 = "Derry|101|22|78, 88, 91"
result = parse_student_data(Student1)
print(f"\n[A] Input: {Student1}\nResult: {result}")

# Invalid Roll
input = "Gerry|A05|20|90, 80, 70"
resultI = parse_student_data(input)
print(f"\n[E] Input: {input}\nResult: {resultI}")



