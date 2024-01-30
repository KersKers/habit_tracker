import sqlite3
from datetime import datetime, date, timedelta

def get_db(name="main.db"):
    """ Function to create and maintain the connection with the database"""
    db = sqlite3.connect(name)
    create_tables(db)
    return db

def create_tables(db):
    """
    Creates two database tables.

    The habit_tracker database consists of the following columns: habit, periodicity, description,
    creation_time, streak, and completion_time.
    The habit_log database has the following columns: habit, completed, streak, and completion_time.
    :param db: To maintain connection with the database
    """
    cur = db.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS habit_tracker (
               habit TEXT PRIMARY KEY , 
               periodicity TEXT,
               descrition TEXT,
               creation_time TEXT,
               streak INT,
               completion_time TEXT   
           )''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS habit_log (
            habit TEXT,
            completed BOOL,
            streak INT DEFAULT 0,
            completion_time TIME,
            FOREIGN KEY (habit) REFERENCES habit_tracker(habit)
        )''')
    db.commit()


def add_habit(db, name, description,periodicity, streak=0):
    """ adds a new habit to the database """
    cur = db.cursor()
    cur.execute("SELECT name FROM Habit WHERE name=?", (name,))
    result = cur.fetchone()
    if result:
        print("Habit already exists")
    else:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO Habit VALUES (?,?,?,?,?)",
                    (name, description, periodicity, created_at, streak, None))
        db.commit()
        print("Habit created successfully")
        print("Information logged.\n")

def check_habit(db, name, checked_at=None, streak=0):
    """ check a specific habit """
    cur = db.cursor()
    if checked_at is None:
        checked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO habit_log VALUES(?,?,?,?)", (name, True, streak, checked_at))
    print("Habit logged successfully")
    print("Name :-", name)
    print("checked_at :-", checked_at)
    db.commit()


def update_habit(db, name, streak):
    """updates the value of a streak in the habit table"""
    cur = db.cursor()
    cur.execute("UPDATE Habit SET streak=? WHERE name=?", (streak, name))
    db.commit()


def verification(db, name):
    """ verifies habit from the database """
    cur = db.cursor()
    cur.execute("SELECT name FROM Habit WHERE name=?", (name,))
    return cur.fetchone()

def last_checked(db, name):
    """ returns the last value of last logged """
    cur = db.cursor()
    cur.execute("SELECT checked_at FROM count WHERE name=?", (name,))
    return cur.fetchall()

def get_streak(db, name):
    """ returns the most current streak from the database """
    cur = db.cursor()
    cur.execute("SELECT streak FROM Habit WHERE name=?", (name,))
    streak_count = cur.fetchall()
    return streak_count[0][0]

def get_streak_from_count(db, name):
    """ returns the longest logged streak from table count """
    cur = db.cursor()
    cur.execute("SELECT streak FROM count WHERE name=?", (name,))
    str_count = cur.fetchall()
    return str_count[0][0]

def update_count(db, name, streak):
    """updates the value of streak in count table"""
    cur = db.cursor()
    cur.execute("UPDATE count SET streak=? WHERE name=?", (streak, name))
    db.commit()


def get_periodicity(db, name):
    """ selects periodicity of a specified habit """
    cur = db.cursor()
    cur.execute("SELECT period FROM Habit WHERE name=?", (name,))
    return cur.fetchall()[0][0]

def show_habits(db):
    """ returns a habit with all logged information """
    cur = db.cursor()
    cur.execute("SELECT * FROM Habit ")
    return cur.fetchall()

def habit_with_periodicity(db,periodicity=None):
    """ returns a list of habit according to selected timeframe """
    if period == "daily":
        cur = db.cursor()
        cur.execute("SELECT * FROM Habit WHERE periodicity=?", (periodicity,))
        return cur.fetchall()
    else:
        cur = db.cursor()
        cur.execute("SELECT * FROM Habit WHERE periodicity=?", (periodicity,))
        return cur.fetchall()

def longest_of_all(db):
    """select the max streak from all defined habit """
    cur = db.cursor()
    cur.execute("SELECT MAX(streak) FROM count")
    return cur.fetchall()[0][0]


def show_all_logs(db, name):
    """ return a list of all habit checked_at dates """
    result = verification(db, name)
    if result:
        cur = db.cursor()
        cur.execute('SELECT checked_at FROM count WHERE name=?', (name,))
        long = cur.fetchone()
        if long:
            cur.execute("SELECT checked_at FROM count WHERE name=?", (name,))
            log = cur.fetchall()
            print(f"Your logs for {name}")
            print(f"checked at \n {log}")
        else:
            print("No Logs For This Habit Yet")
    else:
        print("No logs for this habit exists in our database")

def remove_habit(db, name):
    """ delete the specified habit from the database """
    cur = db.cursor()
    cur.execute("DELETE FROM Habit WHERE name=?", (name,))
    cur.execute("DELETE FROM count WHERE name=?", (name,))
    db.commit()
    print("Habit removed successfully")


def db():
    return None
