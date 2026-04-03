import psycopg2
from config import load_config


def create_table():
    """Create the phonebook table if it doesn't exist."""
    commands = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """

    conn = None
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()
        cur.execute(commands)
        conn.commit()
        cur.close()
        print("Table 'phonebook' is ready.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def ups():
    username = input("Enter username: ").strip()
    phone = input("Enter phone: ").strip()
    sql = "CALL upsert_u(%s, %s);"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (username, phone))
            conn.commit()
            print(f"User {username} upserted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def hz():
    print("Enter list of usernames and list of phones")
    print("Usernames: ", end="")
    u = input().split()
    print("Phones: ", end="")
    p = input().split()

    if len(u) != len(p):
        print("Error: number of usernames and phones must match.")
        return

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            conn.notices.clear()
            with conn.cursor() as cur:
                cur.execute("CALL loophz(%s, %s)", (u, p))

            conn.commit()

            for notice in conn.notices:
                print(notice.strip())

            print("Lists inserted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def delete_contact():
    print("Delete by (1) username or (2) phone?")
    choice = input().strip()

    if choice == "1":
        username = input("Enter username: ").strip()
        sql = "CALL del_user(%s)"
        param = (username,)
    elif choice == "2":
        phone = input("Enter phone: ").strip()
        sql = "CALL del_user(%s)"
        param = (phone,)
    else:
        print("Invalid choice.")
        return

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, param)
            conn.commit()
            print("User deleted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def match_return():
    print("Write the username or phone part that you want to match:")
    a = input().strip()
    sql = "SELECT * FROM records(%s)"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (a,))
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
                else:
                    print("No matching contacts.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def pages():
    print("Enter limit: ", end="")
    lim = int(input())
    print("Enter offset: ", end="")
    offs = int(input())

    sql = "SELECT * FROM pagination(%s, %s)"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (lim, offs))
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
                else:
                    print("No data found.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def main():
    while True:
        print("\n1. Create table")
        print("2. Upsert user")
        print("3. Insert list of users and their phones")
        print("4. Delete contact")
        print("5. Return matching records")
        print("6. Paginated data")
        print("7. Exit")

        try:
            a = int(input("Choose an option: "))

            if a == 1:
                create_table()
            elif a == 2:
                ups()
            elif a == 3:
                hz()
            elif a == 4:
                delete_contact()
            elif a == 5:
                match_return()
            elif a == 6:
                pages()
            elif a == 7:
                print("Bye!")
                return
            else:
                print("Try again!")
                continue

        except ValueError:
            print("Please enter a number.")
            continue

        print("Would you like to continue? y/n")
        while True:
            answer = input().strip().lower()
            if answer == "y":
                break
            elif answer == "n":
                print("Bye!")
                return
            else:
                print("Try again!")


if __name__ == "__main__":
    main()