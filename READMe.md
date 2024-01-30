
# Habit Tracker Overview:

The Habit Tracker, developed as part of Object Oriented and Functional Programming with Python DLBDSOOFPP01 course of the UI international University, provides a solution for users to track and analyze their habits. 
Built using Python 3.8, this command-line application simplifies the habit-tracking process.

# Core Functionality:

The habit tracking solution is a command-line interface (CLI) application designed to help users establish and monitor habits. Users can chose to track habits either daily, weekly or monthly, habits can be analysed accordingly. The application allows users to interactively add, track, analyse, and remove habits through a series of prompts and selections.
This tracker requires at least one daily habit and one weekly habit to be tracked, so it can list irregularities and habit goals reached. The user is able to mark tasks complete depending on the time frame selected.
Habits can be added and deleted, selected time frames can be changed.
All habits that are put in, can appear as a list to provide an overview.
Accordingly habit development or progression can be analysed and saved as JSON file for future use and analysis if the user wishes.

User Workflow:
Start the Application: users are welcomed and prompted to start.
Add Habit: users can add habits by providing the habit name and selecting the periodicity (daily, weekly, or monthly).
Track Habit: users can log events for a specific habit, incrementing the habit‘s streak. Tracked data is saved to a JSON file after each tracking event.
Analyse Habits: users can analyse habits by choosing options such as viewing all habits, analysing habits with a specific periodicity, or finding the longest streak.
Remove Habit: users can remove habits, with a confirmation prompt.
Complete Habit:users can mark habits as completed, updating the habit‘s streak and periodicity.
Exit:users can exit the application, concluding the habit tracking session.
This habit tracking solution provides users with a simple and interactive tool to establish and monitor 
their habits, with additional features for analysis and persistence of tracked data.


# Installation
```shell
pip install  -r requirements.txt
```
Ensure Python 3.8 or later is installed on your system.
Install the Questionary library by running pip install questionary.
Dependencies:
Python 3.8+
Questionary 1.10.0+

# Running the Program:
Download the repository files and store them in a separate folder.
Open the command/terminal window, navigate to the folder, and execute python main.py. 

# Running Tests:
Install Pytest for testing functions: pip install -U pytest.
Navigate to the test folder and run tests with the command pytest.

# Usage
Start 
```shell
python main.py
```
Add/Remove Habit or Category:

Users can add habits by selecting the "Add Habit" option and providing the required information.
Removing habits or categories is done through a user-friendly sub-menu.

Modify Habit's Periodicity:
Users can change the periodicity of a habit by selecting the habit and choosing a new periodicity.

Mark Habit as Completed:
Users can mark habits as completed, with the option to reset streaks if the habit wasn't completed within the specified periodicity.

Show Habits (All or Sort by Periodicity):
View all created habits or filter them by daily, weekly, or monthly periodicity.
Analytics:

Explore analytics options such as viewing all habit streaks, longest streaks of specific habits, and streak history.
Exit:

Safely exit the program.
then follow instructions on screen






Installation:

Ensure Python 3.8 or later is installed on your system.
Install the Questionary library by running pip install questionary.
Dependencies:

Python 3.8+
Questionary 1.10.0+
Running the Program:

Download the repository files and store them in a separate folder.
Open the command/terminal window, navigate to the folder, and execute python main.py or python3 main.py (for Python 3.10+).
Running Tests:

Install Pytest for testing functions: pip install -U pytest.
Install Freezegun for freezing time: pip install freezegun.
Navigate to the test folder and run tests with the command pytest.
Usage:

Add/Remove Habit or Category:

Users can add habits by selecting the "Add Habit" option and providing the required information.
Removing habits or categories is done through a user-friendly sub-menu.
Modify Habit's Periodicity:

Users can change the periodicity of a habit by selecting the habit and choosing a new periodicity.
Mark Habit as Completed:

Users can mark habits as completed, with the option to reset streaks if the habit wasn't completed within the specified periodicity.
Show Habits (All or Sort by Periodicity):

View all created habits or filter them by daily, weekly, or monthly periodicity.
Analytics:

Explore analytics options such as viewing all habit streaks, longest streaks of specific habits, and streak history.
Exit:

Safely exit the program.

# Tests can be run using the following
Start

```shell
pytest . 
``````

The program comes pre-loaded with sample habits: waterPlants, eatVegFruit, GetFitDailyTraining, 
chargePhone and CigarettesSmoked.








