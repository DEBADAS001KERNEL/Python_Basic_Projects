def get_student_info():
    print("Welcome to student's marks management & Study Guide System:")
    name = input("Please Enter Your Name: ")

    num_subjects = int(input("How many subjects are there: "))
    subjects = []

    for _ in range(num_subjects):
        subject_name = input("Enter the subject name: ")
        marks = int(input(f"Enter the marks for {subject_name}: "))
        subjects.append({"subject": subject_name, "marks": marks})

    return name, subjects

def analyze_results(subjects):
    max_subject = max(subjects, key=lambda x: x["marks"])
    min_subject = min(subjects, key=lambda x: x["marks"])

    return max_subject, min_subject

def display_results(name, max_subject, min_subject):
    print(f"\nDear {name}, here are your results:\n")
    
    for subject in subjects:
        print(f"{subject['subject']}: {subject['marks']} marks")

    print(f"\nCongratulations! You got the highest in {max_subject['subject']} with {max_subject['marks']} marks.")
    print(f"Your weakest subject is {min_subject['subject']} with {min_subject['marks']} marks. You should focus more on this.")

if __name__ == "__main__":
    name, subjects = get_student_info()
    max_subject, min_subject = analyze_results(subjects)
    display_results(name, max_subject, min_subject)
