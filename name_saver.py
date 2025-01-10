import csv

csv_file = "users.csv"

def save_name(name):
    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Name"])
        writer.writerow([name])

    print(f"He cambiado esta seccion en el nombre '{name}' saved successfully to {csv_file}.")
    print("Esta es simplemente un nueva linea")


def show_names():
    try:
        with open(csv_file, mode="r") as file:
            reader = csv.reader(file)
            print("\nNames saved in the file:")
            for i, row in enumerate(reader):
                if i > 0:
                    print(row[0])
    except FileNotFoundError:
        print("The file does not contain any names yet.")

while True:
    print("\n--- MENU ---")
    print("1. Save name")
    print("2. Show ALL INSERTED names")
    print("3. GET OUT")
    print("4. Cuarta opcion")

    option = input("Choose an option (1/2/3): ")

    if option == "1":
        name = input("Please enter your name: ")
        save_name(name)
    elif option == "2":
        show_names()
    elif option == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
