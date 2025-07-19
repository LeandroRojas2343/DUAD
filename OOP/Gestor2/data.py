import csv
import os
from student import Student

def export_csv(student_list, filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "section", "spanish", "english", "social_studies", "science"])
            writer.writeheader()
            for student in student_list:
                writer.writerow(student.to_dict())
        print("\nData exported successfully.")
    except Exception as e:
        print(f"Error while exporting: {e}")


def import_csv(filename):
    if not os.path.exists(filename):
        print("\nFile not found. You must export first.")
        return []

    student_list = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    row["name"],
                    row["section"],
                    row["spanish"],
                    row["english"],
                    row["social_studies"],
                    row["science"]
                )
                student_list.append(student)
        print("\nData imported successfully.")
    except Exception as e:
        print(f"Error while importing: {e}")
    return student_list

