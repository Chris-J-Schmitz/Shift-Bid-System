import csv
from collections import defaultdict
import pandas as pd 


#Define Schedule options 
SHIFT_SCHEDULE = {
    #5x8 Shifts
    1: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": "0800 - 1630"},
    2: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": "0830 - 1700"},
    3: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": "0900 - 1730"},
    4: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": "0945 - 1815"},
    5: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": "1000 - 1830"},
    6: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": "1030 - 1900"},
    7: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": "1045 - 1915"},
    8: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "times": "1100 - 1930"},
    #4X9 , 1x4 shifts
    9: {"days": ["Monday", "Wednesday", "Thursday", "Friday", "Saturday"], "times": "0800 - 1730 , 0800 - 1200"},
    10: {"days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"], "times": "0800 - 1730 , 0800 - 1200"},
    11: {"days": ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday"], "times": "0800 - 1730 , 0800 - 1200"},
    #4x8.5 , 1x6 Shifts 
    12: {"days": ["Monday", "Wednesday", "Thursday", "Friday", "Saturday"], "times": "0800 - 1700, 0800 - 1400"},
    13: {"days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"], "times": "0800 - 1700, 0800 - 1400"},
    14: {"days": ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday"], "times": "0800 - 1700, 0800 - 1400"},
    #4x9, 1x4 Shifts  
    15: {"days": ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday"], "times": "0830 - 1800 , 0800 - 1200"},
    16: {"days": ["Monday", "Wednesday", "Thursday", "Friday", "Saturday"], "times": "0900 - 1830 , 0800 - 1200"},
    17: {"days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"], "times": "0900 - 1830 , 0800 - 1200"},
    18: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Saturday"], "times": "0930 - 1900 , 0800 - 1200"},
    19: {"days": ["Monday", "Wednesday", "Thursday", "Friday", "Saturday"], "times": "1000 - 1930 , 1130 - 1530"},
    20: {"days": ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"], "times": "1000 - 1930 , 1145 - 1645"},
    21: {"days": ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday"], "times": "1000 - 1930 , 1145 - 1645"},
    22: {"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Saturday"], "times": "1000 - 1930 , 1200 - 1600"},
    23: {"days": ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday"], "times": "1000 - 1930 , 1200 - 1600"}

}



#Gather employee info from csv file
def readEmployeeData(file_path) :
    employees = []
    with open(file_path, "r") as file: 
        reader = csv.DictReader(file)
        for row in reader:
            employees.append({
                "emp_id": row["emp_id"],
                "emp_name": row["emp_name"],
                "shift_preferences": list(map(int, row["shift_preferences"].strip("[]").split(",",))),
                "seniority_level": int(row["seniority_level"]),
                "performance_rating" : int(row["performance_rating"])
            })
        return employees
    

#Assign Shifts
def assign_shifts(employees):
    """Assigns Shifts to employees based on their preference, seniority and performance"""

    #Sort employee's by performance and seniority 
    employees.sort(key=lambda x: (-x["performance_rating"], -x ["seniority_level"]))

    #initialize the shift dictionary
    shift_assignments = defaultdict(list)
    shift_capacity = {shift: 0 for shift in SHIFT_SCHEDULE.keys()}

    #setting a limit for employees per shift
    shift_limit = 7

    #Assign the Shifts 
    for employee in employees:
        for shift in employee["shift_preferences"]:
            if shift in SHIFT_SCHEDULE and shift_capacity[shift] < shift_limit:
                shift_assignments[shift].append(employee)
                shift_capacity[shift] += 1
                break

    return shift_assignments

#Display shifts in console 
def displayShifts(shift_assignments):
    print("shift assignments")
    for shift in sorted(shift_assignments.keys()):
        print(f"\nshift {shift} - Days: {SHIFT_SCHEDULE[shift]['days']} , Time: {SHIFT_SCHEDULE[shift]['times']}")
        for emp in shift_assignments[shift]:
            print(f" - {emp ['emp_name']} (ID: {emp['emp_id']})")

    



#Create a Dataframe of the shift assignments
def createDataFrame(shift_assignments):
    rows = []
    for shift in sorted(shift_assignments.keys()):
        for emp in shift_assignments[shift]:
            #Create a row 
            row = {
                "Employee_id": emp['emp_id'],
                "Employee_Name": emp['emp_name'],
                "Shift_id": shift,
                "Shift_Days": ",".join(SHIFT_SCHEDULE[shift]["days"]),
                "Shift_Times": SHIFT_SCHEDULE[shift]["times"]
            }

            rows.append(row)

    df = pd.DataFrame(rows)
    return df


def validateAssignments():
    while True:

        user_input = input('Okay to proceed with ? (Y / N)').strip().upper()
        if user_input == 'Y':
            print("Proceeding with assignments...")
            return True
        elif user_input == 'N':
            print("Assignments not confirmed. Exiting process...")
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    



#main function 
def main():
    #file path to the csv file
    file_path = 'employee_data.csv'
    
    #read emp data
    employees = readEmployeeData(file_path)

    #Assign the shifts
    shift_assignments = assign_shifts(employees)

    #Display shifts for review
    displayShifts(shift_assignments)
    
    if validateAssignments():
        print("Saving assignments to a file...")
        shift_df = createDataFrame(shift_assignments)
        shift_df.to_csv("shift_assignments.csv", index=False)
        print("Shift assignments successfully!")
    else:
        print("Process cancelled. ")



    


if __name__ == "__main__":
    main()