""" 
Lagrange interpolation using python 
"""

# Library imports
from prettytable import PrettyTable

# Getting data from user
print("Welcome to Lagrange Interpolation application. This app is supposed to estimate value of a one-variable function in a speciefic point by taking some points of the function.")

data_count = int(input("Please enter how many data row you have, then press enter: "))

print("Good, now I'm going to take the data points, please enter them one by one in the following lines and seperate them with enter.")
print("Example: (DATA 1): 0 0")

# taking data points
data_points = []

for i in range(data_count):
    data_point = input(f"(DATA {i+1}): ").split()
    data_points.append([float(data_point[0]), float(data_point[1])])

print("\n\nData points table:")

# Print data table
table = PrettyTable()
table.field_names = ["X", "Y"]
table.add_rows(data_points)
print(table.get_string() + "\n\n")

estimation_point = float(input("Alright, now please enter x of the point you want to be estimated: "))

# Lagrange algorithm
estimation = 0
for index_i, i in enumerate(data_points):
    lagrangian = i[1]
    for index_j, j in enumerate(data_points): 
        if index_i == index_j:
            continue
        lagrangian *= (estimation_point - j[0]) / (i[0] - j[0])
    estimation += lagrangian

# Print estimation
print(f"\n\n\nVery Well! Everything is done. Your estimated value is: {estimation}")
