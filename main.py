# DOCTOR - PATIENT HEALTH ASSISTANT
#DATA STORAGE
patient_name = ""
patient_age = 0
patient_gender = ""
medical_history = []
medicines = []
visits = []
vitals = []
#INPUT FUNCTIONS
def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")
def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))

            if num > 0:
                return num

            print("Please enter a num greater than 0.")

        except ValueError:
            print("Please enter a whole num.")
def get_num(prompt):
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print("Please enter a valid num.")


#PATIENT SETUP

def setup_patient():

    global patient_name
    global patient_age
    global patient_gender

    print("\n**************************************")
    print("        PATIENT INFORMATION")
    print("*****************************************")

    patient_name = get_text("Enter patient name: ")
    patient_age = get_positive_integer("Enter patient age: ")
    patient_gender = get_text("Enter gender: ")

    # Medical history is collected at the beginning
    print("\n--------- MEDICAL HISTORY ---------")

    num = get_positive_integer(
        "How many previous medical conditions does the patient have? "
    )

    medical_history.clear()

    for i in range(num):

        print("\n--- Medical History", i + 1, "---")

        condition = get_text("Previous illness or condition: ")
        year = get_text("Year or period: ")
        details = get_text("Additional details: ")

        medical_history.append({
            "condition": condition,
            "year": year,
            "details": details
        })

    print("\nPatient information saved successfully!")
    print("Medical history saved successfully!")


#PATIENT SUMMARY
def patient_summary():

    print("\n========================================")
    print("          PATIENT SUMMARY")
    print("========================================")

    print("Name   :", patient_name)
    print("Age    :", patient_age)
    print("Gender :", patient_gender)

    print("\nMedical History:")

    if not medical_history:
        print("No medical history recorded.")
    else:
        for i, record in enumerate(medical_history, 1):

            print(
                f"{i}. {record['condition']} "
                f"({record['year']})"
            )

    print("\nMedicines:", len(medicines))
    print("Doctor Visits:", len(visits))
    print("Vital Records:", len(vitals))


# -------------------- MEDICAL HISTORY --------------------

def medical_history_menu():

    while True:

        print("\n========================================")
        print("          MEDICAL HISTORY")
        print("========================================")
        print("1. Add Medical History")
        print("2. View Medical History")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            condition = get_text(
                "Previous illness or condition: "
            )

            year = get_text(
                "Year or period: "
            )

            details = get_text(
                "Additional details: "
            )

            medical_history.append({
                "condition": condition,
                "year": year,
                "details": details
            })

            print("Medical history added successfully!")

        elif choice == "2":

            if not medical_history:
                print("\nNo medical history recorded.")
                continue

            print("\n--------- MEDICAL HISTORY ---------")

            for i, record in enumerate(medical_history, 1):

                print("\nRecord", i)
                print("Condition :", record["condition"])
                print("Year      :", record["year"])
                print("Details   :", record["details"])

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


# -------------------- MEDICINE TRACKER --------------------

def medicine_menu():

    while True:

        print("\n========================================")
        print("           MEDICINE TRACKER")
        print("========================================")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            name = get_text("Medicine name: ")
            dosage = get_text("Dosage: ")
            timing = get_text("Timing: ")

            medicines.append({
                "name": name,
                "dosage": dosage,
                "timing": timing
            })

            print("Medicine added successfully!")

        elif choice == "2":

            if not medicines:
                print("\nNo medicines recorded.")
                continue

            print("\n--------- MEDICINES ---------")

            for i, medicine in enumerate(medicines, 1):

                print(
                    f"{i}. {medicine['name']} - "
                    f"{medicine['dosage']} - "
                    f"{medicine['timing']}"
                )

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


# -------------------- DOCTOR VISITS --------------------

def visit_menu():

    while True:

        print("\n========================================")
        print("          DOCTOR VISITS")
        print("========================================")
        print("1. Add Doctor Visit")
        print("2. View Doctor Visits")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            doctor = get_text("Doctor name: ")
            date = get_text("Visit date: ")
            reason = get_text("Reason for visit: ")
            notes = get_text("Doctor's notes: ")

            visits.append({
                "doctor": doctor,
                "date": date,
                "reason": reason,
                "notes": notes
            })

            print("Doctor visit added successfully!")

        elif choice == "2":

            if not visits:
                print("\nNo doctor visits recorded.")
                continue

            print("\n--------- DOCTOR VISITS ---------")

            for i, visit in enumerate(visits, 1):

                print("\nVisit", i)
                print("Doctor :", visit["doctor"])
                print("Date   :", visit["date"])
                print("Reason :", visit["reason"])
                print("Notes  :", visit["notes"])

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


# -------------------- VITAL SIGNS --------------------

def vital_menu():

    while True:

        print("\n========================================")
        print("            VITAL SIGNS")
        print("========================================")
        print("1. Add Vital Signs")
        print("2. View Vital Signs")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            date = get_text("Date: ")

            temperature = get_num(
                "Temperature: "
            )

            heart_rate = get_positive_integer(
                "Heart rate: "
            )

            systolic = get_positive_integer(
                "Systolic blood pressure: "
            )

            diastolic = get_positive_integer(
                "Diastolic blood pressure: "
            )

            vitals.append({
                "date": date,
                "temperature": temperature,
                "heart_rate": heart_rate,
                "systolic": systolic,
                "diastolic": diastolic
            })

            print("Vital signs added successfully!")

        elif choice == "2":

            if not vitals:
                print("\nNo vital signs recorded.")
                continue

            print("\n--------- VITAL SIGNS ---------")

            for i, vital in enumerate(vitals, 1):

                print("\nRecord", i)
                print("Date        :", vital["date"])
                print("Temperature :", vital["temperature"])
                print("Heart Rate  :", vital["heart_rate"])
                print(
                    "Blood Pressure:",
                    str(vital["systolic"]) + "/"
                    + str(vital["diastolic"])
                )

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


# -------------------- MAIN PROGRAM --------------------

def main():

    print("========================================")
    print("     DOCTOR - PATIENT HEALTH ASSISTANT")
    print("========================================")

    # Patient information and medical history
    # are entered when the program starts.
    setup_patient()

    while True:

        print("\n========================================")
        print("              MAIN MENU")
        print("========================================")

        print("1. Patient Summary")
        print("2. Medical History")
        print("3. Medicine Tracker")
        print("4. Doctor Visits")
        print("5. Vital Signs")
        print("6. Exit")

        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_summary()

        elif choice == "2":
            medical_history_menu()

        elif choice == "3":
            medicine_menu()

        elif choice == "4":
            visit_menu()

        elif choice == "5":
            vital_menu()

        elif choice == "6":

            print("\nThank you for using")
            print("Doctor - Patient Health Assistant!")

            break

        else:
            print("Invalid choice. Please try again.")
# -------------------- START PROGRAM --------------------
if __name__ == "__main__":
    main()