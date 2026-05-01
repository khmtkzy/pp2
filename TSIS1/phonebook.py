import json
from connect import get_connection


def add_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")

    # group
    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    res = cur.fetchone()
    if res:
        group_id = res[0]
    else:
        cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
        group_id = cur.fetchone()[0]

    # contact
    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES(%s, %s, %s, %s) RETURNING id
    """, (name, email, birthday, group_id))
    contact_id = cur.fetchone()[0]

    # multiple phones (FIXED)
    while True:
        phone = input("Phone (enter to stop): ")

        if not phone:
            break

        ptype = input("Type (home/work/mobile): ").strip().lower()

        if ptype not in ["home", "work", "mobile"]:
            print("Invalid type! Use home/work/mobile")
            continue

        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES(%s, %s, %s)
        """, (contact_id, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added!")


def search():
    conn = get_connection()
    cur = conn.cursor()

    query = input("Search: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (query,))
    rows = cur.fetchall()

    if rows:
        for r in rows:
            print(r)
    else:
        print("No results")

    cur.close()
    conn.close()


def filter_group():
    conn = get_connection()
    cur = conn.cursor()

    group = input("Group: ")

    cur.execute("""
        SELECT c.name, c.email, c.birthday
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    rows = cur.fetchall()

    if rows:
        for r in rows:
            print(r)
    else:
        print("No contacts in this group")

    cur.close()
    conn.close()


def sort_contacts():
    conn = get_connection()
    cur = conn.cursor()

    field = input("Sort by (name/birthday): ").strip().lower()

    if field == "name":
        cur.execute("SELECT name, email FROM contacts ORDER BY name")
    elif field == "birthday":
        cur.execute("SELECT name, email FROM contacts ORDER BY birthday")
    else:
        print("Invalid option")
        return

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def pagination():
    conn = get_connection()
    cur = conn.cursor()

    page = 0
    limit = 5

    while True:
        offset = page * limit

        cur.execute("""
            SELECT name, email FROM contacts
            ORDER BY name
            LIMIT %s OFFSET %s
        """, (limit, offset))

        rows = cur.fetchall()

        if not rows:
            print("No more data")
        else:
            for r in rows:
                print(r)

        cmd = input("next / prev / quit: ").strip().lower()

        if cmd == "next":
            page += 1
        elif cmd == "prev" and page > 0:
            page -= 1
        elif cmd == "quit":
            break
        else:
            print("Invalid command")

    cur.close()
    conn.close()


def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, email, birthday FROM contacts")
    contacts = cur.fetchall()

    result = []

    for c in contacts:
        cid = c[0]

        cur.execute("SELECT phone, type FROM phones WHERE contact_id=%s", (cid,))
        phones = cur.fetchall()

        result.append({
            "name": c[1],
            "email": c[2],
            "birthday": str(c[3]),
            "phones": [{"phone": p[0], "type": p[1]} for p in phones]
        })

    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print("Exported!")

    cur.close()
    conn.close()


def import_json():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.json", encoding="utf-8") as f:
        data = json.load(f)

    for c in data:
        name = c["name"]
        email = c["email"]
        birthday = c["birthday"]
        group = c.get("group", "Other")

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")
            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING", (group,))
        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
        gid = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES(%s, %s, %s, %s) RETURNING id
        """, (name, email, birthday, gid))
        cid = cur.fetchone()[0]

        for p in c["phones"]:
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES(%s, %s, %s)
            """, (cid, p["phone"], p["type"]))

    conn.commit()
    cur.close()
    conn.close()

    print("Imported!")


def menu():
    while True:
        print("""
1 Add contact
2 Search
3 Filter by group
4 Sort
5 Pagination
6 Export JSON
7 Import JSON
0 Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search()
        elif choice == "3":
            filter_group()
        elif choice == "4":
            sort_contacts()
        elif choice == "5":
            pagination()
        elif choice == "6":
            export_json()
        elif choice == "7":
            import_json()
        elif choice == "0":
            print("Bye!")
            break


if __name__ == "__main__":
    menu()