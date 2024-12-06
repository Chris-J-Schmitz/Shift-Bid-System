# Shift Bid System

This project is a Python-based **Shift Bid System** designed to fairly and efficiently assign work shifts to employees based on their preferences, seniority, and performance ratings. It reads employee data from a CSV file and outputs the assigned shifts.

## Features

- **Employee Shift Preferences**: Employees can specify their preferred shifts in a ranked order.
- **Seniority and Performance**: Assignments prioritize employees with higher seniority and performance ratings.
- **Shift Variety**: Includes multiple shift types such as 5x8 (five 8-hour days), 4x9 + 1x4, and 4x8.5 + 1x6.
- **Dynamic Shift Capacity**: Limits the number of employees assigned to each shift to ensure balance.
- **Configurable Schedules**: Easy to modify shift schedules and constraints.

## Shift Schedules

| Shift Type | Days                                    | Times                              |
|------------|----------------------------------------|------------------------------------|
| 5x8        | Monday - Friday                        | Varies: 08:00 - 19:30             |
| 4x9 + 1x4  | Weekdays + Saturday                    | Weekday: 08:00 - 17:30, Sat: 08:00 - 12:00 |
| 4x8.5 + 1x6| Weekdays + Saturday                    | Weekday: 08:00 - 17:00, Sat: 08:00 - 14:00 |

## CSV File Format

The input CSV file should be formatted as follows:

| Column             | Description                                                              |
|--------------------|--------------------------------------------------------------------------|
| `emp_id`           | Unique ID for each employee                                             |
| `emp_name`         | Name of the employee                                                    |
| `shift_preferences`| An array of preferred shifts (ranked)                                   |
| `seniority_level`  | Seniority level of the employee (1-5; higher means more senior)         |
| `performance_rating`| Performance rating of the employee (1-5; higher means better performance)|


## How It Works
1.Input
: Employee data is read from a CSV file.

2.Sorting
: Employees are sorted based on their performance and seniority (highest to lowest).

3.Shift Assignment
: Employees are iterated through in sorted order.
    Shifts are assigned based on their ranked preferences, provided the shift has availability.


4.Output
: The program displays the shift assignments to the console for review and outputs 
to a new CSV file if the output looks acceptable. 

## How To Run
1. Clone The Repository
```
git clone https://github.com/Chris-J-Schmitz/Shift-Bid-System.git
cd shift-bid-system
```
2. Place your employee data in a CSV file (e.g., employee_data.csv).
3. Delete ("shift_assignments.csv") file. Or delete all contents within. 
3. Run The Program
``` 
python main.py
```

Sample Input
```
 emp_id,emp_name,shift_preferences,seniority_level,performance_rating
1,Employee_001,"[9, 3, 22, 5, 23, 11, 12, 7, 2, 18, 1, 10, 21, 15, 17, 19, 4, 8, 13, 20, 6, 14, 16]",4,2
2,Employee_002,"[5, 23, 3, 16, 19, 11, 7, 21, 20, 1, 9, 22, 13, 17, 15, 10, 18, 12, 2, 6, 14, 8, 4]",4,2
3,Employee_003,"[11, 3, 6, 1, 22, 5, 12, 8, 14, 7, 15, 20, 2, 23, 19, 21, 13, 10, 18, 17, 4, 9, 16]",4,1
```

Sample Output
```
Employee_id,Employee_Name,Shift_id,Shift_Days,Shift_Times
14,Employee_014,1,"Monday,Tuesday,Wednesday,Thursday,Friday",0800 - 1630
146,Employee_146,1,"Monday,Tuesday,Wednesday,Thursday,Friday",0800 - 1630
34,Employee_034,1,"Monday,Tuesday,Wednesday,Thursday,Friday",0800 - 1630
53,Employee_053,1,"Monday,Tuesday,Wednesday,Thursday,Friday",0800 - 1630
```

## Customization
- Shift Schedules: Modify the shift schedules dictionary to fit needs.
- Shift Limits: Adjust shift capacity as needed to increase or decrease the employee capacity per shift

## Liscense 
This project is licensed under the MIT License. See the LICENSE file for details.


