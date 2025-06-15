# learned something at least
import sqlite3

DB_FILE = "ballots.db"

def init_db():
    # Complete the code
    con = sqlite3.connect(DB_FILE)
    cursor = con.cursor()

    cursor.execute('''
        create table if not exists ballots(
            id integer primary key autoincrement,
            ranking text
        );
    ''')

    con.commit()
    con.close()


def add_ballot(ranking):
    # Complete the code
    con = sqlite3.connect(DB_FILE)
    cursor = con.cursor()
    data = ','.join(ranking)
    cursor.execute('insert into ballots(ranking) values(?)', (data,))

    con.commit()
    con.close()

def fetch_ballots():
    # Complete the code
    con = sqlite3.connect(DB_FILE)
    cursor = con.cursor()

    cursor.execute('select ranking from ballots')
    rows = cursor.fetchall()
    ans = []
    for row in rows:
        ans.append(row[0].split(','))
    con.close()
    return ans

def get_ballots_from_user():
    print("Welcome to the RCV Vote Counter Simulator!")
    print("Enter ranked ballots (comma-separated). Type 'done' to finish.\n")

    while True:
        entry = input("Ballot: ").strip()
        if entry.lower() == "done":
            break
        if entry:
            ranking = [name.strip() for name in entry.split(",") if name.strip()]
            if ranking:
                add_ballot(ranking)
            else:
                print("Invalid ballot. Please enter at least one candidate.")

def main():
    init_db()
    get_ballots_from_user()
    ballots = fetch_ballots()

    print(ballots)

if __name__ == "__main__":
    main()
