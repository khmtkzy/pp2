import csv
from connect import connect


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Added!")


def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                (row["first_name"], row["phone"])
            )

    conn.commit()
    cur.close()
    conn.close()

    print("CSV imported!")


def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def update_name():
    old_name = input("Old name: ")
    new_name = input("New name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET first_name = %s WHERE first_name = %s",
        (new_name, old_name)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Name updated!")


def update_phone():
    name = input("Enter name: ")
    new_phone = input("Enter new phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE first_name = %s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Phone updated!")


def search_by_name():
    name = input("Enter name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s",
        ("%" + name + "%",)
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search_by_phone_prefix():
    prefix = input("Enter phone prefix: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix + "%",)
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_by_name():
    name = input("Enter name to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted by name!")


def delete_by_phone():
    phone = input("Enter phone to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted by phone!")


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Add from console")
        print("2. Import from CSV")
        print("3. Show all")
        print("4. Update name")
        print("5. Update phone")
        print("6. Search by name")
        print("7. Search by phone prefix")
        print("8. Delete by name")
        print("9. Delete by phone")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            show_all()
        elif choice == "4":
            update_name()
        elif choice == "5":
            update_phone()
        elif choice == "6":
            search_by_name()
        elif choice == "7":
            search_by_phone_prefix()
        elif choice == "8":
            delete_by_name()
        elif choice == "9":
            delete_by_phone()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()