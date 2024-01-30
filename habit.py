from datetime import datetime
from db import db
import _json

""" habit class that allows for interacting with and storing different habits"""
class Habit:
    def __init__(self, db, name: str = None, description: str = None, periodicity: str = None):
        """ Habit class, to track habits
        :param name: str, optional
        the name of the habit
        :param description: the description of the habit
        :param periodicity : str, optional
        The period of time the habit is tracked for (e.g. daily, weekly, monthly)
        """
        self.add_counter = 0
        self.name = name
        self.db = db
        self.description = description
        self.periodicity = periodicity
        self.streak = 0
        self.current_time = datetime.now().strftime("%m/%d/%Y")

    def __str__(self):
        return f"{self.name}: {self.description}: {self.add_counter}: {self.periodicity}"

    # insuring functionality.
    def increment(self):
        self.add_counter += 1

    def increase(self):
        """Increase the streak by 1"""
        self.streak = get_streak(self.db, self.name)
        self.streak += 1

    def reset(self):  # makes it possible to reset streaks
        self.streak = 0

    def save_habit(self, db):
        """creates new habit in the database otherwise update the habit if already exists in db"""
        db.add_habit(self.db, self.name, self.description, self.periodicity)

    def delete_habit(self, db):
        """removes the user habit from the database"""
        name = db.check_habit(self.db, self.name)
        if name:
        db.delete_habit(self.db, self.name)  # Fixing the recursion error here
        self.name = None
        self.description = None
        self.periodicity = None
        self.streak = 0

    else:
    print("Enter a valid habit name")
        else:
            print("Enter a valid habit name")

    def mark_as_completed(self, db):
        pass


def add_event(self, date: str = None):
        """adds a tracked event / habit to the db"""
        self.increase()
        db.check_habit(self.db, self.name)
        update_habit(self.db, self.name, self.streak)
        self.longest(self.db)

    def decrement_event(self, db):
        """resets counter to 1 if streak was broken / missed"""
        self.streak = 1
        check_habit(self.db, self.name)
        update_habit(self.db, self.name, self.streak)
        self.longest(self.db)

    def store(self, db):
        db.add_counter(self.db, self.name, self.periodicity, self.streak)

    def daily_habit(self, db):
        """completed daily habit added to database"""
        today = date.today()
        format = "%Y-%m-%d %H:%M:%S"
        last = last_checked(self.db, self.name)
        last1 = [i[0] for i in last]
        if len(ls) < 0:
            self.add_event(None)
        else:
            ls = last1[-1]
            last_check = datetime.strptime(ls, format).date()
            if today - last_check < timedelta(days=1):
                print("Habit already logged today")
            elif today - last_check < timedelta(days=2):
                self.add_event(None)
            else:
                self.decrement_event(db)

    def weekly_habit(self, db):
        """completed weekly habit and adds it into database"""
        today = date.today()
        format = "%Y-%m-%d %H:%M:%S"
        last = last_checked(self.db, self.name)
        last1 = [i[0] for i in last]
        if len(last1) < 0:
            self.add_event(None)
        else:
            ls = last1[-1]
            last_check = datetime.strptime(ls, format).date()
            if today - last_check < timedelta(days=7):
                print("Habit already checked this week")
            elif today - last_check < timedelta(days=8):
                self.add_event(None)
            else:
                self.decrement_event(db)

    def complete_habit(self, db):
        """completes the habit in the database"""
        name = check_habit(self.db, self.name)
        if name:
            streak = get_streak(self.db, self.name)
            periodicity = get_periodicity(self.db, self.name)
            per = periodicity
            if per == 'daily':
                if streak == 0:
                    self.add_event(db)
                else:
                    self.daily_habit(db)
            else:
                if streak == 0:
                    self.add_event(db)
                else:
                    self.weekly_habit(db)
        else:
            print("Enter a valid habit name")

    def longest(self, db):
        """ Calculates the longest streak using current streak value"""
        streak = get_streak(self.db, self.name)
        count = get_streak_from_count(self.db, self.name)
        if streak >= count:
            self.streak = get_streak(self.db, self.name)
            update_count(self.db, self.name, self.streak)
