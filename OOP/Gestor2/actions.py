from student import Student 

def ask_grade(subject):
    while True:
        try:
            grade = float(input(f"Grade for {subject}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("The grade must be between 0 and 100.")
        except ValueError:
            print("You must enter a valid number.")

def register_students(student_list):
    try:
        how_many_students = int(input("How many students do you want to register?: "))
    except ValueError:
        print("You must enter an integer.")
        return

    for _ in range(how_many_students):
        print("\n--- New Student ---")
        name = input("Full name: ")
        section = input("Section (e.g., 11B): ")
        spanish = ask_grade("Spanish")
        english = ask_grade("English")
        social_studies = ask_grade("Social Studies")
        science = ask_grade("Science")

        student = Student(name, section, spanish, english, social_studies, science)

        student_list.append(student)

def show_students(student_list):
    if not student_list:
        print("\nNo students registered.")
        return
    for st in student_list:
        print("\nName:", st.name)
        print("Section:", st.section)
        print("Spanish:", st.spanish)
        print("English:", st.english)
        print("Social Studies:", st.social_studies)
        print("Science:", st.science)

def top_3_students(student_list):
    if len(student_list) < 3:
        print("\nAt least 3 students are required to view the top 3.")
        return

    averages = [(st.average(), st) for st in student_list]
    top3 = sorted(averages, key=lambda x: x[0], reverse=True)[:3]

    print("\n--- Top 3 Students ---")
    for i, (avg, st) in enumerate(top3, 1):
        print(f"#{i} - {st.name} ({st.section}), Average: {avg:.2f}")

def overall_average(student_list):
    if not student_list:
        print("\nNo students registered.")
        return

    total = sum(st.average() for st in student_list)
    average = total / len(student_list)
    print(f"\nOverall average of all students: {average:.2f}")
