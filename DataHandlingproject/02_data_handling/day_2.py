def collect_student_data():
      students = {}

      while True:
            name = input("Enter student name (or 'exit' to finish): ").strip()
            if name.lower() == 'done':
                  break
            if name in students:
                  print(f"Student {name} already exists. Please enter a different name.")
                  continue

            try:
                 marks = float(input(f"Enter marks for {name}: ").strip())
                 students[name] = marks
            except ValueError:
                 print("Invalid input. Please enter a numeric value for marks.")

      return students


def display_report(students):
      if not students:
            print("No student data ❌")
            return

      marks=list(students.values())
      max_score = max(marks)
      min_score = min(marks)
      average = sum(marks) / len(marks)

      topper = [ name for name, scrore in students.items() if score == max_score]
      bottomer = [ name for name, score in students.items() if score == min_score]

      print("\n Student marks Report :")
      print("-" * 30)
      print(f"average marks for students: {average:.2f}")
      print(f" - Highest Marks: {max_score} by {', '.join(topper)}")
      print(f" - Lowest Marks: {min_score} by {', '.join(bottomer)}")
      print("-" * 30)
      print("Detailed Marks💻💻")
      for name, marks in students.items():
            status = "Pass" if marks >= 50 else "Fail"
            print(f" - {name}: {marks} ({status})")

