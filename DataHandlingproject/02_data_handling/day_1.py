import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
      with open(FILENAME, "w", newline="utf-8")as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Email", "Phone"])


def add_contact():
     name = input("Name: ").strip()
     phone = input("Phone: ").strip()
     email = input("Email: ").strip()

# check for duplicate
     with open(FILENAME, "r", newline="utf-8") as f:
         reader = csv.DictReader(f)
         for row in reader:
                 if row["Name"].lower() == name.lower():
                        print("Contact already exists.")
                        return  



         with open(FILENAME, "a", newline="utf-8") as f:
               writer = csv.writer(f)
               writer.writerow([name, email, phone])
               print("Contact added successfully.")

def view_contatcts():
      with open(FILENAME, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)


            if len(rows) == 1:
                  print("No contacts found.")
                  return
            
            print("\n your contacts: /n")
            for row in rows[1:]:
                  print(f"Name: {row[0]}, Email: {row[1]}, Phone: {row[2]}")
                  print()


def seacrh_contact():
      term = input("Enter name or email to search: ").strip().lower()
      found = False  

      with open(FILENAME, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                  if term in row["Name"].lower() or term in row["Email"].lower():
                        print(f"Name: {row['Name']}, Email: {row['Email']}, Phone: {row['Phone']}")
                        found = True


      if not found:
            print("No matching contacts found.")


def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contatcts()
        elif choice == "3":
            seacrh_contact()
        elif choice == "4":
            print("Thanks for using the Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.") 





if __name__ == "__main__":
    main()