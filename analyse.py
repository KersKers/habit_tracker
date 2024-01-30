from db import get_counter_data, show_all_habit,  get_habit_with_periodicity, verification, get_streak_from_count, longest_of_all

def calculate_count(db, counter):
    """
    Calculate the count of the counter.

    :param db: an initialized sqlite3 database connection
    :param counter: name of the counter present in the DB
    :return: length of the counter increment events
    """
    data = get_counter_data(db, counter)
    return len(data)


def show_all_habits(db):
    """
    Gets information about all habits
    :param db:create connection with database
    :return:a list of all habit with their all information
    """
    habits_list = show_all_habit(db)
    for row in habits_list:
        print("Habit Name: ", row[0])
        print("Specification: ", row[2])
        print("Periodicity: ", row[1])
        print("Creation: ", row[3])
        print("Current streak:", row[4])
        print("\n")

def get_habit_with_periodicity(db, period):
    """
    Gets information from database and return to the user
    :param db:Create a connection with the database
    :param period:timespan of a habit (eg:- daily or weekly)
    :return:a list of habits with specified period
    """
    habits_list = habit_with_period(db, period)
    for row in habits_list:
        print(f"Name: {row[0]}")
        print(f"created_at: {row[3]}")
        print(f"Current streak: {row[4]}")
        print("\n")

def get_longest_streak(db, name):
    """
    Select current streak and from that return the longest run
    :param db:maintain a connection to database
    :param name:name of the specified habit
    :return:longest streak
    """
    verify = verification(db, name)
    if verify:
        cur = db.cursor()
        cur.execute("SELECT name FROM count where name=?", (name,))
        result = cur.fetchone()
        if result:
            longest = get_streak_from_count(db, name)
            print(f"Longest streak for habit '{name}' is \n {longest} days ")
            return longest
        else:
            print(f"Longest streak for habit '{name}' is \n {0} days")
    else:
        print("Enter a valid habit name")

def get_longest_streak_all(db):
    """
     from database returns the longest run streak of all habits
    :param db:Maintain connection with database
    :return:longest run from all defined habit
    """
    long = longest_of_all(db)
    print(f"Longest streak for all defined habits is \n {long} days ")


def habit_periodicity():
    return None
