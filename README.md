# Doctor - Patient Health Assistant

A simple beginner-friendly Python project for organizing basic patient health information through a menu-driven command-line interface.

## 📌 Project Overview

The **Doctor - Patient Health Assistant** allows a user to enter and manage basic patient information and maintain simple health records. The program collects the patient's name, age, gender, and medical history when it starts, then provides a main menu for accessing different health-record modules.

The project is designed as a learning project using basic Python concepts such as functions, lists, dictionaries, loops, conditional statements, input validation, and global variables.

## ✨ Features

### 1. Patient Information
At the beginning of the program, the user enters:
- Patient name
- Patient age
- Patient gender

The program also asks for previous medical conditions at the start.

### 2. Medical History
Users can:
- Add previous illnesses or medical conditions
- Enter the year or period of the condition
- Add additional details
- View all recorded medical history

### 3. Medicine Tracker
Users can:
- Add a medicine
- Enter dosage
- Enter medicine timing
- View all recorded medicines

### 4. Doctor Visits
Users can record:
- Doctor name
- Visit date
- Reason for the visit
- Doctor's notes

Previously recorded doctor visits can also be viewed.

### 5. Vital Signs
The program can record and display:
- Date
- Temperature
- Heart rate
- Systolic blood pressure
- Diastolic blood pressure

Basic validation is included for numeric inputs.

### 6. Patient Summary
The summary displays:
- Patient name
- Age
- Gender
- Recorded medical history
- Number of medicines
- Number of doctor visits
- Number of vital-sign records

## 🛠️ Technologies Used

- **Python 3**
- Command Line / Terminal
- Python built-in functions and data structures

No external Python libraries are required.

## 📂 Project Structure

```text
Doctor-Patient-Health-Assistant/
│
├── main.py
└── README.md
```

The main Python file contains the complete program, including patient setup, menus, data handling, validation, and program execution.

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-repository-link>
```

### 3. Open the Project

```bash
cd Doctor-Patient-Health-Assistant
```

### 4. Run the Program

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## 🧭 How the Program Works

When the program starts, it first collects the patient's basic information and previous medical history.

After setup, the main menu provides these options:

```text
1. Patient Summary
2. Medical History
3. Medicine Tracker
4. Doctor Visits
5. Vital Signs
6. Exit
```

The user selects an option and can add or view the corresponding records.

## 🧠 Python Concepts Demonstrated

This project demonstrates several beginner-level Python concepts:

- Variables
- Functions
- Lists
- Dictionaries
- `if`, `elif`, and `else`
- `while` loops
- `for` loops
- Input handling with `input()`
- Type conversion using `int()` and `float()`
- Exception handling with `try` and `except`
- String formatting
- Global variables
- The `if __name__ == "__main__":` entry point

## 🔒 Data Storage

The current version stores all information in Python lists and dictionaries while the program is running.

There is **no database or file-based permanent storage** in the current implementation. Therefore, the records are lost when the program is closed.

## ⚠️ Important Note

This project is intended for **educational and record-keeping purposes only**. It is not a medical diagnosis or treatment system and should not be used as a replacement for professional medical advice.

## 🚀 Possible Future Improvements

The project could later be extended with:

- Permanent storage using files or a database
- Edit and delete options for records
- Search functionality
- Better date validation
- Multiple patient profiles
- Exporting patient records
- A graphical user interface
- Login and authentication
- More detailed health reports

## 👨‍💻 Project Purpose

This project was created as a beginner Python application to demonstrate how basic programming concepts can be combined to build a practical, menu-driven health-record management system.
